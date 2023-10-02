label finalending_1:

    #voice ""
    ab "NO! NO! I WILL DIE IN HERE, I WILL DIE!"
    #voice ""
    ab "DAMN YOU! DAMN YOU! DAMN YOU!"
    "The voice inside your head thrashes."
    "But it is only inside your head."

    "The old man stares into your eyes for more than a few moments."
    "But he does break the silence."
    voice "dre5-01"
    dr "He’s stuck in there, isn’t he?"
    voice "dre5-02"
    dr "When your time comes to an end, his will, too."
    voice "dre5-03"
    dr "All the tinkering in the world cannot spare you of that fate."
    "He pauses."
    voice "dre5-04"
    dr "I failed."
    voice "dre5-05"
    dr "I had almost saved him, but I ruined it."
    if amalgam_dead:
        voice "dre5-06"
        dr "And my darlings paid the price for it."
    voice "dre5-07"
    dr "Maurice is gone, forever."
    voice "dre5-08"
    dr "He gave me so much. I owe him my livelihood."
    voice "dre5-09"
    dr "How can I ever forgive myself?"
    menu:
        "\"By recognizing how cruel he was to you.\"":
            #voice ""
            dr "Cruel? How do you mean?"
            #voice ""
            dr "He treated me as I deserved to be treated, all things considered."

            he "Ahahahaha! Oh yeah, you deserved it and MUCH worse."
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."

            voice "dre5-10"
            dr "I… hadn’t considered all that."
        "\"By letting yourself die, now that the amalgam is dead.\"" if amalgam_dead:
            #voice ""
            dr "Of course. I suppose that’s the logical conclusion to all this."
            #voice ""
            dr "As painful as it will be…"
        "\"By moving forward and never looking back.\"" if not amalgam_dead:
            #voice ""
            dr "You make it sound so easy."
            #voice ""
            dr "I could never really leave Maurice behind like that, could I?"
            he "Ahahahaha! Oh yeah, you deserved it and MUCH worse."
            if lysander_queststate is 7 or lysander_queststate is 9:
                voice "ly_hap1"
                ly "Not all pain is deserved, even if it feels such. If my time with your latest creation taught me anything, it was that."
            el "I... don't understand all this grown-up talks. But my mother told me someone who says bad words are bad."
            voice "ar_ner5"
            ar "Yes... The way Maurice has been treating you has been... really bad... but... have you truly deserved it..?"
            voice "mae5-01"
            ma "The way that man talks to you... He makes you out to be less than human. That's cruel."

            voice "dre5-10"
            dr "I… hadn’t considered all that."

        "\"You can’t, and you shouldn’t.\"":
            #voice ""
            dr "Quite right."
            #voice ""
            dr "Not as long as I live."

    "The old man takes a seat on the floor of the lab and crosses his legs."
    #voice ""
    dr "I have much to ponder."
    #voice ""
    dr "And so little time to ponder it."
    #voice ""
    dr "I have you to thank — or blame — for all of this."

    #voice ""
    menu:
        dr "With whatever time I have left, what’s next?"

        "\"Continue your experiments, same as before.\"" if not amalgam_dead:
            #voice ""
            dr "I thought I was performing so well under the pressure."
            #voice ""
            dr "200 years of pressure."
            #voice ""
            dr "I can only imagine how I will operate without it."
            #voice ""
            dr "But imagination is one thing I do not fear."
            #voice ""
            dr "I look forward to finding out."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath

        "\"Find another way to sustain yourself, and continue your experiments.\"" if amalgam_dead:
            #voice ""
            dr "I thought I was performing so well under the pressure."
            #voice ""
            dr "200 years of pressure."
            #voice ""
            dr "I can only imagine how I will operate without it."
            #voice ""
            dr "But imagination is one thing I do not fear."
            #voice ""
            dr "I look forward to finding out."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath

        "\"You have to answer this for yourself, Presper.\"":
            #voice ""
            dr "I have not answered anything for myself in 200 years."
            #voice ""
            dr "You are asking quite a lot of me."
            #voice ""
            dr "I don’t think I have the time to learn how to answer for myself before I perish."
            #voice ""
            dr "But, I think you’re right."
            #voice ""
            dr "I have much to ponder."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath
        "\"Leave your experiments behind. Put them in the past.\"":
            #voice ""
            dr "I’ve done so much harm to so many."
            #voice ""
            dr "And all that harm was for naught."
            #voice ""
            dr "If I cannot undo it, I suppose I can only ensure… it won’t get worse."
            #voice ""
            dr "That sounds so insufficient. Surely, there is some penance to perform."
            #voice ""
            dr "Some ways to right all the wrongs."
            voice "dre5-11"
            dr "I suppose I will learn those methods in time."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath
        "\"What’s next? Nothing.\" Kill him.":
            #voice ""
            dr "I - I - WAIT! WAIT!"
            "With little fanfare, you brandish a bonesaw and hack the doctor’s body to pieces."
            if amalgam_vorv:
                "Vorvodoss watches on with a wide grin."
            if amalgam_sedated:
                "The amalgam, in its stupor, can only watch in terror as its master cries for mercy."
            if amalgam_dead:
                "Those cries, of course, are to no avail."
            "Within moments of a strike to the neck, the doctor’s body slumps to the floor."
            "Presper is no more."
            "You stare over the corpse of the old scientist until your eyes glaze over and your vision dissipates."
            jump theonetruedeath

