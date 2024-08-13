from libqtile.config import EzKey as Key
from libqtile.lazy import lazy

from modules.prefs import terminal, browser, file_manager, screenshot, screenshot_manual, rofi, lockscreen, redshift_on, redshift_off, volume_up, volume_down, volume_mute, light_up, light_down



dots_terminal_sizes = {
    'width': 500,
    'height': 300,
    'x': 100,
    'y': 100
}


def dots_terminal(qtile):
    #Abre una terminal
    qtile.cmd_spawn("kitty")

    #Activa el modo flotante en la ventana actual
    qtile.current_window.toggle_floating()

    #Ajusta el tamano de la ventana flotante
    qtile.current_window.cmd_set_size_floating(
        dots_terminal_sizes['width'],
        dots_terminal_sizes['height'],
    )

    #Ajusta la posicion de la ventana
    qtile.current_window.cmd_set_position_floating(
        dots_terminal_sizes['x'],
        dots_terminal_sizes['y'],
    )


keys = [
    Key('M-d',                      lazy.function(dots_terminal),),
    # Switch between windows
    Key('M-h',                      lazy.layout.left(),                     desc='Move focus to left'),    
    Key('M-l',                      lazy.layout.right(),                    desc='Move focus to right'),    
    Key('M-j',                      lazy.layout.down(),                     desc='Move focus to down'),    
    Key('M-k',                      lazy.layout.up(),                       desc='Move focus to up'),    

    # Move windows between left/right columns or move up/down in current stack
    Key('M-S-h',                    lazy.layout.shuffle_left(),             desc='Move window to left'),
    Key('M-S-l',                    lazy.layout.shuffle_right(),            desc='Move window to right'),
    Key('M-S-j',                    lazy.layout.shuffle_down(),             desc='Move window to down'),
    Key('M-S-k',                    lazy.layout.shuffle_up(),               desc='Move window to up'),

    # Grow windows
    Key('M-C-h',                    lazy.layout.grow_left(),                desc='Grow window to left'),
    Key('M-C-l',                    lazy.layout.grow_right(),               desc='Grow window to right'),
    Key('M-C-j',                    lazy.layout.grow_down(),                desc='Grow window to down'),
    Key('M-C-k',                    lazy.layout.grow_up(),                  desc='Grow window to up'),
    Key('M-C-n',                    lazy.layout.normalize(),                desc='Reset all window size'),

    # Toggle between different layouts 
    Key('M-<Tab>',                  lazy.next_layout(),                     desc='Toggle between layouts'),

    # Toggle bar
    Key('M-S-b',                    lazy.hide_show_bar(),                   desc='Toggle bar'),

    # More Window Stuff
    Key('M-f',                      lazy.window.toggle_floating(),          desc='Toggle floating window'),
    Key('M-m',                      lazy.window.toggle_fullscreen(),        desc='Toggle fullscreen'),

    # Base Qtile
    Key('M-C-r',                    lazy.restart(),                         desc='Restart Qtile'),
    Key('M-C-q',                    lazy.shutdown(),                        desc='Shutdown Qtile'),
    Key('M-w',                      lazy.window.kill(),                     desc='Kill focused window'),

    # Launch Applications
    Key('M-<Space>',                lazy.spawn(rofi),                       desc='Launch Menu'),
    Key('M-<Return>',               lazy.spawn(terminal),                   desc='Launch Terminal'),
    Key('M-t',                      lazy.spawn(file_manager),               desc='Launch File Manager'),
    Key('M-b',                      lazy.spawn(browser),                    desc='Launch Browser'),
    Key('M-g',                      lazy.spawn(lockscreen),                 desc='Launch Lockscreen'),
    Key('M-r',                      lazy.spawn(redshift_on),                desc='Launch Redshift'),
    Key('M-S-r',                    lazy.spawn(redshift_off),               desc='Kill Redshift'),
    Key('M-s',                      lazy.spawn(screenshot),                 desc='Launch Screenshot Tool'),
    Key('M-S-s',                    lazy.spawn(screenshot_manual),          desc='Launch Screenshot Manual'),

    # Media Hotkeys
    # you need install "pulsectl_asymcio"
    Key('<XF86AudioRaiseVolume>',   lazy.spawn(volume_up),                  desc='Raise Volume'),
    Key('<XF86AudioLowerVolume>',   lazy.spawn(volume_down),                desc='Lower Volume'),
    Key('<XF86AudioMute>',          lazy.spawn(volume_mute),                desc='Mute Volume'),

    # Lights Hotkeys
    Key('<XF86MonBrightnessUp>',    lazy.spawn(light_up),                   desc='Raise Light'),
    Key('<XF86MonBrightnessDown>',  lazy.spawn(light_down),                 desc='Down Light'),
]

