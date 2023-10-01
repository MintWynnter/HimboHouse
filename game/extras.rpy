style tembuttons:
    hover_color "#FF90F4"
    size 90

style bembuttons:
    hover_color "#FF90F4"
    size 48

init:
    transform headzoom:
        zoom .456

screen extras(mtype, subtype):
    tag menu
    add "gui/setting_bg.png"
    textbutton "ART":
        text_style "tembuttons"
        if mtype == "Art":
            text_color "#F4BB4F"
        xpos .101563
        ypos .038889
        action ShowMenu("extras", "Art", "Characters")
    textbutton "MUSIC":
        text_style "tembuttons"
        if mtype == "Music":
            text_color "#F4BB4F"
        xpos .271354
        ypos .038889
        action ShowMenu("extras", "Music", "1")
    textbutton "CREDITS":
        text_style "tembuttons"
        if mtype == "Credits":
            text_color "#F4BB4F"
        xpos .498958
        ypos .038889
        action ShowMenu("extras", "Credits", "")
    textbutton "TITLE":
        text_style "tembuttons"
        xpos .768229
        ypos .038889
        action ShowMenu("main_menu")
    if mtype == "Art":
        textbutton "CHARACTERS":
            text_style "bembuttons"
            if subtype == "Characters":
                text_color "#F4BB4F"
            xpos .145313
            ypos .903704
            action ShowMenu("extras", "Art", "Characters")
        textbutton "BACKGROUNDS":
            text_style "bembuttons"
            if subtype == "Backgrounds":
                text_color "#F4BB4F"
            xpos .421875
            ypos .903704
            action ShowMenu("extras", "Art", "Backgrounds")
        textbutton "OTHERS":
            text_style "bembuttons"
            if subtype == "Others":
                text_color "#F4BB4F"
            xpos .719227
            ypos .903704
            action ShowMenu("extras", "Art", "Others")
        if subtype == "Characters":
            imagebutton:
                idle "images/headshot_lysander.png"
                xpos .134375
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_herman.png"
                xpos .290104
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_elizabeth.png"
                xpos .445833
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_marianne.png"
                xpos .601563
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_abbe.png"
                xpos .744792
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_presper.png"
                xpos .134375
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_aures.png"
                xpos .290104
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_minoru.png"
                xpos .445833
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_abbe.png"
                xpos .601563
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_amalgam.png"
                xpos .744792
                ypos .565741
                at headzoom
        if subtype == "Backgrounds":
            imagebutton:
                idle "images/headshot_lysander.png"
                xpos .134375
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_herman.png"
                xpos .290104
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_elizabeth.png"
                xpos .445833
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_marianne.png"
                xpos .601563
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_abbe.png"
                xpos .744792
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_presper.png"
                xpos .134375
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_aures.png"
                xpos .290104
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_minoru.png"
                xpos .445833
                ypos .565741
                at headzoom