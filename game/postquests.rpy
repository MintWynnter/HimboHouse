label postquest:

    $questsdone = questsdone + 1

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
    voice "abq0-14"
    ab "That you haven’t lost a finger altogether is remarkable."
    #voice
    ab "That said, I wouldn’t rule out the possibility."
    jump exposition1

label decomp2:

    #tongue
    "You press your tongue to the roof of your mouth in thought."
    "The roof does not push back. Instead, the tongue melts into the roof, disintegrating into an almost gelatinous paste."
    "You can feel the paste abrade against your gums and fill the gaps between your remaining teeth."
    "A bit emerges onto your lip."
    "It is of an inconsistent texture and hue — shades of green and brown and red correspond to chunkier or more fluid consistencies."
    "It dribbles down your lip, and onto your chin."
    #voice
    ab "Oh my."
    voice "abq0-15"
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
    voice "abq0-16"
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
    "Instead, you press against the exposed flesh."
    "The squelch of shifting tissue bounds off your eardrum, which your finger is just short of punching through altogether."
    voice "abq0-17"
    ab "I suppose the cartilage was always going to go."
    #voice
    ab "I similarly recommend you avoid picking your nose, if your ear is anything to go by."
    jump exposition4

label decomp5:

    #gallbladder
    "Suddenly, you are disrupted by a smell — somehow more vile than the stench you’ve been carrying thus far."
    "Finding the source is not easy. The smell is pervasive, everywhere. It follows you from place to place."
    "If it is another of your ghastly smells, then it is new and it is intense."
    "Searching your person yields the answer: A deep brown-green fluid seeps out of a small hole in your torso."
    "Swiping a drop on your finger, you find it not to be viscous like blood."
    "Rather, it rolls rather easily down your finger, filling in the grooves of your fingerprint as it descends."
    "It smells of excrement, and is highly concentrated."
    voice "abq0-18"
    ab "Bile, I’m sure of it."
    voice "abq0-19"
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
    voice "abq0-20"
    ab "Awfully debilitating, that."
    voice "abq0-21"
    ab "You’d best leave that arm alone for now, lest the whole thing rip off."
    voice "abq0-22"
    ab "Then again, maybe it’s dead weight anyway."
    voice "abq0-23"
    ab "Aha, \"dead.\""
    jump exposition6

label exposition1:

    voice "abq0-s901"
    ab "Well, judging by this decomposition, it seems you’re not entirely human, either."
    #voice
    ab "You’re certainly corporeal, unlike these spectral denizens."
    #voice
    ab "But your capacity for decay is rather… accelerated."
    voice "abq0-s902"
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
    voice "abq0-s903"
    ab "I’ve roamed the halls of this mansion for a great many years."
    #voice
    ab "And your particular cadaver is novel."
    #voice
    ab "Where you come from, I don’t know."
    voice "abq0-s904"
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
    $ abbe_name = "Abbé Maurice"
    voice "abq0-s906"
    ab "I am Abbé Maurice Lachaise, owner and proprietor of this mansion."
    #voice
    ab "I passed some 200 years ago, but my essence remained here in this mansion."
    #voice
    menu:
        ab "And now, for some reason, I’m in the back of your head."

        "\"A pleasure to meet you, Maurice.\"":
            voice "abq0-s907"
            ab "The pleasure is mine, for the most part."
            #voice
            ab "It’s not every day I feel comfortable confiding in a dead man."
        "\"Why didn’t you tell me this earlier?\"":
            voice "abq0-s908"
            ab "As mentioned, I don’t know who you are."
            #voice
            ab "I could have chosen to remain a disembodied figment of your subconscious."
            #voice
            ab "But I decided to trust you. Don’t make me regret it."
        "\"What is an abbé?\"":
            #voice
            ab "The French styling of abbot. A religious official."
            voice "abq0-s909"
            ab "Always was a bit of a sinecure, though. Not that I’m complaining."

    "He lets out a gentle cough."
    #voice
    ab "As for the ghosts in this place, I precede all of them."
    #voice
    ab "I knew none of them in life and do not wish to know them."
    voice "abq0-s910"
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
    voice "abq0-s911"
    ab "I still don’t know what you are or why you’re here."
    voice "abq0-s912"
    ab "Or, why I am bound to you."
    #voice
    ab "But, as I said before, you will know with time."
    #voice
    ab "Even if I don’t."

    call screen minimap()

