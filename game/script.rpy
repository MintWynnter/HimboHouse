﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    transform spritezoom:
        zoom .1

define a = Character("Aures", image="aures")
define w = Character("Minoru", image="minoru")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aures yanderepose at spritezoom

    call screen minimap()

    # These display lines of dialogue.
label testing:
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    a "Why are you here? This part is not done yet."

    # This ends the game.

    return

label lysan:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    w "This is where Lysander's stuff will be."
    call screen hubScreen("Lysander")
    return

label liz:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    w "This is where Elizabeth's's stuff will be."
    call screen hubScreen("Elizabeth")
    return

label mari:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    w "This is where Marianne's stuff will be."
    call screen hubScreen("Marianne")
    return
