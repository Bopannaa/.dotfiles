#!/usr/bin/env python3
from libqtile import widget
import colors

colors = colors.Palenight

widgetlist1 = [
                widget.GroupBox(),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.CurrentLayoutIcon(scale = 0.6),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.Prompt(),
                widget.WindowName(background = colors[2], foreground = colors[8]),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.Systray(background = colors[0], foreground = colors[5]),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.Memory(background = colors[0], foreground = colors[5]),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.CPU(background = colors[0], foreground = colors[5]),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background = colors[0], foreground = colors[5]),
                widget.TextBox("", background = colors[0], foreground = colors[4], fontsize=18),
]

widgetlist2 = [
                widget.CurrentLayoutIcon(scale = 0.6),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(background = colors[2], foreground = colors[8]),

                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.Memory(background = colors[0], foreground = colors[5]),

                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.CPU(background = colors[0], foreground = colors[5]),

                widget.TextBox("  ", background = colors[0], foreground = colors[6], fontsize=15),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background = colors[0], foreground = colors[5]),

                widget.Systray(background = colors[0], foreground = colors[5]),
]

widgetlist3 = [
                widget.CurrentLayoutIcon(scale = 0.6),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(background = colors[2], foreground = colors[8]),

                widget.Spacer(background = colors[0], length = 10),

                widget.Image(filename = "~/.config/qtile/icons/ram-memory.png", background = colors[0], margin = 2),
                widget.Memory(background = colors[0], foreground = colors[5],format = '{MemUsed: .0f}{mm}'),

                widget.Spacer(background = colors[0], length = 10),

                widget.Image(filename = "~/.config/qtile/icons/cpu.png", background = colors[0], margin = 3),
                widget.CPU(background = colors[0], foreground = colors[5],format = '{load_percent}%'),

                widget.Spacer(background = colors[0], length = 10),

                widget.Image(filename = "~/.config/qtile/icons/schedule.png", background = colors[0], margin = 2),
                widget.Clock(format="%d-%m-%Y %a %I:%M %p", background = colors[0], foreground = colors[5]),

                widget.Spacer(background = colors[0], length = 10),

                widget.Systray(background = colors[0], foreground = colors[5]),
]

widgetlist = widgetlist3
