screen devChoice():
    $config.allow_skipping = False
    $config.keymap["dismiss"] = []
    #show minoru neutral at spritezoom
    #w "This is where the character would be, if we had the sprites right now."
    textbutton "Marie Minuet":
        pos (.25, .5)
        action [Hide("devChoice"), Jump("marMin")]
    textbutton "Dagon Grey":
        pos (.5, .5)
        action [Hide("devChoice"), Jump("Dagon")]
    textbutton "Rumi":
        pos (.75, .5)
        action [Hide("devChoice"), Jump("rumi")]
    textbutton "Maya":
        pos (.25, .25)
        action [Hide("devChoice"), Jump("maya")]
    textbutton "Jett":
        pos (.5, .25)
        action [Hide("devChoice"), Jump("Jett")]
    textbutton "Kat":
        pos (.75, .25)
        action [Hide("devChoice"), Jump("Kat")]
    textbutton "Faust":
        pos (.25, .75)
        action [Hide("devChoice"), Jump("Faust")]
    textbutton "Eufasy":
        pos (.5, .75)
        action [Hide("devChoice"), Jump("Eufasy")]
    textbutton "Elina":
        pos (.75, .75)
        action [Hide("devChoice"), Jump("elina")]
    textbutton "Michael":
        pos (.9, .25)
        action [Hide("devChoice"), Jump("michael")]
    textbutton "Mint":
        pos (.9, .5)
        action [Hide("devChoice"), Jump("mint")]
    textbutton "Kylie":
        pos (.9, .75)
        action [Hide("devChoice"), Jump("kylie")]
    textbutton "Max":
        pos (.9, .9)
        action [Hide("devChoice"), Jump("maxherz")]
    textbutton "Main Menu":
        pos (0, 0)
        action Return()