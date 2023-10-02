# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    transform spritezoom:
        zoom .1
    transform splashy:
        zoom .537815

define a = Character("Aures", image="aures")
define w = Character("Minoru", image="minoru")
image splash = "images/splash.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash at splashy
    with Pause(2)

    hide splash
    with Pause(1)

    return

transform lysander_spot:
    xpos 550 ypos 0

transform aures_spot:
    xpos 200 ypos 0

transform elizabeth_spot:
    xpos 300 ypos 70

transform marianne_spot:
    xpos 550 ypos 0

transform presper_spot:
    xpos 550 ypos 0

transform minoru_spot:
    xpos 200 ypos 0

transform arabella_spot:
    xpos 300 ypos 50

transform herman_spot:
    xpos 825 ypos 0

# The game starts here.

label start:
    $ quick_menu = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.\
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])

    #debugparty
    #$ elizabeth_queststate = 1
    #$ lysander_queststate = 2
    #$herman_queststate = 1
    #$q3_state = 1
    #$ marianne_queststate = 1
    #$ auresQuestState = 2

    jump gameintro

    call screen minimap()



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
    jump lysander_garden
    call screen hubScreen("Lysander")
    return

label liz:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump elizabeth_livingroom
    call screen hubScreen("Elizabeth")
    return

label aures:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump aures_ballroom
    w "This is where Aures's stuff will be."
    call screen hubScreen("Aures")
    return

label herman:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump herman_lounge
    call screen hubScreen("Herman")
    return

label arabella:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump arabella_foyer
    call screen hubScreen("Arabella")
    return

label mari:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump marianne_bedroom
    call screen minimap()

label pres:
    hide aures
    show minoru neutral at spritezoom
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
    jump presper_hub
    call screen minimap()
