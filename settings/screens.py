from libqtile import bar
from libqtile.config import Screen
from .widgets import widgets, colors

screens = [
  Screen(
    top=bar.Bar(
      widgets, 
      27, 
      background=colors["bg"],
      foreground=colors["fg"]
    ),
  ),
]