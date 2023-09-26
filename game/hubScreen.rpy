screen hubScreen(character):
    $config.allow_skipping = False
    $config.keymap["dismiss"] = []
    #show minoru neutral at spritezoom
    #w "This is where the character would be, if we had the sprites right now."
    imagebutton:
        idle "gui/button/Start.png"
        pos (.25, .5)
        action [Hide("hubScreen"), Jump("testing")]
    imagebutton:
        idle "gui/button/Start.png"
        pos (.5, .5)
        action [Hide("hubScreen"), Jump("testing")]
    imagebutton:
        idle "gui/button/Start.png"
        pos (.75, .5)
        action [Hide("hubScreen"), Jump("testing")]