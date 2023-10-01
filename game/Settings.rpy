style tbmbuttons:
    hover_color "#FF90F4"
    size 90

style bbmbuttons:
    hover_color "#FF90F4"
    size 48

style smallbuttons:
    hover_color "#FF90F4"
    size 32

default variableName = 0

screen bigMenu(mtype, subtype):
    tag menu
    add "gui/setting_bg.png"
    textbutton "SAVE":
        text_style "tbmbuttons"
        if mtype == "Save":
            text_color "#F4BB4F"
        xpos .097917
        ypos .038889
        action ShowMenu("bigMenu", "Save", "1")
    textbutton "LOAD":
        text_style "tbmbuttons"
        if mtype == "Load":
            text_color "#F4BB4F"
        xpos .28125
        ypos .038889
        action ShowMenu("bigMenu", "Load", "1")
    textbutton "SETTINGS":
        text_style "tbmbuttons"
        if mtype == "Settings":
            text_color "#F4BB4F"
        xpos .478646
        ypos .038889
        action ShowMenu("bigMenu", "Settings", "Graphics")
    textbutton "TITLE":
        text_style "tbmbuttons"
        xpos .770833
        ypos .038889
        action ShowMenu("main_menu")
    textbutton "RETURN":
        text_style "smallbuttons"
        xpos .026563
        ypos .935185
        action Return()
    
    if mtype == "Settings":
        textbutton "GRAPHICS":
            text_style "bbmbuttons"
            if subtype == "Graphics":
                text_color "#F4BB4F"
            xpos .197396
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Graphics")
        textbutton "AUDIO":
            text_style "bbmbuttons"
            if subtype == "Audio":
                text_color "#F4BB4F"
            xpos .457813
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Audio")
        textbutton "CONTROLS":
            text_style "bbmbuttons"
            if subtype == "Controls":
                text_color "#F4BB4F"
            xpos .673958
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Controls")
        if subtype == "Graphics":
            text "Display" xpos .125 ypos .202778 size 48
            text "Skip" xpos .420833 ypos .202778 size 48
            text "Text Speed" xpos .125 ypos .39537 size 48
            text "Auto-Play Speed" xpos .125 ypos .55 size 48
            text "Skip Speed" xpos .125 ypos .7046296 size 48
            text "Slow" xpos .153125 ypos .466667 size 32
            text "Slow" xpos .153125 ypos .622222 size 32
            text "Fast" xpos .646354 ypos .466667 size 32
            text "Fast" xpos .646354 ypos .622222 size 32
            textbutton "Fullscreen":
                text_style "smallbuttons"
                xpos .153125
                ypos .262037
                action Preference("display", "fullscreen")
            textbutton "Windowed":
                text_style "smallbuttons"
                xpos .153125
                ypos .306481
                action Preference("display", "window")
            textbutton "Unseen Text":
                text_style "smallbuttons"
                xpos .445833
                ypos .262037
                action Preference("skip", "toggle")
            textbutton "After Choices":
                text_style "smallbuttons"
                xpos .445833
                ypos .306481
                action Preference("after choices", "toggle")
            hbox:
                style_prefix "slider"
                xpos .194792
                ypos .472222
                vbox:
                    if variableName == 1:
                        label "Weak"
                    if variableName == 2:
                        label "Normal"
                    bar value Preference("text speed")
            hbox:
                style_prefix "slider"
                xpos .194792
                ypos .626852
                vbox:
                    if variableName == 1:
                        label "Weak"
                    if variableName == 2:
                        label "Normal"
                    bar value Preference("auto-forward time")
        #have the settings be buttons that are super janky. Hopefully it uses the same style react does

        