label exposition3:

    jump midpoint

label exposition4:

    "The levity is short-lived."
    #voice
    ab "So. Presper. The scientist. Doctor. However he brandishes himself."
    voice "abq0-127"
    ab "Antoine. I knew him."
    #voice
    ab "I built this mansion 200 years ago to seclude myself from the world."
    #voice
    ab "And when I grew old, I hired him to tend to me."
    voice "abq0-128"
    ab "He failed, and it seems to have gotten to his head."
    #voice
    menu:
        ab "What he’s doing alive and… well 200 years later is beyond me."

        "\"Sounds like he’s gone off the deep end.\"":
            #voice
            ab "Quite. And it doesn’t seem he’ll be out of the proverbial pool any time soon."
        "\"Sounds like he’s trying to bring you back.\"":
            #voice
            ab "That is kind of him. But I don’t think his means are the kind one ought to be comfortable with."
            #voice
            ab "And as far as the ends go, who knows if they’re that clear-cut."
        "\"Sounds like you and he have a lot in common.\"":
            #voice
            ab "Don’t remind me. I went isolationist before he did, let it be known."

    voice "abq0-129"
    ab "Antoine is responsible for both our predicaments. Let us keep the little worm under scrutiny until we know more."

    call screen minimap()

label exposition5:
    "His voice sharpens. You can feel his hypothetical teeth clench."
    voice "abq0-130"
    ab "Presper."
    voice "abq0-131"
    ab "That good for nothing little scoundrel."
    #voice
    ab "He was always so eager to please. A shame he was no good at it."
    voice "abq0-132"
    ab "I was an old man. I needed help. He promised it."
    #voice
    menu:
        ab "And the ungrateful, lazy bastard got me killed instead."

        "\"For all his morbidity, he doesn’t seem like the killing type.\"":
            #voice
            ab "What, you think this vessel we’re walking around in came from a morgue or something?"
            #voice
            ab "You’ve got a slice cut deep into your head, for crying out loud."
            #voice
            ab "He must have swiped you with a shovel, the cretin."

        "\"Did he experiment on you like he did me?\"":
            #voice
            ab "Considering I’m a disembodied spirit now, I suspect he did toy with some part of my metaphysics."
            #voice
            ab "Not that I asked for it. The miserable little twerp must have thought he was doing a speck of good."
        "\"Sounds like you were old, you were going to die anyway.\"":
            #voice
            ab "That’s why I brought the idiot here in the first place, don’t you understand?"

    "Maurice’s anger grows sharper."
    #voice
    ab "Presper, that bumbling buffoon."
    voice "abq0-133"
    ab "I gave him the world, every kind of amenity you could imagine."
    voice "abq0-134"
    ab "And he still let me die."
    #voice
    menu:
        ab "A spoiled brat who’s only further spoiled since my departure."

        "\"Settle, Maurice. You’re getting awfully riled up.\"":
            pass
        "\"How did he let you die? Did he do something to you?\"":
            pass
        "\"Some people just don’t know how good they have it.\"":
            pass

    #voice
    ab "The more I think about the negligent malpractitioner, the more I remember how he betrayed me."
    #voice
    ab "No, he didn’t outright kill me. He was too much a coward for that."
    #voice
    ab "He tried to save me, to keep me alive and well."
    #voice
    ab "But no matter how hard a blustering nincompoop tries…"
    voice "abq0-135"
    ab "No matter how many years he spends tinkering in a basement with the powers of a demigod —"
    voice "abq0-136"
    ab "He will always be a failure."
    voice "abq0-137"
    ab "I will speak no more of it. Let’s move on."

    call screen minimap()

