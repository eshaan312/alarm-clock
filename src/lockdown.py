import os

def begin():
    os.system("rm ~/.config/sxhkd/sxhkdrc")
    os.system("cp ~/.config/sxhkd/sxhkdrc_nac ~/.config/sxhkd/sxhkdrc")
    os.system("pkill -USR1 -x sxhkd")

    keymap_disabler = "xmodmap"
    keys = [64, 108, 37, 105, 122, 123, 121]
    for key in keys:
        keymap_disabler += f" -e 'keycode {key} = NoSymbol'"
    os.system(keymap_disabler)

def end():
    os.system("cat ~/.config/sxhkd/ac >> ~/.config/sxhkd/sxhkdrc")
    os.system("pkill -USR1 -x sxhkd")
    os.system("setxkbmap")