label finalending_2:

    #voice ""
    ab "I owe you my thanks, zombie, I really do."
    #voice ""
    ab "I know I’ve spoken ill of you before, but…"
    #voice ""
    ab "When one actually proves their utility, I will always recognize it."
    #voice ""
    ab "Now, I have much work to do."
    #voice ""
    if amalgam_dead:
        ab "First and foremost, of course, is finding a way to sustain myself."
    #voice ""
    ab "You seem to be nearing your end, so the least I can do is —"
    "He puts out the doctor’s hand. It hangs a little limp."
    voice "abe5-01"
    ab "The least I can do is shake your hand, since we couldn’t before."

    menu:
        "\"No. For my last trick, I'm going to kill {i}you{\i}.\"":
            jump finalending_2_kill
        "Shake his hand. \"Godspeed, Maurice.\"":
            jump finalending_2_shake
        "\"I don't think so. Vorvodoss, consume.\"" if amalgam_vorv:
            jump finalending_2_consume
        "\"I think I'm going to cut your life a little shot.\" Slay the amalgam.\"" if amalgam_sedated:
            jump finalending_2_cutoff
        "\"Sustain yourself? I think not.\" Destroy the lab." if amalgam_dead:
            jump finalending_2_destroy


label finalending_2_kill:
    #voice ""
    ab "What?! After all this?"
    #voice ""
    ab "No! NO! NO!"
    #voice ""
    menu:
        ab "What have I done to draw your ire, after everything!"
        "\"You are both irredeemably wicked men. You left me no choice.\"":
            pass
        "\"I wanted you to taste success just before taking it all away.\"":
            pass
        "\"Presper always needed to die. You knew that.\"":
            pass
    #voice ""
    voice "abe5-02"
    ab "YOU INSOLENT -"
    "With little fanfare, you brandish a bonesaw and hack the doctor’s body to pieces."
    if amalgam_sedated:
        "The amalgam, in its stupor, can only watch in terror as its master cries for mercy."
    if amalgam_vorv:
        "Vorvodoss watches on with a wide grin."
    voice "abe3-02"
    ab "NO. NO. I WILL NOT GO. I WILL NOT DIE."
    voice "abe3-03"
    ab "I WILL NOT BE JUDGED. I REFUSE TO BE JUDGED."
    voice "abe3-04"
    ab "I AM ASHAMED, DON’T YOU UNDERSTAND?"
    voice "abe3-05"
    ab "I CANNOT BE JUDGED."
    if amalgam_dead:
        "Those cries, of course, are to no avail."
    "Within moments of a strike to the neck, the doctor’s body slumps to the floor."
    "Maurice and Presper are no more."
    "You stare over the corpse of the old scientist until your eyes glaze over and your vision dissipates."
    jump theonetruedeath

