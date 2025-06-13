import sys
import os
import pty
import select
import shutil
from ui import window

BUFFER_READ_BYTES = 1024


class Terminal:
    def __init__(self):
        self.masterRecvBuf = bytes()
        self.inEscape = False
        self.shellPath = self.get_shell()
        self.initiate_shell()
            
    def get_shell(self):
        shellPath = shutil.which("bash")
        if shellPath is None:
            print("ERROR: Shell path not found - Did you install a shell?")
            raise OSError
        else:
            return shellPath

    def initiate_shell(self):
        self.processID, self.master = pty.fork()
        if self.processID == 0:
            print("Shell Initiated")
            os.execvp(self.shellPath, [self.shellPath])

    def set_winsize(self, cols, rows):
        cols = con.WIDTH // self.character_size[0]
        rows = con.HEIGHT // self.character_size[1]
        winsize = struct.pack('HHHH', rows, cols, 0, 0)
        try:
            fcntl.ioctl(self.master, termios.TIOCSWINSZ, winsize)
            print(f"Terminal size set to {cols}x{rows}")
        except OSError as e:
            print(f"Failed to set terminal size: {e}")

    def read_master(self):
        rlist, wlist, elist = select.select([self.master], [], [self.master], 0)
        if rlist or elist:
            for i in rlist:
                try:
                    byte = os.read(i, 1)
                except:
                    print("Shell exited")
                    os._exit(0)
                    return
                return byte
            for i in elist:
                print("Exception")
                return

    def check_input(self, rlist):
        # Reads from the user input to find stdin
        if sys.stdin in rlist:
            inputs = os.read(sys.stdin.fileno(), BUFFER_READ_BYTES)
            if inputs:
                os.write(self.master, inputs)

    def check_output(self, rlist):
        # Reads from the user to find stdout (returned from master)
        if self.master in rlist:
            output = os.read(self.master, BUFFER_READ_BYTES)
            if output:
                # os.write(sys.stdout.fileno(), output)
                return output

    def send_input(self, key: str):
        b = key.encode('utf-8')
        os.write(self.master, b)