label lysander_hub:

    # custom greeting if not and not lysander_ded
    if lysander_ded:
        "Lysander is no longer in the garden."

label lysander_convohub:

    # show lysander neutral if not lysander_ded #does this syntax even work?

    menu:

        "\"OK, I'm ready to make our decision.\"" if lysander_queststate is 6:
            jump lysander_bigdecision

        "\"I read some peculiar books in the lounge...\"" if lysander_queststate is 3:
            jump lysander_readsome

        "\"I found this green book in the lounge...\"" if lysander_queststate is 4:
            jump lysander_gottome

        "\"Tell me about yourself.\"" if not lysander_ded:
            #voice lyq1-12
            show lysander neutral
            ly "Certainly. What would you like to know?"
            jump lysander_convohub_myself

        "Check the garden for something dated to show Herman." if herman_queststate is 10 and not herman_date:
            jump herman_garden

        "\"What did you want me to do, again?\"" if lysander_queststate is 2 or lysander_queststate is 3 or lysander_queststate is 4:
            #voice ly_hap1
            show lysander neutral
            ly "Ideally, I'd like you to track down some documentation regarding the bindings keeping me tethered to this mansion."
            #voice ly_puz2
            show lysander neutral
            ly "I've scoured most bookshelves, nooks, and crannies throughout these halls, but there is one store of books I've never been able to access."
            #voice ly_mad1
            show lysander thinking
            ly "I know it's somewhere on the western side of the mansion, but it's like the place is…repelling me, somehow."
            jump lysander_convohub

        "\"What did you want me to do, again?\"" if lysander_queststate > 5 and not lysander_questdone:
            #voice ly_hap5
            show lysander neutral
            ly "Based on the literature you found, it seems as though we have a few options for how to proceed. Should we figure out what we'd like to do now, or would you prefer to wait a while longer?"
            "I'm ready; let's figure this out."
            #voice ly_hap4
            show lysander grateful
            ly "Absolutely."
            "I'd like a little more time."
            #voice ly_hap1
            show lysander neutral
            ly "Take however long you need—you know where to find me."
            #REVISIT THIS IN A HOT SEC

        "\"What led up to your death?\"" if lysander_queststate > 5 and not lysander_ded:
            jump lysander_convohub_truedeath

        "\"You said something about losing yourself…\"" if lysander_queststate > 5 and not lysander_ded:
            jump lysander_convo_hub_losing

        "\"Tell me about the garden.\"" if not lysander_ded:
            #voice lyht-01
            ly "There’s something wonderful about watching the peonies return every year. It’s a reminder that dormancy doesn't mean death, and that death doesn't mean departure."
            #voice lyht-02
            ly "Did you know that black dahlias aren’t actually black? In reality, they’re just an extremely dark red."
            #voice lyht-03
            ly "…there was once a visitor to this garden amazed by their vibrancy, only to be tragically disappointed when they saw a petal up close."
            #voice lyht-04
            ly "White hydrangeas were always my sister’s favorite, but I prefer those with pink or blue hues. "
            #voice lyht-05
            ly "While the white is predictable, the ability of the pink or blue flower to shift its coloration in response to its environment is admirable. "
            #voice lyht-06
            ly "Given my current state, I must say I’m a bit jealous."
            #voice lyht-07
            ly "I got very into hybridizing roses for a couple of decades. I stopped not because I grew tired of the practice, but because I liked it a little too much."
            #voice lyht-08
            ly "…I may have lost some other denizens of the garden due to my misplaced focus."
            jump lysander_convohub

        "\"Tell me about the mansion…\"" if not lysander_ded:
            #voice lyht-24
            ly "There are strange sounds that occasionally drift from somewhere in the depths of this manor. While I haven’t been able to identify their precise source…"
            "He stops momentarily, shuddering."
            #voice lyht-25
            ly "I honestly haven’t tried to."
            #voice lyht-26
            ly "While I wasn’t a particularly skilled dancer in life, I can’t deny the beauty of the ballroom here. It might be a little ostentatious, but I suppose that spectacularity does have its appeal."
            #voice lyht-27
            ly "If you haven’t already, you should take a look at the garden from the second floor. I’ve never tried to make it particularly elegant when viewed from above, but the combination of colors is still pleasant."
            #voice lyht-28
            ly "If a lounge is meant for relaxation… Why do I feel such a sense of unease when I pass by its entrance?"
            jump lysander_convohub


        "\"Tell me about the other ghosts.\"" if not lysander_ded and marianne_queststate + elizabeth_queststate + herman_queststate + q3_state + aures_queststate > 0:
            jump lysander_convohub_ghosts

        "\"I should be going.\"":

            if lysander_queststate is 1:
                jump lysander_abouttoleave

            if lysander_queststate is 5:
                jump lysander_quest2intro

            # a goodbye message (if lysander_angy = True then make it the angy goodbye, if lysander_ded do not play a greeting)
            call screen minimap()


