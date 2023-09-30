label marianne_hub:

    # custom greeting

label marianne_convohub:

    menu:
        "\"Is there something I can do for you, [marianne_name]?\"" if marianne_queststate is 1:
            jump marianne_startquest
            # this is the topic that jumps to

        "\"I have the camcorder you were asking for.\"" if marianne_queststate is 3:
            jump marianne_gotcamcorder

        "\"What do you know about this mansion?\"":
            #voice mar-ht01
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
            jump marianne_convohub

        "\"What do you think of the other ghosts?\"":
            #voice mar-ht03
            ma "I try not to tangle with too many of the others, but they’re kindly enough."
            #voice mar-ht04
            ma "Arabella, Elizabeth, Lysander… all real sweet, a real sweet bunch."
            #voice
            ma "Aures might have more glitz and glamor than me, color me a little bit jealous."
            #voice
            ma "And, well, Herman is… from a different time. You know how it is."
            jump marianne_convohub

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
            jump marianne_convohub

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

            call screen minimap()

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
