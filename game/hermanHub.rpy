label herman_hub:

    menu:
        "\"Is there something I can do for you, Herman?\"" if marianne_queststate is 1:
            jump marianne_startquest
            # this is the topic that jumps to


        "\"See you later, Herman.\"":
            # a goodbye line
            if marianne_queststate is 2:
                jump marianne_abouttoleave
            else:
                call screen minimap()