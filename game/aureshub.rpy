

label aures_hub:

    default au_greeting_kill = True
    default au_greeting_1 = True
    default au_greeting_2 = True
    default au_greeting_3 = True
    default au_greeting_4 = True

    default au_farewell_selfish = True
    default au_farewell_1 = True
    default au_farewell_2 = True
    default au_farewell_3 = True
    default au_farewell_4 = True

    show aures neutral at aures_spot
    with dissolve

    if auresQuestState > 5:
        show minoru neutral at minoru_spot
        with dissolve

    #greeting
    if au_greeting_kill and killPath:
        $ au_greeting_kill = False
        #voice "aug-06"
        au "Oh, hello. Have you seen Minoru? I can't find him."
    elif au_greeting_1:
        $ au_greeting_1 = False
        #voice "aug-01"
        au "Ohohohohoho!"
    elif au_greeting_2:
        $ au_greeting_2 = False
        #voice "aug-02"
        au "Why hello, my friend."
    elif au_greeting_3:
        $ au_greeting_3 = False
        #voice "aug-03"
        au "Would you like some tea?"
    elif au_greeting_4:
        $ au_greeting_4 = False
        #voice "aug-04"
        au "Oh, I didn't notice you standing there."
    else:
        $ au_greeting_1 = True
        $ au_greeting_2 = True
        $ au_greeting_3 = True
        $ au_greeting_4 = True
        #voice "aug-05"
        au "Would you like to dance for a bit?"

    if auresQuestState == 7:
        if killPath:
            jump auresScene7K
        else:
            jump auresScene7NK

label aures_convohub:

    show aures neutral
    menu:
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 2:
            jump auresScene2
        "\"So, about this boy you spoke about: Minoru?\"" if auresQuestState is 3:
            jump auresScene3
        "\"Is there something I can do for you, Aures?\"" if auresQuestState is 4:
            jump auresScene4
        "\"Remind me, what did you need of me?\"" if auresQuestState is 5 and not hasTeleporter:
            au "I needed a teleporter device, if you can find one."
            au "Go see Lysander, he's out in the garden."
            jump aures_convohub
        "\"How are things with Minoru, Aures?\"" if auresQuestState is 6:
            if killPath:
                jump auresScene6K
            else:
                jump auresScene6NK
        "\"Is our new ghost doing OK, Aures?\"" if auresQuestState is 8:
            jump auresScene8
        "Hand Aures the teleporter." if auresQuestState is 5 and hasTeleporter:
            jump auresScene5

        "\"About Elizabeth...\"" if elizabeth_queststate is 2:
            jump aures_elizabeth

        "\"Aures, I could use your help with a map.\"" if elizabeth_queststate is 4 and q5_location is 1:
            jump aures_elizabeth2

        "\"Would you happen to have some bourbon for Herman in here?\"" if herman_queststate is 1:
            au "I bet he wants his fancy glasses, too."
            "Aures visibly scowls."
            au "Herman. I hate that man. Just take them. They are over in that cabinet."
            "Sure enough, in the far cabinet is a large bottle and a pristine crystal glass."
            "You take both from the cabinet, taking great care not to drop or damage them."
            $ herman_queststate = 2
            jump aures_convohub

        "Check the ballroom for information on Arabella." if q3_state is 1 and not q3_priest_journal and not q3_keyneeded:
            jump arabella_priestjournal

        "Open the lockbox with the key you found in the living room." if q3_state is 1 and not q3_priest_journal and q3_keyneeded and q3_mom_journal:
            jump arabella_priestjournal_open


        "\"I want to ask to you about something.\"":
            jump aures_convohub_questions
            #put conversation options here

        "\"See you later, Aures.\"":

            # a goodbye line
            if selfish >= 15 and au_farewell_selfish:
                $ au_farewell_selfish = False
                #voice "auf-04"
                au "Oh, you're leaving me? I see. This will not be forgotten."
            elif au_farewell_1:
                $ au_farewell_1 = False
                #voice "auf-01"
                au "Are you leaving? Would you like a cup of tea for the road?"
            elif au_farewell_2:
                $ au_farewell_2 = False
                #voice "auf-02"
                au "How about one final waltz before you go?"
            elif au_farewell_3:
                $ au_farewell_3 = False
                #voice "auf-03"
                au "Farewell. I hope our paths will cross again soon."
            elif au_farewell_4:
                $ au_farewell_4 = False
                #voice "auf-05"
                au "I'll have some tea ready for you next time you arrive."
            else:
                $ au_farewell_1 = True
                $ au_farewell_2 = True
                $ au_farewell_3 = True
                $ au_farewell_4 = True
                #voice "auf-06"
                au "Do you have time for one more dance before you go?"
            scene black
            call screen minimap()