label exposition6:

    jump gameend

label marianne_reflection:

    $ marianne_justfinished = False

    "The voice in your head chides."
    voice "abq0-s801"
    ab "The time it takes, indeed."

    if marianne_queststate is 4:
        jump marianne_reflection_marianne
    if marianne_queststate is 5:
        jump marianne_reflection_daisy
    if marianne_queststate is 6:
        jump marianne_reflection_new

label marianne_reflection_marianne:

    voice "abq0-s802"
    ab "All things considered, she does make a good Marianne."
    #voice
    ab "Though, chances are, the actual Marianne is still traipsing around somewhere out there."
    voice "abq0-s803"
    ab "Undeath can be one big costume party if you let it, but…"
    #voice
    menu:
        ab "Doesn't seem like that self-loathing is going anywhere, huh?"
        "\"She was in too much pain seeing Daisy. She had to keep Marianne.\"":
            voice "abq0-s804"
            ab "That she was. But I won’t be the first to say that a little emotional turmoil can go a long way."
            #voice
            ab "For good or for ill, though, I suppose. Perhaps you’re right."
        "\"Being Marianne seemed to bring out the best in her.\"":
            voice "abq0-s805"
            ab "Yes, well, I think her perception of that Marianne might have soured her tonight."
            #voice
            ab "She seemed utterly convinced that the girl was happy all the time."
            #voice
            ab "A daft assumption to make, but it’s one we’ve managed to shatter."
            #voice
            ab "Let’s hope it doesn’t eat at her too much."
        "\"I’m not her counselor. She can keep playing pretend.\"":
            voice "abq0-s806"
            ab "I suppose she is an adult, after all."
            #voice
            ab "She can make her own decisions. I don’t suppose a zombie knows any better than she."

    jump marianne_reflection_end

label marianne_reflection_daisy:
    #voice
    ab "I’ll be honest with you, if you’ll let me."
    voice "abq0-s807"
    ab "I don’t think Daisy rolls that well off her tongue."
    #voice
    ab "She’s clearly unhappy with it."
    #voice
    menu:
        ab "Perhaps that will change with time?"
        "\"She’ll learn to love herself. It starts with Daisy.\"":
            voice "abq0-s808"
            ab "It does start with Daisy, that’s for sure."
            #voice
            ab "You’d think when all you have is yourself, you’d have to love it."
            #voice
            ab "Hopefully, that’s the conclusion Daisy comes to as well."
        "\"Either way, she’s not living a lie anymore.\"":
            voice "abq0-s809"
            ab "I suppose that is some kind of progress."
            #voice
            ab "I don’t doubt that honesty puts a good foot forward."
            #voice
            ab "And perhaps that’s the most reasonable thing you could have done for her."
        "\"It will or it won’t. It’s not my business.\"":
            #voice
            ab "It is not. You are not one who particularly has time, anyway."
            voice "abq0-s810"
            ab "Her fate is hers to decide. At least her means Daisy, now."

    jump marianne_reflection_end

label marianne_reflection_new:

    #voice
    ab "I’ll be honest with you, if you’ll let me."
    voice "abq0-s811"
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
            voice "abq0-s812"
            ab "Still, it sounds like progress. I wish her the best."
        "\"More vulnerable conversations with the other ghosts.\"":
            #voice
            ab "That might be a lot to ask of her, or maybe of them."
            #voice
            ab "But is the only way she’s going to get anywhere."
            voice "abq0-s813"
            ab "Ruminating in this room has done her no good, after all."
            #voice
            ab "We shall see if she takes such initiative. That is for time to tell."
        "\"I don’t know. I didn’t really think it through.\"":
            #voice
            ab "Ah, I suspected as much."
            voice "abq0-s814"
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

