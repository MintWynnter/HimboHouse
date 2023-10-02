label ghosts_telloff_maurice:

label ghosts_tell_presperkill:



label gameend:

    "His giggle morphs into a cackle."
    #voice ""
    ab "AHAHAHAHA."
    # BLACK SCREEN
    voice "abe1-01"
    ab "What a pathetic pet project you turned out to be."
    #voice ""
    ab "Presper — the fool — killed a gravedigger in cold blood just to have you shamble around for barely an evening."
    #voice ""
    ab "Look at you, you’re on your last legs - in every sense of the phrase!"
    #voice ""
    menu:
        ab "That man was never worthy of my patronage, of my grace."

        "\"You seem less concerned with his means than his ends.\"":
            #voice ""
            ab "What about his means?"
        "\"What was your patronage for, exactly?\"":
            #voice ""
            ab "Not for much. All I asked for was a modicum of effort."
        "\"No, he isn’t worthy of much at all.\"":
            #voice ""
            ab "You do not understand the extent to which you are right."

    #voice ""
    ab "200 years ago, I sent the old bat on a wild goose chase."
    #voice ""
    ab "And here he is, 200 years later, no closer to catching that goose."
    #voice ""
    ab "And now, I’m trapped in the body of a dilapidating corpse —"
    #voice ""
    ab "— possibly for eternity, if your ultimate collapse doesn’t free me."
    #voice ""
    menu:
        ab "But I won’t consider the latter. Presper would never let me go."

        "\"I cannot tell: Are you grateful for or resentful of that?\"":
            #voice ""
            ab "Ha! It matters not how I feel. It’s simply a fact. Presper will not let me go."
            #voice ""
            ab "He cannot afford to."
        "\"Do you want to be free or not?\"":
            #voice ""
            ab "I want to be alive."
            #voice ""
            ab "Prepser cannot afford to have me end up otherwise."
        "\"Why wouldn’t Presper let you go?\"":
            #voice ""
            ab "You and I might know he’s a failure, but he won’t believe it himself till he loses me."
            #voice ""
            ab "He cannot afford that revelation."

    voice "abe1-02"
    ab "He can only afford to return me to the land of the living."
    voice "abe1-03"
    ab "To do so is the only thing that gives him worth."
    #voice ""
    ab "Without me, he is — "
    #voice ""
    #AMALGAM SHRIEK
    "A ghastly shriek echos through the mansion."
    "The beast."
    "You hear the mansion’s ghosts congregating in the foyer."
    "The ring you found after Lysander's disappearance hums with an eerie energy. Could he be…?"

    # JUMP TO THE FOYER

    ar "Wh-what... was that terrifying sound...?"
    voice "ly_mad1"
    ly "An utterly inhuman noise... I've never heard anything like it."
    voice "mae1-01"
    ma "I have... I think."
    #voice ""
    au "It sounds even more scared than Minoru usually does!"
    #voice ""
    he "Sounds like someone skin'n a rabbit before it's ready!"
    #voice ""
    el "W-what was that sound???"

    "Herman is the first to notice you."
    #voice ""
    he "Well, if it isn’t our not so alive friend."
    voice "ar_ner2"

    ar "You... you heard that sound as well... yes...?"
    #voice ""
    au "Quite the disruption."
    if lysander_queststate is 8 or lysander_queststate is 10:
        "Even Lysander has been temporarily roused from his ring by the shrieking."
    voice "ly_dis1"

    ly "Any idea what that could be?"
    voice "ly_puz5"

    if lysander_queststate is 8 or lysander_queststate is 10:
        ly "Surely, monsters must be able to recognize their kin."

    menu:
        "\"There’s some kind of beast in the basement below us.\"":
            #voice ""
            el "A beast? Like, A MONSTER?"
            voice "ar_sur5"

            ar "It... will be alright little one... Do not be worried..."
            #voice ""
            el "I’m not worried! Why is there a monster here?"
        "\"I have no idea where that could have come from.\"":
            #voice ""
            he "What use you are."
            voice "ar_puz1"

            ar "It... sounds as though it came from... below us..."
        "\"I didn’t hear anything, actually.\"":
            voice "ly_puz2"

            ly "Ah, I had forgotten about your ear. My apologies."
            voice "ar_puz1"

            ar "It... sounds as though it came from... below us..."

    #voice ""
    ma "Below us… the basement."
    #voice ""
    he "Well no shit, \"the basement\", ya'want a cookie for that astute observation, Sherlock?"
    #voice ""
    ma "That’s where the camcorder must have…"
    "Marianne turns to you."

    voice "mae1-02"
    ma "Take us there. We have to confront whatever’s down there."

    menu:
        "\"Sure. Follow me.\"":
            "You guide the ghosts to the basement. They follow shortly behind."
        "(I should probably warn Presper before they find him themselves.)":
            "You flee to the basement to warn the old man. The ghosts follow shortly behind."
        "\"No. It’s not your business.\"":
            #voice ""
            he "Not our —"
            "Herman is seething."
            voice "ar_ner2"

            ar "I'm sorry... but I believe it to be our business... For some, it has been the only home we've known... in life and in death... If there is something going on... then I wish to know of it..."
            #voice ""
            ma "I know how to get there."
            voice "ly_dis5"

            ly "I do too, I think. There’s a hatch out by the gardens I never bothered to touch."
            "The voice in your head makes a suggestion."
            ab "They’ll find him and that sooner or later. You may as well be there when all hell breaks loose."

    # BLACK SCREEN

    "The walk to the lab wears at your body in quantities and qualities not yet seen."
    "Toes pop off your foot and rumble around freely in your boot."
    "The skin between your thighs peels off with each chafe."
    "Your jaw begins to swivel side to side each time you shift your weight."
    #voice ""
    ab "Clocks, a’ticking, zombie."

    # IN THE LAB NOW

    "You are the first to arrive to Presper’s lab."
    "The old man himself is leaned up against the rusted iron door, behind which the beast pounds mercilessly."
    #BIG SCARY AMALGAM ROAR
    voice "dre1-01"
    dr "Shhh-shh-shh. Come now, darlings, come now."
    #voice ""
    menu:
        dr "There is nothing to fear, nothing to fear."

        "\"Presper, the ghosts are coming to find you.\"":
            #voice ""

            dr "Whah? Huh? How do you mean?"
            "He braces himself yet more firmly against the iron door."
        "\"Need some help, old man?\"":
            #voice ""
            dr "Whah? Huh? Help? No!"
            "He braces himself yet more firmly against the iron door."
        "Silently observe Presper.":
            "He is distraught beyond words."
            "He coos the beast under his breath, all while bracing himself yet more firmly against the iron door."

    "Myriad dents pop from the iron anyway."
    voice "dre1-02"

    dr "Cadaver!"
    #voice ""
    menu:
        dr "Put your weight on this door, immediately!"


        "Help Presper hold back the beast.":
            "You throw your weight at the door."
            "Your body squelches and flattens against it."
        "Watch him struggle.":
            "You stand motionless, save for the loose arm swinging at your side."
        "Pull him from the iron door.":
            "You reach for the old man to pull him away from his clamoring."
            "But engaging your muscles is fruitless."
            "Instead, your arms simply begin to tear. First the skin, then the fascia."
            "You release him before you manage to sever your muscles altogether."

    "A voice emerges from you. It is not your own, but it its all too familiar."
    "For the first time, its voice fills more than just your brain. It fills the room in which you stand."
    # SHOW THE ABBE FINALLY
    "Its shadow pours out of your ear and onto the floor beside you."
    voice "abe1-04"
    ab "Presper. Pathetic, as always."
    "The old man’s eyes widen."
    voice "dre1-03"
    dr "Maurice."
    "He falls to his knees."
    voice "dre1-04"
    dr "I thought I had lost you."
    voice "abe1-05"
    ab "You almost did."
    #voice ""
    dr "Maurice, I’ve nearly done it. I’ve nearly brought you back."
    #voice ""
    ab "Nearly? Look at this thing."
    "He’s talking about you."
    #voice ""
    menu:
        ab "A bucket of bolts, this is. I can’t even control it."

        "\"How rude!\"":
            pass
        "\"I do seem to be on the way out. I’m literally falling apart.\"":
            pass
        "\"You don’t seem to appreciate how impressive bringing anything back to life is.\"":
            pass

    #voice ""
    ab "Quiet, zombie! You’ve done your bidding."
    #voice ""
    ab "But much less than appease the ghosts, they’re coming down here as we speak."
    #voice ""
    dr "They are?"
    #voice ""
    ab "They are."
    #voice ""
    dr "Oh, dear. How embarrassing. I really should clean up."
    #voice ""

    dr "You know, I’ve been far too busy with my work to trifle with things like laundry and —"
    voice "abe1-06"
    ab "Busy? 200 years and the only thing you’ve got to show for it is about to collapse into a puddle of paste and marrow."
    #voice ""
    ab "Busy? Lazy. And a slob, at that."
    #voice ""
    dr "Of course, you’re right, of course."
    #voice ""

    dr "Let me make it right, Maurice."
    #voice ""
    ab "You’ve always had my permission to make it right."
    #voice ""
    au "Hello?"
    #voice ""
    he "Who’s rustlin' around down there? Yain't being quiet!"
    "The beast bangs louder against the iron door."
    "Presper crawls to and rakes at it. His voice wavers."
    #voice ""
    dr "Shh - shhh… No need, no need."
    #voice ""
    ab "It’s not listening to you, Prepser. Why would it?"
    voice "ar_sur5"

    ar "These voices... Whose are they...?"
    #voice ""
    ma "I’m keen on finding out."
    voice "dre1-05"
    dr "I will make this right, I will make this right."
    #voice ""
    el "They're here!"
    voice "ly_dis3"

    ly "Brace yourselves, friends."
    # SHOW EVERY GHOST
    "Before you stand the six ghosts of the mansion."
    "Elizabeth. Arabella. Lysander."
    "Herman. [marianne_name]. Aures."
    "They watch - wordlessly - the cloying old man, desperately trying to soothe the thing behind the door."
    "They observe you, broken and battered and showing every sign of decay."
    "And they stare at the shadow that has formed beside you. At Maurice."

    #voice ""
    he "Just what'n the hell is all this?"
    voice "ly_puz1"

    ly "A laboratory."
    #voice ""
    au "A dungeon."
    #voice ""
    el "A home."
    voice "ar_ner2"

    ar "This... this energy... I do not like it... It feels... very dark..."
    #voice ""
    ma "Oh, you think?"

    "Presper turns toward the spectral cadre. He is sweating profusely. His face is a deep, deep red."
    voice "dre1-06"
    dr "I mean you no harm! I am just a man. Just a man…"
    voice "ar_ner2"

    ar "I... I want to believe that to be the truth... but... this place... makes me feel otherwise..."
    #voice ""
    he "This is every kind of sideways."
    voice "ly_puz2"

    ly "I think this explains where our friend came from."

    #voice ""
    menu:
        ma "What is going on, here?"

        "\"This is Dr. Presper’s lab. He wants to bring someone back to life.\"":
            "The red in his face deepens."
            #voice ""

            dr "I… I suppose… that’s right."
        "\"Dr. Presper, why don’t you tell them?\"":
            "The red in his face deepens."
            #voice ""

            dr "It’s… it’s a rather long story."
        "\"Mr. Lachaise, won’t you answer her?\"":
            #voice ""
            ab "I don’t owe anyone any answers."
            #voice ""
            ab "But I will entertain you this once."

    "The room chills. The shadow beside you presents himself to the six ghosts."
    #voice ""
    ab "Spectres. Trespassers."
    voice "abe1-07"
    ab "I am Abbé Maurice Lachaise. This is my home."
    voice "abe1-08"
    ab "And this is my faithful lackey, Dr. Presper."
    voice "abe1-09"
    ab "Say hello, Antoine."
    voice "dre1-07"

    dr "... Hello."
    #voice ""
    ab "Good."
    #voice ""
    ab "Dr. Presper is here to ensure I remain on these grounds, preferably alive."
    #voice ""
    ab "See, I do not share your luxury, ghosts."
    #voice ""
    ab "I have no unfinished business, no binding contacts, no ties to planes beyond."
    #voice ""
    ab "No reason to linger, as it were. Once I, or my vessel, die, I will pass."
    #voice ""
    dr "But we will not let that happen, will we, Maurice? I could never let that happen."
    #voice ""
    ab "Precisely."
    #voice ""
    au "Look at these two. Such a lovely pair."
    voice "ly_puz3"

    ly "I’m hesitant to use the word \"lovely.\""
    #voice ""
    he "What the... are you sayin', you coulda saved me those 100 years ago?"
    #voice ""
    ab "That said, this vessel of mine is very much on its way out."
    #voice ""
    ab "Where does that leave us, hmm?"
    #voice ""
    ma "It leaves you in a prime position to die properly like the rest of us."
    voice "ar_sad2"

    ar "It's... nearly an end... for the dark energy within these mansion walls... I hope..."
    #voice ""
    ab "Tut tut. Incorrect answers."

    "The shadow turns to you."
    #voice ""
    ab "You’ve been making all sorts of wise and foolish decisions tonight."
    #voice ""
    ab "I will take your advice to heart."
    #voice ""
    menu:
        ab "Where shall I go from here?"

        "\"You need to give up this pipe dream of immortality. Pass on.\"":
            if lysander_queststate is 8 or lysander_queststate is 10:
                voice "ly_hap1"
                ly "There is no use in trying to escape your fate."

            #voice ""
            el "Pouting and saying no doesn’t work, either."
            #voice ""
            ab "I’m afraid I cannot accept that as an option."
        "\"You need to find a more permanent body to suit you.\"":
            #voice ""
            he "I respect a man with ambition, Maurice. You’re a go-getter."
            if marianne_queststate is 4:
                #voice ""
                ma "Ain’t so hard to do, being someone else."
            #voice ""
            ab "You’re certainly right."
        "\"Wait, where were you before Presper made me?\"":
            voice "ar_sur5"

            ar "Before he... made you...? What... does he mean by that...?"
            voice "ly_sad4"

            ly "I thought they might have had something to do with each other…"
            #voice ""
            ab "I was kept waiting, is all I will say."

    voice "abe1-10"
    ab "I need a new vessel."
    #voice ""
    ab "Presper, you have made it this far, some 243 years, yes?"
    voice "abe1-11"
    ab "Why don’t you let me have… you."
    voice "dre1-08"

    dr "Me? But I need me! I mean, you need me!"
    #voice ""
    ab "I’ve learned a thing or two about sharing a headspace."
    "The shadow nods to you."
    #voice ""
    ab "You can take a back seat. It can be arranged."
    "Presper’s eyes dart about the room."
    "To the ghosts. To Maurice. To you. Back to Maurice."
    #voice ""
    dr "P-p-p… Perhaps —"
    "The iron door bursts open."
    "Presper is flung across the room."
    "The beast {w} emerges."
    #voice ""
    # FINALLY SHOW THE AMALGAM FUCKER
    # BIG OL ROAR
    #voice ""
    # SOMEONE'S SCREAM
    #voice ""
    he "What in the holy fuck'n duck is THAT thing?"
    "The beast crawls over the mangled scrap it carved out of the door."
    voice "ar_ner4"

    ar "What... what is that thing...?! How long... has it been down here...?!"
    "Its figure becomes clear."
    #voice ""
    "Aures lets out a gasp."
    "It radiates the warmth of many dozens of bodies, grasping desperately at the air around them."
    "Stitches bind torsos to fingers, heads to thighs, chests to spines."
    #voice ""
    ma "Oh my god."
    "Endless pairs of eyes dart across the room, surveying the laboratory."
    "Their pupils are all narrow slits."
    voice "ly_sur1"

    ly "It's… Not right, this thing."
    "Presper, heavily bruised, pulls himself off the floor and shambles toward the beast."
    "The tubes that hang from his arms catch on debris, and he stops to retrieve them."
    "The tubes lead into the beast."
    "The amalgam."

    #voice ""
    ab "You want to know where this buffoon put me for 200 years?"
    #voice ""
    ab "There’s your answer."
    #voice ""
    # BIG OL ROAR AGAIN
    voice "ly_mad1"

    ly "Someone escort Elizabeth out of here."
    voice "ar_hap2"

    ar "I'll take her, Uncle... Elizabeth... we need to get you out of here... Please... I need you to come with me..."
    #voice ""
    el "No! It is time to be brave!"

    menu:
        "The beast clambers toward you."

        "Defend yourself.":
            "You seize one of the doctor’s surgical tools: a bonesaw."
            "You brandish it at the beast. It recoils for a moment…"
            "… until it barrels into you."
        "Let it approach you.":
            "Its pace does not slacken."
            "It barrels into you."
        "Flee.":
            "You turn to run from the beast."
            "But not before it barrels into you."

    "You can hear the shadow beside you squeal in terror."
    #voice ""
    ab "NO! NO! SOMEONE STOP IT!"
    "Beneath the weight of the beast, deep in its stitches and folds, you make out two figures sown within."
    "One is that of the man whose portrait hangs over the living room fireplace."
    "Abbé Maurice Lachaise."
    "Your recognize the second figure immediately."
    "As does [marianne_name]."
    voice "mae1-03"
    ma "No… no.. no no no no."
    voice "mae1-04"
    ma "No… no.. no no no no."
    #voice ""
    ma "That’s not me anymore, that’s not me. That’s not me."
    #voice ""
    ma "Somebody kill this thing. Kill it. Kill it."

    #voice ""
    ab "This thing has housed me long enough."
    #voice ""
    ab "Spare this thing, but do not let it have me."



    ly "Respectfully… Its cries of agony indicate otherwise."
    #voice ""
    au "Please, get it away. I don't like this. I'm scared."
    #voice ""
    el "Why... does it sounds so sad? Ugh, I don't wanna look!"
    voice "ar_sad2"

    #voice ""
    he "Ya'know, something like this here could be rather... useful."
    voice "ly_sad3"

    ar "Is... is there anything that could've... been done for it? It... it wasn't its fault that this happened to it..."
    #voice ""

    if herman_queststate is 7:
        "Herman looks to you."
        #voice ""
        he "Young'n, I owe you one."
        #voice ""
        vo "Observation. Aleatory variable makes suitable reactant."
        #voice ""
        he "My new benefactor could have a lot of fun with that beast under his thumb, just saying."

    #voice ""
    ab "What are you waiting for? Get this thing off of you."
    jump gameend2
