label gameend3:

    "The shadow puts a hand on your shoulder."
    #voice ""
    ab "Well, tata, then."
    "You feel the shadow start to pull away from you."
    "As its trail unravels past your ear, your eardrum bursts, and your head bursts fluid alongside the smoke and shade."
    #voice ""
    ab "Open up, Presper."
    "The shadow reaches for Presper’s scalp. The old man looks up in revelry."
    "An urge inside of you surfaces."
    "From your brain? Your heart? What’s left of your spine?"
    menu:
        "The urge takes hold of the shade’s waning tail."

        "Keep Maurice's essence bound to your dying, decaying zombie body.":
            "You wield the urge like a gauntlet. You grasp at the shadow’s tail and pull it back into your skull."
            voice "abe3-01"
            ab "WHAT ARE YOU DOING? UNHAND ME! UNHAND ME!"
            "His protestations do not overwhelm your force of will."
            "Before long, the voice is once again rattling in your head."

            jump finalending_1

        "Let Maurice take control of Dr. Presper.":
            "You let the urge pass without event."
            "Your ear pops as the last of the shadow exits your head and slips through your ear canal."
            "With one stroke, the shadow slices through the skin of Presper’s scalp…"
            "…and peels it back."
            #voice ""
            dr "If this is what is best…"
            #voice ""
            ab "Do not doubt me. It is."
            #voice ""
            dr "It is. It —"
            "The shadow slips into Presper’s skull, worming its way into his psyche."
            "The old man convulses, despite his attempts to keep composure and steady himself."
            "He falls prone and his eyes shut."
            "When they open, they are no longer his."
            "A voice escapes from his mouth."
            #voice ""
            ab "It is a start."

            jump finalending_2

        "Wrangle the shade back into your brain, but let Maurice control you.":

            "You wield the urge like a gauntlet. You grasp at the shadow’s tail and pull it back into your skull."
            voice "abe3-01"
            ab "WHAT ARE YOU DOING? UNHAND ME! UNHAND ME!"
            "His protestations do not overwhelm your force of will."
            "Before long, the shadow is pulled into the cerebral fissure between the hemispheres of your mushy, rotting brain."
            "It assumes control."
            "You sit at the back of the zombie’s mind, watching the world through their eyes and listening through what’s left of their ears."
            "The head echos as they — Maurice — screams."
            #voice ""
            ab "DAMN IT! DAMN IT! THIS IS USELESS!"
            #voice ""
            ab "Get me out, Presper, get me out!"
            #voice ""
            dr "I… I don’t think I can."
            voice "dre3-01"
            dr "Forgive me, Maurice —"
            #voice ""
            ab "Never! You worthless, defective old coot."
            #voice ""
            ab "I bankrolled you and your entire goddamn family for the entirely of my life, and then some!"
            #voice ""
            ab "And you repay me with nothing but incompetence, torture, and failure."
            #voice ""
            ab "I will die in a shambling corpse because of you, Presper."
            #voice ""
            ab "And as much as I crave to see you carry the shame you so clearly deserve for the rest of eternity…"
            #voice ""
            ab "I’m afraid I can’t help but put you out of your misery myself, while I still can."
            #voice ""
            dr "No, no! I’m sorry! No!"
            "The zombie lunges at Presper and pins the old man to the ground."

            if amalgam_dead:

                "If the amalgam is dead."
                "You can only watch as the zombie sinks their teeth into Presper's neck."
                jump finalending_3
            else:
                jump other_options

