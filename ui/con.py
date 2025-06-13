import pyray as pr

WIDTH = 800
HEIGHT = 450

keys = {
    # Letters
    65: "a", 66: "b", 67: "c", 68: "d", 69: "e", 70: "f", 71: "g", 72: "h", 73: "i",
    74: "j", 75: "k", 76: "l", 77: "m", 78: "n", 79: "o", 80: "p", 81: "q", 82: "r",
    83: "s", 84: "t", 85: "u", 86: "v", 87: "w", 88: "x", 89: "y", 90: "z",
    
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

shiftKeys = {
    # Capital letters
    pr.KEY_A: 'A', pr.KEY_B: 'B', pr.KEY_C: 'C', pr.KEY_D: 'D', pr.KEY_E: 'E',
    pr.KEY_F: 'F', pr.KEY_G: 'G', pr.KEY_H: 'H', pr.KEY_I: 'I', pr.KEY_J: 'J',
    pr.KEY_K: 'K', pr.KEY_L: 'L', pr.KEY_M: 'M', pr.KEY_N: 'N', pr.KEY_O: 'O',
    pr.KEY_P: 'P', pr.KEY_Q: 'Q', pr.KEY_R: 'R', pr.KEY_S: 'S', pr.KEY_T: 'T',
    pr.KEY_U: 'U', pr.KEY_V: 'V', pr.KEY_W: 'W', pr.KEY_X: 'X', pr.KEY_Y: 'Y',
    pr.KEY_Z: 'Z',
    
    # Shifted numbers (symbols)
    pr.KEY_ONE: '!', pr.KEY_TWO: '@', pr.KEY_THREE: '#', pr.KEY_FOUR: '$',
    pr.KEY_FIVE: '%', pr.KEY_SIX: '^', pr.KEY_SEVEN: '&', pr.KEY_EIGHT: '*',
    pr.KEY_NINE: '(', pr.KEY_ZERO: ')',
    
    # Shifted punctuation
    pr.KEY_MINUS: '_',
    pr.KEY_EQUAL: '+',
    pr.KEY_LEFT_BRACKET: '{',
    pr.KEY_RIGHT_BRACKET: '}',
    pr.KEY_BACKSLASH: '|',
    pr.KEY_SEMICOLON: ':',
    pr.KEY_APOSTROPHE: '"',
    pr.KEY_GRAVE: '~',
    pr.KEY_COMMA: '<',
    pr.KEY_PERIOD: '>',
    pr.KEY_SLASH: '?',
}

ctrlKeys = {
    pr.KEY_A: '\x01', pr.KEY_B: '\x02', pr.KEY_C: '\x03', pr.KEY_D: '\x04',
    pr.KEY_E: '\x05', pr.KEY_F: '\x06', pr.KEY_G: '\x07', pr.KEY_H: '\x08',
    pr.KEY_I: '\x09', pr.KEY_J: '\x0a', pr.KEY_K: '\x0b', pr.KEY_L: '\x0c',
    pr.KEY_M: '\x0d', pr.KEY_N: '\x0e', pr.KEY_O: '\x0f', pr.KEY_P: '\x10',
    pr.KEY_Q: '\x11', pr.KEY_R: '\x12', pr.KEY_S: '\x13', pr.KEY_T: '\x14',
    pr.KEY_U: '\x15', pr.KEY_V: '\x16', pr.KEY_W: '\x17', pr.KEY_X: '\x18',
    pr.KEY_Y: '\x19', pr.KEY_Z: '\x1a',
    pr.KEY_LEFT_BRACKET: '\x1b',    # Ctrl + [
    pr.KEY_BACKSLASH: '\x1c',       # Ctrl + \
    pr.KEY_RIGHT_BRACKET: '\x1d',   # Ctrl + ]
    pr.KEY_GRAVE: '\x1e',           # Ctrl + `
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