label lysander_reflection:

    "The voice in your head opines."

    if lysander_queststate is 7:
        jump lysander_reflection_free

    if lysander_queststate is 8:
        jump lysander_reflection_doom

    if lysander_queststate is 9:
        jump lysander_reflection_trade

    if lysander_queststate is 10:
        jump lysander_reflection_doom

label lysander_reflection_free:

    #voice
    ab "You got him out. Very impressive."
    #voice
    ab "And you even somehow managed to make a perpetually guilty man not feel so guilty."
    #voice
    ab "That was a tall ask to extend such kindness, and I don’t recall anyone actually asking."
    voice "abq0-s507"
    menu:
        ab "This compassion, what has prompted it?"
        "\"Lysander has suffered enough. He needed relief.\"":
            voice "abq0-s508"
            ab "You’re right to say that. The poor sap has gone through hell and back."
            voice "abq0-s509"
            ab "Something tells me he’ll never really be free."
            #voice
            ab "But, undoing the curse is an excellent start."
            jump lysander_reflection_end

        "\"Compassion doesn’t need prompting, you know.\"":
            voice "abq0-s510"
            ab "A bleeding heart, we are. The man died whilst shooting another."
            #voice
            ab "To assume compassion is warranted is… naive, I think."
            #voice
            ab "Not to sound callous."
            voice "abq0-s511"
            ab "A more level head would serve you, is all."
            jump lysander_reflection_end

        "\"Kindness begets kindness. I expect it in turn.\"":
            voice "abq0-s512"
            ab "Selfish, but with good means. I quite like that tack."
            #voice
            ab "Kill ‘em with kindness, as they say."
            voice "abq0-s513"
            ab "I’m sure Lysander is enough of a pushover to return the favor."
            jump lysander_reflection_end

label lysander_reflection_trade:

    voice "abq0-s519"
    ab "Well, it’s all yours. The curse, that is."
    #voice
    ab "I suppose it’s your lot, now."
    #voice
    ab "I’m not sure how that will manifest."
    voice "abq0-s520"
    ab "Perhaps it won’t matter. Perhaps it will spell something worse."
    #voice
    ab "I couldn’t tell you, but I can ask:"
    voice "abq0-s521"
    menu:
        ab "Why make a trade like that?"

        "\"Lysander has suffered enough. He needed relief.\"":
            voice "abq0-66.01"
            ab "You’re right to say that. The poor sap has gone through hell and back."
            voice "abq0-s509"
            ab "Something tells me he’ll never really be free."
            #voice
            ab "But, undoing the curse is an excellent start."

        "\"Compassion doesn’t need prompting, you know.\"":
            voice "abq0-s510"
            ab "A bleeding heart, we are. The man died whilst shooting another."
            #voice
            ab "To assume compassion is warranted is… naive, I think."
            #voice
            ab "Not to sound callous."
            voice "abq0-s511"
            ab "A more level head would serve you, is all."

        "\"Kindness begets kindness. I expect it in turn.\"":
            voice "abq0-s512"
            ab "Selfish, but with good means. I quite like that tack."
            #voice
            ab "Kill ‘em with kindness, as they say."
            voice "abq0-s513"
            ab "I’m sure Lysander is enough of a pushover to return the favor."

    jump lysander_reflection_end

label lysander_reflection_doom:

    voice "abq0-s514"
    ab "That is… not how I expected you to handle this, if I’ll be honest."
    #voice
    ab "The boy doesn't seem like he'll be getting out of the ground anytime soon."
    ab "Not without that piece of jewlery you found, at least."
    #voice
    ab "I expect this spirit will be forever in poor… spirits."
    voice "abq0-s515"
    menu:
        ab "Is that what you wanted, for him to suffer?"

        "\"Yes.\"":
            #voice
            ab "Aha. I see."
            voice "abq0-s516"
            ab "Well, full points for you then, he is certainly suffering."
            #voice
            ab "(sigh) At least you do what you set out to do."
            #voice
            ab "I cannot say that of everyone."
        "\"I don’t want it. He just deserves it.\"":
            voice "abq0-s517"
            ab "And you are the arbiter of that deserving?"
            #voice
            ab "That’s certainly news to me."
            #voice
            ab "Still, I cannot fault you. He brought it on himself."
            #voice
            ab "The least he can do is own up to it."
        "\"This was a misunderstanding. I didn't want this for him.\"":
            ab "Well, it doesn't seem the fates are that keen on heeding your wants."
            ab "Still, I cannot fault you. He brought it on himself."
            ab "The least he can do is own up to it."

    jump lysander_reflection_end