label aures_convohub_questions:
    menu:
        au "What would you like to talk about?"
        "\"What do you think of Herman?\"":
            #voice "auht-01"
            au "That man is horrifying. I feel pain whenever I see him, all over my body. I try to avoid him whenever possible."
            #voice "auht-02"
            au "I can't think of why, though. Every time I try to figure out the reason he scares me so, I get a terrible headache, then wake up on the ground."
            jump aures_convohub_questions

        "\"What do you think of Arabella?\"":
            if auresQuestState < 7:
                #voice "auht-03"
                au "I think she is wonderful! I love her dresses, they all look so beautiful. I always try talking to her when I pass by the foyer."
            else:
                #voice "au_mad2"
                au "Why would you even mention the name of that man-stealing wench in front of me?!"
            jump aures_convohub_questions


        "\"Why do you always wear those dresses and drink tea?\"":
            #voice "auht-05"
            au "I aspire to be the pinnacle of elegance and grace. Hence, I must wear these gowns."
            #voice "auht-06"
            au "Tea is also very healthy for you; not that that matters now. But I still enjoy the scent and taste of it, so I try to have at least four cups a day."
            jump aures_convohub_questions

        "\"Something else, please.\"":
            jump aures_convohub

label aures_elizabeth:

    $ elizabeth_queststate = 3
    $ q5_location = 1

    #voice ""
    mc "I’m not here to dance. I’m looking for some stuff."
    #voice ""
    au "Ugh, a ballroom is a place for dancing and party, not for a boring activity such as... writing."
    #voice ""
    mc "That’s what I told her, but she told me to come here."
    #voice ""
    menu:
        au "Who?"
        "\"It’s for Elizabeth.\"":
            #voice ""
            mc "You know, a little girl with short hair, running around all drenched?"
            "Aures gasps."
            #voice ""
            au "Did you see her? Is she okay?"
            #voice ""
            au "You didn’t do anything to her did you?!"
            #voice ""
            mc "Calm down! She is okay, she asked me to find a pen and paper, and she sent me here because she said you might help."
            #voice ""
            au "Oh..."
            #voice ""
            au "Thank goodness if she is alright, at least..."
            #voice ""
            mc "Do you know her?"
            #voice ""
            au "Poor kid arrived here all confused, everything seems to terrify her—it doesn’t help that half of the residents here are all dressed or talk weirdly."
            #voice ""
            au "She thought I was a princess when she saw me. What a sweet kid, don’t you agree?"
            #voice ""
            au "She told me she needs to go home because she just made a big, BIG mistake, and ran away from home."
            #voice ""
            au "THEN, she suddenly felt scared and ran away from me. I was never able to find her again after that."
            #voice ""
            au "Tell me, is she okay?"
            #voice ""
            mc "She almost hit me with a book."
            #voice ""
            au "She is okay then."
            "Aures laughs."
            #voice ""
        "\"It’s for someone you know, but I can’t say who.\"":
            #voice ""
            au "Do I know her?"
            #voice ""
            mc "She said so."
            #voice ""
            au "Is she big or small?"
            #voice ""
            mc "Uh..."
            "You gestured at about your chest height."
            #voice ""
            au "OH!"
            "Aures seems to realize what you mean, but immediately closed her mouth."
            #voice ""
            au "Is she okay?"
            #voice ""
            mc "She almost hit me with a book."
            #voice ""
            au "She is okay then."
            "Aures laughs."
            #voice ""
            au "The last time I saw her, she told me she just made a big mistake and ran away from home."
            #voice ""
            au "But then she ran away from me. I have never been able to find her since."
            #voice ""
        "\"Just someone.\"":
            #voice ""
            au "Do I know her?"
            #voice ""
            mc "No."
            #voice ""
            au "Well then I’m not helping."
            #voice ""
            mc " Ugh. She’s someone that’s stuck in this mansion"
            "Aures seem to be thinking."
            #voice ""
            au "Did she... say anything about me?"
            #voice ""
            mc "She told me you’re a kind big sister."
            #voice ""
            au "OH IT’S HER!"
            #voice ""
            au "Sorry, got a bit too excited there."
            #voice ""
            au "Oh I’m glad she’s still around. Or wait, should I be worried instead?"
            #voice ""
            mc "You know anything about her?"
            #voice ""
            au "The last time I saw her, she told me she just made a big mistake and ran away from home."
            #voice ""
            au "But then she ran away from me. I have never been able to find her since."
    #voice ""
    au "If it’s a pen and paper, there’s some in that drawer over there."
    #voice ""
    au "Don’t take too much, I need them too."
    #voice ""
    mc "You said this place isn’t suitable for writing."
    #voice ""
    au "WELL, I might change my mind."
    "You walk to the drawer. Aures points and you take a piece of paper and a pen."
    #voice ""
    mc "Thank you for this."
    #voice ""
    au "If she is okay with it, can you come back and tell me what’s going on with her?"
    #voice ""
    mc "I will ask her later. Thank you for the paper."
    jump aures_convohub