label lysander_convohub_myself:

    menu:

        "\"How did you die?\"" if lysander_queststate < 6:
            #voice lyq1-13
            show lysander neutral
            ly "In short: the aftermath of a duel. I was victorious, but the wound my opponent managed to inflict eventually made me very ill."
            #voice lyq1-14
            show lysander neutral
            ly "The festering of it was what actually killed me."
            jump lysander_convohub_myself

        "\"Why did you get into gardening?\"":
            #voice lyq1-15
            show lysander grateful
            ly "I never had much interest in it during my time alive. I suppose I developed the hobby out of necessity."
            #voice lyq1-16
            show lysander neutral
            ly "After I died, I remained my sister’s guardian, but… Well…"
            #voice lyq1-17
            show lysander neutral
            ly "You may have noticed that, although ghosts cannot be touched, we can physically interface with the world around us. "
            #voice lyq1-18
            show lysander disappointed
            ly "This ended up presenting problems."
            #voice lyq1-19
            show lysander disappointed
            ly "My sister would become immensely distressed when things around her would move—even if I was simply trying to dust a shelf or return a misplaced item to its proper home."
            #voice lyq1-20
            show lysander unique
            ly "My presence seemed to heighten her paranoia, which in turn drove her further and further into religious literature and a hatred for all things metaphysical."
            #voice lyq1-21
            show lysander neutral
            ly "I eventually decided it was in her best interest if I kept a slightly further distance, so I began spending most of my day out here."
            #voice lyq1-22
            show lysander grateful
            ly "Gardening proved to be the most enjoyable way I could pass the time."
            jump lysander_convohub_myself

        "\"How long have you been here?\"":
            #voice lyq1-23
            show lysander grateful
            ly "Keeping track of the years grows increasingly difficult as they pass. I used to track my death date yearly, then every other year, then every five…"
            #voice lyq1-24
            show lysander grateful
            ly "I kept extending the duration, so now I simply mark the passage of time in quarter-centuries."
            #voice lyq1-25
            show lysander unique
            ly "Next time I do so, it will have been two hundred years…"
            jump lysander_convohub_myself

        "\"I have a question about something else.\"":
            jump lysander_convohub


label lysander_convohub_ghosts:

    menu:

        "\"About Herman…\"" if herman_queststate > 0:
            #voice lyht-09
            ly "He’s an amicable enough fellow, at least on the surface. His time in the mansion was accompanied by…well, I’m not exactly sure what."
            #voice lyht-10
            ly "I would caution you that Mr. Grover may not be all that he seems."
            jump lysander_convohub_ghosts
        "\"About Arabella…\"" if q3_state > 0:
            #voice lyht-11
            ly "Ah. I didn’t have much of a chance to watch her grow up before my duel, and afterward—well, I thought it was safest for her and Evangeline if I kept what distance I could."
            #voice lyht-12
            ly "That’s an explanation, not an excuse."
            "Lysander sighs with the weariness of someone far older than his appearance would suggest."
            #voice lyht-13
            ly "…I’m sorry. It isn’t your fault for asking."
            #voice lyht-14
            ly "I didn’t know the full extent of what she endured, but I realize now that my decision to remain afar was a terrible, terrible mistake."
            #voice lyht-15
            ly "I’d like to mend that wound as best I can, but I leave the impetus to her. People have forced her to comply with their wishes far too much already."
            jump lysander_convohub_ghosts
        "\"About Elizabeth…\"" if elizabeth_queststate > 0:
            #voice lyht-16
            ly "Elizabeth? …Oh! The little girl trapped in perpetual cold."
            #voice lyht-17
            ly "She’s a newer denizen of these haunted halls, but her tendency to flee from adults means that I, unfortunately, don’t know much about her."
            #voice lyht-18
            ly "Perhaps you might have better luck striking up a conversation."
            jump lysander_convohub_ghosts
        "\"About Marianne…\"" if marianne_queststate > 0:
            #voice lyht-19
            ly "She’s something of an enigma. While her appearance implies that her death date should fall relatively close to Herman’s, her conduct is slightly unusual. "
            #voice lyht-20
            ly "Though I confess my understanding of that time’s decorum is fairly limited."
            #voice lyht-21
            ly "She occasionally comes to walk the garden paths at sunset. The light reflects beautifully on her dress."
            jump lysander_convohub_ghosts
        "\"About Aures…\"":
            #voice lyht-22
            ly "I’ve… never been particularly comfortable around landed gentry. I would describe our interactions as ‘tolerable’ rather than something I actively seek out."
            #voice lyht-23
            ly "How much of her intensity is innate, rather than a product of her environment? I couldn’t say."
            jump lysander_convohub_ghosts
        "\"I have a question about something else.\"":
            jump lysander_convohub