label finalending_2_shake:
    "Maurice bows the old man’s head. His head."
    #voice ""
    ab "You’d make quite the handy laboratory assistant, if only your hands were still intact."
    #voice ""
    ab "Alas."
    "Without skipping a beat, the doctor’s body traipses about the room, examining each item and specimen in the laboratory with a newfound curiosity."
    "He drops a vial, but you do not hear the glass shatter."
    jump theonetruedeath

label finalending_2_consume:
    #voice ""
    vo "Entity Request Confirmed. Execute Subroutine: Consume and Transfer."
    #voice ""
    ab "What?! After all this?"
    #voice ""
    ab "No! NO! NO!"
    #voice ""
    menu:
        ab "What have I done to draw your ire, after everything?"
        "\"You are both irredeemably wicked men. You left me no choice.\"":
            pass
        "\"I wanted you to taste success just before taking it all away.\"":
            pass
        "\"Presper always needed to die. You knew that.\"":
            pass
    voice "abe5-02"
    ab "YOU INSOLENT -"
    "His curse is interrupted by the gaping maw of the amalgam."
    "In one motion, it swoops down and wraps its jaws around the old man."
    "In a moment, he is gone."
    "Muffled screams emanate from the mouth of the beast. Then, the neck."
    "Then, the center of the thing."
    "And then… there is quiet."
    #voice ""
    vo "Transfer complete. Subroutine Exit."
    "The amalgam lets out a rippling belch, but you do not seem to hear it."
    jump theonetruedeath

label finalending_2_cutoff:

    "You sink your fingers into the flesh of the sedated amalgam."
    #voice ""
    ab "No! What are you doing?"
    "You can feel your arm ripping apart as you thrust it past one of the amalgam’s many orifices and into a mass of muscle tissue."
    #voice ""
    "The amalgam wails and spasms involuntarily in response."
    "You reach in with your other arm and grab another hunk of flesh on its opposite side."
    "The many eyes of the amalgam, one by one, focus onto you."
    "You begin to pull. To extract."
    "The eyes begin to blink in rapid succession."
    "Others shed tears."
    "One of the amalgam’s flailing arms swipes at your leg."
    "Your foot goes flying across the room. Your pants soil with blood."
    "You pull at every seam you can find."
    "The amalgam begins to unravel."
    "As you rip and pull and tear, the amalgam’s weight on you lessens."
    "Its constituents fall to either side, either clawing away from or back into the beast."
    #voice ""
    "Every mouth is screaming."
    "But as the mouths lose their lungs, then their windpipes —"
    "As the amalgam unfolds like origami —"
    #voice ""
    "As the beast falls apart, the screams grow hoarser."
    "When the screams have finally dissipated, the beast lies immobile."
    "The old man balls his fists in rage."
    #voice ""
    menu:
        ab "How could you do this?"

        "\"They needed to be put out of their misery.\"":
            #voice ""
            ab "Misery? What the hell do you care about the damn thing?"
        "\"I need to put a stop to you, Maurice. Now, your days are numbered.\"":
            #voice ""
            ab "Numbered? I won’t make it two hours without the damn thing!"
        "\"You deserve the torment, Maurice.\"":
            #voice ""
            ab "The torment of a slow death?"

    #voice ""
    ab "I will be dead within the day because of you!"
    #voice ""
    ab "You have screwed me! SCREWED ME!"
    voice "abe5-03"
    ab "YOU WILL PAY FOR THIS."
    "The old man lunges at you, but you do not feel the impact, nor the ensuing carnage on your body."
    jump theonetruedeath