label aures_elizabeth2:

    $ elizabeth_queststate = 5

    au "Why have you come to me?"
    mc "Can you tell me where this is?"
    "You show Aures the map you’ve drawn."
    au "Is this a map?"
    au "Wait. Ice skating lake—does this belong to Elizabeth?! Did she send you here?"
    mc "Yes, I’d like to ask you something."
    au "What is it? Did she have something to say to me?"
    mc "Can you tell me everything you know about her?"
    au "Eh? Um..."
    mc "What? She said you are close to her, she trusts you."
    au "Well, it’s not like I know much about her. We just happened to meet and she tells me—"
    mc "It’s too late for that, tell me what you know. Please, I want to help her as much as you do."
    "Aures looks conflicted. She looks down to the floor, glances at you, and finally sighs."
    au "This is for her, okay? I didn’t do this for you."
    au "She was running from room to room, terrified as if being chased by something. Then, she ends up coming to this very place."
    au "Fortunately, this appearance of mine was a solace for her, for she admired it."
    au "After she settled, she told me that she woke up on the river behind the mansion, and wandered in."
    au "She apparently promised her parents to go to a skating place, she used a shortcut, and all of a sudden she appeared here. Curious tale, yes?"
    au "But then, I also found those."
    "Aures nods at a couple of newspaper clippings on a nearby table."
    "On the first paper you see, is a clear picture of Elizabeth, with slightly longer hair, more lively expressions, and less water dripping from her entire being."
    "Under the picture, a sentence ‘HAVE YOU SEEN ME?’, printed large on the paper."
    "You take out the second paper. On it, in the middle of crowding police, a picture of a woman in her thirites is seen holding a children's jacket."
    "She was entirely disheveled with dried tears and dark circles under her eyes."
    "—Was last seen going out of the house at 4 p.m., walking towards the bridge."
    "It is reported that there was a slight argument between her and the mother before the time she was last seen. Police are currently investigating—"
    "The third paper, there was no picture this time, only a big headline ‘SEARCH CALLED OFF’."
    "—Being discontinued. The reason is insufficient leads or clues regarding the whereabouts of the missing person."
    "\"I hope you’re happy and safe, I love you so much, and I’m sorry I can’t be a better mother for you,\" The mother of the little girl told our editor."
    "A small message we all hope Elizabeth will read. The family has decided to move away from their residence but will keep close contact with the police."
    "The police will still receive any information regarding the missing Elizabeth—"
    "You read them all carefully. Every gear in your head turns as you process all the broken messages into one string of story."
    menu:
        au "What do you think?"
        "\"She fell into a river after running away.\"":
            au "Yes, I was thinking the same thing."
        "\"Her mother killed her and ran away.\"":
            au "Oh? Are you sure?!"
            "Aures snatches the newspapers from you and starts reading quickly."
            au "That’s not it at all! She just ran away from home and came here!"
        "\"She got lost and ended up here.\"":
            au "Yes, yes. That makes sense."
            mc "I’m kidding. She ran away from home after an argument, and some accidents led her here."
            au "You—"
    au "Well, still, it’s a very unfortunate story for her. She was so terrified of everything when she came here."
    mc "Any kid who ran away from home and got lost forever will certainly be traumatized."
    au "Then, do you really tell all of that to her? She’s a little girl!"
    menu:
        "\"I will tell her the truth.\"":
            "Aures gasps."
            au "You’re going to make her cry."
            mc "I know. But the longer we keep her in the dark, the more anxious she will be."
        "\"I can’t show her this, it’s too much for her.\"":
            au "Then, what are you going to tell her?"
            mc "Anything that’s not all of this, of course."
            au "She still wants to go home though. She will feel betrayed."
            mc "I will think of something."
        "\"Maybe it’s better for her to stay here.\"":
            au "But is still going to miss her mother, her family though.This is hard..."
            au "Ah, can’t you just bring her family here?"
            mc "That’s not happening. I can’t deal with more of you."
    au "Well, whatever. It’s up to you now, but are you sure she is going to be okay with it?"
    au "Oh no, she will be mad, no—she will be so upset!"
    menu:
        "\"She deserves the truth.\"":
            mc "This is for her own good."
            au "That’s true, but—"
            "Aures seems to be thinking of an excuse, but fails. She sighs."
        "\"I won’t tell her, it’s too cruel.\"":
            au "Of course! I mean... that’s a clever choice. I know I can’t bring myself to tell that to her..."
        "\"...I have to think this through some more.\"":
            au "Oh, yes, that’s a good plan. Honestly, I don’t know what to do about her."
    "Holding the newspaper clippings in your hand, you sigh deeply, thinking of the choice you’re about to make."
    "You shove the papers into your pocket and walk away."
    mc "I’ll go back to her for now."
    "Aures nods."
    au "Just... talk to her slowly, okay? She’s been through a lot."
    jump aures_convohub

    # however mint wants this to go