label lysander_convohub_truedeath:

    #voice ly_dis3
    show lysander disappointed
    ly "I wish it were a more cheerful story. My sister was… Attacked. The man's name was Henry."
    #voice ly_sad3
    show lysander disappointed
    ly "They'd grown up together, Henry and Evangeline — and, by most accounts, he was a respectable man from a respectable family."
    #voice ly_puz2
    show lysander disappointed
    ly "She didn't come home at sundown that day, so I went out looking for her."
    #voice ly_sad4
    show lysander unique
    ly "I found her. I…was the only other person to see what he did."
    #voice ly_mad2
    show lysander distraught2
    ly "I don't think I've ever been as angry as I was in that moment. My soul screamed for justice, for some way to grant her reprieve—but there was none."
    #voice ly_sad3
    show lysander distraught2
    ly "I helped her recover as best she could before we went home. She never told our family the full extent of it; I'm not sure what would've happened if she had."
    #voice ly_mad1
    show lysander distraught2
    ly "But I understood what I needed to do, so I went looking for Henry."
    #voice ly_dis4
    show lysander distraught2
    ly "We decided to call it a duel of jealousy, rather than defense. "
    #voice ly_mad5
    show lysander disappointed
    ly "Henry knew that the truth of what he'd done would've easily destroyed his reputation. "
    #voice ly_sad5
    show lysander disappointed
    menu:
        ly "And, in the event things hadn't gone my way, I didn't want to torment Evangeline with knowing how she led to my death."

        "\"You respected his wishes?\"":
            #voice ly_sad4
            show lysander thinking
            ly "I did. I hated him more than any other person on this Earth, but I knew he wouldn't have agreed to the duel without my vow of silence."
            #voice ly_puz2
            show lysander thinking
            ly "Holding the truth in confidence was my only gift to him, and only then to save my sister the pain of seeing that history laid bare."
        "\"You should've exposed what he did, regardless of what he wanted.\"":
            #voice ly_sad4
            show lysander distraught2
            ly "Mm. Perhaps. But, before you call me a coward, I know revealing that history would have caused my sister immense pain."
            #voice ly_puz2
            show lysander disappointed
            ly "I doubt such a disclosure would've triggered any real recourse at the time. Still, even if it had… my priorities lay firmly on keeping Evangeline from harm. I suspect my silence was all but guaranteed."
        "\"But you won! Why didn't you just tell people afterward?\"":
            #voice ly_mad1
            show lysander grateful
            ly "I suppose I hold my sense of honor a little too dear. I couldn't go back on my word; and, besides, the deed was done."
            #voice ly_sad5
            show lysander distraught2
            ly "In any event, although I'd been victorious in our duel, I hadn't escaped entirely unscathed. My wound was small and non-vital, nothing to trouble a doctor over…until it festered."
            #voice ly_dis4
            show lysander unique
            ly "I waited too long, and I paid for it with my life."

    jump lysander_convohub

