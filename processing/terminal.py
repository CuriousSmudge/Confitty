import sys
import os
import pty
import termios
import tty
import select

BUFFER_READ_BYTES = 1024


class Terminal:
    def __init__(self):
        self.shellPath = self.get_shell()
        self.initiate_shell(self.shellPath)

    def get_shell(self):
        shellPath = os.getenv("SHELL")
        if shellPath is None:
            print("ERROR: Shell path not found - Did you install a shell?")
            raise OSError
        else:
            return shellPath

    def initiate_shell(self, shellPath):
        self.processID, self.master = pty.fork()

        if self.processID == 0:
            print("Shell Initiated")
            os.execvp(shellPath, [shellPath])

    def enter_raw_mode(self):
        # Backs up the terminal configuration so emulator can be reverted
        print("Entering Raw Mode")
        self.backup = termios.tcgetattr(sys.stdin)
        print("Terminal backed up successfully")
        tty.setraw(sys.stdin.fileno())

    def check_input(self, rlist):
        # Reads from the user input to find stdin
        if sys.stdin in rlist:
            inputs = os.read(sys.stdin.fileno(), BUFFER_READ_BYTES)
            if not inputs:
                return
            os.write(self.master, inputs)

    def check_output(self, rlist):
        # Reads from the user to find stdout (returned from master)
        if self.master in rlist:
            output = os.read(self.master, BUFFER_READ_BYTES)
            if not output:
                return
            os.write(sys.stdout.fileno(), output)

    def run(self):
        if self.processID == 0:
            # pty.fork(), Slave/child process always has processID == 0
            print("Slave refused access")
            return
        self.enter_raw_mode()

        try:
            while True:
                # Get the inputs and outputs and then check them
                rlist, _, _ = select.select([sys.stdin, self.master], [], [])
                self.check_input(rlist)
                self.check_output(rlist)
        finally:
            print("Restoring...")
            self.restore_terminal()
            print("Terminal restored. Quitting...")

    def restore_terminal(self):
        if self.backup:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.backup)
