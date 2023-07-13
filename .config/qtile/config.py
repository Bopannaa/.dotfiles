# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List

mod = "mod4"
myTerm = "alacritty"
myBrowser = "firefox"
sleepCommand = "sleep 1 && xset -display :0.0 dpms force off"
ssh_youtube = "sshpass -p '23121989' ssh bopanna@192.168.43.231 DISPLAY=:0 ytfzf -Df"
power_menu_cmd = "echo -e 'poweroff\nreboot\nsuspend' | dmenu -l 5 -fn 'Ubuntu-18' | xargs systemctl"


def power_menu(qtile):
    subprocess.run([power_menu_cmd], shell=True)

def Sleep_laptop(qtile):
    subprocess.run([sleepCommand], shell=True)

def browse_youtube_remote(qtile):
    subprocess.run([ssh_youtube], shell=True)

keys = [
    ### The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launches My Terminal"),
    Key([mod], "d", lazy.spawn("dmenu_run"), desc="Run Launcher"),
    Key([mod], "s", lazy.function(Sleep_laptop), desc="Laptop Sleep"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="Launch Firefox"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload Qtile Config"),
    Key([mod, "shift"], "q", lazy.function(power_menu), desc="Shutdown Qtile"),

    ### Window controls
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod],
        "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MonadTall), decrease number in master pane (Tile)",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Expand window (MonadTall), increase number in master pane (Tile)",
    ),
    Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    Key(
        [mod],
        "m",
        lazy.layout.maximize(),
        desc="toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    ### Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XmonadTall)",
    ),
    Key(
        [mod],
        "Tab",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),

    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    KeyChord(
        [mod],
        "e",
        [
            Key(
                [],
                "e",
                lazy.spawn("emacsclient -c -a 'emacs'"),
                desc="Emacsclient Dashboard",
            ),
            Key(
                [],
                "a",
                lazy.spawn(
                    "emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"
                ),
                desc="Emacsclient EMMS (music)",
            ),
            Key(
                [],
                "b",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                desc="Emacsclient Ibuffer",
            ),
            Key(
                [],
                "d",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                desc="Emacsclient Dired",
            ),
            Key(
                [],
                "i",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                desc="Emacsclient ERC (IRC)",
            ),
            Key(
                [],
                "n",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                desc="Emacsclient Elfeed (RSS)",
            ),
            Key(
                [],
                "s",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                desc="Emacsclient Eshell",
            ),
            Key(
                [],
                "v",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                desc="Emacsclient Vterm",
            ),
            Key(
                [],
                "w",
                lazy.spawn(
                    "emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"
                ),
                desc="Emacsclient EWW Browser",
            ),
        ],
    ),
    # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
    KeyChord(
        [mod],
        "p",
        [
            Key([], "y", lazy.spawn("ytfzf -Df"), desc="Browse Youtube"),
            Key([], "d", lazy.function(ssh_youtube), desc="Browse Youtube Remote"),
        ],
    ),
]

colors = [
    ["#282c34", "#282c34"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"],
]

groups = [
    Group("DEV", layout="monadtall"),
    Group("WWW", layout="monadtall"),
    Group("DOC", layout="monadtall"),
    Group("CHAT", layout="monadtall"),
    Group("MUS", layout="monadtall"),
    Group("VID", layout="monadtall"),
    Group("GFX", layout="floating"),
    Group("SYS", layout="monadtall"),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder

dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[6],  # "e1acff",
    "border_normal": "1D2330",
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    # layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="Ubuntu Bold", fontsize=10, padding=2, background=colors[2])
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.Image(
            filename="~/.config/qtile/icons/python-white.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm)},
        ),
        widget.Sep(linewidth=0, padding=6, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="474747",
            padding=2,
            fontsize=14,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7,
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0], padding=5),
        widget.TextBox(
            text="|",
            font="Ubuntu Mono",
            background=colors[0],
            foreground="474747",
            padding=2,
            fontsize=14,
        ),
        widget.WindowName(foreground=colors[6], background=colors[0], padding=0),
        widget.Systray(background=colors[0], padding=5),
        widget.Sep(linewidth=0, padding=6, foreground=colors[0], background=colors[0]),
        widget.Net(
            interface="wlan0",
            format="Net: {down} ↓↑ {up}",
            foreground=colors[1],
            background=colors[3],
            padding=5,
        ),
        widget.ThermalSensor(
            foreground=colors[1],
            background=colors[4],
            threshold=90,
            fmt="Temp: {}",
            padding=5,
        ),
        widget.Memory(
            foreground=colors[1],
            background=colors[6],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            fmt="Mem: {}",
            padding=5,
        ),
        widget.Volume(
            foreground=colors[1], background=colors[7], fmt="Vol: {}", padding=5
        ),
        widget.Clock(
            foreground=colors[1], background=colors[9], format="%A, %B %d - %H:%M "
        ),
    ]
    return widgets_list


def init_widgets_screen():
    widgets_screen = init_widgets_list()
    return widgets_screen


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20)),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen = init_widgets_screen()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),  # tastyworks exit box
        Match(title="Qalculate!"),  # qalculate-gtk
        Match(wm_class="kdenlive"),  # kdenlive
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])
    subprocess.call([home + "/.config/change_resolution.sh"])


wmname = "LG3D"
