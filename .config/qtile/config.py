import os
import subprocess
from libqtile import hook


from modules.ezkeys import *
from modules.groups import *
from modules.screens import *


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