label finalending_2_destroy:

    "You take hold of every shelf, cabinet, dresser, and drawer."
    "You overturn them."
    "Chemicals pour out onto the concrete floor and seep into the ground."
    "Biological specimens splatter against the walls and the concrete."
    "Power tools are smashed to bits, and surgical implements are dented and contorted beyond recognition."
    "The old man watches in horror as the lab’s inventory disintegrates before his eyes."
    #voice ""
    ab "HOW COULD YOU?"
    #voice ""
    menu:
        ab "HOW COULD YOU SET ME UP LIKE THIS?"
        "\"You are both irredeemably wicked men. You left me no choice.\"":
            pass
        "\"I wanted you to taste success just before taking it all away.\"":
            pass
        "\"Presper always needed to die. You knew that.\"":
            pass
    #voice ""
    ab "Everything I built. Sponsored. Ushered."
    #voice ""
    ab "It is gone."
    "The old man clenches his fists in rage."
    voice "abe5-02"
    ab "YOU INSOLENT -"
    "The old man lunges at you, but you do not feel the impact, nor the ensuing carnage on your body."
    jump theonetruedeath


label finalending_3:

    "The blood drips down the zombie’s chin."
    "Presper writhes on the floor, bleeding profusely and slowing his convulsions with each passing second."
    "Presper eeks out his final words:"
    voice "dre3-01"
    dr "Forgive me, Maurice."

    menu:
        "\"Even in his last moments, he’s pathetic.\"":
            "The zombie closes his eyes and lets out a contented sigh."
            #voice ""
            ab "Always was."
        "\"At least pretend to forgive him, Maurice.\"":
            "The zombie closes his eyes and lets out a contented sigh."
            #voice ""
            ab "Never."
        "\"Look how you ruined this poor man, Maurice\"":
            "The zombie closes his eyes and lets out a contented sigh."
            #voice ""
            ab "He was always ruined."

    "The zombie takes a seat on the concrete floor of the lab, watching the blood pool around the old man’s head."
    #voice ""
    ab "Well, it’s just you and me, now."
    #voice ""
    ab "We have mere moments until everything I worked for vanishes before my eyes."
    #voice ""
    ab "And, hell, they’re not even my eyes."
    #voice ""
    ab "I hoped ripping out his jugular would soothe my nerves."
    #voice ""
    ab "It did not work."
    #voice ""
    menu:
        ab "Do you not fear what is coming? Judgment?"

        "\"Judgment is not coming. Only the void.\"":
            pass
        "\"I have no reason to fear judgment. I will be absolved.\"":
            pass
        "\"I do fear it. It was always going to catch up with me.\"":
            pass

    "The zombie purses his lips."
    "And then his eyes grow wide."
    #voice ""
    ab "Oh no. It’s coming."
    #voice ""
    ab "No no no NO no NO NO NO -"
    #voice ""
    "You can feel your faculties waning in time with his."
    "Maurice’s frenzy escalates to a fever pitch."
    voice "abe3-02"
    ab "NO. NO. I WILL NOT GO. I WILL NOT DIE."
    voice "abe3-03"
    ab "I WILL NOT BE JUDGED. I REFUSE TO BE JUDGED."
    voice "abe3-04"
    ab "I AM ASHAMED, DON’T YOU UNDERSTAND?"
    voice "abe3-05"
    ab "I CANNOT BE JUD—"
    "The rest of his cries are inaudible."
    jump theonetruedeath

label finalending_4:

    "You can hear the old man calling from beyond the gums and teeth."
    dr "Maurice!"
    ab "PRESPER! FREE ME!"
    dr "What do I do? What do I do?"
    ab "FREE ME."
    "The old man peers closer into the mouth. He raises his hand and rests it on the amalgam’s bottom lip."

    menu:
        dr "How do I help?"
        "\"You don't, Presper! Let Maurice die.\"":
            jump finalending_4_lethimdie

        "\"You're going to have to pull us out.\"":
            jump finalending_4_pullusout

        "\"You're going to have to kill the amalgam.\"":
            jump finalending_4_killamalgam

        "\"Oh, Vorvodoss! Eat Presper too, will you?\"" if amalgam_vorv:
            jump finalending_4_eatpresper

label finalending_4_lethimdie:
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



