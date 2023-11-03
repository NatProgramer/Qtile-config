from libqtile.config import Group, Key
from libqtile.command import lazy
from .keys import keys, mod

# ----------- Groups ----------- #

groups = [Group(i) for i in [
  "   ", " 󰨞  ", "   ", "   ", " 󰉋  ", "   ", "   ", "   ", "   "
]]

for i, group in enumerate(groups):
  actual_key = str(i + 1)
  keys.extend([
    Key([mod], actual_key, lazy.group[group.name].toscreen()),
    Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
  ])