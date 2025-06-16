import pyray as pr
from ui import con
from ui import button
from processing import terminal
from dataclasses import dataclass
import configparser


@dataclass
class Cell:
    text: str = ""


@dataclass
class Cursor:
    x: int = 0
    y: int = 0


class MainWindow:
    def __init__(self):
        pr.init_window(con.WIDTH, con.HEIGHT, "Confitty")
        pr.set_target_fps(60)
        self.term = terminal.Terminal()

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        # Lambda is so cool :)
        tf = lambda s: True if s.lower() == "true" else False

        self.in_dark_mode: bool = tf(self.config['config']["dark_mode"])
        print(self.config['config']["dark_mode"])
        print(self.in_dark_mode)

        self.update_colours(self)

        self.character_size = (10, 10)
        self.width = con.WIDTH // self.character_size[0]
        self.height = con.HEIGHT // self.character_size[1]

        self.canvas = [[Cell() for i in range(self.height)] for j in range(self.width)]
        self.cursor = Cursor()

        self.InEscapeSequence = False
        self.inCSI = False
        self.inFE = False
        self.ESCBuffer = bytearray()
        print("Terminal has started in raylib")

        self.settings = button.Button((con.WIDTH-120, con.HEIGHT-440, 110, 40), "Settings", self.second_background, self.text_col)
        self.run()

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(self.background_col)
            self.settings.render_button()
            while self.settings.is_clicked(pr.get_mouse_position()):
                settings = SettingsWindow(self)
                settings.run()
            self.run_terminal()
            self.display_output()
            self.get_inputs()
            pr.end_drawing()

        pr.close_window()

    def run_terminal(self):
        if self.term.processID == 0:
            # pty.fork(), Slave/child process always has processID == 0
            return

        if self.cursor.x >= self.width:
            self.cursor.x = 0
            self.cursor.y += 1
        if self.cursor.y >= self.height:
            # self.canvas = self.canvas[::][1:]
            new_canvas = []
            for i in range(len(self.canvas)):
                new_canvas.append(self.canvas[i][1:])
                new_canvas[i].append(Cell())
            self.canvas = new_canvas

            # self.canvas.append([Cell() for i in range(self.width)])
            self.cursor.y -= 1

        # Get the inputs and outputs and then check them
        byte = self.term.read_master()

        if self.InEscapeSequence:
            self.handle_escape_sequence(byte)
            return
        match byte:
            case b"\n":
                self.cursor.y += 1
                self.cursor.x = 0
                print("Newline")
            case b"\x07":
                print("BEEP")
            case b"\x08":
                if self.cursor.x > 0:
                    self.cursor.x -= 1
            case b"\x1B":
                # Start escape sequence
                self.InEscapeSequence = True
            case None | b"\r":
                pass
            case _:
                s = byte.decode("utf-8")
                self.canvas[self.cursor.x][self.cursor.y].text = s
                self.cursor.x += 1

    def get_inputs(self):
        if key_code := pr.get_key_pressed():
            shift, ctrl, alt = self.get_modifier_state()
            if not ctrl and not shift and not alt and key_code in con.keys:
                key = con.keys[key_code]
                self.term.send_input(key)
            if ctrl and not shift and not alt:
                if key_code in con.ctrlKeys:
                    key = con.ctrlKeys[key_code]
                    self.term.send_input(key)
            if shift and not ctrl and not alt:
                if key_code in con.shiftKeys:
                    key = con.shiftKeys[key_code]
                    self.term.send_input(key)

    @staticmethod
    def is_shift_pressed():
        left, right = pr.is_key_down(pr.KEY_LEFT_SHIFT), pr.is_key_down(
            pr.KEY_RIGHT_SHIFT
        )
        if left == True or right == True:
            return True
        else:
            return False

    @staticmethod
    def is_ctrl_pressed():
        left, right = pr.is_key_down(pr.KEY_LEFT_CONTROL), pr.is_key_down(
            pr.KEY_RIGHT_SHIFT
        )
        if left == True or right == True:
            return True
        else:
            return False

    @staticmethod
    def is_alt_pressed():
        left, right = pr.is_key_down(pr.KEY_LEFT_ALT), pr.is_key_down(pr.KEY_RIGHT_ALT)
        if left == True or right == True:
            return True
        else:
            return False

    def get_modifier_state(self) -> tuple:
        return (self.is_shift_pressed(), self.is_ctrl_pressed(), self.is_alt_pressed())

    def display_output(self):
        # pr.draw_text(self.displayString, 10, 10, 12, con.TEXT)
        draw_pos = [0, 0]
        for line in self.canvas:
            for cell in line:
                pr.draw_text(cell.text, draw_pos[1], draw_pos[0], 12, self.text_col)
                draw_pos[0] += self.character_size[0]

            draw_pos[0] = 0
            draw_pos[1] += self.character_size[1]

    def handle_escape_sequence(self, byte):
        self.ESCBuffer += byte
        byteVal = ord(byte)
        print(f"Escape Sequence Byte: 0x{byte.hex()}")

        # CSI Sequence (ESC[)
        if len(self.ESCBuffer) == 1 and byte == b"[":
            print("In CSI/C2 Escape Sequence")
            self.inCSI = True
            return
        if self.inCSI:  # Handle CSI Sequences
            if 0x40 <= byteVal <= 0x7E:
                print(f"Ending CSI Sequence with Final Byte: 0x{byte.hex()}")
                self.handle_csi_sequence()
                self.end_escape_sequence()
                return
            return

        # C1 Control Codes
        if (
            len(self.ESCBuffer) == 1 and 0x40 <= byteVal <= 0x5F
        ):  # byte > b"\x40" and byte < b"\x5f":
            # https://en.wikipedia.org/wiki/C0_and_C1_control_codes
            print(f"C1 Control Cdoe: ESC{chr(byteVal)}")
            self.inFE = True
            self.end_escape_sequence()

        # C0 Single Character Escape Sequences
        if len(self.ESCBuffer) == 1 and (
            0x60 <= byteVal <= 0x7E or 0x20 <= byteVal <= 0x2F
        ):
            print(f"C0 Single Character Escape: ESC{chr(byte(val))}")
            self.end_escape_sequence()
            return

    def handle_csi_sequence(self):
        sequence = self.ESCBuffer.decode("utf-8", errors="ignore")
        print(f"Handling CSI Sequence: ESC{sequence}")
        final_byte = sequence[-1] if sequence else ""

        match final_byte:
            case "K":  # Erase in Line
                print("Erase in Line (K)")
                for x in range(self.cursor.x, self.width):
                    self.canvas[x][self.cursor.y].text = ""
            case "J":  # Erase in Display
                print("Erase in Display (J)")
                for x in range(self.width):
                    for y in range(self.height):
                        self.canvas[x][y].text = ""
            case "H" | "f":  # Cursor Position
                print(f"Cursor Position ({final_byte})")
                self.cursor.x = 0
                self.cursor.y = 0
            case _:
                print(f"Unhandled CSI Sequence: {final_byte}")

    def end_escape_sequence(self):
        self.InEscapeSequence = False
        self.inCSI = False
        self.inFE = False
        self.ESCBuffer = bytearray()
        print("Escape Sequence Ended")

    @staticmethod
    def update_colours(obj):
        if obj.in_dark_mode:
            obj.background_col = con.BASE
            obj.second_background = con.MANTLE
            obj.text_col = con.TEXT
        else:
            obj.background_col = con.TEXT
            obj.second_background = con.OVERLAY2
            obj.text_col = con.BASE


