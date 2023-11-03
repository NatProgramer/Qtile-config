from libqtile import layout
from settings.keys import keys, mod
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.path import path, qtile_path

import subprocess

from libqtile import hook

# ----------- Autostart ----------- #

@hook.subscribe.startup_once
def autostart():
  subprocess.call([path.join(qtile_path, 'autostart.sh')])

# ----------- Global Variables ----------- #

auto_fullscreen = True
bring_front_click = False
cursor_warp = True
dgroups_key_binder = None
dgroups_app_rules = []
floats_kept_above = True
focus_on_window_activation = "smart"
follow_mouse_focus = True
reconfigure_screens = True
wmname = "LG3D"
auto_minimize = True
wl_input_rules = None