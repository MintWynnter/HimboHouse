label presper_hub:

    menu:
        "\"Have you seen a camcorder around here?\"" if marianne_queststate is 10:
            jump marianne_presper

        "\"See ya later, Presper.\"":
            call screen minimap()
