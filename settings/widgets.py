from libqtile import widget

# ----------- Widgets ----------- #

colors = dict(
  bg = '#282a36',
  fg = '#f8f8f2',
  black = '#44475a',
  color2 = '#6272a4',
  cyan = '#8be9fd',
  green = '#70fa66',
  orange = '#f0983c',
  pink = '#ff55c6',
  purple = '#7777ff',
  red = '#ff1155',
  yellow = '#f1fa8c'
)

def Base(bg='bg', fg='fg'):
  return dict(
    background = colors[bg],
    foreground = colors[fg],
  )

def parse_texts(text):
  for string in [" - Brave"]: 
    text = text.replace(string, "") 
    return text 

def powerline(fg='fg', bg='bg'):
  return widget.TextBox(
    " ",
    background = colors[bg],
    foreground = colors[fg],
    fontsize = 35,
    padding = -2
  )

def icon(fg='fg', bg='black', fontsize=16, text="?"):
  return widget.TextBox(
    **Base(bg, fg),
    fontsize=fontsize,
    text=text,
    padding=5
  )

def separator(bg='bg'):
  return widget.TextBox(**Base(bg), linewidth=0, padding=5)

def workspaces():
  return [
    widget.GroupBox(
      background=colors['bg'],
      foreground=colors['fg'], 
      font='UbuntuMono Nerd Font',
      fontsize=20,
      margin_y=2,
      margin_x=0,
      padding_y=18,
      padding_x=6,
      borderwidth=2,
      active=colors['fg'],
      inactive=colors['black'],
      rounded=False,
      highlight_method='line',
      highlight_color=[colors['bg']],
      urgent_alert_method='block',
      urgent_border=colors['red'],
      this_current_screen_border=colors['purple'],
      this_screen_border=colors['orange'],
      other_current_screen_border=colors['cyan'],
      other_screen_border=colors['yellow'],
    ),

    widget.WindowName(
      **Base(fg='black'),
      format='{name}', 
      padding=1,
      parse_text=parse_texts
    ),
  ]
  

widgets = [
  *workspaces(), 

  powerline(bg='black', fg='bg'),

  icon(bg='black', text=' ' ),

  widget.Clock(**Base('black'), fontsize=17, format="%I:%M:%S"),

  powerline(bg='purple', fg='black'),

  icon(bg='purple', text=' '),

  widget.Net(
    **Base('purple'), 
    format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}",
    interface='wlan0'
  ),

  powerline(bg='pink', fg='purple'),

  icon(bg='pink',fontsize=18, text=' '),

  widget.CheckUpdates( 
    background=colors['pink'],
    fontsize=19,
    colour_have_updates=colors['fg'],
    colour_no_updates=colors['fg'],
    no_update_string='0',
    display_format='{updates}',
    update_interval=300,
    distro='Arch'
  ),

  powerline(bg='red', fg='pink'),

  icon(bg='red',fontsize=18, text=' '),

  widget.CPU(**Base(bg='red'), format='{freq_current}GHz'),

  powerline(bg='green', fg='red'),

  icon(bg='green', fg='black', fontsize=20, text="󰕾 "),

  widget.Volume(
    **Base(bg="green", fg='black'),
    volume_app='pulseaudio',
    get_volume_command='pamixer --get-volume-human',
    volume_up_command='pamixer --increase 5',
    volume_down_command='pamixer --decrease 5',
    update_interval=0.1,
    channel='Master'
  ),

  widget.Cmus(
    **Base(bg='green', fg='black'),
    play_color=colors['black'],
    noplay_color=colors['black'],
    padding=5,
    play_icon=' ',
    format='{play_icon} - {title}',
    update_interrval=0.2,
    width=100,
    scroll=True,
  ),

  powerline(bg='orange', fg='green'),

  widget.CurrentLayoutIcon(**Base(bg='orange'), scale=0.8),

  widget.CurrentLayout(**Base('orange'), fontsize=18),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=17,
    padding=3,
)

extension_defaults = widget_defaults.copy()