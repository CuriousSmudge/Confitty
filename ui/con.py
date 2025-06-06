import pyray as pr

WIDTH = 800
HEIGHT = 450

keys = {
    # Letters
    65: "a", 66: "b", 67: "c", 68: "d", 69: "e", 70: "f", 71: "g", 72: "h", 73: "i",
    74: "j", 75: "k", 76: "l", 77: "m", 78: "n", 79: "o", 80: "p", 81: "q", 82: "r",
    83: "s", 84: "t", 85: "u", 86: "v", 87: "w", 88: "x", 89: "y", 90: "z",
    
    # Capital Letters (when shift is held)
    '65_shift': "A", '66_shift': "B", '67_shift': "C", '68_shift': "D", '69_shift': "E",
    '70_shift': "F", '71_shift': "G", '72_shift': "H", '73_shift': "I", '74_shift': "J",
    '75_shift': "K", '76_shift': "L", '77_shift': "M", '78_shift': "N", '79_shift': "O",
    '80_shift': "P", '81_shift': "Q", '82_shift': "R", '83_shift': "S", '84_shift': "T",
    '85_shift': "U", '86_shift': "V", '87_shift': "W", '88_shift': "X", '89_shift': "Y",
    '90_shift': "Z",
    
    # Numbers (top row)
    48: "0", 49: "1", 50: "2", 51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9",
    
    # Special characters
    32: " ",        # SPACE
    39: "'",        # APOSTROPHE
    44: ",",        # COMMA
    45: "-",        # MINUS
    46: ".",        # PERIOD
    47: "/",        # SLASH
    59: ";",        # SEMICOLON
    61: "=",        # EQUAL
    91: "[",        # LEFT_BRACKET
    92: "\\",       # BACKSLASH
    93: "]",        # RIGHT_BRACKET
    96: "`",        # GRAVE
    
    # Numpad
    320: "0",       # KP_0
    321: "1",       # KP_1
    322: "2",       # KP_2
    323: "3",       # KP_3
    324: "4",       # KP_4
    325: "5",       # KP_5
    326: "6",       # KP_6
    327: "7",       # KP_7
    328: "8",       # KP_8
    329: "9",       # KP_9
    330: ".",       # KP_DECIMAL
    331: "/",       # KP_DIVIDE
    332: "*",       # KP_MULTIPLY
    333: "-",       # KP_SUBTRACT
    334: "+",       # KP_ADD
    335: "\n",      # KP_ENTER
    336: "=",       # KP_EQUAL
    
    # Control keys
    257: "\n",      # ENTER
    258: "\t",      # TAB
    259: "\b",      # BACKSPACE
    260: "\x1b[D",  # RIGHT (escape sequence for terminal)
    261: "\x1b[C",  # LEFT (escape sequence for terminal)
    262: "\x1b[A",  # UP (escape sequence for terminal)
    263: "\x1b[B",  # DOWN (escape sequence for terminal)
    264: "\x1b[H",  # HOME (escape sequence for terminal)
    265: "\x1b[F",  # END (escape sequence for terminal)
    266: "\x1b[5~", # PAGE_UP (escape sequence for terminal)
    267: "\x1b[6~", # PAGE_DOWN (escape sequence for terminal)
    268: "\x1b",    # INSERT (escape)
    269: "\x7f",    # DELETE (DEL)
    280: "\x1b",    # ESCAPE
    340: "",        # LEFT_SHIFT (no character)
    341: "",        # LEFT_CONTROL (no character)
    342: "",        # LEFT_ALT (no character)
    343: "",        # LEFT_SUPER (no character)
    344: "",        # RIGHT_SHIFT (no character)
    345: "",        # RIGHT_CONTROL (no character)
    346: "",        # RIGHT_ALT (no character)
    347: "",        # RIGHT_SUPER (no character)
    348: "",        # KB_MENU (no character)
    
    # Shifted symbols (when shift is held)
    # These would typically be handled by the application logic
    # based on whether shift is pressed
    '48_shift': ")",    # SHIFT + 0
    '49_shift': "!",    # SHIFT + 1
    '50_shift': "@",    # SHIFT + 2
    '51_shift': "#",    # SHIFT + 3
    '52_shift': "$",    # SHIFT + 4
    '53_shift': "%",    # SHIFT + 5
    '54_shift': "^",    # SHIFT + 6
    '55_shift': "&",    # SHIFT + 7
    '56_shift': "*",    # SHIFT + 8
    '57_shift': "(",    # SHIFT + 9
    '59_shift': ":",    # SHIFT + ;
    '61_shift': "+",    # SHIFT + =
    '44_shift': "<",    # SHIFT + ,
    '45_shift': "_",    # SHIFT + -
    '46_shift': ">",    # SHIFT + .
    '47_shift': "?",    # SHIFT + /
    '91_shift': "{",    # SHIFT + [
    '92_shift': "|",    # SHIFT + \
    '93_shift': "}",    # SHIFT + ]
    '96_shift': "~",    # SHIFT + `
    '39_shift': "\"",   # SHIFT + '
    
    # Terminal control sequences (Ctrl + key combinations)
    '65_ctrl': "\x01",  # CTRL + A (Start of heading)
    '66_ctrl': "\x02",  # CTRL + B (Start of text)
    '67_ctrl': "\x03",  # CTRL + C (End of text / SIGINT)
    '68_ctrl': "\x04",  # CTRL + D (End of transmission / EOF)
    '69_ctrl': "\x05",  # CTRL + E (Enquiry)
    '70_ctrl': "\x06",  # CTRL + F (Acknowledge)
    '71_ctrl': "\x07",  # CTRL + G (Bell)
    '72_ctrl': "\x08",  # CTRL + H (Backspace)
    '73_ctrl': "\x09",  # CTRL + I (Horizontal tab)
    '74_ctrl': "\x0A",  # CTRL + J (Line feed)
    '75_ctrl': "\x0B",  # CTRL + K (Vertical tab)
    '76_ctrl': "\x0C",  # CTRL + L (Form feed)
    '77_ctrl': "\x0D",  # CTRL + M (Carriage return)
    '78_ctrl': "\x0E",  # CTRL + N (Shift out)
    '79_ctrl': "\x0F",  # CTRL + O (Shift in)
    '80_ctrl': "\x10",  # CTRL + P (Data link escape)
    '81_ctrl': "\x11",  # CTRL + Q (Device control 1)
    '82_ctrl': "\x12",  # CTRL + R (Device control 2)
    '83_ctrl': "\x13",  # CTRL + S (Device control 3)
    '84_ctrl': "\x14",  # CTRL + T (Device control 4)
    '85_ctrl': "\x15",  # CTRL + U (Negative acknowledge)
    '86_ctrl': "\x16",  # CTRL + V (Synchronous idle)
    '87_ctrl': "\x17",  # CTRL + W (End of transmission block)
    '88_ctrl': "\x18",  # CTRL + X (Cancel)
    '89_ctrl': "\x19",  # CTRL + Y (End of medium)
    '90_ctrl': "\x1A",  # CTRL + Z (Substitute / SIGTSTP)
    '91_ctrl': "\x1B",  # CTRL + [ (Escape)
    '92_ctrl': "\x1C",  # CTRL + \ (File separator / SIGQUIT)
    '93_ctrl': "\x1D",  # CTRL + ] (Group separator)
    '94_ctrl': "\x1E",  # CTRL + ^ (Record separator)
    '95_ctrl': "\x1F",  # CTRL + _ (Unit separator)
    
    # Function keys
    290: "\x1bOP",     # F1
    291: "\x1bOQ",     # F2
    292: "\x1bOR",     # F3
    293: "\x1bOS",     # F4
    294: "\x1b[15~",   # F5
    295: "\x1b[17~",   # F6
    296: "\x1b[18~",   # F7
    297: "\x1b[19~",   # F8
    298: "\x1b[20~",   # F9
    299: "\x1b[21~",   # F10
    300: "\x1b[23~",   # F11
    301: "\x1b[24~",   # F12
}

