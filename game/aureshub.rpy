

label auresHub:
    #greeting
    if auresQuestState == 7:
        if killPath:
            jump auresScene7K
        else:
            jump auresScene7NK
    menu:
        "\"Is there something I can do for you, Aures?\"":
            if auresQuestState == 2:
                jump auresScene2
            elif auresQuestState == 3:
                jump auresScene3
            elif auresQuestState == 4:
                jump auresScene4
            elif auresQuestState == 6:
                if killPath:
                    jump auresScene6K
                else:
                    jump auresScene6NK
            elif auresQuestState == 8:
                jump auresScene8

        "Hand Aures the teleporter." if auresQuestState is 5 and hasTeleporter:
            jump auresScene5

        "\"I want to talk to you.\"":
            au "What would you like to talk about?"
            #put conversation options here

        "\"See you later, Aures.\"":

            # a goodbye line

            call screen minimap()