###################################################
#### QTILE CONFIGURATION FILE OF MARCO AGUIRRE ####
#
#___  ___           _                   __   ______
#|  \/  |          | |                 /  | |___  /
#| .  . | __ _ _ __| | _____  ___  ___ `| |    / / 
#| |\/| |/ _` | '__| |/ / _ \/ __|/ _ \ | |   / /  
#| |  | | (_| | |  |   < (_) \__ \ (_) || |_./ /   
#\_|  |_/\__,_|_|  |_|\_\___/|___/\___/\___/\_/


# IMPORTS
import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from widgets.volume_text import VolumeText
from widgets.battery_text import BatteryText
from tenet import tenet
from spotify import Spotify

# VARIABLES
mod = "mod4"                                # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"                            # My terminal of choice
myBrowser = "google-chrome-stable"          # My browser of choice
satan = tenet()

# KEYBINDINGS
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),


    # MY KEIBINDINGS
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    Key([mod, "shift"], "Return", lazy.spawn("cool-retro-term --fullscreen")),
    Key([mod], "space", lazy.spawn("rofi -show run"), desc="Abrir menu"),
    Key([mod], "b", lazy.spawn('firefox')),
    Key([mod], "g", lazy.spawn("betterlockscreen -l"), desc="lock screen"),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # ------------ Hardware Configs ------------

    #Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    #Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Volume / INSTALL 
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    #Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    
    #Instalar Pamixer
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    

    # Captura de pantalla
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),
    

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2800k"), desc="Luz Nocturna"),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x"), desc="Desactiva luz noctuRna")
]

