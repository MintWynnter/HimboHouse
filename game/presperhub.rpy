label presper_hub:

    # custom greeting

label presper_convohub:

    menu:

        "\"Start the midpoint event, please.\"":
            jump midpoint
        "\"Have you seen a camcorder around here?\"" if marianne_queststate is 10:
            jump marianne_presper

        "Search for Herman's signet ring." if herman_queststate is 5:
            jump herman_basement

        "\"How are you still alive?\"":
            #voice drht-01
            dr "Truth be told, I couldn’t tell you with certainty."
            #voice drht-02
            dr "Most of my organs have failed on me altogether, some more essential than others."
            #voice drht-03
            dr "At this point, I keep them mostly for the sentimental value."
            #voice drht-04
            dr "Luckily, my darlings have plenty of organs in tip-top shape, so we like to share."
            "He picks up the tubes dangling from one arm."
            #voice drht-05
            dr "What’s theirs is mine, and vice versa."
            #voice drht-06
            dr "We make an excellent team, that way."
            jump presper_convohub

        "\"Do you know the other ghosts in this mansion?\"":
            "The old man ponders the question."
            #voice drht-07
            dr "I know of them, but to say I know them or know them well would be incorrect."
            #voice drht-08
            dr "Some make their presence known more than others."
            #voice drht-09
            dr "I’ll tell you, anyone within a mile can hear that young girl when she’s having her tantrum."
            #voice drht-10
            dr "But, beyond recognizing their noises, I do not make a point to know them."
            jump presper_convohub

        "\"Why did you make me?\"":
            #voice drht-11
            dr "I am a scientist. What do you expect of me but to experiment?"
            #voice drht-12
            dr "And although your shelf life leaves something to be desired…"
            #voice drht-13
            dr "I’ve certainly learned a great many things for next time."
            jump presper_convohub

        "\"Who was I in life, before you made me a zombie?\"":
            #voice drht-14
            dr "What, your body?"
            #voice drht-15
            dr "A gravedigger. Digging graves on private property."
            #voice drht-16
            dr "It was self-defense. I won’t speak more of it."
            jump presper_convohub


        "\"See ya later, Presper.\"":
            # a goodbye line
            call screen minimap()
