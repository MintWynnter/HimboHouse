label gameend4:

    #voice ""
    ab "I will not die with you, stupid zombie!"
    #voice ""
    ab "I will not submit myself to this wretched thing."
    #voice ""
    ab "I will have to make it mine."
    "You feel the shadow start to pull away from you."
    "As its trail unravels past your ear, your eardrum bursts, and your head bursts fluid alongside the smoke and shade."
    #voice ""
    ab "Open up, beast!"
    "The shadow reaches for of the tears in the roof of the beast’s mouth and rips it clean open."
    "As blood pours atop your body, the shadow rips deeper and deeper, pulling itself up as it claws."
    "An urge inside of you surfaces."
    "From your brain? Your heart? What’s left of your spine?"
    menu:
        "Whatever it is, the urge takes hold of the shade’s waning tail."

        "Keep Maurice's essence bound to your chewed-up zombie body.":
            "You wield the urge like a gauntlet. You grasp at the shadow’s tail and pull it back into your skull."
            voice "abe3-01"
            ab "WHAT ARE YOU DOING? UNHAND ME! UNHAND ME!"
            "His protestations do not overwhelm your force of will."
            "Before long, the voice is once again rattling in your head."
            #voice ""
            ab "NO! NO! I WILL DIE IN HERE, I WILL DIE!"
            #voice ""
            ab "DAMN YOU! DAMN YOU! DAMN YOU!"
            "The voice inside your head thrashes."
            "But only inside your head."

            jump finalending_5

        "Let Maurice take control of the amalgam.":
            jump maurice_amalgam_control

        "Wrangle the shade back into your brain. Let Maurice control your chewed-up body.":

            "You wield the urge like a gauntlet. You grasp at the shadow’s tail and pull it back into your skull."
            voice "abe3-01"
            ab "WHAT ARE YOU DOING? UNHAND ME! UNHAND ME!"
            "His protestations do not overwhelm your force of will."
            "Before long, the shadow is pulled into the cerebral fissure between the hemispheres of your mushy, rotting brain."
            "It assumes control."
            "You now sit at the back of the zombie’s mind, watching the world through their eyes and listening through what’s left of their ears."
            "The cavern that is the mouth of the beast echos as they — Maurice — scream."
            #voice ""
            ab "DAMN IT! DAMN IT! THIS IS USELESS!"
            #voice ""
            ab "Get me out, Presper, get me out!"
            #voice ""
            dr "I… I don’t think I can."
            "The rows of teeth take turns gnashing through the leather of the boots, the cloth of the zombie’s attire, then the flesh, and then the bone."
            voice "dre3-01"
            dr "Forgive me, Maurice —"
            #voice ""
            ab "Never! You worthless, defective old coot."
            "You can feel the parts of the zombie’s body disconnect from each other."
            #voice ""
            ab "I bankrolled you and your entire goddamn family for the entirely of my life, and then some!"
            "An arm lost. Then a foot. The whole leg."
            #voice ""
            ab "And you repay me with nothing but incompetence, torture, and failure."
            "One crunch shatters the jaw just beneath your viewport."
            #voice ""
            ab "I will die in a shambling corpse because of you, Presper."
            "Splinters of bone cut into the tongue, gums, and roof of the beast’s mouth."
            voice "abe3-02"
            ab "NO. NO. I WILL NOT GO. I WILL NOT DIE."
            "Its blood mixes with the zombie’s as it chews."
            voice "abe3-03"
            ab "I WILL NOT BE JUDGED. I REFUSE TO BE JUDGED."
            voice "abe3-04"
            ab "I AM ASHAMED, DON’T YOU UNDERSTAND?"
            voice "abe3-05"
            ab "I CANNOT BE JUDGED."
            "None of his pleas slow the voracity of the beast’s emaciating mastication."

            jump finalending_4