label lysander_reflection_end:

    ab "Anyhow, that is that, as they say. Onward."
    jump postquest

label herman_reflection:

    $ herman_questjustfinished = False

    "Now that Herman has disregarded you, per usual, the voice in your head finally eeks out a response."

    if herman_queststate is 7:
        jump herman_reflection_gave
    if herman_queststate is 8:
        jump herman_reflection_threw

label herman_reflection_end:

    ab "Well, never mind that. There is more to this mansion. Let us venture forth."
    jump postquest

label herman_reflection_gave:

    voice "abq0-067"
    ab "You saw that, uh, thing as well, right?"
    #voice
    ab "Nothing against the crooked Dixie lad, but —"
    voice "abq0-068"
    menu:
        ab "Surely, it was unwise to hand that ring over to him, right?"
        "\"I didn’t expect that ring to actually have any power!\"":
            voice "abq0-069"
            ab "Yes, well, perhaps the supernatural nature of everything you’ve seen tonight would clue you in on that fact."
            voice "abq0-070"
            ab "Then again, maybe that was all just a trick of the light."
            #voice
            ab "Here’s hoping, at least."
        "\"I just did as I was told.\"":
            voice "abq0-071"
            ab "I cannot argue with that."
            voice "abq0-072"
            ab "Actually, I could. But, I see no benefit."
            #voice
            ab "What’s done is done."
            #voice
            ab "Hopefully this newfound power of his doesn’t come back to bite us."
        "\"Nah, it’s cool. I wanted him to have eldritch power.\"":
            voice "abq0-073"
            ab "You did?"
            #voice
            ab "I mean, of course you did."
            voice "abq0-074"
            ab "What’s one more undead monstrosity roaming the house?"
            #voice
            ab "Hopefully this newfound power of his doesn’t come back to bite us."
            #voice
            ab "It’s not as if that never happens in horror stories…"

    jump herman_reflection_end

label herman_reflection_threw:

    voice "abq0-075"
    ab "You know, I expected him to handle that refusal with less… grace."
    #voice
    ab "But, clearly he doesn’t see you as much of an obstacle."
    voice "abq0-076"
    menu:
        ab "That concerns you at least a little, does it not?"

        "\"I suppose I had better watch my back…\"":
            voice "abq0-077"
            ab "That might be wise, given his history of… stubbornness."
            #voice
            ab "Still, perhaps he’s bluffing. We won’t know till we know."
            #voice
            ab "And here’s to hoping we never know."
        "\"Herman is welcome to underestimate me.\"":
            voice "abq0-078"
            ab "I will say, Herman has been around the undead block."
            #voice
            ab "But perhaps you bring something to the table that neither of us recognize."
            #voice
            ab "Not that I underestimate you, I simply…"
            #voice
            ab "... I need not worry."
        "\"He’s an oaf. How he feels does not concern me.\"":
            voice "abq0-079"
            ab "I do not believe Herman is one to share in your apathy."
            #voice
            ab "Not that I disagree with you on the first count. He is not bright."
            #voice
            ab "But he is ambitious. And, at least for that, you might show some concern."

    jump herman_reflection_end

label aures_reflection_end:

    voice "abq0-094"
    ab "Well, that’s enough of that."
    jump postquest

