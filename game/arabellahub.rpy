label arabella_hub:

    # custom greeting

label arabella_convohub:

    #show arabella neutral or whatever

    menu:

        "\"About Elizabeth...\"" if elizabeth_queststate is 2:
            jump arabella_elizabeth

        "\"We need to talk about Elizabeth again.\"" if elizabeth_queststate is 4 and q5_location is 0:
            jump arabella_elizabeth2

        "\"This mansion seems to hold centuries of history. Can you tell me more about its origins and your connection to it?\"":
            show arabella melancholic
            #voice "arht-01"
            ar "This mansion, as old as time itself, has been a sanctuary for many families for generations. It has witnessed joyous celebrations and mournful farewells."
            show arabella joyful
            #voice "arht-02"
            ar "My earliest memories are of playing in these halls, the echo of my laughter juxtaposed against the house's solemn silence."
            #voice "arht-03"
            ar "Every stone, every tapestry tells a tale, some of which I yearn to remember fully."
            jump arabella_convohub

        "\"Your need to remember your lost memories is interesting to me. Is there anything you can recall of your life before everything became hazy?\"":
            show arabella melancholic
            #voice "arht-04"
            ar "There are moments, fleeting like the embers of a dying fire, that I clutch onto. I remember a pendant, the scent of roses in the garden, and the shadow of my Uncle Lysander always close by."
            #voice "arht-05"
            ar "Yet, there's a barrier... like a thick mist... obscuring deeper memories. I often wonder if there's a reason some moments remain veiled."
            jump arabella_convohub

        "\"You’re not the only other spirit here, are you? Have you encountered others bound to this place?\"":
            show arabella contemplative
            #voice "arht-06"
            ar "You have a keen sense. Indeed, this mansion is not just my prison. Over the years, I've sensed other souls, each ensnared by their own tales."
            #voice "arht-07"
            ar "Some are mere whispers, transient and evasive... Others, like Lysander, hold a more dominant presence."
            #voice "arht-08"
            ar "While our stories differ, our shared fate binds us to this timeless mansion..."
            jump arabella_convohub

        "\"Can you tell me, how did you die?\"":
            if q3_death_convo_trigger:
                "Arabella refuses to speak any more about this."
                jump arabella_convohub
            else:
                show arabella melancholic
                #voice "arht-09"
                ar "... That... is a topic that I would rather not indulge in... Would the truth of my death make a difference on this quest?"
                $ q3_death_convo_trigger = True
                jump arabella_convohub

        "Leave.":
            # custom goodbye
            call screen minimap()



label arabella_elizabeth:

    ar "Oh, the little girl?"
    ar "I heard her scream..."
    mc "I surprised her at first, but then we spoke for a while."
    ar "She… allowed you to talk with her? It had taken so long… for her to open up to me…"
    mc "Well, she seems to be scared of all of you."
    ar "Oh dear…"
    ar "... I say this as a warning to you… Leave Elizabeth be... Please..."
    ar "You should stay away. No harm can come to her."
    mc "I'm just here to run an errand for her, that's all..."
    "Arabella sighs, then turns back at you."
    ar "... What is it that you seek?"
    mc "All I need is a pen and some paper."
    ar "I see... And may I ask what she would want these items for?"

    menu:
        "\"She wants to draw a map.\"":
            "Arabella's face crosses briefly with a look that is mixed of both confusion and concern."
            ar "But... why would she...?"
            ar "I see... I... I understand what is happening..."
            ar "I am not a stranger to the kinds of people who do not put others' best interests at heart."
            mc "It's not for me, it's for her. She wants to go home."
            ar "... You... you swear this to be the truth? She... asked you for your aid?"
            mc "I promise."
            "Arabella looks around for a moment, sighs hard in reluctance, then recomposes herself."

        "\"I'm in a hurry, Arabella. Where are the paper and pen?\"":
            "Arabella gives you a look you can't place. It's intimidating, but you try to hold a poker face."
            "She doesn't speak — doesn't even move."

        "(Lie) \"She wants to draw something, that's all.\"":
            ar "... Is that so...?"
            mc "You know... I mean, what do you expect?"
            mc "She's a little girl, and kids get bored easily…"
            mc "Besides, she doesn't exactly have anyone to really play with, and she gets kind of scared around you ghosts."
            ar" I do not believe you..."
            mc "What else would she need a pen and paper for, then?"
            ar "To write a letter, perhaps...? To use it to have someone draw a map for her...?"
            mc "She doesn't even know where she lives!"
            ar "And are you so sure about this? How are you so sure she doesn't?"
            "You shift under her gaze, looking away from her briefly, gulping hard."
            ar "I knew it."

    ar "So... It is you... You are the one to bring her back to her... tragic truth..."
    mc "What... what do you mean?"
    ar "Is it not obvious? A little girl, in a thin jacket... In the middle of winter... seemingly running away from home...?"
    ar "What could possibly drive a child away from the warmth and safety of their home?"
    "Arabella is staring sharply at you."
    "If Elizabeth's glare shows fear and anxiety, Arabella shows you a clear warning and hostility."
    "The way she looks at you, you feel as if you're staring at a different person now."
    ar "I warn you once more... You must leave her be, if you know what's best for everybody..."
    ar "She needs not your help... She... she is safe here..."
    "Arabella shoves a pen and paper at you."
    "You stare at it for a while."
    ar "Please, I beg of you..."
    ar "Just... leave the poor girl be in peace..."
    "You grab the pen and paper and stow them away."
    $ elizabeth_queststate = 3
    $ q5_location = 0
    jump arabella_convohub

