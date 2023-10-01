

label aures_hub:
    #greeting
    if auresQuestState == 7:
        if killPath:
            jump auresScene7K
        else:
            jump auresScene7NK

label aures_convohub:

    show aures neutral
    menu:
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 2:
            jump auresScene2
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 3:
            jump auresScene3
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 4:
            jump auresScene4
        "\"Remind me, what did you need of me?\"" if auresQuestState is 5 and not hasTeleporter:
            au "I needed a teleporter device, if you can find one."
            au "Go see Lysander, he's out in the garden."
            jump aures_convohub
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 6:
            if killPath:
                jump auresScene6K
            else:
                jump auresScene6NK
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 8:
            jump auresScene8
        "Hand Aures the teleporter." if auresQuestState is 5 and hasTeleporter:
            jump auresScene5

        "\"I want to talk to you.\"":
            au "What would you like to talk about?"
            jump aures_convohub
            #put conversation options here

        "\"See you later, Aures.\"":

            # a goodbye line

            call screen minimap()
