label gameend2:

    menu:
        "Rip apart the amalgam. Kill it.":
            $ amalgam_dead = True
            jump end2_5

        "Resist the amalgam":
            $ amalgam_sedated = True
            jump end2_62

        "Let the amalgam consume you.":
            $ getting_chewed = True
            jump end2_109

        "Let Vorvodoss command the amalgam." if herman_queststate is 7:
            $ amalgam_vorv = True
            jump end2_134


label end2_5:

    "You sink your fingers into the flesh of the amalgam."
    voice "dre2-01"
    dr "No! What are you doing?"
    "The sheer weight of the beast pressing down on you cracks your ribs."
    "One rib punctures your stomach. Another puts a gash in your liver."
    "You can feel your arm ripping apart as you thrust it past one of the amalgam’s many orifices and into a mass of muscle tissue."
    #voice ""
    #BIG OL SCREAM
    "The amalgam wails and spasms into response."
    "You reach in with your other arm and grab another hunk of flesh."
    "The many eyes of the amalgam, one by one, focus onto you."
    "You begin to pull. To extract."
    voice "dre2-02"
    dr "Please! You’re hurting them!"
    "The eyes begin to blink in rapid succession."
    "Others shed tears."
    "One of the amalgam’s flailing arms swipes at your leg."
    "Your foot goes flying across the room. Your pants soil with blood."
    "You pull at every seam you can find."
    "The amalgam begins to unravel."
    "As you rip and pull and tear, the amalgam’s weight on you lessens."
    "Its constituents fall to either side, clawing at the floor."
    #voice ""
    "Every mouth is screaming."
    "But as the mouths lose their lungs, then their windpipes —"
    "As the amalgam unfolds like origami —"
    #voice ""
    "As the beast falls apart, the screams grow hoarser."
    "When the screams have finally dissipated, the beast lies immobile."
    "The old man collapses onto the floor."
    #voice ""
    dr "My dears, oh, my dears."
    "He lies in silence for a few moments until he manages to eek out:"
    #voice ""
    dr "How could you do this?"
    "The shadow echos his cry."
    #voice ""
    menu:
        ab "How could you do this?"

        "\"They needed to be put out of their misery.\"":
            #voice ""
            dr "Misery? No, there was no misery."
            #voice ""
            dr "There was no misery. I swear it. I swear it."

        "\"I need to put a stop to you, Presper. It started with the amalgam.\"":
            #voice ""
            dr "You didn’t have to —"
            #voice ""
            dr "They didn’t have to be a part of this."

        "\"You deserve the torment, old man.\"":
            #voice ""
            dr "I don’t care what I deserve. They didn’t deserve this."
            #voice ""
            dr "They didn’t have to be a part of this."

    #voice ""
    dr "You didn’t have to… my dears."
    #voice ""
    ab "You have doomed me, you fool! That was the only thing keeping Prepser alive!"
    #voice ""
    ab "Presper, tell me there is an alternative."
    #voice ""
    dr "I swear, they understood. There was no misery."
    #voice ""
    ab "PRESPER."
    "The old man jolts up. To do so imparts on him an intense fatigue."
    #voice ""
    ab "Tell me there is an alternative way to sustain you."
    #voice ""
    dr "It… Perhaps. I have some ideas we can —"
    #voice ""
    ab "Good, good."
    #voice ""
    ab "I will simply have {i}you{\i}, then. We will work quickly."
    #voice ""
    dr "N- no. I mean, of course. Of course."

    jump gameend3

