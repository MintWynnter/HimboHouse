label elizabeth_hub:

    # custom greeting


label elizabeth_convohub:

    #show elizabeth neutral or whatever

    menu:

        "\"Still looking for your pen and paper, Elizabeth.\"" if elizabeth_queststate is 2:
            el "OK! Thanks for telling me!"
            jump elizabeth_convohub

        "\"Be careful where you throw things, you almost hit me earlier!":
            "The little girl crosses her arms and pouts."
            el "It was just a pillow, you know."
            el "Are you scared of pillows or something?"
            jump elizabeth_convohub

        "Check the living room for information about Lysander's situation." if lysander_queststate is 2:
            jump lysander_livingroom

        "Check the living room for information on Arabella." if q3_state is 1 and not q3_mom_journal:
            jump arabella_motherjournal

        "\"Goodbye, Elizabeth.\"":
            # goodbye message
            call screen minimap()
