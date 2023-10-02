label marianne_hub:

    default ma_greeting_1 = True
    default ma_greeting_2 = True
    default ma_greeting_3 = True
    default ma_greeting_4 = True

    default ma_farewell_1 = True
    default ma_farewell_2 = True
    default ma_farewell_3 = True
    default ma_farewell_4 = True

    show marianne smile at marianne_spot
    with dissolve

    # custom greeting

    if ma_greeting_1:
        $ ma_greeting_1 = False
        #voice "mag-01"
        ma "How ya faring, hon?"
    elif ma_greeting_2:
        $ ma_greeting_2 = False
        #voice "mag-02"
        ma "Welcome back, darlin'."
    elif ma_greeting_3 and not marianne_questdone:
        $ ma_greeting_3 = False
        #voice "mag-03"
        ma "What can Marianne do for you, huh?"
    elif ma_greeting_4:
        $ ma_greeting_4 = False
        #voice "mag-04"
        ma "Why, hello-there-howdy!"
    else:
        $ ma_greeting_1 = True
        $ ma_greeting_2 = True
        $ ma_greeting_3 = True
        $ ma_greeting_4 = True
        #voice "mag-05"
        ma "Looking fresh, zombiepie!"

label marianne_convohub:

    menu:
        "\"Is there something I can do for you, [marianne_name]?\"" if marianne_queststate is 1:
            jump marianne_startquest
            # this is the topic that jumps to

        "\"I have the camcorder you were asking for.\"" if marianne_queststate is 3:
            jump marianne_gotcamcorder

        "Check the bedroom for something dated to show Herman." if herman_queststate is 10 and not herman_newspaper:
            jump herman_bedroom

        "\"I have questions about you.\"":
            jump marianne_herself



        "Search the nearby desk for clues on Arabella's past." if q3_state is 1 and not q3_own_journal:
            # hey can i get marianne to fade away here?
            jump marianne_arabella

        "Search the nightstand for clues on Arabella's past." if q3_state is 1 and not q3_pendant_encounter:
            $ q3_pendant_encounter = True
            # hey can i get marianne to fade away here?
            jump marianne_arabella_pendant

        "\"See you later, [marianne_name].\"":

            if marianne_queststate is 2:
                jump marianne_abouttoleave
            if marianne_questjustfinished:
                jump marianne_reflection

            # a goodbye line

            if ma_farewell_1:
                $ ma_farewell_1 = False
                #voice "maf-01"
                ma "Come on back around sometime soon, alright?"
            elif ma_farewell_2:
                $ ma_farewell_2 = False
                #voice "maf-02"
                ma "I'll be counting petals till you're back, don't keep me waiting!"
            elif ma_farewell_3:
                $ ma_farewell_3 = False
                #voice "maf-03"
                ma "Oh, go on, then. Take the time it takes, I'll be right here."
            elif ma_farewell_4:
                $ ma_farewell_4 = False
                #voice "maf-04"
                ma "Ta-ta for now!"
            else:
                $ ma_farewell_1 = True
                $ ma_farewell_2 = True
                $ ma_farewell_3 = True
                $ ma_farewell_4 = True
                #voice "maf-05"
                ma "Keep it peachy, sugar."

            call screen minimap()

label marianne_herself:
    menu:
        "\"What do you know about this mansion?\"":
            voice "mar-ht01"
            ma "Why, next to nothing, sorry."
            #voice
            ma "I know it’s old, it’s full of ghosts like me —"
            #voice
            ma "— and I hear a few too many bloodcurdling noises to ever get a real good night’s sleep."
            #voice mar-ht02
            ma "Still, I’ve settled into quite the comfy nook here. It suits me just fine."
            #voice
            ma "Livin’ my best life, as far as the undead go."
            #voice
            ma "And besides that, it ain’t really my business to pry."
            jump marianne_herself

        "\"What do you think of the other ghosts?\"":
            #voice mar-ht03
            ma "I try not to tangle with too many of the others, but they’re kindly enough."
            #voice mar-ht04
            ma "Arabella, Elizabeth, Lysander… all real sweet, a real sweet bunch."
            #voice
            ma "Aures might have more glitz and glamor than me, color me a little bit jealous."
            #voice
            ma "And, well, Herman is… from a different time. You know how it is."
            jump marianne_herself

        "\"How did you die?\"":
            #voice mar-ht05
            ma "No beating around the bush with you, huh?"
            #voice mar-ht06
            ma "Well, your brazen britches ain’t doing you any good this time."
            #voice mar-ht07
            ma "Mostly because I don’t entirely know what happened to me."
            #voice
            ma "I remember climbing down into the basement for some liquor."
            #voice
            ma "And that’s that. All sortsa things coulda happened to me."
            #voice
            ma "But, six of one, half a dozen the other."
            #voice
            ma "Dead is dead, and I ain’t even complaining."
            jump marianne_herself
        "\"That's all for now, [marianne_name].\"":
            jump marianne_convohub


label marianne_arabella:
    "You pick up one of the books from the desk."
    menu:
        "Upon further inspection, you see that it’s a carefully hand-bound journal."

        "Read the journal.":
            $ q3_own_journal = True
            jump arabella_journalentries

        "Don't read the journal.":
            $ q3_own_journal = True
            "You decide not to read the journal, feeling it to be a major invasion of privacy."
            "You put the journal back on the desk, deciding not to bring the journal with you, though the information from it seems to shed some new light on a few things."
            jump marianne_convohub

label marianne_arabella_pendant:

    "Your attention is drawn towards the walnut nightstand."
    "The closed drawer beneath beckons silently."
    "The brass handle feels cool to the touch as you open the drawer."
    "Nestled inside, amidst a few parchment letters and dried lavender sprigs, lay a radiant pendant."
    "It’s a moonstone, set within an intricate silver setting, its delicate glow seemingly emanating its own soft luminescence."
    "The stone seems to capture the very essence of moonlight, its translucent surface dancing with milky blues and silvers, reflecting a mesmerizing play of colors."

    menu:
        "Take the pendant.":
            $ q3_pendant_keep = True
            "You decide to take the pendant. The energy radiating from it feels too important not to take."

        "Leave the pendant alone.":
            $ q3_pendant_keep = False
            "You put the pendant back on the nightstand. The energy radiating from it feels too important to take."

    jump marianne_convohub
