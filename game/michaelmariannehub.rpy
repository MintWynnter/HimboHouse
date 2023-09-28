label marianne_hub:

    menu:
        "\"Is there something I can do for you, [marianne_name]?\"" if marianne_queststate is 1:
            jump marianne_startquest
            # this is the topic that jumps to

        "\"I have the camcorder you were asking for.\"" if marianne_queststate is 3:
            jump marianne_gotcamcorder


        "\"See you later, [marianne_name].\"":
            # a goodbye line
            if marianne_queststate is 2:
                jump marianne_abouttoleave