class SettingsWindow:
    def __init__(self, parent):
        self.background_col = parent.background_col
        self.second_background = parent.second_background
        self.text_col = parent.text_col
        self.in_dark_mode = parent.in_dark_mode
        self.parent = parent
        print("Creating new Window")
        pr.init_window(con.WIDTH-80, con.HEIGHT-40, "Settings")
        print("New Window Created")
        self.settings = button.Button((25, 100, 200, 40), "Toggle Dark mode", self.second_background, self.text_col)
        
        self.close_butt = button.Button((con.WIDTH - 80 - 40, 20, 40, 40), "X", self.second_background, self.text_col)
    

    def toggle_dark_mode(self, butt):
        if self.in_dark_mode:
            self.in_dark_mode = False
        else:
            self.in_dark_mode = True
        
        self.parent.update_colours(self)
        # Write the new config to file
        self.parent.config['config']['dark_mode'] = str(self.in_dark_mode)
        with open('config.ini', 'w') as f:
            self.parent.config.write(f)

    def run(self):
        should_exit = False
        while not should_exit:
            pr.begin_drawing()
            pr.clear_background(self.background_col)
            pr.draw_text("Settings", 24, 24, 48, self.text_col)

            self.settings.render_button()
            if self.settings.is_clicked(pr.get_mouse_position()):
                self.toggle_dark_mode(self.settings)

            self.close_butt.render_button()
            if self.close_butt.is_clicked(pr.get_mouse_position()):
                should_exit = True

            pr.end_drawing()

        pr.close_window()
        a = MainWindow()
        a.run()