label aures_reflection:

    "As you part from the two, the voice in your head makes his presence known."

    if aures_good:
        jump aures_reflection_good
    else:
        jump aures_reflection_bad

label aures_reflection_good:

    #voice
    ab "I, erm… hmm."
    voice "abq0-083"
    ab "I must say I was averse to all of this."
    #voice
    ab "But, despite your methods, it is sweet."
    voice "abq0-084"
    menu:
        ab "Something about her makes me quite uncomfortable, though I can’t quite put a name to it."
        "\"She hyperfixates to an unnerving degree,that’s for sure.\"":
            voice "abq0-085"
            ab "Yes, to an extent that zeal of hers is charming, but…"
            #voice
            ab "Perhaps that level of militant fervor is best left in the Middle Ages."
            #voice
            ab "Still, she managed to make do."
        "\"The word you're looking for is ‘yandere.’\"":
            voice "abq0-086"
            ab "I beg your pardon?"
            #voice
            ab "Sounds either foreign or newfangled to me."
            voice "abq0-087"
            ab "What did you say? Yawn-duh-ray?"
            #voice
            ab "Well, if that’s what you say she is, that’s what she is."
            #voice
            ab "I’m in no position to argue."
        "\"I didn’t notice anything wrong with her.\"":
            #voice
            ab "I… hmm…"
            voice "abq0-088"
            ab "No, of course you didn’t. Why would you?"
            #voice
            ab "Just a standup young girl she is, obnoxious laugh and all."
            #voice
            ab "I won’t cast judgment. To each their own."

    jump aures_reflection_end

label aures_reflection_bad:

    voice "abq0-089"
    ab "That poor lad…"
    #voice
    ab "That Aures girl has really flown off the handle."
    #voice
    ab "And now, he’s hers. Bit of a downer for him, I imagine."
    voice "abq0-090"
    menu:
        ab "Did he really deserve this fate?"
        "\"Surely he did something to draw her attention in the first place.\"":
            voice "abq0-091"
            ab "I suppose you are right. We don’t know him like she does."
            #voice
            ab "Although, I’d be hard-pressed to say anything warrants being at her beck and call."
            #voice
            ab "I know of many insidious men who have performed deeply insidious deeds."
            ab "I would introduce none of them to Aures."
        "\"No, but it’s out of our hands, now.\"":
            #voice
            ab "Yes, I suppose so."
            voice "abq0-092"
            ab "And besides,this was always going to be the logical conclusion to things."
            #voice
            ab "She wants, and now she has. Who are we to intervene?"
        "\"He’s got a hot undead girlfriend, he’ll be fine.\"":
            #voice
            ab "Perhaps we have differing tastes."
            voice "abq0-093"
            ab "She might be a looker, but I prefer my partners a little less… possessive."
            #voice
            ab "Luckily, I’ll never be in a position to have to turn her down, now."
            #voice
            ab "Minoru has solved that problem for us, at least."
    jump aures_reflection_end


label elizabeth_reflection_end:

    voice "abq0-036"
    ab "Come. There is more to do."
    jump postquest


label elizabeth_reflection:

    if elizabeth_queststate is 6:
        jump elizabeth_reflection_truth
    if elizabeth_queststate is 7:
        jump elizabeth_reflection_lie

label elizabeth_reflection_truth:

        "You can sense the voice in your head watching the young girl."
        voice "abq0-033"
        ab "That must have been… difficult."
        #voice
        ab "She took it quite well, all things considered…"
        voice "abq0-034"
        ab "But do you really think the truth was worth the turmoil?"
        menu:
            "\"Of course. She deserved to know.\"":
                voice "abq0-035"
                ab "Is that a testament to your compassion or your pity?"
                #voice
                ab "It does not matter to me, I suppose."
                #voice
                ab "But, chew on that, won’t you."
            "\"The truth is always worth knowing.\"":
                voice "abq0-037"
                ab "I admire your commitment to such absolutes."
                #voice
                ab "I agree quite firmly."
                #voice
                ab "Still, I don’t think that made the look on her face any easier to stomach."
            "\"Turmoil was the point, actually.\"":
                voice "abq0-038"
                ab "I see."
                #voice
                ab "It builds character, I suppose."
                #voice
                ab "She’s a bit young for that kind of… harsh reality."
                voice "abq0-039"
                ab "But, start them early, as they say."

        jump elizabeth_reflection_end