label finalending_4_pullusout:

    dr "I can’t do that. I can’t do it."
    ab "YOU MUST! YOU MUST."
    dr "I - I -"
    "The old man braces himself and reaches into the amalgam’s mouth."
    "With immediacy, the amalgam slams Presper’s arm with both sets of teeth."
    "The old man howls in pain."
    dr "My dearest, please. Please."
    "The amalgam’s teeth remain clenched, but the old man’s fingers continue to grope and feel for any salvageable part of the zombie."
    "Even as blood gushes from his arm, the old man manages to take hold of a good chunk of the zombie’s head."
    "He yanks it out."
    "The head drops to the floor."
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
            voice "dre5-14"
            dr "There, there Maurice."
            voice "abe5-02"
            ab "YOU INSOLENT -"
            "You do not catch the rest of the zombie’s hollering, nor the rest of Presper’s soothing words."
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
            "Presper looms over the mangled zombie head."
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


label finalending_4_killamalgam:

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

label finalending_4_eatpresper:
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


label finalending_6:

    "Presper looks up at the beast."
    dr "My darlings. What happened to my darlings?"
    ab "I am your darling, now, Antoine."
    ab "Isn’t that what you wanted?"
    dr "I… Yes, Maurice."
    ab "You have much work ahead of you, Antoine."
    dr "I am experiencing a hunger I have never felt in any other body."
    ab "You should attend to it. To me."
    dr "Yes… Maurice."
    "The rest of Presper’s groveling and Maurice’s dictating are lost on you as your vision and hearing fade."
    jump theonetruedeath



label finalending_7:

    "The amalgam looks to you and gives a million-tooth smile."
    ab "I suppose it will take a while to… integrate… Antoine fully."
    ab "But I thank you for your cooperation. Your benevolence."
    "The beast reaches out a hand from the back of its neck."
    "The arm is outstretched."
    ab "Put her there, partner."
    "The rest of Maurice’s words are lost on you."
    jump theonetruedeath


label finalending_8:

    "The old man stares into your eyes for more than a few moments."
    "But he does break the silence."
    voice "dre5-01"
    dr "He’s stuck in there, isn’t he?"
    dr "My darlings have passed on, and so has he."
    dr "All the tinkering in the world cannot spare him of that fate."
    "He pauses."
    voice "dre5-04"
    dr "I failed."
    voice "dre5-05"
    dr "I had almost saved him, but I ruined it."
    voice "dre5-06"
    dr "And my darlings paid the price for it."
    voice "dre5-07"
    dr "Maurice is gone, forever."
    voice "dre5-08"
    dr "He gave me so much. I owe him my livelihood."
    "The old man takes a seat on the floor of the lab and crosses his legs."
    #voice ""
    dr "I have much to ponder."
    #voice ""
    dr "And so little time to ponder it."
    #voice ""
    dr "I have you to thank — or blame — for all of this."

    #voice ""
    menu:
        dr "With whatever time I have left, what’s next?"

        "\"Find another way to sustain yourself, and continue your experiments.\"":
            #voice ""
            dr "I thought I was performing so well under the pressure."
            #voice ""
            dr "200 years of pressure."
            #voice ""
            dr "I can only imagine how I will operate without it."
            #voice ""
            dr "But imagination is one thing I do not fear."
            #voice ""
            dr "I look forward to finding out."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath

        "\"You have to answer this for yourself, Presper.\"":
            #voice ""
            dr "I have not answered anything for myself in 200 years."
            #voice ""
            dr "You are asking quite a lot of me."
            #voice ""
            dr "I don’t think I have the time to learn how to answer for myself before I perish."
            #voice ""
            dr "But, I think you’re right."
            #voice ""
            dr "I have much to ponder."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath
        "\"Leave your experiments behind. Put them in the past.\"":
            #voice ""
            dr "I’ve done so much harm to so many."
            #voice ""
            dr "And all that harm was for naught."
            #voice ""
            dr "If I cannot undo it, I suppose I can only ensure… it won’t get worse."
            #voice ""
            dr "That sounds so insufficient. Surely, there is some penance to perform."
            #voice ""
            dr "Some ways to right all the wrongs."
            voice "dre5-11"
            dr "I suppose I will learn those methods in time."
            "The next words that leave Presper’s mouth do not register."
            jump theonetruedeath