label maurice_amalgam_control:

    "You let the urge pass without event."
    "Your ear pops as the last of the shadow exits your head and slips through your ear canal."
    "With one stroke, the shadow seizes the rip in the amalgam’s mouth…"
    "…and peels it back."
    #voice ""
    ab "Submit to me, beast."
    "The shadow slips into the beast’s labyrinthian organ system, worming its way into its decentralized psyche."
    "The amalgam’s chewing starts and stops sporadically as the shadow overpowers, one by one, each being bound to the monster."
    "Before long, the beast spits you back out onto the floor of the lab."
    "What faculties you still have are barely functional. Most are inaccessible."
    "What constitutes you now is little more than the top half of your head and an exposed spinal cord leading to an emaciated third of a torso."
    "You have one arm and two fingers."
    "In a familiar voice, the amalgam’s many mouths begin to speak in unison."
    #voice ""
    ab "This is not ideal, but it's not over, either."
    "The amalgam — Maurice — shambles over to Presper."
    "The old man looks up in revelry."
    #voice ""
    ab "What to do with you, Presper?"
    #voice ""
    ab "If I cannot be you, then I have no choice but to lead you."
    #voice ""
    ab "We can do this together…"
    #voice ""
    ab "Literally or figuratively."
    "The old man recoils."
    #voice ""
    dr "What… what do you mean?"
    #voice ""
    ab "Don’t make me spell it out for you."
    #voice ""
    ab "You love your darlings so."
    #voice ""
    ab "So… Why don’t you join us?"
    voice "abe4-01"
    ab "Think of all the minds of this thing, working in unison."
    #voice ""
    ab "I know you would like to join me."
    #voice ""
    dr "I… I…"
    "The amalgam turns to you."
    #voice ""
    menu:
        ab "Don’t you think that would be ideal?"

        "\"I think you two are better of seperate.\"":
            #voice ""
            ab "There are trade-offs, yes."
            "The amalgam lets out a long, tired groan."
            #voice ""
            ab "Very well. We will operate on our own terms."
            jump finalending_6

        "\"It would be ideal. You should {i}integrate{\i} Presper.\"":
            #voice ""
            ab "Yes."
            #voice ""
            dr "No!"
            "And just as the amalgam took you before, it swoops down and wraps its jaws around the old man."
            "In a moment, he is gone."
            "Muffled screams emanate from the mouth of the beast. Then, the neck."
            "Then, the center of the thing."
            "And then… there is quiet."
            jump finalending_7

        "\"Dr. Presper, you have to kill this thing.\'":
            jump presper_gotta_killit

        "\"It's not any of my business...\"":
            #voice ""
            ab "Very well. I will, as they say…."
            #voice ""
            ab "Follow my gut."
            "And just as the amalgam took you before, it swoops down and wraps its jaws around the old man."
            "In a moment, he is gone."
            "Muffled screams emanate from the mouth of the beast. Then, the neck."
            "Then, the center of the thing."
            "And then… there is quiet."
            jump finalending_7



label presper_gotta_killit:

    #voice ""
    dr "What? No! I couldn’t!"
    #voice ""
    ab "And you shouldn’t."
    #voice ""
    menu:
        dr "Of course! I shouldn’t!"

        "\"Presper, nothing poses a greater threat than Maurice in this form.\"":
            pass
        "\"It’s time you stood up to someone who’s pushed you around for too long.\"":
            pass
        "\"Your whole centuries-long experiment is twisted. It needs to end.\"":
            pass

    "Presper hesitates."
    #voice ""
    ab "Don’t listen to him, you damn fool."
    #voice ""
    ab "It’s idiocy of the highest degree."

label tell_him_to_kill_it:

    he "That sum'bitch kept me trapped here for a damn century! I'd curb stomp his teeth with my manure boot if I could!"
    voice "ly_dis4"
    ly "With this power, Maurice is now a danger reaching far beyond these grounds. Destroying him could save countless lives."
    #voice ""
    au "That thing is repulsive. It's an eyesore, so get rid of it."
    #voice ""
    el "What if it goes out of this place and starts eating people?!"
    #voice ""
    ar "Arabella doesn't seem to be herself. She chuckles."
    ar "Hmm... Some things are better left dead, I suppose."
    voice "mae4-01"
    ma "Kill it! Just kill it!!"

    "The old man stiffens. His eyes dart about the room."
    "The amalgam begins to lunge."
    "At once, Presper exerts what little strength he has…"
    "… and lunges for a bonesaw."
    "He grasps it and plunges it into the beast."
    #voice ""
    ab "AAARGH! Presper! What are you doing?"
    "The old man pulls with all his might, and the saw slices through a line of seams along the torso of the beast."
    #voice ""
    "The amalgam wails and spasms involuntarily in response."
    "Presper lets loose a flurry of slashes with the saw and with the long, sharp fingernails on his opposite hand."
    "The eyes of the amalgam begin to blink in rapid succession."
    "Others shed tears."
    "Presper sheds tears in turn. But it does not slow him."
    "He makes quick work of the beast, pulling at every seam he can find."
    "The amalgam begins to unravel."
    "Its constituents fall to either side, either clawing away from or back into the beast."
    #voice ""
    "Every mouth is screaming."
    "But as the mouths lose their lungs, then their windpipes —"
    "As the amalgam unfolds like origami —"
    #voice ""
    "As the beast falls apart, the screams grow hoarser."
    "When the screams have finally dissipated, the beast lies immobile."
    "The old man breaks into tears."
    #voice ""
    dr "My dears, oh, my dears."

    jump finalending_8