label arabella_elizabeth2:

    ar "I'm sorry... but I do not wish to have that conversation with you… I can't..."
    mc "Can you at least hear me out and let me ask my questions, please?"
    ar "Listen to me carefully..."
    ar "I appreciate what you have been doing here, for all of us..."
    ar "But... Elizabeth... Just... Leave her be."
    "Arabella seems to think for a moment, then after a few beats nods in a way that is obviously not directed at you."
    ar "I fear that any information I may or may not have on Elizabeth could be used in... nefarious ways."
    ar "In ways that will lead to her becoming hurt more than she has already been, in life and in death..."
    ar "So I am sorry, but we cannot help you this time..."
    mc "How are you so sure that the information you have will hurt her?"
    ar "How do you plan to 'help' the poor child? By forcing her to remember one of the single most painful things one can ask another to recall?"
    ar "And for what? To help a child's resolve that she cannot possibly grasp the reality of?"
    ar "I urge you, since you want to know the truth so bad... Take a look at these."
    "Arabella hands you a couple of newspaper clippings."
    # HEY IT'S THE HAVE YOU SEEN ME ICON LMAO
    "On the first paper you see, it was the exact face of Elizabeth, with slightly longer hair, more lively expressions, and less water dripping from her entire being."
    "Under the picture, a sentence 'HAVE YOU SEEN ME?' printed big on the paper."
    "You take out the second paper. On it, in the middle of crowding police, a picture of a woman in her 30s is seen holding a children's jacket."
    "She was entirely disheveled with dried tears and dark circles under her eyes."
    "\"—Was last seen going out of the house at 4 p.m., walking towards the bridge.\""
    "\"It is reported that there was a slight argument between her and the mother before the time she was last seen. Police are currently investigating—\""
    "The third paper, there was no picture this time, only a big headline 'SEARCH CALLED OFF'."
    "\"—Being discontinued, due to insufficient leads regarding the whereabouts of the missing person.\""
    "\"'I hope you're happy and safe, I love you so much, and I'm sorry I can't be a better mother for you,' The mother of the little girl told our editor, a small message we all hope Elizabeth will read.\""
    "\"The family has decided to move away from their residence but will keep close contact with the police.\""
    "\"The police will still receive any information regarding the missing Elizabeth—\""
    "You read them all carefully."
    "Every gear in your head turns as you process the entire broken messages into one string of story."

    menu:
        ar "What do you think happened to her?"

        "She fell into a river after running away.":
            ar "Do you feel her situation to be that simplistic? Perhaps there was more at play?"
            mc "It said she had an argument before leaving home—"
            ar "I understand. The child's mother, she was not good to her daughter most of the time."
            ar "I suspect she was simply cruel."
            ar "That poor girl had been suffering. That's why she fled in the dead of winter."
            mc "Didn't you read the mother's quote? She sounded desperate to have her daughter back."
            ar "People are quick to recant, even from thr worst of things."
            ar "I... cannot fathom a loving mother would force her child to feel that their only option… was to run off in sub-zero temperatures with nowhere to go…"
            ar "I could hardly fathom that same mother leave the home before her child was safely back in her arms... I cannot understand it..."

        "Her mother killed her and ran away.":
            "Arabella flinches at the word \"killed.\""
            ar "No. Such cruelty is inhuman. Human cruelty is much more subtle."
            ar "Don't you find it odd though… That the family just up and moved without knowing the whereabouts of their daughter?"
            ar "If she had returned home, she would have found it completely empty and would have probably succumbed to the same fate..."
            mc "Now, why would she wish to return if her mother was the cause of her running away in the first place?"
            ar "...Family is a powerful force. I'm afraid that is not the point I am trying to get across..."
            mc "But, isn't that the most important point, here?"

        "She got lost and ended up here.":
            ar "But... she wouldn't have ended up here... had her mother gone searching for her child after they ran off... right?"
            ar "I cannot understand... a mother that would allow her child to wander alone in such harsh conditions..."

    mc "Are you alright? You're speaking to something deeper than the facts."
    ar "Hmm? Oh... yes... I'm... I'm alright..."
    "She averts her gaze, now avoiding eye contact with you."
    "Something… doesn't feel right with her. She seems on edge."
    mc "Well, I think we should stick with the facts instead of going off of a hunch or any assumptions."
    mc "Look, we have the newspaper articles right here, but I don't feel like we have the whole story here."
    ar "What if… the stories had been fabricated? By the mother, the police… anybody… to try to paint the mother in a light that made her stand out to be something that she was not...?"
    ar "If what I believe is to be reality... how... would you be able to help Elizabeth then... without hurting her...?"
    menu:
        "I will still tell her the truth.":
            ar "No... the truth will only hurt her... There has to be another way to go about this..."
            mc "You can't expect to have her sheltered from the truth for the rest of eternity, can you?"
            ar "..."
            mc "You've asked me to help you discover your truth, Arabella."
            mc "Do you beleive that what you find will be too painful for someone like Elizabeth?"
            "Arabella's eyes well up with tears."
            "You see it in her face, in her eyes, that you seem to have gotten through to her."
            "She doesn't look at you. Her resolve seems to have shattered."

        "I won't show her this, it's too much for her.":
            "Arabella seems to visibly relax, but only slightly. She doesn't answer you, but she gives you the smallest nod in acknowledgment."

        "Maybe it's better for her to stay here.":
            "Arabella sighs in obvious relief and visibly relaxes, as if a huge weight had been lifted off of her shoulders. She doesn't answer you, but she gives a small smile beaming with contentedness."

    ar "Do you think she will be okay with that?"
    menu:
        "She deserves the truth.":
            pass
        "I won't tell her, it's too cruel.":
            pass
        "...I have to think this through some more.":
            pass


    "Holding the newspaper clippings in your hand, you sigh deeply, thinking of the choice you're about to make."
    "You shove the papers into your pocket."

    $ q5_state = 5
    jump arabella_convohub