label lysander_convo_hub_losing:

    #voice lyq1-42
    show lysander grateful
    ly "I suppose I did. It’s funny—I’ve been here for so long that, in some ways, this state is more comforting to me than being alive."
    #voice lyq1-43
    show lysander neutral
    ly "I’d like to see my family again; I’d like to make things right, to say things I never had the chance to say. I can’t do that if I remain here, but…"
    "Lysander shakes his head, laughing more openly than you’ve seen at any other point in your conversations."
    #voice lyq1-44
    show lysander grateful
    ly "It’s ridiculous to even say aloud. …I’m afraid that I won’t retain my memories, my sense of self, if I let go."
    #voice lyq1-45
    show lysander thinking
    ly "After all, when Evangeline… When it was her time to go… She simply departed. I was left behind."
    #voice lyq1-46
    show lysander unique
    menu:
        ly "Surely, that’s proof enough that she was no longer herself."

        "\"You don’t know that.\"":
            #voice lyq1-47
            show lysander distraught
            ly "No. I know she lost herself when her essence departed; that’s the only way that… She would never…"
            #voice lyq1-48
            show lysander disappointed
            ly "She wouldn’t have left without taking me with her."
            jump lysander_convohub

        "\"Maybe she didn’t want to take you with her.\"":
            $ lysander_angy = True
            "You see Lysander’s jaw tighten, a flash of some as-yet-unseen darkness momentarily crossing his face."
            "Although his expression relaxes, you can sense a certain level of tension in his incorporeal body."
            #voice lyq1-49
            show lysander thinking
            ly "I would consider your next few comments very carefully were I in…your position."
            #voice lyq1-50
            show lysander unique
            ly "Perhaps Evangeline had not been aware of my existence in this state, even after entering it herself; perhaps she was simply pulled away too quickly to draw me to her side."
            #voice lyq1-51
            show lysander thinking
            ly "There could be far more at play than simple betrayal."
            "Lysander looks down and clears his throat."
            #voice lyq1-52
            show lysander disappointed
            ly "I’m sorry. Truly. That was too harsh of me… I’m sure you meant no real offense."
            jump lysander_convohub

        "\"You would really rather stay here?\"":
            #voice lyq1-53
            show lysander neutral
            ly "Faced with the alternative of losing oneself to oblivion…would you not at least consider the same?"
            jump lysander_convohub_losing_rather




label lysander_convohub_losing_rather:

    #voice lyq1-54
    show lysander disappointed
    menu:
        ly "This existence is a lonely, cruel affront to nature, but through it, I could at least bring others the safety they deserved."

        "\"But what about yourself? There’s no guarantee that you’ll lose what makes you who you are.\"":
            #voice lyq1-55
            show lysander disappointed
            ly "Who I am… Who am I if not a guardian?"
            "Lysander places a hand upon his fatal wound."
            #voice lyq1-56
            show lysander unique
            ly "Who was I, truly, before all this? Do I even recall?"
            #voice lyq1-57
            show lysander unique
            ly "Is there truly any part of me left to lose?"
            jump lysander_convohub
        "\"You deserve to do what you feel is best, not what you feel obligated to do.\"":
            "Lysander is caught entirely off-guard by the statement."
            #voice lyq1-58
            show lysander distraught2
            ly "I…"
            #voice lyq1-59
            show lysander unique
            ly "A-Apologies. I have conditioned myself to be accustomed to…a certain level of duty."
            #voice lyq1-60
            show lysander thinking
            ly "The idea of acting beyond those bounds for my own benefit is certainly something to consider."
            jump lysander_convohub
        "\"You let that poor girl be tortured!\"": # needs to be conditioned on soemthing hi maya
            $ lysander_angy = True
            #voice lyq1-61
            show lysander distraught
            ly "That wasn't my FAULT!"
            #voice lyq1-62
            show lysander distraught
            ly "Ask yourself what you would have done. Whenever I stayed by her side, Evangeline suffered. When Evangeline suffered, so did Arabella. "
            jump lysander_convohub_losing_rather_arabella

label lysander_convohub_losing_rather_arabella:

    #voice lyq1-63
    show lysander distraught
    menu:
        ly "What was I supposed to do?"

        "\"You could've stopped Evangeline.\"":
            "The fire in Lysander's eyes is replaced with an equally harsh steeliness. The tension throughout his body is palpable."
            #voice lyq1-64
            show lysander thinking
            ly "And how would you suggest I accomplish such a task? In this form, in the absence of verbal communication…"
            #voice lyq1-65
            show lysander thinking
            ly "Would you suggest I grab her? Strike her? Turn a weapon against her?"
            #voice lyq1-66
            show lysander distraught2
            ly "I surrendered and perpetuated my existence so that she might be safe. "
            #voice lyq1-67
            show lysander distraught2
            ly "My later decisions did not treat Arabella as sacrificial; they ensured that Evangeline was not driven to harm her due to the agony my accursed presence caused."
        "\"You could have taken Arabella.\"":
            #voice lyq1-68
            show lysander distraught
            ly "And done what with her, exactly? My bindings are tied to her mother."
            #voice lyq1-69
            show lysander distraught
            ly "Even if she were to somehow converse with me and agree to depart, where would we have gone?"
        "\"...\"":
            pass

    #voice lyq1-70
    show lysander disappointed
    ly "I know how my choices appear. I have torn myself asunder again and again because of how I failed that child."
    #voice lyq1-71
    show lysander disappointed
    ly "...I just didn't see how dire things had become. I didn't see another way."
    jump lysander_convohub
