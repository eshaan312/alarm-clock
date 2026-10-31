# alarm-clock
personal project to get me to wake up

# why
I tried this app called alarmy which made you do puzzles to wake up, but in the morning I just started powering off my phone or uninstalling the app rather than waking up. In order to make a more foolproof version for myself, I designed this program to be similar to Alarmy, but it uses the window manager and keymap changing to stop me from figuring out a way to turn off the alarm without solving the puzzle. I also taped a quarter over the power button several times over so I have no way out.

# requires
use sxhkd, x11, polybar (not required but if you use any other bars, you gotta replace this), alacritty (you have to start the program in this or change the code), xmodmap, setxkbmap. i use bspwm but im pretty sure nothing i used requires it explicitly.      
        
in your sxkhd config, have 3 files ready: one called sxhkdrc (your main one, unchanged); a second one called sxhkdrc_nac (your main one, without audio controls); and a third one called ac (just the audio conttols that sxhkdrc_nac removes.).         
         
you can super easily modify the program in the main and lockdown files to fit your environment.