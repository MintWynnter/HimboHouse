init:
    transform chibizoom:
        zoom .1

screen minimap():
    $config.allow_skipping = False
    $config.keymap["dismiss"] = []
    zorder 99
    add "images/just_a_black_screen.png"
    add "images/mansionLayout.png"
    imagebutton:
        if elizabeth_queststate == 0:
            idle "question_mark.png"
        else:
            idle "chibi_elizabeth.png"
        pos (.1, .1)
        action [Hide("minimap"), Jump("liz")]
        at chibizoom
    imagebutton:
        if lysander_queststate == 0:
            idle "question_mark.png"
        else:
            idle "chibi_lysander.png"
        pos (.3, .3)
        action [Hide("minimap"), Jump("lysan")]
        at chibizoom
    imagebutton:
        if marianne_queststate == 0:
            idle "question_mark.png"
        else:
            idle "chibi_marianne.png"
        pos (.5, .5)
        action [Hide("minimap"), Jump("mari")]
        at chibizoom
    imagebutton:
        if auresQuestState == 1:
            idle "question_mark.png"
        else:
            idle "chibi_aures.png"
        pos (.7, .5)
        action [Hide("minimap"), Jump("aures")]
        at chibizoom
    imagebutton:
        if herman_queststate == 0:
            idle "question_mark.png"
        else:
            idle "chibi_herman.png"
        pos (.5, .3)
        action [Hide("minimap"), Jump("herman")]
        at chibizoom
    imagebutton:
        if q3_state == 0:
            idle "question_mark.png"
        else:
            idle "chibi_arabella.png"
        pos (.8, .3)
        action [Hide("minimap"), Jump("arabella")]
        at chibizoom
    imagebutton:
        if True:
            idle "question_mark.png"
        else:
            idle "question_mark.png"
        pos (.8, .7)
        action [Hide("minimap"), Jump("presper_hub")]
        at chibizoom
