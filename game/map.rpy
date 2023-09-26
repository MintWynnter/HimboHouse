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
        idle "Cera_idle.gif"
        pos (.7, .5)
        action [Hide("minimap"), Jump("testing")]
    imagebutton:
        idle "Cera_idle.gif"
        pos (.5, .3)
        action [Hide("minimap"), Jump("testing")]
    imagebutton:
        idle "Cera_idle.gif"
        pos (.8, .3)
        action [Hide("minimap"), Jump("testing")]
    