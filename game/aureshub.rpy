

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

    show aures neutral
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
                au_farewell_selfish = False
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
    jump aures_convohub

    # HOWEVER MINT WANTS THIS TO GO

label aures_elizabethtwo:

    $ elizabeth_queststate = 5
    jump aures_convohub

    # however mint wants this to go
