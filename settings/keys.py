from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
  # ----------- Tiling Manage ----------- #

  # Focus
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "k", lazy.layout.up()),
  Key([mod], "space", lazy.layout.next()),

  # Move Windows
  Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
  Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
  Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
  Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

  # Grow or Shrink Windows
  Key([mod, "control"], "h", lazy.layout.grow_left()),
  Key([mod, "control"], "l", lazy.layout.grow_right()),
  Key([mod, "control"], "j", lazy.layout.grow_down()),
  Key([mod, "control"], "k", lazy.layout.grow_up()),

  # Toogle Floating 
  Key([mod, "shift"], "f", lazy.window.toggle_floating()),

  # Normalize
  Key([mod], "n", lazy.layout.normalize()),

  # Terminal
  Key([mod], "Return", lazy.spawn('/opt/Hyper/hyper')),

  # Change Layout
  Key([mod], "Tab", lazy.next_layout()),
  Key([mod, "shift"], "Tab", lazy.prev_layout()),

  # Kill Window
  Key([mod], "w", lazy.window.kill()),

  # To Fullscreen Window
  Key([], "F11", lazy.window.toggle_fullscreen()),
  
  # ----------- System ----------- #

  # Qtile
  Key([mod, "control"], "r", lazy.reload_config()),
  Key([mod, "control"], "q", lazy.shutdown()),

  # Active cmd Widget
  Key([mod], "r", lazy.spawncmd()),

  # ----------- Applications ----------- #

  # Browser
  Key([mod], "b", lazy.spawn('brave-browser-beta')),

  # Rofi
  Key([mod], "m", lazy.spawn("rofi -show drun")),
  Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

  # Volume
  Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
  Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
  
  # Brightness
  Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
  Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]