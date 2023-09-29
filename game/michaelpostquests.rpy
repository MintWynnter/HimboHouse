label postquest:

    # you just had a reflection, so figure out how you decompose and what exposition gets told

    if questsdone is 1:
        jump decomp1

    if questsdone is 2:
        jump decomp2

    if questsdone is 3:
        jump decomp3

    if questsdone is 4:
        jump decomp4

    if questsdone is 5:
        jump decomp5

    if questsdone is 6:
        jump decomp6


    call screen minimap()


label decomp1:

    #fingers
    "Your thoughts are interrupted by the sensation of something viscous sliding down your fingers."
    "It is semi-coagulated blood, dripping out of the torn webbing between each digit."
    "On closer inspection, it seems merely manipulating your fingers has stretched the tissue enough to tear it — past the knuckle down into the palm of your hand."
    "Your capacity to manipulate remains sufficient, but you can now see the muscles being pulled, the bones being curled around, and the puss squeezed out by every contraction and every flexion."
    #voice abq0-14
    ab "That you haven’t lost a finger altogether is remarkable."
    #voice
    ab "That said, I wouldn’t rule out the possibility."
    jump exposition1

label decomp2:

    #tongue
    "You press your tongue to the roof of your mouth in thought."
    "The roof does not push back. Instead, the tongue melts into the roof, disintegrating into an almost gelatinous paste."
    "You can feel the paste abrade against your gums and fill the gaps between your remaining teeth."
    "A bit emerges onto your lip. It is of an inconsistent texture and hue — shades of green and brown and red correspond to chunkier or more fluid consistencies."
    "It dribbles down your lip, and onto your chin."
    #voice
    ab "Oh my."
    #voice abq0-15
    ab "It might be a struggle to speak clearly now, but you must make your best effort, I suppose."
    #voice
    ab "Perhaps a mint is in order, if you can find one."
    jump exposition2

label decomp3:

    #knees
    "You casually shift your weight from one leg to another."
    "As you do, you feel a strange shift in your knee, as if your knee itself was being pulled toward the ground."
    "Looking down, it appears your knee cap has in fact sunken, down to your shin."
    "Your leg flexes as normal, but each movement realigns the cap, sliding back and forth along and around your leg."
    "Eventually, the cap rests just above your ankle, bulging the weakened skin above it."
    #voice abq0-16
    ab "It seems your meniscus has altogether melted. I do not envy you."
    #voice
    ab "Well, watch your step, I suppose. Taking a tumble might mean taking off your leg."
    jump exposition3

label decomp4:

    #ear
    "Your thoughts are not interrupted by anything in particular, yet your focus shifts."
    "It seems the soundscape of the mansion has shifted, gotten just a bit quieter."
    "You pause for just a moment, to capture the new perception, tilting your head back and forth."
    "One side feels lighter than the other."
    "You press your hand to your left ear — and find it missing."
    "Instead, you press against the exposed flesh. The squelch of shifting tissue bounds off your eardrum, which your finger is just short of punching through altogether."
    #voice abq0-17
    ab "I suppose the cartilage was always going to go."
    #voice
    ab "I similarly recommend you avoid picking your nose, if your ear is anything to go by."
    jump exposition4

label decomp5:

    #gallbladder
    "Suddenly, you are disrupted by a smell — somehow more vile than the stench you’ve been carrying thus far."
    "Finding the source is not easy. The smell is pervasive, everywhere. It follows you from place to place."
    "If it is another of your ghastly smells, then it is new and it is intense."
    "Searching your person yields the answer: A deep brown-green fluid seeps out of a small hole in your torso. Swiping a drop on your finger, you find it not to be viscous like blood. Rather, it rolls rather easily down your finger, filling in the grooves of your fingerprint as it descends."
    "It smells of excrement, and is highly concentrated."
    #voice abq0-18
    ab "Bile, I’m sure of it."
    #voice abq0-19
    ab "I have bad news for you: Your gallbladder has popped."
    #voice
    ab "Although you didn’t have a use for it anyway, anyone with a nose will find this absolutely revolting."
    #voice
    ab "Luckily, there’s only one such person here, and he has other reasons to be disgusted."
    jump exposition5