# Arabella Greetings upon return
label q3_greetings:
    $ q3_random_greeting = renpy.random.randint(0,4)
    if q3_random_greeting == 0:
        ar "Ah, a familiar face amid these ever-whispering walls. What brings you?"
    if q3_random_greeting == 1:
        ar "Your presence stirs the memories of this mansion. Ready for another journey into the unknown?"
    if q3_random_greeting == 2:
        ar "Every return of yours feels like a step closer to the truth. How shall we proceed?"
    if q3_random_greeting == 3:
        ar "Between these walls, our quest continues. What stories have you come to share?"
    if q3_random_greeting == 4:
        ar "The winds of time seem to pause when you're here. To what mystery shall we attend today?"

# Arabella Farewell
label q3_farewell:
    $ q3_random_farewell = renpy.random.randint(0,4)
    if q3_random_farewell == 0:
        ar "As you step beyond these doors, remember the tales they hold. Until next time."
    elif q3_random_farewell == 1:
        ar "May our shared quest echo in your thoughts till we meet again in these ancient corridors."
    elif q3_random_farewell == 2:
        ar "Each parting is but a brief pause in our tale. Farewell, and let the mysteries guide you back."
    elif q3_random_farewell == 3:
        ar "Our paths have intertwined for a reason. Go safely, and remember the mysteries we seek to unveil."
    else:
        ar "As the mansion's whispers fade, take our shared memories with you. Until our spirits reunite."

# Arabella Exit
label foyer_exit:
    call screen minimap()