# Catppuccin Mocha Color Palette
# Base
BASE = pr.Color(30, 30, 46, 255)        # #1e1e2e
MANTLE = pr.Color(24, 24, 37, 255)      # #181825
CRUST = pr.Color(17, 17, 27, 255)       # #11111b

# Text
TEXT = pr.Color(205, 214, 244, 255)     # #cdd6f4
SUBTEXT0 = pr.Color(166, 173, 200, 255) # #a6adc8
SUBTEXT1 = pr.Color(186, 194, 222, 255) # #bac2de

# Surface
SURFACE0 = pr.Color(49, 50, 68, 255)    # #313244
SURFACE1 = pr.Color(69, 71, 90, 255)    # #45475a
SURFACE2 = pr.Color(88, 91, 112, 255)   # #585b70

# Overlay
OVERLAY0 = pr.Color(108, 112, 134, 255) # #6c7086
OVERLAY1 = pr.Color(127, 132, 156, 255) # #7f849c
OVERLAY2 = pr.Color(147, 153, 178, 255) # #9399b2

# Colors
ROSEWATER = pr.Color(245, 224, 220, 255) # #f5e0dc
FLAMINGO = pr.Color(242, 205, 205, 255)  # #f2cdcd
PINK = pr.Color(245, 194, 231, 255)      # #f5c2e7
MAUVE = pr.Color(203, 166, 247, 255)     # #cba6f7
RED = pr.Color(243, 139, 168, 255)       # #f38ba8
MAROON = pr.Color(235, 160, 172, 255)    # #eba0ac
PEACH = pr.Color(250, 179, 135, 255)     # #fab387
YELLOW = pr.Color(249, 226, 175, 255)    # #f9e2af
GREEN = pr.Color(166, 227, 161, 255)     # #a6e3a1
TEAL = pr.Color(148, 226, 213, 255)      # #94e2d5
SKY = pr.Color(137, 220, 235, 255)       # #89dceb
SAPPHIRE = pr.Color(116, 199, 236, 255)  # #74c7ec
BLUE = pr.Color(137, 180, 250, 255)      # #89b4fa
LAVENDER = pr.Color(180, 190, 254, 255)  # #b4befe