label end2_62:

    "You fight back against the mass that sits atop you."
    "The sheer weight of the beast pressing down on you cracks your ribs."
    "One rib punctures your stomach. Another puts a gash in your liver."
    "You fend off the most aggressive of its arms, letting the less effectual limbs claw at you."
    "Hunks of fat are rended from your torso, but you are spared from yet more devastating blows."
    "One of the beast’s stumped limbs swings toward your skull."
    "You deflect it with your hand, but not without shattering the bones in your forearm."
    "Shards of the shattered bone slice through both you and the amalgam."
    "The amalgam’s primary maw grabs hold of your foot."
    "It does not pull you, because the foot is altogether lost to the beast."
    "The rows of teeth take turns gnashing through the leather of the boot, then the flesh, and then the bone."
    "Before long, the amalgam swallows what remains: paste."
    #voice ""
    "It yearns for more."
    "But its loudest roar is interrupted by a barrage of surgical tubing, wrapped tight around the neck of one of the amalgam’s primary heads."
    "Presper, exerting all his might, is straddling the beast, yanking back on the tubing."
    "The amalgam wails and gurgles, one of its airways pinched off the by Presper’s strangulation."
    #voice ""
    dr "Settle, dears. Settle!"
    "The constituent bodies of the beast thrash in unison, bucking the scientist back and forth."
    "He unsheathes a syringe and jams it between a set of seams."
    "Before long, the amalgam{w} settles."
    "The beast remains conscious, its eyes still surveying you and the room with some fervor."
    "But the body sits docile."
    "Lackadaisical."
    "Presper clambers down from the back of the amalgam."
    "He gives each head and mouth a gentle kiss on his way down."
    #voice ""
    dr "Thank you, my decrepit child."
    #voice ""
    ab "Yes, thank you. That cannot have been pleasant."
    "Your hear [marianne_name] call from behind."

    #voice ""
    menu:
        ma "Why on God’s green earth didn’t you kill that damn thing?"
        "\"It doesn’t deserve to die.\"":
            ar "... Mercy... comes in many forms... Perhaps... perhaps this is just one of them..."
            #voice ""
            ma "Deserve to — what kinda moral compass lets that thing drag my body around?"
        "\"It’s keeping Presper alive, that’s why.\"":
            #voice ""
            ma "The hell do you want with Presper?"
            #voice ""
            ma "What could you want from the man who sewed me into a monster?"
        "\"I don’t want it dead.\"":
            #voice ""
            ma "The hell do I care what you want?"
            #voice ""
            ma "It’s my body getting dragged around by that..."
            #voice ""
            ma "What can I even call it?"

    #voice ""
    ab "Her concerns are irrelevant."

    jump gameend3

label end2_109:

    "You relax your muscles and let the amalgam drag its maw across your torso."
    #voice ""
    ab "What are you doing? You damn fool!"
    "With one fell swoop, the beast takes you into its mouth."
    "The rows of teeth take turns gnashing through the leather of your boots, the cloth on your back, then the flesh, and then the bone."
    "You can feel the parts of your body disconnect from each other."
    "An arm lost. Then a foot. The whole leg."
    "One crunch shatters your jaw."
    "Splinters of bone cut into the tongue, gums, and roof of the beast’s mouth."
    "Its blood mixes with yours as it chews."
    "The shadow screams as it flickers in and out of being."
    #voice ""
    menu:
        ab "HOW COULD YOU BETRAY ME?"

        "\"It’s time for you to pass on, Maurice.\"":
            #voice ""
            ab "NO. It is not. It is not. It is not."
            #voice ""
            ab "I will not be judged. I will not. I refuse it."
            #voice ""
            ab "I REFUSE IT."
        "\"I thought the amalgam was the best place to keep you.\"":
            #voice ""
            ab "I told you I cannot be here any longer!"
            #voice ""
            ab "It is tortuous. It drives you mad, is that what you want of me?"
        "\"Who’s to say I can’t be a meaningful part of this amalgam?\"":
            #voice ""
            ab "What are you saying? You’ll be ground to bits, not assimilated!"
            #voice ""
            ab "Your premise is pure speculation, and it’s going to kill me!"

    jump gameend4

label end2_134:

    "The sheer weight of the beast pressing down on you cracks your ribs."
    "One rib punctures your stomach. Another puts a gash in your liver."
    "You give Herman — Vorvodoss? — the cue to intervene."
    #voice ""
    vo "Request Confirmed. Execute Subroutine: Intercession."
    "In a flash, Herman is gone."
    #HIDE HERMAN
    "And the amalgam recedes."
    "You manage to sit back up. The severed ribs roll down your chest cavity and shred at your intestines."
    "Presper takes a wary step back."
    voice "dre2-03"
    dr "What have you done? What have you unleashed?"
    "In a familiar voice, the amalgam’s many mouths begin to speak in unison."
    #voice ""
    vo "Observation: Vessel is amplus."
    #voice ""
    he "Oh now THIS is just horridly disgusting! Yet so powerful. Fine, what are we doing next?"
    voice "ly_dis5"
    ly "What kind of horrible power is this?"
    voice "ly_dis3"
    ly "Answer me."
    voice "ly_sur4"
    ly "Do you know what kind of power you’re playing with?"
    menu:

        "\"You heard the demon, he owes me!\"":
            #voice ""
            ma "Sure, sure, elder gods always keep their word."
            voice "ly_mad4"
            ly "To be fair, they do — just never in the way you think."
        "\"I suppose we’ll find out.\"":
            #voice ""
            vo "Entity Observation: Adaquate."
            voice "ar_puz4"

            ar "Are we sure... that to be a wise decision...?"
        "\"No, but I live for the chaos.\"":
            #voice ""
            au "I don't like this, it hurts my head..."
            #voice ""
            el "Woah, you’re like Godzilla, uncle Herman!"

    jump gameend3
