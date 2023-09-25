screen minimap():
    $config.allow_skipping = False
    $config.keymap["dismiss"] = []
    imagebutton:
        idle "Cera_idle.gif"
        pos (.1, .1)
        action [Hide("minimap"), Jump("testing")]
    imagebutton:
        idle "Cera_idle.gif"
        pos (.3, .3)
    imagebutton:
        idle "Cera_idle.gif"
        pos (.5, .5)
    imagebutton:
        idle "Cera_idle.gif"
        pos (.7, .5)
    imagebutton:
        idle "Cera_idle.gif"
        pos (.5, .3)
    imagebutton:
        idle "Cera_idle.gif"
        pos (.8, .3)
    