label decomp6:

    # shoulder
    "Before your next thought comes to you, you recoil to a stimulus in your left arm."
    "Your left shoulder drops about 2 inches down, hanging by your breast."
    "You flex your fingers — the muscles are still operable — but"
    "You shrug, trying to lift your shoulder back into its socket. It complies, but only briefly."
    "As it gives, you can feel individual strands of sinew snap before the arm finally drops again."
    "The disruption has left your shoulder and upper arm heavily bruised."
    #voice abq0-20
    ab "Awfully debilitating, that."
    #voice abq0-21
    ab "You’d best leave that arm alone for now, lest the whole thing rip off."
    #voice abq0-22
    ab "Then again, maybe it’s dead weight anyway."
    #voice abq0-23
    ab "Aha, \"dead.\""
    jump exposition6

label exposition1:

    #voice abq0-s901
    ab "Well, judging by this decomposition, it seems you’re not entirely human, either."
    #voice
    ab "You’re certainly corporeal, unlike these spectral denizens."
    #voice
    ab "But your capacity for decay is rather… accelerated."
    #voice abq0-s902
    menu:
        ab "I think most would call you a zombie."

        "\"A zombie?!\"":
            #voice
            ab "You’re familiar with the term, are you not?"
            #voice
            ab "A walking corpse? Zombie? Yes?"
        "\"Cool, a zombie!\"":
            #voice
            ab "I’m… happy to hear this excites you."
            #voice
            ab "It would not have been my reaction."
        "\"That would explain a lot.\"":
            #voice
            ab "It would certainly explain why you reek so horrifically."
            #voice
            ab "You’re lucky not every ghost feels the need to employ a sense of smell."

    #voice
    ab "Whatever the case, you’re not a zombie I’ve ever seen."
    #voice abq0-s903
    ab "I’ve roamed the halls of this mansion for a great many years."
    #voice
    ab "And your particular cadaver is novel."
    #voice
    ab "Where you come from, I don’t know."
    #voice abq0-s904
    ab "But you are not of this place."
    #voice
    menu:
        ab "Might be hard to believe with all these undead roaming around."

        "\"How do you know so much?\"":
            pass
        "\"What are you, exactly?\"":
            pass
        "\"How do you think I got here?\"":
            pass

    #voice abq0-s905
    ab "You will know with time."
    #voice
    ab "That is all."

    call screen minimap()

label exposition2:

    #voice
    ab "The state of your body is in rapid decline."
    #voice
    ab "I don’t know how much longer you have before you’re simply a pile of limbs and organs."
    #voice
    ab "I’d rather not think about it. Squeamish and all."
    #voice
    ab "Still, I think you deserve an introduction. To me."
    #voice abq0-s906
    ab "I am Abbé Maurice Lachaise, owner and proprietor of this mansion."
    #voice
    ab "I passed some 200 years ago, but my essence remained here in this mansion."
    #voice
    menu:
        ab "And now, for some reason, I’m in the back of your head."

        "\"A pleasure to meet you, Maurice.\"":
            #voice abq0-s907
            ab "The pleasure is mine, for the most part."
            #voice
            ab "It’s not every day I feel comfortable confiding in a dead man."
        "\"Why didn’t you tell me this earlier?\"":
            #voice abq0-s908
            ab "As mentioned, I don’t know who you are."
            #voice
            ab "I could have chosen to remain a disembodied figment of your subconscious."
            #voice
            ab "But I decided to trust you. Don’t make me regret it."
        "\"What is an abbé?\"":
            #voice
            ab "The French styling of abbot. A religious official."
            #voice abq0-s909
            ab "Always was a bit of a sinecure, though. Not that I’m complaining."

    "He lets out a gentle cough."
    #voice
    ab "As for the ghosts in this place, I precede all of them."
    #voice
    ab "I knew none of them in life and do not wish to know them."
    #voice abq0-s910
    ab "Frankly, they’re trespassing, although I don’t have the means to enforce it."
    #voice
    menu:
        ab "What happens to them seems to be up to you."

        "\"They seem to appreciate the help.\"":
            #voice
            ab "Quite."
        "\"I have been very busy with them…\"":
            #voice
            ab "Quite."
        "\"They’re not my responsibility.\"":
            #voice
            ab "If that’s how you feel, then that’s how it is."

    #voice
    ab "But even as we talk, me and you, your body continues to fall apart."
    #voice abq0-s911
    ab "I still don’t know what you are or why you’re here."
    #voice abq0-s912
    ab "Or, why I am bound to you."
    #voice
    ab "But, as I said before, you will know with time."
    #voice
    ab "Even if I don’t."

    call screen minimap()

label exposition3:

    jump midpoint

label exposition4:

label exposition5:

label exposition6:

label marianne_reflection:

    $ marianne_justfinished = False

    "The voice in your head chides."
    #voice abq0-s801
    ab "The time it takes, indeed."

    if marianne_queststate is 4:
        jump marianne_reflection_marianne
    if marianne_queststate is 5:
        jump marianne_reflection_daisy
    if marianne_queststate is 6:
        jump marianne_reflection_new

label marianne_reflection_marianne:

    #voice abq0-s802
    ab "All things considered, she does make a good Marianne."
    #voice
    ab "Though, chances are, the actual Marianne is still traipsing around somewhere out there."
    #voice abq0-s803
    ab "Undeath can be one big costume party if you let it, but…"
    #voice
    menu:
        ab "Doesn't seem like that self-loathing is going anywhere, huh?"
        "\"She was in too much pain seeing Daisy. She had to keep Marianne.\"":
            #voice abq0-s804
            ab "That she was. But I won’t be the first to say that a little emotional turmoil can go a long way."
            #voice
            ab "For good or for ill, though, I suppose. Perhaps you’re right."
        "\"Being Marianne seemed to bring out the best in her.\"":
            #voice abq0-s805
            ab "Yes, well, I think her perception of that Marianne might have soured her tonight."
            #voice
            ab "She seemed utterly convinced that the girl was happy all the time."
            #voice
            ab "A daft assumption to make, but it’s one we’ve managed to shatter."
            #voice
            ab "Let’s hope it doesn’t eat at her too much."
        "\"I’m not her counselor. She can keep playing pretend.\"":
            #voice abq0-s806
            ab "I suppose she is an adult, after all."
            #voice
            ab "She can make her own decisions. I don’t suppose a zombie knows any better than she."

    jump marianne_reflection_end

label marianne_reflection_daisy:
    #voice
    ab "I’ll be honest with you, if you’ll let me."
    #voice abq0-s807
    ab "I don’t think Daisy rolls that well off her tongue."
    #voice
    ab "She’s clearly unhappy with it."
    #voice
    menu:
        ab "Perhaps that will change with time?"
        "\"She’ll learn to love herself. It starts with Daisy.\"":
            #voice abq0-s808
            ab "It does start with Daisy, that’s for sure."
            #voice
            ab "You’d think when all you have is yourself, you’d have to love it."
            #voice
            ab "Hopefully, that’s the conclusion Daisy comes to as well."
        "\"Either way, she’s not living a lie anymore.\"":
            #voice abq0-s809
            ab "I suppose that is some kind of progress."
            #voice
            ab "I don’t doubt that honesty puts a good foot forward."
            #voice
            ab "And perhaps that’s the most reasonable thing you could have done for her."
        "\"It will or it won’t. It’s not my business.\"":
            #voice
            ab "It is not. You are not one who particularly has time, anyway."
            #voice abq0-s810
            ab "Her fate is hers to decide. At least her means Daisy, now."

    jump marianne_reflection_end

label marianne_reflection_new:

    #voice
    ab "I’ll be honest with you, if you’ll let me."
    #voice abq0-s811
    ab "Soul-searching sounds like a difficult thing for a ghost."
    #voice
    ab "I suspect she will find some success…"
    #voice
    menu:
        ab "But what do you think that will look like?"

        "\"A mix of brutal and compassionate self-honesty.\"":
            #voice
            ab "I think you’re quite right."
            #voice
            ab "How far that will get her is for us to… probably never know."
            #voice abq0-s812
            ab "Still, it sounds like progress. I wish her the best."
        "\"More vulnerable conversations with the other ghosts.\"":
            #voice
            ab "That might be a lot to ask of her, or maybe of them."
            #voice
            ab "But is the only way she’s going to get anywhere."
            #voice abq0-s813
            ab "Ruminating in this room has done her no good, after all."
            #voice
            ab "We shall see if she takes such initiative. That is for time to tell."
        "\"I don’t know. I didn’t really think it through.\"":
            #voice
            ab "Ah, I suspected as much."
            #voice abq0-s814
            ab "It didn’t seem Maria— didn’t seem she quite knew what she was up against, either."
            #voice
            ab "Still, I think ditching the names might symbolize something meaningful for her."
            #voice
            ab "Even if it doesn’t give her much direction, she knows where not to return."
            #voice
            ab "And that, in some sense, is progress."

    jump marianne_reflection_end

label marianne_reflection_end:
    #voice
    ab "Anyhow, there is yet still more to be attended to."
    jump postquest
