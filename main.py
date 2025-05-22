from processing import terminal
from ui import window


def main():
    Window = window.Window()
    Window.run()
    Term = terminal.Terminal()
    while True:
        Term.run()



if __name__ == "__main__":
    main()
