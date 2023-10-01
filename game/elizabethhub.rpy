label elizabeth_hub:

    show elizabeth neutral
    with dissolve

    # custom greeting


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
            call screen minimap()
