style tbmbuttons:
    hover_color "#FF90F4"
    size 90

style bbmbuttons:
    hover_color "#FF90F4"
    size 48

screen bigMenu(mtype, subtype):
    tag menu
    show "gui/setting_bg.png"
    textbutton "SAVE":
        text_style "tbmbuttons"
        if mtype == "Save":
            text_color "#F4BB4F"
        xpos .097917
        ypos .038889
        action ShowMenu("bigMenu", "Save")
    textbutton "LOAD":
        text_style "tbmbuttons"
        if mtype == "Load":
            text_color "#F4BB4F"
        xpos .28125
        ypos .038889
        action ShowMenu("bigMenu", "Load")
    textbutton "SETTINGS":
        text_style "tbmbuttons"
        if mtype == "Settings":
            text_color "#F4BB4F"
        xpos .478646
        ypos .038889
        action ShowMenu("bigMenu", "Settings")
    textbutton "TITLE":
        text_style "tbmbuttons"
        xpos .770833
        ypos .038889
        action ShowMenu("main_menu")
    textbutton "RETURN":
        hover_color "#FF90F4"

        xpos .770833
        ypos .038889
        action return
    
    if mtype == "Settings":

        