import os
from libqtile.config import Screen, Group, DropDown
from libqtile import bar, qtile, widget, layout, extension
from libqtile.lazy import lazy
from modules.colors import tokyonight as cl
from typing import List
from libqtile.widget import spacer



# color def
dark = cl[0]
greys = cl[1]
light = cl[2]
text = cl[3]
focus = cl[4]
inactive = cl[5]
urgent = cl[6]
color1 = cl[7]
color2 = cl[8]
color3 = cl[9]
color4 = cl[10]
color5 = cl[11]
newBG = cl[12]

layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": focus,
                "border_normal": greys
                }

floating_layout = layout.Floating(
        border_with = 2,
        margin = 6,
        border_focus = focus,
        border_normal = greys,
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

def base(fg=3, bg=12, fontsize=15, font='HackNerdFont', padding=3): 
    return {
        'foreground': cl[fg],
        'background': cl[bg],
        'fontsize'  : fontsize,
        'font'      : font,
        'padding'   : padding
    }


def open_sep(fg): 
    return  widget.TextBox(foreground=fg, background=cl[12], font='HackNerdFont', padding=3, fontsize=15, text = '[')


def close_sep(fg): 
    return  widget.TextBox(foreground=fg, background=cl[12], font='HackNerdFont', padding=3, fontsize=15, text = ']')


def icon():
    return [
        open_sep(color2),
        widget.TextBox(**base(fg=8),text = '󰟪'),
        close_sep(color2)
    ]


def cpu_info():
    return [
        open_sep(focus),
        widget.CPU(**base(fg=4), format=' CPU {load_percent}%'),
        widget.ThermalSensor(**base(fg=4), format='󰔏 {temp:.0f}{unit} ', threshold=85, foreground_alert= '#FF0000'),
        close_sep(focus)
    ]


def memory():
    return [
        open_sep(color4),
        widget.Memory(**base(fg=10), format=' {MemUsed: .1f}{mm}', measure_mem='G'),
        close_sep(color4)
    ]


def net():
    return [
        open_sep(color5),
        widget.Net(**base(fg=11, padding=5), format="󰈀 {down} ↓↑ {up}", perfix = "k"),
        close_sep(color5)
    ] 


def current_lay():
    return [
        open_sep(urgent),
        widget.CurrentLayout(**base(fg=6)),
        close_sep(urgent)
    ] 


def volume():
    return [
        open_sep(color3),
        widget.TextBox(**base(fg=9), text = ' '),
        widget.PulseVolume(**base(fg=9), limit_max_volume = "True"),
        close_sep(color3)
    ]


def test():
    return [
        open_sep(cl[9]),
        widget.CurrentLayout(**base(fg=6)),
        close_sep(cl[9])
    ]


def battery():
    return [
        open_sep(color2),
        widget.Battery(
            **base(fg=8),
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
        close_sep(color2)
    ] 



def timedate():
    return [
        open_sep(color1),
        widget.Clock(**base(fg=7), format="󰸗 %d %b, %Y 󰥔 %H:%M", mouse_callbacks={"Button1": lazy.spawn("show_cal")}),
        close_sep(color1)
    ]


def workspaces():
    return [
        widget.GroupBox(
            **base(fg=6),
            disable_drag = True,
            center_aligned = True,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            highlight_method = "line",
            rounded = True,
            inactive = color1,
            active = urgent,
            highlight_color = inactive,
            this_current_screen_border = color3,
            this_screen_border = color3,
            other_current_screen_border = color4,
            other_screen_border = color4,
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
            *test(),
            *current_lay(),
        ],
        25,
        margin = [5, 6, 0, 6]
    ),),

]
