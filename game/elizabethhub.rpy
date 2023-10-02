label elizabeth_hub:

    default el_greeting_1 = True
    default el_greeting_2 = True
    default el_greeting_3 = True
    default el_greeting_4 = True
    default el_greeting_5 = True

    default el_farewell_1 = True
    default el_farewell_2 = True
    default el_farewell_3 = True
    default el_farewell_4 = True
    default el_farewell_5 = True
    

    show elizabeth neutral at elizabeth_spot
    with dissolve

    # custom greeting
    if el_greeting_1:
        $ el_greeting_1 = False
        #voice "elg-01"
        el "*gasp and a small shriek*"
    elif el_greeting_2:
        $ el_greeting_2 = False
        #voice "elg-02"
        el "You're back! What took you so long?!"
    elif el_greeting_3:
        $ el_greeting_3 = False
        #voice "elg-03"
        el "*gasp* Oh it's you! Geez, don't scare me like that!"
    elif el_greeting_4:
        $ el_greeting_4 = False
        #voice "elg-04"
        el "*sniffles* I... I thought you wouldn't come back..."
    elif el_greeting_5:
        $ el_greeting_5 = False
        #voice "elg-05"
        el "Hi! Uum, I didn't touch anything, I promise."
    else:
        $ el_greeting_1 = True
        $ el_greeting_2 = True
        $ el_greeting_3 = True
        $ el_greeting_4 = True
        $ el_greeting_5 = True
        #voice "elg-06"
        el "... Oh! Umm..."





label elizabeth_convohub:

    #show elizabeth neutral or whatever

    menu:

        "\"Still looking for your pen and paper, Elizabeth.\"" if elizabeth_queststate is 2:
            el "OK! Thanks for telling me!"
            jump elizabeth_convohub

        "\"I brought you what you asked for, Elizabeth.\"" if elizabeth_queststate is 3:
                jump elizabeth_gotpaperpen

        "\"Be careful where you throw things, you almost hit me earlier!":
            "The little girl crosses her arms and pouts."
            el "It was just a pillow, you know."
            el "Are you scared of pillows or something?"
            jump elizabeth_convohub

        "Check the living room for information about Lysander's situation." if lysander_queststate > 1 and lysander_queststate < 5:
            jump lysander_livingroom

        "Check the living room for information on Arabella." if q3_state is 1 and not q3_mom_journal:
            jump arabella_motherjournal

        "Check the living room for a photograph that might pertain to Herman." if herman_queststate is 3:
            jump herman_livingroom

        "\"Goodbye, Elizabeth.\"":
            # goodbye message
            if el_farewell_1:
                $ el_farewell_1 = False
                #voice "elf-01"
                el "Promise me, you'll be back soon. Please..."
            elif el_farewell_2:
                $ el_farewell_2 = False
                #voice "elf-02"
                el "Please be careful of the strangers out there..."
            elif el_farewell_3:
                $ el_farewell_3 = False
                #voice "elf-03"
                el "Can't you just stay here?... Nevermind..."
            elif el_farewell_4:
                $ el_farewell_4 = False
                #voice "elf-04"
                el "Okay... I'll be good and wait here."
            elif el_farewell_5:
                $ el_farewell_5 = False
                #voice "elf-05"
                el "Okay... bye..."
            else:
                $ el_farewell_1 = True
                $ el_farewell_2 = True
                $ el_farewell_3 = True
                $ el_farewell_4 = True
                $ el_farewell_5 = True
                #voice "elf-06"
                el "You're not leaving because of me, right? Promise?"

            call screen minimap()