label elizabeth_reflection_lie:

    "You can sense the voice in your head watching the young girl."
    voice "abq0-040"
    ab "Ignorant bliss, if I’ve ever seen it."
    #voice
    ab "Your secret is safe with me, but…"
    voice "abq0-041"
    ab "You don’t think you should have told her the truth?"
    menu:
        "\"It would have been too much for her.\"":
            #voice
            ab "Perhaps."
            voice "abq0-042"
            ab "She’s so temperamental now — I can only imagine how much worse it could get."
            #voice
            ab "Keeping it to yourself was, in that way, wise."
        "\"She’ll find out on her own, eventually.\"":
            #voice
            ab "‘Eventually’ could be another century, seeing as all she wants to do is warm herself by the fire."
            voice "abq0-043"
            ab "But, what is time to a ghost? Perhaps there is no harm in it."
        "\"She’s a brat. I don’t owe her anything.\"":
            voice "abq0-044"
            ab "You are… not incorrect. On both counts, I suppose."
            #voice
            ab "Still, I would not equate her temperament with vitriol."
            #voice
            ab "She will need help, but I admit it needn’t be from us."

    jump elizabeth_reflection_end


label arabella_reflection_end:

    ab "Now, let’s leave this girl be."
    jump postquest

label arabella_reflection:

    "Although it has none, the voice in your head clears its throat."

    if q3_state is 2 or q3_state is 3:
        jump arabella_reflection_bad

    if q3_state is 4:
        jump arabella_reflection_good


label arabella_reflection_bad:
    voice "abq0-028"
    ab "This mansion is, in many ways, labyrinthian."
    #voice
    ab "There hide a great many more secrets than could be found in one evening."
    #voice
    ab "I think she sensed how much more there is to find."
    voice "abq0-029"
    ab "But surely, to dig through this decrepit place is asking much of you, is it not?"
    menu:
        "\"I cannot spare the time.\"":
            voice "abq0-030"
            ab "I suppose you cannot. You’ve been a very busy zombie thus far, I will say."
        "\"What I found is what I gave her. I did my part.\"":
            voice "abq0-031"
            ab "She seems to have a bit more self-awareness than before, yes."
            #voice
            ab "I suppose that’s a tall ask for a ghost, so good on you."
        "\"I am not her servant. She should be grateful I heard her out at all.\"":
            voice "abq0-032"
            ab "That you did, and she sounded grateful enough."
            #voice
            ab "Although I find gratitude so, so hollow. I prefer results."

    jump arabella_reflection_end

label arabella_reflection_good:

    voice "abq0-023"
    ab "You went through an awful lot of trouble for this girl."
    #voice
    ab "She was mistreated at every turn, and even still she finds it in her heart to forgive."
    voice "abq0-024"
    ab "Is that strength of character, or naivety?"
    menu:
        "\"It takes a lot of courage to forgive those who hurt you.\"":
            voice "abq0-025"
            ab "‘Courage’ is perhaps not the word I’d use… But I see your point."
            #voice
            ab "I shall dwell on that."
        "\"She is a child, all she can do is accept what comes at her.\"":
            voice "abq0-026"
            ab "She has certainly played the part."
            #voice
            ab "It might do her good. Anything to get her out of this place."
        "\"Worse, it’s folly.\"":
            voice "abq0-027"
            ab "I was always of the mind that to forgive is to forget."
            #voice
            ab "If that is true, though. then I must say I quite envy her."
    jump arabella_reflection_end
