label finalending_5:

    "You can hear the old man calling from beyond the gums and teeth."
    dr "Maurice!"
    ab "PRESPER! FREE ME!"
    dr "What do I do? What do I do?"
    ab "FREE ME."
    "The old man peers closer into the mouth. He raises his hand and rests it on the amalgam’s bottom lip."

    menu:
        dr "How do I help?"
        "\"You don't, Presper! Let Maurice die.\"":
            jump finalending_5_lethimdie

        "\"You're going to have to pull us out.\"":
            jump finalending_5_pullusout

        "\"You're going to have to kill the amalgam.\"":
            jump finalending_5_killamalgam

        "\"Oh, Vorvodoss! Eat Presper too, will you?\"" if amalgam_vorv:
            jump finalending_5_eatpresper

label finalending_5_lethimdie:
    dr "I can't do that!"
    menu:
        dr "How could I ever let Maurice go?"
        "\By recognizing how cruel he was to you.\"":
            dr "Cruel? How do you mean?"
            dr "He treated me as I deserved to be treated, all things considered."
            #voice ""
            he "Ahahahaha! Oh yeah, you deserved it and MUCH worse."
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            #voice ""
            #voice ""
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."
            voice "dre5-10"
            dr "I… hadn’t considered all that."

        "\"By moving forward and never looking back.\"":
            dr "You make it sound so easy."
            dr "I could never {i}really{\i} leave Maurice behind like that, could I?"
            dr "He treated me as I deserved to be treated, all things considered."
            #voice ""
            he "Ahahahaha! Oh yeah, you deserved it and MUCH worse."
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            #voice ""
            #voice ""
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."
            voice "dre5-10"
            dr "I… hadn’t considered all that."

        "\"You can't, and you shouldn't.\'":
            dr "Quite right."
            dr "Not as long as I live."

    "The old man retracts his hand from the beast’s lip."
    dr "Goodbye, you two. Goodbye, Maurice."
    voice "dre3-01"
    dr "Forgive me, Maurice."
    ab "DAMN YOU, PRESPER! DAMN YOU! DAMN YOU TO THE-"
    "The rest of his cries are inaudible."
    jump theonetruedeath



label finalending_5_pullusout:

    dr "I can’t do that. I can’t do it."
    ab "YOU MUST! YOU MUST."
    dr "I - I -"
    "The old man braces himself and reaches into the amalgam’s mouth."
    "With immediacy, the amalgam slams Presper’s arm with both sets of teeth."
    "The old man howls in pain."
    dr "My dearest, please. Please."
    "The amalgam’s teeth remain clenched, but the old man’s fingers continue to grope and feel for any salvageable part of you."
    "Even as blood gushes from his arm, the old man manages to take hold of a good chunk of your head."
    "He yanks it out."
    "Your head drops to the floor."
    "The old man’s arm dangles limply at his side, mangled and soaked in blood."
    "The amalgam swallows heartily and relaxes its posture."
    dr "Maurice?"
    ab "Antoine."
    ab "You will never fix this."
    dr "I know, Maurice."
    ab "Do you, swine?"
    dr "I do, I do."
    ab "Say it. \"I will never fix this.\""
    menu:
        dr "I… I will…"
        "\"Don’t submit to him, Presper. Ignore him.\"":
            dr "What? How could I -"
            ab "Don’t keep me waiting, Antoine. Your creation is FADING."
            dr "I can’t just let him go, can I?"
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            #voice ""
            #voice ""
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."
            voice "dre5-10"
            dr "I… hadn’t considered all that."
            ab "Why defy me now, Antoine?"
            dr "Shh.. sh…. Maurice."
            ab "NO! NO! I AM FADING, ANTOINE."
            voice "dre5-15"
            dr "There, there Maurice."
            voice "abe5-02"
            ab "YOU INSOLENT -"
            "You do not catch the rest of Maurice's hollering, nor the rest of Presper’s soothing words."
            jump theonetruedeath
        "\"Fight back, Presper. Stomp his skull in.\"":
            dr "What? How could I -"
            ab "Don’t keep me waiting, Antoine. Your creation is FADING."
            dr "I can’t just let him go, can I?"
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            #voice ""
            #voice ""
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."
            voice "dre5-10"
            dr "I… hadn’t considered all that."
            "Presper looms over your mangled zombie head."
            "And raises his foot."
            ar "DON'T YOU DARE, PRESPER."
            voice "dre5-13"
            dr "This was going to happen to you anyway, Maurice."
            dr "Just let me end it quickly."
            ab "NO! NO NO NO NO -"
            "And all goes black."
            jump theonetruedeath
        "\"Say it, Presper. Acknowledge your failure.\"":
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            #voice ""
            #voice ""
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."
            "..."
            voice "dre5-12"
            dr "I will never fix this."
            ab "If only that made up for any of this."
            "Presper loses his composure, if he had any at all."
            "You do not catch the rest of Presper’s wallowing, nor the rest of Maurice’s chides."
            jump theonetruedeath


label finalending_5_killamalgam:

    "Presper looks down at his hands."
    dr "Whatever I must do for Maurice."
    "The old man stiffens. His eyes dart about the room."
    "At once, Presper exerts what little strength he has…"
    "… and lunges for a bonesaw."
    "He grasps it and plunges it into the beast."
    #voice ""
    "The old man pulls with all his might, and the saw slices through a line of seams along the torso of the beast."
    #voice ""
    "am The amalgam wails and spasms involuntarily in response."
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
    "When the screams have finally dissipated, the beast lies immobile around you."
    "You hear the old man breaks into tears, but those sounds subside."
    jump theonetruedeath

label finalending_5_eatpresper:
    #voice ""
    vo "Entity Request Confirmed. Execute Subroutine: Consume."
    #voice ""
    dr "What?! After all this?"
    #voice ""
    dr "No! NO! NO!"
    #voice ""
    menu:
        dr "What have I done to draw your ire, after everything?"
        "\"You are an irredeemably wicked man. You left me no choice.\"":
            pass
        "\"I wanted you to taste success just before taking it all away.\"":
            pass
        "\"You always needed to die. You knew that.\"":
            pass
    voice "dre2-01"
    dr "No! What are you doing?"
    "His plea is interrupted by the gaping maw of the amalgam."
    "In one motion, it swoops down and wraps its jaws around the old man."
    "In a moment, he is gone."
    "Muffled screams emanate from the mouth of the beast. Then, the neck."
    "Then, the center of the thing."
    "And then… there is quiet."
    #voice ""
    vo "Consumption complete. Subroutine Exit."
    "The amalgam lets out a rippling belch, but you do not seem to hear it."
    jump theonetruedeath
