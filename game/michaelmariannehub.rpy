label marianne_hub:

    # custom greeting

label marianne_convohub:

    menu:
        "\"Is there something I can do for you, [marianne_name]?\"" if marianne_queststate is 1:
            jump marianne_startquest
            # this is the topic that jumps to

        "\"I have the camcorder you were asking for.\"" if marianne_queststate is 3:
            jump marianne_gotcamcorder

        #"Look around the room for information about Arabella.":
        #    jump WHEREEVER MAYA SAYS THIS CONTENT IS

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

        "\"See you later, [marianne_name].\"":

            if marianne_queststate is 2:
                jump marianne_abouttoleave
            if marianne_questjustfinished:
                jump marianne_reflection

            # a goodbye line

            call screen minimap()
