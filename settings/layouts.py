from libqtile import layout
from libqtile.config import Match

# ----------- Layouts ----------- #

def Base():
  return dict(
    border_focus="#6099ee",
    border_width=1,
    margin=2
  )

layouts = [
  layout.Max(),
  layout.Bsp(**Base(), lower_righ=False),
  layout.Matrix(**Base()),
  layout.MonadTall(**Base()),
  layout.MonadWide(**Base()),
  layout.RatioTile(**Base()),
]

# Floating layout

floating_layout = layout.Floating(
  float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),
    Match(wm_class="makebranch"),
    Match(wm_class="maketag"),
    Match(wm_class="ssh-askpass"),
    Match(title="branchdialog"),
    Match(title="pinentry"),
  ]
)
