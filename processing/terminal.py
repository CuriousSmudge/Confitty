import sys
import os
import pty
import termios
import tty
import select
import shutil

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

    def read_master(self):
        print("Entered read_master()")
        rlist, wlist, elist = select.select([self.master], [], [self.master], 0)
        print("rlist Obtained")
        if rlist or elist:
            for i in rlist:
                try:
                    byte = os.read(i, 1)
                except:
                    print("Shell exited")
                    os._exit(0)
                    return
                return self.handle_inputs(byte)
            for i in elist:
                print("Exception")
                return
    
    def handle_inputs(self, byte):
        print(f"Master PTY recieved: {byte}")
        if byte == b'\r':
            pass
        else:
            return byte.decode('utf-8')

    # def enter_raw_mode(self):
    #     # Backs up the terminal configuration so emulator can be reverted
    #     print("Entering Raw Mode")
    #     self.backup = termios.tcgetattr(sys.stdin)
    #     print("Terminal backed up successfully")
    #     tty.setraw(sys.stdin.fileno())

    # def restore_terminal(self):
    #     if self.backup:
    #         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.backup)

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