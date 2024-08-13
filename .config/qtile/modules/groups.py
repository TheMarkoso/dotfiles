from libqtile.config import Group, ScratchPad, DropDown, EzKey as Key
from libqtile.lazy import lazy
from modules.ezkeys import keys
from modules.prefs import terminal 

groups = [Group(i) for i in [
    "一", "二", "三", "四", "五", "六"
    ]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key('M-'+actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key('M-S-'+actual_key, lazy.window.togroup(group.name))
        ])
