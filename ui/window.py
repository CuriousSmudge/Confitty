import pyray as pr
import select
import sys
from processing import terminal

keys = {
    65: "a",
    66: "b",
    67: "c",
    257: "/n"
}

class Window():
    def __init__(self):
        pr.init_window(800, 450, "Confitty")
        pr.set_target_fps(60)
        self.term = terminal.Terminal()
        print("Terminal has started in raylib")
        self.run()

    def run(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            print("Drawing has been started")
            self.run_terminal()
            print("Terminal has been run")
            self.get_inputs()
            print("Inputs have been gotten")
            pr.clear_background(pr.BLACK)
            print("Background blackened")
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
        rlist, _, _ = select.select([self.term.master], [], [])
        print("rlist Obtained")
        # self.term.check_input(rlist)
        output = self.term.check_output(rlist)
        print("Output checked")
        if output:
            print("Output found, displaying...")
            self.display_output(output)
    
    def get_inputs(self):
        print(pr.get_key_pressed)
        if (key_code := pr.get_key_pressed()):
            key = keys[key_code]
            print(key)
            self.term.send_input(key)
    
    def display_output(self, output: str):
        print(output)
        pr.draw_text(output, 190, 200, 20, pr.WHITE)
        return
        
    def update_ui():
        ...