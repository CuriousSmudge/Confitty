import pyray as pr
from ui import con
from processing import terminal
from dataclasses import dataclass

@dataclass
class Cell():
    text: str = ""

@dataclass
class Cursor():
    x: int = 0
    y: int = 0 

class Window():
    def __init__(self):
        pr.init_window(con.WIDTH, con.HEIGHT, "Confitty")
        pr.set_target_fps(60)
        self.term = terminal.Terminal()
        
        self.width = 80
        self.height = 80

        self.character_size = (10, 10)

        self.displayString = ""
        # self.canvas = [[Cell()]*10]*10
        self.canvas = [[Cell() for i in range(self.width)] for j in range(self.height)]
        self.cursor = Cursor()
        self.InEscapeSequence = False
        self.ESCBuffer = bytearray()
        print("Terminal has started in raylib")
        self.run()

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(con.BASE)
            self.run_terminal()
            self.display_output()
            self.get_inputs()
            pr.end_drawing()

        pr.close_window()
    
    def run_terminal(self):
        if self.term.processID == 0:
            # pty.fork(), Slave/child process always has processID == 0
            return
        
        # Get the inputs and outputs and then check them
        byte = self.term.read_master()
        if self.InEscapeSequence:
            self.handle_escape_sequence(byte) 
        match byte:
            case b"\n":
                self.cursor.y += 1
                self.cursor.x = 0
                print("Newline")
            case b"\r":
                pass
            case b"\x07":
                print("BEEP")
            case b"\x08":
                self.displayString = self.displayString[:-1]
            case b"\x09":
                print("Tab Stop")
            case b"\0x0D":
                pass
            case b"0x0E":
                print("G1 Character Set")
            case b"0x0F":
                print("G0 Character Set")
            case b"0x1B":
                # Start escape sequence
                self.InEscapeSequence = True
            case None:
                pass
            case _:
                print(f"byte: 0x{byte.hex()}")
                s = byte.decode('utf-8')
                print(f"String: {s}")
                self.canvas[self.cursor.x][self.cursor.y].text = s
                self.cursor.x += 1
                # self.displayString += s
    
    def get_inputs(self):
        if (key_code := pr.get_key_pressed()):
            key = con.keys[key_code]
            self.term.send_input(key)
    
    def display_output(self):
        # pr.draw_text(self.displayString, 10, 10, 12, con.TEXT)

        draw_pos = [0, 0]
        for line in self.canvas:
            for cell in line:
                pr.draw_text(cell.text, draw_pos[1], draw_pos[0], 12, con.TEXT)
                draw_pos[0] += self.character_size[0]

            draw_pos[0] = 0
            draw_pos[1] += self.character_size[1]

    def handle_escape_sequence(byte):
        self.ESCBuffer += byte
        match ESCBuffer:
            case b"c" | b"D" | b"E" | b"H" | b"M" | b"Z" | b"7" | b"8" | b"":
                pass
            case _:
                pass