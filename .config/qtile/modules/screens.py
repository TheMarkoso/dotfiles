import os
from libqtile.config import Screen, Group, DropDown
from libqtile import bar, qtile, widget, layout, extension
from libqtile.lazy import lazy
from modules.colors import tokyonight as cl
from typing import List
from libqtile.widget import spacer



# color def
dark = cl[0]
grey = cl[1]
light = cl[2]
text = cl[3]
focus = cl[4]
inactive = cl[5]
urgent = cl[6]
color1 = cl[7]
color2 = cl[8]

layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": cl[4],
                "border_normal": cl[1]
                }

floating_layout = layout.Floating(
        border_with = 2,
        margin = 6,
        border_focus = cl[4],
        border_normal = cl[1],
        )

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
]

#widget_defaults = dict(
#    font = 'HackNerdFont',
#    fontsize = 15,
#    padding = 3,
#    foreground = cl[15],
#    background = cl[0]
#)

def base(fg=3, bg=0, fontsize=15, font='HackNerdFont', padding=3): 
    return {
        'foreground': cl[fg],
        'background': cl[bg],
        'fontsize'  : fontsize,
        'font'      : font,
        'padding'   : padding
    }


def open_sep(): 
    return  widget.TextBox(**base(), text = '[')


def close_sep(): 
    return  widget.TextBox(**base(), text = ']')


def icon():
    return [
        open_sep(),
        widget.TextBox(**base(),text = '󰟪'),
        close_sep()
    ]


def cpu_info():
    return [
        open_sep(),
        widget.CPU(**base(), format=' CPU {load_percent}%'),
        widget.ThermalSensor(**base(), format='󰔏 {temp:.0f}{unit} ', threshold=85, foreground_alert= '#FF0000'),
        close_sep()
    ]


def memory():
    return [
        open_sep(),
        widget.Memory(**base(), format=' {MemUsed: .1f}{mm}', measure_mem='G'),
        close_sep(),
    ]


def net():
    return [
        open_sep(),
        widget.Net(**base(padding=5), format="󰈀 {down} ↓↑ {up}", perfix = "k"),
        close_sep(),
    ] 


def current_lay():
    return [
        open_sep(),
        widget.CurrentLayoutIcon(**base(), custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")], scale=0.7),
        close_sep(),
    ] 


def volume():
    return [
        open_sep(),
        widget.TextBox(**base(), text = ' '),
        widget.PulseVolume(**base(), limit_max_volume = "True"),
        close_sep(),
    ]


def battery():
    return [
        open_sep(),
        widget.Battery(
            **base(),
            format='{char} {percent:2.0%}',
            full_char='󰁹', 
            charge_char='󰂄', 
            discharge_char='󱟞',
            empty_char='󰂃', 
            not_charging_char='󰚥',
            low_foreground= '#FF0000', 
            low_percentage = 0.2, 
            notify_below=20, 
            show_short_text=False, 
        ),
        close_sep(),
    ] 



def timedate():
    return [
        open_sep(),
        widget.TextBox(**base(), text = " "), 
        widget.Clock(**base(), format="󰸗 %d %b, %Y 󰥔 %H:%M", mouse_callbacks={"Button1": lazy.spawn("show_cal")}),
        close_sep()
    ]


def workspaces():
    return [
        widget.GroupBox(
            **base(),
            disable_drag = True,
            center_aligned = True,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            highlight_method = "line",
            rounded = True,
            inactive = cl[1],
            active = cl[5],
            highlight_color = cl[3],
            this_current_screen_border = cl[5],
            this_screen_border = cl[5],
            other_current_screen_border = cl[2],
            other_screen_border = cl[2],
        ),
    ]

def sep():
    return widget.Spacer(**base())


screens = [
    Screen(
        top=bar.Bar(
        [
            *icon(), 
            *memory(), 
            *cpu_info(),
            *net(),
            sep(),
            *workspaces(),
            sep(),
            *current_lay(),
            *volume(),
            *battery(),
            *timedate()
        ],
        25,
        margin = [5, 6, 0, 6]
    ),),
    Screen(
        top=bar.Bar(
        [
            *icon(), 
            sep(),
            *workspaces(),
            sep(),
            *current_lay(),
        ],
        25,
        margin = [5, 6, 0, 6]
    ),),

]