label other_options:

    if amalgam_sedated:
        "You can only watch as the zombie bares his teeth."
        "You can sense Maurice intends to rip the jugular clean out of his neck."
        #voice ""
        "But you also hear a rumbling. The amalgam stirs."
        "Out of the corner of the zombie’s eyes, you watch the amalgam, recovering from its sedation."
        menu:
            "It clambers toward the zombie aggressor with a rapidly accelerating fervor."

            "\"Maurice, on our right! Watch out for the amalgam!\"":
                $ amalgam_dead = True
                $ amalgam_sedated = False
                #voice ""
                ab "Cheers."
                "The zombie turns to face the amalgam."
                "As it approaches, you watch Maurice sink the zombie’s fingers into the flesh of the amalgam."
                voice "dre2-01"
                dr "No! What are you doing?"
                "You can feel the zombie’s arm ripping apart as it thrusts past one of the amalgam’s many orifices and into a mass of muscle tissue."
                #voice ""
                "The amalgam wails and spasms involuntarily in response."
                "The other arm follows suit and grabs another hunk of flesh on its opposite side."
                "The arms begin to pull. To extract."
                voice "dre2-02"
                dr "Please! You’re hurting them!"
                "The eyes begin to blink in rapid succession."
                "Others shed tears."
                "The arms make quick work of the beast, pulling at every seam they can find."
                "The amalgam begins to unravel."
                "Its constituents fall to either side, either clawing away from or back into the beast."
                #voice ""
                "Every mouth is screaming."
                "But as the mouths lose their lungs, then their windpipes —"
                "As the amalgam unfolds like origami —"
                "As the beast falls apart, the screams grow hoarser."
                "When the screams have finally dissipated, the beast lies immobile."
                "The old man breaks into tears."
                #voice ""
                dr "My dears, oh, my dears."
                "He lies in silence for a few moments until he manages to eek out:"
                #voice ""
                dr "How could you do this?"
                "The zombie does not answer."
                "Instead, they sink their teeth into Presper’s neck."
                voice "dre3-02"
                "A blood-curdling scream bursts from his mouth as curdled blood pours out of his jugular."

                jump finalending_3


            "Keep quiet. Let the amalgam take you, Maurice, and the zombie body.":
                jump lethimtakeya

    if amalgam_vorvo:

        menu:
            "The amalgam, Vorvodoss, patiently watches on."
            "\"Consume us, Vorvodoss, before he kills Presper!\"":
                "The amalgam smiles."
                #voice ""
                vo "Confirm. Begin subroutine, Consume."
                "Before Maurice can strike, and with one fell swoop…"
                "The beast takes the zombie into its mouth."
                #voice ""
                ab "AAAAAAAAAAAH!"
                "The rows of teeth take turns gnashing through the leather of the boots, the cloth of the zombie’s attire, then the flesh, and then the bone."
                "You can feel the parts of the zombie’s body disconnect from each other."
                #voice ""
                ab "NO! NO! NO!"
                "An arm lost. Then a foot. The whole leg."
                "One crunch shatters the jaw just beneath your viewport."
                "Splinters of bone cut into the tongue, gums, and roof of the beast’s mouth."
                "Its blood mixes with the zombie’s as it chews."
                "The shadow screams as it flickers in and out of being."
                voice "abe3-02"
                ab "NO. NO. I WILL NOT GO. I WILL NOT DIE."
                voice "abe3-03"
                ab "I WILL NOT BE JUDGED. I REFUSE TO BE JUDGED."
                voice "abe3-04"
                ab "I AM ASHAMED, DON’T YOU UNDERSTAND?"
                voice "abe3-05"
                ab "I CANNOT BE JUDGED."
                jump finalending_4
            "\"Let him kill Presper, Vorvodoss.\"":
                #voice ""
                vo "Acknowledged."
                "You watch as the zombie sinks their teeth into Presper’s neck."
                voice "dre3-02"
                "A blood-curdling scream bursts from his mouth as curdled blood pours out of his jugular."
                jump finalending_3

            "\"Actually, can you give me control of my body back, Vorvodoss?\"":
                "The amalgam smiles."
                #voice ""
                vo "Request Confirmed. Terminate Subroutine: Intercession."
                "In an instant, you find yourself back in full control of the zombie body."
                jump finalending_1




label lethimtakeya:

    "You allow the amalgam to approach the zombie unnoticed."
    "Before Maurice can strike, and with one fell swoop…"
    "The beast takes the zombie into its mouth."
    #voice ""
    ab "AAAAAAAAAAAH!"
    "The rows of teeth take turns gnashing through the leather of the boots, the cloth of the zombie’s attire, then the flesh, and then the bone."
    "You can feel the parts of the zombie’s body disconnect from each other."
    #voice ""
    ab "NO! NO! NO!"
    "An arm lost. Then a foot. The whole leg."
    "One crunch shatters the jaw just beneath your viewport."
    "Splinters of bone cut into the tongue, gums, and roof of the beast’s mouth."
    "Its blood mixes with the zombie’s as it chews."
    "The shadow screams as it flickers in and out of being."
    voice "abe3-02"
    ab "NO. NO. I WILL NOT GO. I WILL NOT DIE."
    voice "abe3-03"
    ab "I WILL NOT BE JUDGED. I REFUSE TO BE JUDGED."
    voice "abe3-04"
    ab "I AM ASHAMED, DON’T YOU UNDERSTAND?"
    voice "abe3-05"
    ab "I CANNOT BE JUDGED."
    menu:
        "\"It’s time to reckon with your fate, Maurice.\"":
            pass
        "\"See ya on the other side, Maurice.\"":
            pass
        "\"You deserve all the divine punishment you might receive.\"":
            pass
    jump finalending_4
