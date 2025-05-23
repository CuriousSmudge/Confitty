import pyray as pr
import select
from ui import con
import sys
from processing import terminal

class Window():
    def __init__(self):
        pr.init_window(800, 450, "Confitty")
        pr.set_target_fps(60)
        self.term = terminal.Terminal()
        self.displayString = ""
        print("Terminal has started in raylib")
        self.run()

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            print("Drawing has been started")
            pr.clear_background(con.BASE)
            print("Background blackened")

            self.run_terminal()

            self.display_output()
            print("Terminal has been run")
            self.get_inputs()
            print("Inputs have been gotten")
            pr.end_drawing()
            print("Drawing finished")

        pr.close_window()
    
    def run_terminal(self):
        print("Checking Slave")
        if self.term.processID == 0:
            # pty.fork(), Slave/child process always has processID == 0
            print("Slave refused access")
            return
        print("Slave checked")
        
        # Get the inputs and outputs and then check them
        output = self.term.read_master()
        if not output is None:
            self.displayString += output
    
    def get_inputs(self):
        print(pr.get_key_pressed)
        if (key_code := pr.get_key_pressed()):
            key = con.keys[key_code]
            print(key)
            self.term.send_input(key)
    
    def display_output(self):
        pr.draw_text(self.displayString, 10, 10, 12, con.TEXT)

    def update_ui():
        ...