label gameintro:

    show bg mansion exterior
    $config.allow_skipping = True
    $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])

    "A mansion stands before you."
    menu:
        "It beckons you in."

        "Approach the front door of the mansion.":
            "A voice in the back of your head, echoing ever so slightly, lauds you."
            #voice abq0-01
            ab "A wise choice. Better in there than out here."

        "\"Wait, what? What’s going on?\"":
            "A voice in the back of your head, echoing ever so slightly, answers your question."
            #voice abq0-02
            ab "A pertinent question. It seems we’re a bit stranded."

        "Stay put. Gauge your surroundings.":
            "You twist your body and gaze into the dense forest all around you."
            "A voice in the back of your head, echoing ever so slightly, chimes in."
            #voice abq0-03
            ab "It seems we’re a bit stranded."

    "Sure enough, in every direction is the densest of foliage — the underbrush climbs up to the canopy, and the canopy hangs deep into the underbrush."
    "Not even the quaint dirt road on which you stand points to a clearing."
    "It only points to the mansion under which you stand."
    "The voice chimes in again."
    #voice abq0-04
    menu:
        ab "Do you see those lights there? Flickering inside?"

        "\"I do. What do you make of them?\"":
            #voice abq0-05
            ab "I’m not one to speculate. Or, we are not one to speculate."

        "\"Do I? Are you not me?\"":
            #voice abq0-06
            ab "Unclear. I will say, though: It’s quite roomy in here."

        "\"There can’t be anyone inside. This place is decrepit.\"":
            #voice abq0-07
            ab "Decrepit? Maybe so. Absent, perhaps not."
            #voice abq0-08
            ab "We’re here, after all. Whatever {i}we{\i} implies."

    #voice abq0-09
    ab "But — Whatever I am, and whatever you are, and whatever I am to you or you to me —"
    #voice abq0-10
    ab "I prefer to have my existential crises indoors. It’s getting late."
    #voice abq0-11
    ab "And we smell rather awful. If anything, we might find a way to rinse off, or at least disrobe."
    "The voice is correct. You reek."
    "From what part of your person the stench emanates is not entirely clear."
    menu:
        "You’d speculate it’s the whole of you that carries the stench of rot."

        "Investigate your hands.":
            "Your hands are sickly pale."
            "Many veins bulge just beneath your skin, but a great many more are varicose or outright ruptured."
            "You can see the blood that has pooled just under the dermal tissue, trickling up and down your knuckles as you turn your wrist and open and clench your fist."
        "Investigate your apparel.":
            "The weight of your shirt, vest, and jacket all weigh heavily on you."
            "The outermost layers are caked in grime, but as you peel back the layers — and it does take some peeling — that grime is exchanged for blood."
            "Not all of that blood is dry, though, even if it isn’t fresh."
        "Feel your face.":
            "The skin on your face sinks as you press your fingers against it."
            "It does not rise back — the divot persists, and only the act of protruding your jaw manages to stretch the tissue back over the depression."
            "Even your jaw seems to have a peculiar freedom of motion."
            "It becomes evident that not all of your teeth are present, nor is all of your tongue."


    #voice abq0-12
    ab "A bit worse for wear, it seems. And maybe worse than that."
    #voice abq0-13
    menu:
        ab "Please, let’s head inside. At least to rest what I am sure are your weary and worn muscles."

        "\"Well, since there’s nowhere else to go…\"":
            pass
        "\"Well, since I need to rest…\"":
            pass
        "\"Well, since you said so…\"":
            pass

    "The door swings open. The mansion looms larger."
    "It beckons you in."

    call screen minimap()