# GROUPS
groups = [Group(i) for i in [
    "一", "二", "三", "四", "五", "六",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# SETTINGS FOR LAYOUTS
layout_conf = {
        'border_focus': '#2ac3de',
        'border_normal': ['#1a1b26','#1a1b26'], #6
        'border_width': 3,
        'margin': 6
        }

# LAYOUTS
layouts = [
        layout.Columns(**layout_conf),
        layout.Max(**layout_conf),
        layout.MonadTall(**layout_conf),
        layout.Matrix(**layout_conf),
        layout.Bsp(**layout_conf),
        ]


# COLORS
colors = [
        ["#1a1b26","#1a1b26"],  # 0 - dark/text
        ["#353c4a","#353c4a"],  # 1 - grey
        ["#f1ffff","#f1ffff"],  # 2 - light/active
        ["#bb9af7","#bb9af7"],  # 3 - focus
        ["#4c566a","#4c566a"],  # 4 - inactive
        ["#f7768e","#f7768e"],  # 5 - urgent
        ["#a151d3","#a151d3"],  # 6 - color 1
        ["#F07178","#F07178"],  # 7 - color 2
        ["#fb9f7f","#fb9f7f"],  # 8 - color 3
        ["#ffd47e","#ffd47e"],  # 9 - color 4
        ["#bf5db1","#bf5db1"]   # 10 - color 5
        ]


# COLORS TOKYO NIGHT
colors2 = [
        ['#f7768e','#f7768e'], #0
        ['#ff9e64','#ff9e64'], #1
        ['#e0af68','#e0af68'], #2
        ['#9ece6a','#9ece6a'], #3
        ['#73daca','#73daca'], #4
        ['#b4f9f8','#b4f9f8'], #5
        ['#2ac3de','#2ac3de'], #6
        ['#7dcfff','#7dcfff'], #7
        ['#7aa2f7','#7aa2f7'], #8
        ['#bb9af7','#bb9af7'], #9
        ['#c0caf5','#c0caf5'], #10
        ['#a9b1d6','#a9b1d6'], #11
        ['#9aa5ce','#9aa5ce'], #12
        ['#cfc9c2','#cfc9c2'], #13
        ['#565f89','#565f89'], #14
        ['#414868','#414868'], #15
        ['#24283b','#24283b'], #16
        ['#1a1b26','#1a1b26'], #17
        ]


# COLOR ALTERNATIVE
colors3 = [
        ['#6083AF','#6083AF'], #0
        ['#4F8085','#4F8085'], #1
        ['#326471','#326471'], #2
        ['#26525D','#26525D'], #3
        ['#1B414F','#1B414F'], #4
        ['#0B1D22','#0B1D22'], #5
        ['#1a1b26','#1a1b26'], #6
        ]


# COLOR FINAL
colors4 = [
        ['#7aa2f7','#7aa2f7'], #0
        ['#bb9af7','#bb9af7'], #1
        ['#73daca','#73daca'], #2
        ['#f7768e','#f7768e'], #3
        ['#ff9e64','#ff9e64'], #4
        ['#0B1D22','#0B1D22'], #5
        ['#1a1b26','#1a1b26'], #6
        ]



colors5 = [
        ['#7aa2f7','#7aa2f7'], #0
        ['#bb9af7','#bb9af7'], #1
        ['#ff9e64','#ff9e64'], #2
        ['#73daca','#73daca'], #3
        ['#f7768e','#f7768e'], #4
        ['#0B1D22','#0B1D22'], #5
        ['#1a1b26','#1a1b26'], #6
        ]



# DEFAULT WIDGETS SETTINGS
widget_defaults = {
        'font': 'JetBrainsMono Nerd Font',
        'fontsize': 18,
        'padding': 2,
        'background': colors3[5],
        }
extension_defaults = widget_defaults.copy()



# SCREENS/WIDGETS
screens = [
        Screen(
            top=bar.Bar(
                [
                # widget.KhalCalendar(),
                widget.Image(
                    filename='~/Descargas/pentagram_red.png',
                    mouse_callbacks={"Button1": lazy.spawn("notify-send '{0}\n HAIL SATAN!'".format(tenet()))},
                    ),
                widget.GroupBox(
                    font='JetBrainsMono Nerd Font',
                    fontsize=16,
                    foreground = colors3[4],
                    highlight_method="block",
                    highlight_color=["000000", "#1a1b26"],
                    ),
                # widget.CurrentLayout(),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.9,
                    use_mask=True,
                    ),
                Spotify(),
                widget.Spacer(),
                widget.Clock(
                    format='%H:%M:%S',
                    fontsize=16,
                    background=colors[0],
                    ),
                widget.Spacer(),

                # NET WIDGET
                widget.TextBox(
                    text=" ",
                    font="JetBrainsMono Nerd Font",
                    background=colors4[5],
                    foreground=colors4[0],
                    padding=-8,
                    fontsize=48,
                    ),
                widget.Net(
                    format='直 {down} ↓↑ {up}',
                    fontsize=16,
                    background=colors4[0],
                    foreground=colors4[6],
                    ),

                # VOLUME WIDGET
                widget.TextBox(
                    text="",
                    font="JetBrainsMono Nerd Font",
                    background=colors4[0],
                    foreground=colors4[1],
                    padding=-6,
                    fontsize=42,
                    ),
                #VolumeText(
                #    4,
                #    background=colors[8],
                #    foreground=colors[0],
                #    font="JetBrainsMono Nerd Font",
                #    fontsize=16,
                #    ),
                widget.TextBox(
                    text='墳',
                    background=colors4[1],
                    foreground=colors4[6],
                    fontsize=16,
                    ),
                widget.PulseVolume(
                    font='JetBrainsMono Nerd Font',
                    background=colors4[1],
                    foreground=colors4[6],
                    fontsize = 16,
                    ),

                # BLACKLIGHT WIDGET
                widget.TextBox(
                    text="",
                    font="JetBrainsMono Nerd Font",
                    background=colors4[1],
                    foreground=colors4[2],
                    padding=-6,
                    fontsize=42,
                    ),
                widget.TextBox(
                    "",
                    background=colors4[2],
                    foreground=colors4[6],
                    fontsize=16,
                    padding=5
                    ),
                widget.Backlight(
                    brightness_file="/sys/class/backlight/amdgpu_bl0/brightness",
                    max_brightness_file="/sys/class/backlight/amdgpu_bl0/max_brightness",
                    background=colors4[2],
                    foreground=colors4[6],
                    ),

                # BATERY WIDGET
                widget.TextBox(
                    text="",
                    font="JetBrainsMono Nerd Font",
                    background=colors4[2],
                    foreground=colors4[3],
                    padding=-6,
                    fontsize=42,
                    ),
                BatteryText(
                    10,
                    background=colors4[3],
                    foreground=colors4[6],
                    fontsize=16,
                    ),

                # POWER WIDGET
                widget.TextBox(
                    text="",
                    font="JetBrainsMono Nerd Font",
                    background=colors4[3],
                    foreground=colors4[4],
                    padding=-6,
                    fontsize=42,
                    ), 
                widget.TextBox(
                    text=" ",
                    background=colors4[4],
                    foreground=colors4[6],
                    fontsize=21,
                    mouse_callbacks={"Button1": lazy.spawn('rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu')},
                    ),

                    ],
                24,
                opacity=0.83,
                ),
            ),
        ]

# DRAG FLOATING LAYOUTS
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# STARTUP APPS
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


