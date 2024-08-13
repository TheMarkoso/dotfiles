import os
from libqtile.config import Screen, Group, DropDown
from libqtile import bar, qtile, widget, layout, extension
from libqtile.lazy import lazy
from modules.colors import colors as cl
from typing import List
from libqtile.widget import spacer


layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": cl[14],
                "border_normal": cl[2]
                }

floating_layout = layout.Floating(
        border_with = 2,
        margin = 6,
        border_focus = cl[14],
        border_normal = cl[2],
        )

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
]

widget_defaults = dict(
    font = 'HackNerdFont',
    fontsize = 15,
    padding = 3,
    foreground = cl[15],
    background = cl[0]
)

def open_sep(): 
    return  widget.TextBox(text = '[', fontsize = 20, font = 'HackNerdFont', foreground = cl[10], )

def close_sep(): 
    return  widget.TextBox(text = ']', fontsize = 20, font = 'HackNerdFont', foreground = cl[10], )



screens = [
    Screen(
        top=bar.Bar(
        [
            open_sep(),
            widget.TextBox(
                text = '󰟪',
                padding = 3,
                mouse_callbacks={"Button1": lazy.spawn('rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu')},
                ),
            close_sep(),

            open_sep(),
            widget.Memory(
                format=' {MemUsed: .1f}{mm}', 
                measure_mem='G', 
                ),
            close_sep(),

            open_sep(),
           widget.CPU(
                format=' CPU {load_percent}%', 
                ),
            widget.ThermalSensor(
                format='󰔏 {temp:.0f}{unit} ', threshold=85, foreground_alert= '#FF0000', 
                ),
            close_sep(),

            open_sep(),
            widget.Net(
                format="󰈀 {down} ↓↑ {up}",
                perfix = "k",
                padding = 5,
                ),
            close_sep(),


            widget.Spacer(),
            widget.GroupBox(
                font = 'HackNerdFont',
                disable_drag = True,
                center_aligned = True,
                fontsize = 17,
                margin_y = 3,
                margin_x = 0,
                padding_y = 5,
                padding_x = 3,
                borderwidth = 3,
                highlight_method = "line",
                rounded = True,
                inactive = cl[2],
                active = cl[15],
                highlight_color = cl[9],
                this_current_screen_border = cl[15],
                this_screen_border = cl[15],
                other_current_screen_border = cl[7],
                other_screen_border = cl[7],
                foreground = cl[15],
                background = cl[0]
                ),
            widget.Spacer(),

            open_sep(),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=cl[5],
                scale=0.7,
                ),
            close_sep(),

            open_sep(),
            widget.TextBox(
                text = ' ',
                ),
            widget.PulseVolume(
                limit_max_volume = "True",
                ),
            close_sep(),
            

            open_sep(),
            widget.Battery(
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

            open_sep(),
            widget.TextBox(
                text = " ",
                ), 
            widget.Clock(
                format="󰸗 %d %b, %Y 󰥔 %H:%M", 
                mouse_callbacks={"Button1": lazy.spawn("show_cal")}, 
                ),
            close_sep(),

        ],
        25,
        margin = [5, 6, 0, 6]
    ),),
]
