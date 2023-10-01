init:
    transform chibizoom:
        zoom .1

screen minimap():
    $config.allow_skipping = False
    $config.keymap["dismiss"] = []
    imagebutton:
        idle "chibi_elizabeth.png"
        pos (.1, .1)
        action [Hide("minimap"), Jump("liz")]
        at chibizoom
    imagebutton:
        idle "chibi_lysander.png"
        pos (.3, .3)
        action [Hide("minimap"), Jump("lysan")]
        at chibizoom
    imagebutton:
        idle "chibi_marianne.png"
        pos (.5, .5)
        action [Hide("minimap"), Jump("mari")]
        at chibizoom
    imagebutton:
        idle "chibi_aures.png"
        pos (.7, .5)
        action [Hide("minimap"), Jump("testing")]
        at chibizoom
    imagebutton:
        idle "chibi_herman.png"
        pos (.5, .3)
        action [Hide("minimap"), Jump("herman")]
        at chibizoom
    imagebutton:
        idle "chibi_arabella.png"
        pos (.8, .3)
        action [Hide("minimap"), Jump("arabella")]
        at chibizoom
    imagebutton:
        idle "question_mark.png"
        pos (.8, .7)
        action [Hide("minimap"), Jump("presper_hub")]
        at chibizoom
