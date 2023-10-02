label lysander_garden:

    scene bg garden
    with fade

    #show whatever bg i don't remember the syntax

    if lysander_queststate > 0:
        jump lysander_hub

    if lysander_queststate is 0:
        jump lysander_intro


label lysander_intro:
    $ lysander_queststate = 1
    "You push open a grand set of double doors at the back of the mansion’s living room and find yourself at the start of a weathered yet surprisingly well-maintained stone path."
    "Stepping out, you feel a light breeze brush against your skin—a comforting and somehow nostalgic feeling."
    "Walking along the cobblestones, you hear nothing but the sound of your footfalls and the occasional rustling of wind in the trees around you."
    "To your surprise, you find that the path leads to the entrance of a lush garden. At its entry point is an arbor adorned with a plethora of vibrant and well-tended flowers. "
    "As you take in the sights around you, you realize that, despite this place seeming to function as a cemetery, it’s positively brimming with colorful and hearty plant life."
    "You continue to walk along the path through the garden only to find yourself within earshot of what seems to be a human voice."
    "It modulates strangely, but the sound is not unpleasant. In fact, it almost seems to draw you in…"
    "Following the source of the noise leads you to the edge of a little man-made pond. Along its edge crouches a figure wearing a plum tailcoat."
    menu:
        "If not for the being’s semi-translucence and the strange noises coming from their body, you may not have noticed them at all."

        "\"Hello? What are you doing?\"":
            "With a slight start, the noises from the figure cease, and their work on the ground comes to an end."
            "As if by habit, they move to dust off their hands as they stand up, only to laugh softly to themself."
            "While turning to face you, they briefly expose their palms, revealing that — perhaps predictably for a ghost — no dirt has lingered on them."
            voice "lyq1-01"
            show lysander neutral at lysander_spot
            ly "Apologies if I’ve disturbed you; I was just replanting this iris. "
            voice "lyq1-02"
            show lysander neutral
            ly "But... it’s a rare gift that I get visitors to this garden, and I don’t believe we’ve met. My name is Lysander."
        "Try to tap the figure on the shoulder.":

            "You approach the figure, hearing the strange noises grow louder from their body as you close the distance."
            "When you try to place a hand on their shoulder, you instead feel it pass straight through them."
            "Touching their form sends a cold shiver through your body."
            "But just as you begin to lose your balance, the figure whirls around to face you and steadies your wrist with their hand."
            "Despite the speed of their movement and the strength of their grip, the figure does not appear angry or even overly surprised."
            voice "lyq1-03"
            show lysander grateful at lysander_spot
            ly "Are you alright? I’m sorry if I grabbed you too firmly. I just didn’t want you to fall into the water."
            "The figure floats upward rather than standing in the typical fashion, taking pains to maintain your balance throughout your mutual ascent."
            voice "lyq1-04"
            show lysander neutral
            ly "Now that we’ve ensured that you stay comfortable and dry... I don’t believe we’ve met before. My name is Lysander."
        "Walk away from the figure.":
            "As you begin walking away from the figure, you notice a grave marker shaped like a strange, four-legged beast."
            "A dim sense of recognition twitches at the periphery of your subconscious; something about this headstone makes you laugh."
            voice "lyq1-05"
            show lysander grateful at lysander_spot
            ly "Ah, I see you’ve met this garden’s most amusing resident already!"
            voice "lyq1-06"
            show lysander neutral
            ly "I may be less fun company, but I’d like to think I’m more talkative. My name is Lysander."
    menu:

        "\"You’re a ghost…\"":
            voice "lyq1-07"
            show lysander neutral
            ly "I am. I’ve been here for a long time, too, so please feel free to ask me any questions you might have. I’ll do my best to answer them."
        "\"It’s nice to meet you.\"":
            voice "lyq1-08"
            show lysander grateful
            ly "Likewise! And please, don’t hesitate to ask any questions you might have. I know these grounds can be a bit much to take in."
        "\"This is an impressive garden.\"":
            voice "lyq1-09"
            show lysander neutral
            ly "Thank you. I’ve developed something of a horticultural habit in my time here, so I do my best to keep all the plants healthy and happy."
            voice "lyq1-10"
            show lysander grateful
            ly "That said, I doubt you’ve come to this mansion in pursuit of plant-tending knowledge, so please… If you have any questions, don’t feel as though you need to shy away from asking them."

    jump lysander_convohub


label lysander_abouttoleave:
    $ lysander_queststate = 2
    voice "lyq1-26"
    show lysander neutral
    ly "I understand. But, before you depart… I’d like to ask something of you, if you don’t mind."
    voice "lyq1-27"
    show lysander neutral
    ly "You may be aware that there are other spirits bound to this place—as I am. I don’t know why all of them linger, but I do know the cause of my persistence."
    voice "lyq1-28"
    show lysander distraught2
    ly "I…made a vow to always protect my sister. I knew I’d be engaged in a duel the next morning, and though I proved victorious, I had no way of predicting that outcome at the time."
    "Lysander’s hand goes to the bloodstained portion of his jacket as if reflexively."
    "He looks at you with a certain level of pained embarrassment."
    voice "lyq1-29"
    show lysander unique
    ly "I’m not sure who or what heard my plea and decided to take pity on me, but my wish was granted. I was simply granted a bit more time before this…"
    "Lysander makes a short gesture toward the sickly discoloration on the left side of his neck."
    voice "lyq1-30"
    show lysander disappointed
    ly "Although the infection ended my life, I was allowed to persist in this form — following alongside my sister, protecting her from what threats I could. "
    voice "lyq1-31"
    show lysander neutral
    ly "I did my duty as well as I could manage."
    voice "lyq1-32"
    show lysander distraught2
    ly "But, there was always one threat I knew I could never stave off…one existential inevitability. And so, as all humans must, Evangeline eventually died."
    voice "lyq1-33"
    show lysander unique
    ly "She departed. I could not. And it was only then that I realized the truth of the vow I had made—the cosmic joke I had failed to see."
    voice "lyq1-34"
    show lysander disappointed
    ly "My desperate request to serve as her perpetual guardian had been applied to her physical form alone. Her essence could transcend this world, but her body could not. "
    voice "lyq1-35"
    show lysander neutral
    ly "And, thus… Here I remain."
    "Lysander smiles, shaking his head slightly."
    voice "lyq1-36"
    show lysander neutral
    ly "Really, I got what I asked for. When you know the possibility of death is staring you in the face… I can’t say that I considered the specifics."
    voice "lyq1-37"
    show lysander grateful
    ly "My request to you is not grave-robbing, nor profane desecration of a person I still hold very dear."
    voice "lyq1-38"
    show lysander grateful
    ly "All that I burden you with is a request for information: data or documentation regarding the nature of the bindings currently tethering me to Evangeline and this world as a whole."
    voice "lyq1-39"
    show lysander neutral
    ly "I’ve been fortunate to access a good deal of the mansion over the years, but there is a collection of knowledge I have never been able to reach."
    voice "lyq1-40"
    show lysander neutral
    ly "I strongly suspect whatever that stash of literature contains is otherworldly in nature and may provide me with the means to alter the ties that bind me here…but I need your help in acquiring it."
    voice "lyq1-41"
    show lysander grateful
    menu:
        ly "Could I trouble you for this kindness?"
        "\"I'll look into it, Lysander.\"":
            pass
        "\"I'll think about it.\"":
            pass
        "\"No, you cannot.\"":
            pass

    "As you walk back toward the mansion, a dark and inquisitive sensation shifts nebulously in the back of your mind."
    "It feels oppressive and heavy, making the world around you distant and hazy—almost as if you're trying to peer through a thick fog."
    "You stop, close your eyes, shake your head vigorously, and feel a degree of levity return to your mental state."
    #voice ABBE'S LAUGH
    "The voice in your head laughs, feeling at once very present and very far away."
    ab "If his suspicions are true, the literature he seeks should be in my living room."

    call screen minimap()

label lysander_livingroom:
    "You find yourself struck with a simultaneous feeling of warmth and disconcertment."
    "As tempted as you are to take a seat by the fireplace, you can't help but feel as though the portrait immediately above its mantle is…observing you, somehow."
    "You glance around the room, deliberately avoiding the harsh gaze of the painting before you, and spot a bookshelf against the wall to your right."
    "Approaching the bookcase, you feel a sudden urge to run your fingers along the spines of the titles it holds."
    "You take in the names of each book and see they encompass a breadth of subjects—poetry, philosophy, mythology, history—but none catch your eye so much as those entirely unmarked."
    "You draw out one of the two you can see before you. It is a small, thin volume bound in grey-black cloth grown faded with age."
    "You flip open the front cover to see that, in lieu of a title page, the book begins with a handwritten note in small, clean lettering:"
    #"[Show Lysander note text, LysanderNote.png in Icon Art]"
    "Flipping through the pages reveals a small collection of charcoal drawings:"
    "A little girl with blonde hair and pained, hopeful eyes..."
    "A woman in a black dress laughing and holding a small vase of hydrangeas..."
    "Even a very messy sketch of a markedly less tired-looking Lysander. Curiously, both of his eyes seem to be the same color in this illustration."
    "The final illustration in the sketchbook appears much more recent. It depicts a rabbit viewed from afar, sitting next to the pond where you first encountered Lysander."
    "Iris petals are scattered around it, and it looks as though an iris petal is in the process of being consumed in the illustration."
    "You smile and shut the sketchbook, sliding it back onto its place on the shelf."
    "You doubt that this is the location Lysander wanted you to check."
    "After all, didn't he send you on this knowledge-hunting quest because he was unable to access the location in which that information was held?"
    jump elizabeth_convohub

label lysander_lounge:

    "You find yourself accosted with the remnants of cigar smoke, hard liquor, and an aroma you can't entirely place."
    "The entire experience of the room seems to feel more overwhelming than you can previously recall."
    "You rest a hand on the curved entryway to the lounge in a bid to steady yourself and adjust to the space, only for something to catch your eye."
    "In the corner to your left—seemingly as far away from the lounge bar and fireplace as possible—is a tiny and peculiarly-shaped wooden table."
    "Although the surface area of the table is very small, it contains what appears to be a series of drawers."
    "As you examine the table structure, you notice that each drawer is designed to pull outward in a different direction."
    "When all are fanned out, they form a diamond, with the peculiarly-shaped tabletop surface filling in the central gap created at their center."
    "Without giving it a second thought, you pull each of the four drawers outward in their respective directions."
    "Each contains an impressively large tome, their vibrant leather covers emblazoned in extravagant and beautifully-preserved embossed artwork."

label lysander_lounge_books:

    menu:
        "Which would you like to read?"

        "The white tome.":
            if lysander_queststate < 4:
                $ lysander_queststate = 3
            "You pick up the white tome from its drawer, taking in the illustration of a bird of prey on its cover."
            "The book is musty, but smells markedly better than most everything else in the lounge."
            "As you begin flipping through the book, you realize that it is a firsthand account detailing the design and construction of the mansion, courtesy of one \"A.M.L.\""
            "Although the bulk of the book seems to have been formally printed—the ornate lettering seems to indicate as much—there are handwritten notes added throughout."
            "These additions are in a flowy, confident script… Though you sense that whomever wrote the notes began documenting them more erratically and with less care over time."
            "Near the end of the book is a harshly-scrawled note, presumably from the author to himself, in nigh-incomprehensible capital lettering:"
            "\"THE PROJ…UNTIL WE ARE…TELL ANTOINE…WHETHER NEW OR…FOREV…\""
            "The final page in the book contains a watercolor painting of the mansion as it appeared when first constructed."
            "You feel a strange sense of pride whilst taking in the illustration. "
            "Snapping back to your own thoughts for a moment, you realize that this book may not be of great utility to you or Lysander, and place it back in its drawer."
            jump lysander_lounge_books

        "The red tome.":
            if lysander_queststate < 4:
                $ lysander_queststate = 3
            "You pull the red tome from its drawer, gazing at the strange, interlinking symbols shaped to form a circle upon its cover."
            "The book reeks of smoke, alcohol, and something vaguely metallic."
            "As you tentatively pull open the pages of the book, you see that each of its pages are bordered in incredibly detailed illustrations, albeit with one disconcerting theme."
            "While half of the border is filled with scenes of nature, contented animals, and sometimes even children playing..."
            "...the other half quickly fades into grotesque distortions of those same moments of levity."
            "You try to ignore the illustrations, but one recurring character continuously catches your eye:"
            "A portly and good-natured king, bearded and extravagantly-dressed, whose mirror image becomes emaciated and haggard, screaming as blood drips from his gouged-out eyes."
            "You do your best to turn your attention away from the tortured king and onto the text."
            "It reads almost like a prophecy or book of guidelines, continuously speaking about \"The One Who Waiteth in the Outer Dark.\""
            "There are abstract mentions of subroutines and other passages in a script you cannot hope to understand."
            "The longer you spend with this book, the more you feel a profound sense of unease around it."
            "Unwilling to wait any longer before returning it, you place the tome back into its drawer on the upper-right of the diamond and slide it inward."
            jump lysander_lounge_books

        "The black tome.":
            if lysander_queststate < 4:
                $ lysander_queststate = 3
            "You grab the black tome and remove it from its drawer, noting the skull and various other skeletal structures etched upon its cover in thin, silver lines."
            "The odor emanating from it is sickeningly sweet, as if trying to mask the lingering scent of putrescence."
            "The book is surprisingly heavy for its size, and upon opening to its first section, titled \"On the Body,\" you quickly realize that it is a book on anatomy and human physiology."
            "You begin to flip through the pages of tiny, handwritten text and take in the finely-detailed, if somewhat clinical, diagrams of various structures in the body."
            "Upon reaching the second half of the book, you are surprised to find another cover page in an entirely different font, this time reading \"On Reanimation.\""
            "Looking down at the bindings of the book, you realize that this tome's weight is likely not a product of its initial composition."
            "Rather, it is two separate titles stitched together at the tome's midpoint."
            "You try to read more into the latter section of the tome, but the highly technical language and almost disorganized flow of thought makes your mind swim."
            "You skim through the sections."
            "Although the book details the construction of artificial bodies in detail and granting them the ability to move..."
            "...it completely skips over the concept of imbuing them with any kind of metaphysical essence."
            "Begrudgingly, you accept that this book may not be particularly helpful to you or Lysander at the moment, and place it back into its drawer."
            jump lysander_lounge_books

        "The green tome." if lysander_queststate < 4:
            $ lysander_queststate = 4
            "You place a hand on either side of the green tome and remove it from its drawer."
            "Looking down at the book, you notice that this volume seems slightly more faded than the others within the drawers, as if it had once sat directly in the path of the sun"
            "On its cover is an etched illustration depicting two finches."
            "Curiously, this book lacks a traditional cover page or table of contents."
            "Instead, it starts with a note from the author: a warning."
            " It cautionins the reader that the topics contained within the tome are detailed purely for use in the realms of the theoretical and academic, rather than practical application."
            "\"In fact,\" concludes one paragraph, \"to apply these principles and techniques within one's own life...\""
            "\"...would almost guarantee a profound degree of suffering for oneself and all that they love.\""
            "It is a highly detailed breakdown of philosophical and practical approaches to metaphysics and the scientific structure of supernatural phenomena."
            "Much of the information contained within comes from a place of supposition rather than hard science."
            "You take special note of a chapter titled \"The Shackling of the Soul: Theories Regarding Perpetuation.\""
            "While much of the chapter's contents elude you due to their highly technical language and presumption of existing knowledge on the topic, a certain subsection catches your eye:"
            "\"After nearly a century of continued research, it is the belief of this author...\""
            "\"...that a mechanism through which an individual may release themselves from this plane by sheer force of will does, in fact, exist.\""
            "\"Putting an end to one's perpetuated existence unaided, and without the presence of a being or object firmly shackled to the plane upon which they are bound...\""
            "\"...remains inadvisable on a number of counts—but, contrary to my previous findings, it does appear to be possible.\""
            "\"Consider the canine Archibald (detailed previously in the fourth chapter of this volume), whose essence was asserted to remain in proximity to his master for the remainder of that man's life.\""
            "\"Upon the death of the human Archibald held in such high esteem, all metaphysical phenomena related to the dog also ceased.\""
            "\"As we discovered in the writings of Qaribah al-Saqr, indefinite perpetuation of the spirit is not guaranteed an attachment to the physical or energetic definite perpetuation of a person, object, or entity...\""
            "\"Therefore, we can postulate that Archibald's decision to depart alongside his master signifies that he was not bound to the man's physical body or to their mutual home...\""
            "\"...but instead either to the man's essence or nothing at all.\""
            "\"The latter case is of special interest to me; my own state was brought about by a passion for research...\""
            "\"...and thus (to my knowledge) exists independently from a physical or metaphysical source.\""
            "\"In any event, more research will be needed.\""
            "The chapter goes on to describe other observations on the nature of metaphysical bindings."
            "Their intensity can be amplified, de-amplified, or even transferred between beings."
            "But these actions cannot be taken in rapid succession, or too frequently, without the effort failing."
            "For as detailed as the book is, its design is surprisingly nondescript."
            "The pages are left unadorned, and the only notes or markings left behind are occasional spots of sun-bleaching or page weathering."
            "Its final section reads almost like a confessional from the author, once again cautioning the reader against applying any of the principles or techniques detailed within the tome."
            "The final page of the book reveals the name of the author—a certain Frederik Anderssen."
            "The page lists his lifespan as \"1742-1819; perpetuated until 1902, upon which time I released myself through the conclusion of my research.\""
            "Instead of returning this book to its drawer, you decide to keep it sitting next to you."
            jump lysander_lounge_books
        "I'm done reading.":
            "You slide each portion of the diamond back into place underneath the central tabletop. You shudder momentarily; what strange books."
            "Despite the more bizarre qualities of your recent reading material, you recognize that Lysander might be interested in some of your findings."
            jump herman_convohub


label lysander_ballroom:

    "You can see a mural of a battle scene painted on the wall, framed on either side by a pair of glass display cases left almost entirely empty."
    "Their shelves presumably populated and emptied as the mansion passed from owner to owner."
    "Although these structures could certainly hold books or notes of some variety, they seem to be designed much more for gaudy display pieces."
    "Even if such things were of interest to Lysander, he'd still be out of luck."
    "With the exception of one unusually dusty and roughly-whittled sculpture of a small bird sitting on a shelf in the case nearest you, the displays are completely vacant."
    jump aures_convohub


label lysander_readsome:

    voice "lyq1-72"
    show lysander neutral
    ly "So, have you found anything of note?"
    "You tell Lysander about the books in the lounge. He looks more than a bit surprised."
    voice "lyq1-73"
    show lysander grateful
    ly "You're far braver than I; while I admittedly try to avoid that place when possible, I also would've never considered it as a potential place to store literature."
    voice "lyq1-76"
    show lysander grateful
    ly "That being said, I'm afraid none of those books sound as though they'd be particularly helpful for my…situation. Out of curiosity, were there other books available to you?"
    "You smile sheepishly and admit that you may not have read all the books at your disposal."
    voice "lyq1-77"
    show lysander distraught2
    ly "If you felt as though you needed to leave that space before reviewing everything, I don't blame you. …nor would I hold it against you if returning to that place seems too unpleasant at the moment. Please, erm, do what feels manageable."
    jump lysander_convohub

label lysander_gottome:
    $ lysander_queststate = 5
    voice "lyq1-72"
    show lysander neutral
    ly "So, have you found anything of note?"
    "You tell Lysander about the books in the lounge. He looks more than a bit surprised."
    voice "lyq1-73"
    show lysander grateful
    ly "You're far braver than I; while I admittedly try to avoid that place when possible, I also would've never considered it as a potential place to store literature."
    "You mention the green tome to Lysander and summarize the contents of what you read from the chapter regarding theories of perpetuation. His eyes light up at the description, then grow wide and joyful when you retrieve Frederik Anderssen's book and pass it to him."
    voice "lyq1-74"
    show lysander grateful
    ly "What an incredible discovery! I never would've guessed that any scholarly research had been done into my condition, let alone by someone who experienced it for themselves!"
    voice "lyq1-75"
    show lysander neutral
    ly "This will be of immense help to me. Thank you, truly."
    jump lysander_convohub

label lysander_quest2intro:
    $ lysander_queststate = 6

    voice "lyq1-78"
    show lysander neutral
    ly "I'm sorry to trouble you with this, but could you stay awhile longer? I'd like a moment to look over the book you've brought me."
    "You shrug, then find a comfortable patch of grass to lie down in."
    "The air around you feels refreshing, and the light breeze in the trees and plant life is soothing…"
    "You can't help but close your eyes…"
    #black screen, and back to garden
    "You awake to find Lysander nudging you extremely gently on the shoulder."
    "His expression of concern relaxes considerably when you open your eyes."
    voice "lyq1-79"
    show lysander distraught
    ly "Ah! Did I disturb your nap? That wasn't my intention; I was worried you might've collapsed and hurt yourself, or…"
    menu:
        "He trails off and looks away for a moment."

        "\"I guess I did fall asleep.\"":
            voice "ly_lch3"
            show lysander grateful
            ly "I admittedly don't recall the sensation of sleep—well, not in the traditional sense, anyway—but I know it's extremely important to be well-rested! I'm truly sorry if I disrupted you."

        "\"Well, I'm fine, but I guess your plants might not be.\"":
            #voice ly_lch2
            show lysander grateful
            ly "Considering that you weren't sleeping in any of the flower arrangements, I highly doubt that they'll mind."

        "\"It'd take a lot more than that to kill me, Lysander.\"":
            #voice ly_sur1
            show lysander distraught2
            ly "I... have no doubt. I'm sorry if that was how my comment came across; I was just worried about you."


    "Lysander perks up a bit and looks back at you, his enthusiasm palpable."
    voice "lyq1-80"
    show lysander grateful
    ly "Thank you for your patience with me during my reading. I think I've largely gotten a handle on the sections regarding metaphysical bindings and what the author refers to as ‘indefinite perpetuation' — that is, existing in a state of immortality."
    voice "ly_puz2"
    show lysander neutral
    ly "If my understanding is correct, it sounds as though I might be able to alter the nature and intensity of my bindings to Evangeline—and to this manor—with or without the rituals described in the foremost chapters of this tome."
    #voice ly_hap5
    show lysander neutral
    ly "That said, I'd benefit immensely from your assistance in the process. I…admittedly don't know of anyone or anything besides you that could serve as such a robust point of reference for entities bound to this plane of existence."
    #voice ly_mad3
    show lysander thinking
    ly "After we make a decision as to how to proceed and begin our…ritual, for lack of a better word…I will gladly yield my will to yours. At that point, we should combine our efforts and willpower, both physical and metaphysical, and execute our choice."

    voice "lyq1-81"
    show lysander grateful
    ly "We have two options, with one of them carrying a condition that I'd like to propose after detailing them both."
    voice "lyq1-82"
    show lysander neutral
    ly "The first is to essentially duplicate the process by which Mr. Anderssen released himself from the bonds tying him to this world. We would simply…"
    "Lysander stops and brings a hand to his face for a moment before sighing and addressing you once more."
    voice "lyq1-83"
    show lysander disappointed
    ly "We would break the vow I made to Evangeline."
    voice "lyq1-84"
    show lysander unique
    ly "…even speaking that phrase feels like a violation, but it gets to the heart of the process."
    voice "lyq1-85"
    show lysander neutral
    ly "The other option is something I bring up only if it might be of scientific or personal curiosity to you. If you'd like, I could exchange my current bindings with yours."
    voice "ly_dis2"
    show lysander neutral
    ly "For me, this would serve the same purpose as releasing the bonds, but it would allow for you to persist indefinitely—even without being a ghost."
    voice "ly_sad4"
    show lysander neutral
    ly "Additionally, there are… Other perks. I'll warn you now, though: they are accompanied by a certain level of pain to establish."

    # OY THIS IS WHERE THE EFFING CG GOES PUT IT IN YOU PUT IT IN AHAHA
    show cg_lysander
    hide lysander
    with dissolve

    "Lysander points to his left eye."
    #voice ly_hap3
    #show lysander grateful
    ly "The most notable feature of my eye is the ability to detect metaphysical and magical bindings upon other objects or entities."
    #voice ly_puz3
    #show lysander neutral
    ly "It's a situationally useful quality. Certain parts of the mansion may become more overwhelming with it, but it will at least give you insight as to why."
    #voice ly_hap4
    #show lysander neutral
    ly "Whether or not you wish to pursue that path lies entirely with you. But there is one detail within the first option that I'd…"
    "Lysander's expression grows almost wistful for a moment, then settles into a state of concerned contentment."
    "He gestures to the book you brought him."
    #voice ly_sad5
    #show lysander neutral
    ly "Please, if you find anything—whether in this tome or in any literature spread throughout the mansion—that would eliminate the risk of losing myself, my sense of myself, during the ritual… Please tell me."

    hide cg_lysander
    show lysander at lysander_spot
    with dissolve

    voice "lyq1-86"
    #show lysander neutral
    ly "I completely understand if you'd like some more time to weigh these options, but I also know that I'm far from the only resident of this mansion. If you'd like for us to make and execute our choice now, I wouldn't be offended."

    menu:

        "\"I'm ready to make a choice.\"":
            #voice ly_hap4
            show lysander grateful
            ly "Absolutely."
            jump lysander_bigdecision
        "\"I'd like a little more time.\"":
            #voice ly_hap1
            show lysander neutral
            ly "Take however long you need — you know where to find me."
            call screen minimap()


label lysander_bigdecision:

    "After a brief period of preparation and a final walkthrough of the mansion, Lysander stands before you, a determined smile upon his face."
    "Using a piece of chalk procured from some obscure cupboard in the living room, he draws a moderately sized circle—its interior completely plain—and stands at its center."
    voice "lyq1-87"
    show lysander grateful
    ly "I'm doubtful that this distance between us will actually be necessary, but I'd hate to see you hurt on my account."
    "Lysander closes his eyes and exhales deeply."
    "You notice that his feet actually drift downward and touch the ground. "
    "All around you, the plant life seems to hum with an indescribable energy, as if anticipating the events to come."
    "The breeze so often felt within this garden is completely absent, lending the area an unusual level of quiet."
    "What feels like minutes pass before Lysander gasps, both eyes snapping open."
    "Within his left iris, you can see a faint, amber glow."
    "When he speaks to you, his voice is soft, but amplified almost as if emanating from within your own body."
    $lysander_questdone = True
    voice "lyq1-88"
    show lysander disappointed
    menu:
        ly "Now."

        "\"You served as a guardian in life and in death. I free you from your stewardship.\"":
            $ lysander_queststate = 7
            "You stand in awe as Lysander's ghostly form is enveloped in a gentle amber light, seemingly drawing him back upward into his typical floating posture."
            "As the light grows in intensity, you can see its color begin to shift—first to a more yellow color, and then to an incredibly intense white."
            "Despite the brilliance of the light, the amber glow from Lysander's eye is still visible, as are tendrils of amber beneath his clothing, snaking down his left arm and across his abdomen."
            "They seem to fan outward from the wound on his shoulder, like tiny tree roots running through his veins."
            "Lysander looks down to you and then up at the sky, smiling gently."
            voice "lyq1-89"
            show lysander grateful
            ly "I'd…prefer not to depart right at this moment, if that's alright."
            voice "lyq1-90"
            show lysander grateful
            ly "After all, it's a beautiful night, and I'd like to be sure my friend still has me here for as long as they need."
            "Lysander descends slowly, as if being gingerly lowered, and you notice that the tendrils of light running up and down the left side of body have retracted slightly."
            "As he nears you once more, you see that their retreat is gradual—almost like the rising or setting of the sun."
            "By the time he touches back down upon the ground, only a small orb of light remains within the hole in his jacket."
            "With a soft but surprisingly sharp crack and the scent of sulfur, the orb shatters, its ephemeral remains fading into nothingness in the space between Lysander and yourself. "
            "You are once again standing in front of Lysander, and can't help but notice:"
            "Although his physical appearance looks largely unchanged — his brown eye somehow looks both less vibrant and more joyful."
            "His entire essence seems to carry a sense of relief."
            voice "lyq1-91"
            show lysander neutral
            ly "Saying that I'm thankful for your help frankly feels ill-fitting for this moment, but I… Frankly, I'm a bit lost for words."
            "Lysander takes a step closer to you and places a hand on the side of your right shoulder, squeezing it gently."
            voice "lyq1-92"
            show lysander unique
            ly "I know I don't deserve the kindness you've shown me, but I'll never forget it. So, as long as you remain here…"
            voice "lyq1-93"
            show lysander neutral
            ly "If you ever need anything, know that I would be honored to be by your side. Whatever it is, I'll be there through it all."
            "The man before you takes in the garden he has spent nearly two centuries cultivating, and laughs more heartily than you've heard at any moment before."
            voice "lyq1-94"
            show lysander grateful
            ly "...well, let's say that I can be there in fifteen minutes. It looks as though, in all our excitement, I completely forgot to trim the roses."
            "You nod in understanding at Lysander and begin walking back toward the mansion, as if out of habit."
            "Crossing through the arbor, you feel a strange, wet sensation on your face, as if struck by water falling from above."
            "Stepping out from underneath the arbor and glancing up at the plant life wrapped around its structure, you are bewildered by the lack of any real moisture on the flowers…"
            "...until you feel the fluid running down the left side of your face."
            "You reach a hand up to the dampness and cautiously trace the fluid to its source, only to pull your fingers away in surprise."
            "You gaze down at your hand with your remaining eye, noting the shine of aqueous and vitreous humor upon its surface."
            "After blinking firmly a few times, both out of confusion and as if to seek confirmation regarding your lost sensory organ, you wipe your soiled hand upon one of your legs."
            "What else were you meant to do with it?"
            "You resume your walk back toward the mansion with markedly more care, taking pains not to stumble over any irregular stones upon the path. "
            "Although the loss of your left eye was painless and silent, you realize that its absence has altered your judgment of distance and depth."
            jump lysander_reflection


        "\"I promise, Lysander—you will never, ever lose who you are.\"":
            $ lysander_queststate = 8
            $ lysander_ded = True
            "With a sharp CRACK and faint scent of sulfur, you witness Lysander's entire body grow tense, then nearly double over as if struck in the abdomen. He covers his left eye with his opposite hand, breathing raggedly."
            voice "lyq1-95"
            show lysander distraught
            ly "What is… Something's…very wrong…"
            "As if in response, another resounding {i}CRACK{\i} fills the air around you. "
            "As Lysander's right hand darts to his left shoulder, you realize you can see a faint amber glow spreading across his body:"
            "Starting from his left shoulder and running steadily down his arm, across his torso, and down his abdomen."
            "When Lysander looks at you again, you see that his left eye is engulfed in light of the same color, as if being consumed by some silent flame."
            "His expression is one of horrified agony."
            "With a faster, more resonant {i}CRACK{\i}, Lysander's right hand twists unnaturally and slams its palm into his left shoulder — an involuntary motion contrary to the previous grasping at the spreading glow. "
            "The sound recurs and his left hand mirrors the path of his right, the fingers on each hand straining as they remain curled inward. "
            "Lysander's ragged breathing gradually slows, and as his struggling ceases, you see the light upon his skin slowly overtake the entire left half of his face. You take a few steps forward, only for him to call out to you."
            voice "lyq1-96"
            show lysander distraught2
            ly "No! This is… Done."
            "Lysander stands unmoving in the center of the circle, his body contorted and tense."
            "At the center of his illuminated, ghostly form, you notice a small object, its shape comparatively dark in relation to the rest of his body."
            "He looks at you with a smile, tears in his eyes."
            voice "lyq1-97"
            show lysander grateful
            ly "I know we were… Simply doing what we thought was best…"
            "With two ear-splitting {i}CRACKS{\i} and an overwhelming flash of light, the figure before you vanishes."
            "All that remains in his place is a bronze ring—elegant, but not particularly ostentatious—on a necklace chain."
            "The band is lightly engraved, and the circular framing of its central diamond is accentuated by three small orbs."
            "You feel compelled to pick the ring up, but as you do, you feel yourself grow incredibly lightheaded."
            "Falling to your knees, eyes closed in some bid to steady yourself, you see the glowing form of Lysander in your mind's eye."
            "He is trapped within a stone sarcophagus, nearly nose-to-nose with a rotted corpse dressed in feminine clothing."
            "In the darkness illuminated only by the lingering amber glow from his cursed body, Lysander begins to cry."
            "The vision fades and you find yourself on your hands and knees in the garden, the ring on a chain now swaying gently as it dangles from your neck."
            "You don't have any recollection of putting it on, but its presence is not intrusive."
            "But you feel the fluid running down the left side of your face."
            "You reach a hand up to the dampness and cautiously trace the fluid to its source, only to pull your fingers away in surprise."
            "You gaze down at your hand with your remaining eye, noting the shine of aqueous and vitreous humor upon its surface."
            "After blinking firmly a few times, both out of confusion and as if to seek confirmation regarding your lost sensory organ, you wipe your soiled hand upon one of your legs."
            "What else were you meant to do with it?"
            "You resume your walk back toward the mansion with markedly more care, taking pains not to stumble over any irregular stones upon the path. "
            "Although the loss of your left eye was painless and silent, you realize that its absence has altered your judgment of distance and depth."
            jump lysander_reflection

        "\"I will take this burden from you. Pass the pain of your vow to me.\"":
            $ lysander_queststate = 9
            "Lysander gestures for you to approach him."
            "You step into the chalk circle and walk up to Lysander."
            "You can clearly see a dim glow within the entirety of his left iris, the irregularly-shaped amber light flickering softly."
            voice "lyq1-98"
            show lysander neutral
            ly "I'd like to hold onto your forearm…if you'd be so kind."
            "He extends his left hand, which you mirror with your right. He nods with an unusually brisk politeness and clasps his left hand firmly onto your arm, just below the elbow."
            "The pressure is not uncomfortable, but also feels unyielding."
            "You hear a moderately loud CRACK that seems to come from both everywhere and nowhere around you, accompanied by the smell of sulfur."
            "Lysander's body tenses, and he smiles at you apologetically."
            voice "lyq1-99"
            show lysander distraught2
            ly "I'm sorry. I…don't want to hurt you."
            "With a markedly softer crack and only a mild flinch from Lysander, you realize you can see a faint amber glow spreading across his body:"
            "Starting from the wound within his left shoulder and running steadily down his arm, across his torso, and down his abdomen. "
            "The light descends like tiny tree roots running through his veins. Lysander continues clasping onto your arm."
            "You realize that the light is beginning to migrate across his body, the tendrils seeming to snake laterally across his frame and down his right side."
            "The glow within his left iris grows more intense, its quality more akin to flame than a mere glow."
            "For the first time, you realize that the irregularity of the light is not a byproduct of Lysander's eye, but instead…"
            "As if on cue, you feel a profound tearing deep within the tissues of your own left eye. You grimace and nearly fall to your knees, only for Lysander to hold you firmly upright."
            "You feel his grip begin slightly shaking."
            voice "lyq1-100"
            show lysander disappointed
            ly "I-It's alright. We'll be…done soon…"
            "The unknowable script carving its way into your retina burns intensely, but not quite enough to mask the burning sensation steadily making its way across your body."
            "You look down at your torso to see that the amber light from Lysander's body has flowed seamlessly into your own, steadily making its way back to its previous placement."
            "The sensation is what you imagine it would be like if your veins were to suddenly start writhing through your body."
            "But whatever pain this part of the process would cause is drowned out entirely by the agony within your eye."
            "Lysander looks at you in a mixture of bewilderment and horror, but says nothing."
            "You suspect he is unable to speak from the pain."
            "As suddenly as it began, the agony within your body ceases."
            "Lysander's grip breaks from your arm and he stumbles backward, only to resume his typical floating posture in a bid to catch his balance."
            "You are not quite so lucky, and instead fall backward, landing in a disheveled—but more or less seated—position."
            voice "lyq1-101"
            show lysander distraught2
            ly "Are you…did we…"
            "You gaze up at Lysander and blink hard, aware of a change to your field of vision."
            "Reaching up to the left side of your face, you feel something warm and wet. Lysander grimaces."
            voice "lyq1-102"
            show lysander disappointed
            ly "Your eye didn't make it."
            "You pull your hand away from your face and gaze down at it, noting the shine of aqueous and vitreous humor upon its surface."
            "As you continue looking at the material, you sense a dim awareness from the left side of your face."
            "Even without sight, you know that this material carries the same sensation as the fiery pain that spread through your body."
            "Sensing your confusion, Lysander closes the distance between the two of you."
            voice "lyq1-103"
            show lysander neutral
            ly "The remaining tissues of your left eye should still be able to detect the nature of whatever bindings exist on a given object or substance. Is that what you're feeling?"
            "You nod and quickly wipe your soiled hand upon one of your legs."
            "What else were you meant to do with it?"
            "Lysander helps you back up to your feet and offers a brief explanation of how his eye typically functions."
            "How to differentiate objects bound to the same entity versus objects that entity had recently interacted with:"
            "How to tune out certain energetic signals, and even how to utilize the signals to easily locate other ghosts within the mansion."
            "As Lysander explains the mechanics of his prior abilities, you can't help but notice that, although his appearance remains largely unchanged, his own left eye seems both less vibrant and more joyous than you remember."
            "After concluding his explanation, Lysander looks at you with a warmth that has grown strangely familiar to you."
            voice "lyq1-104"
            show lysander neutral
            ly "Saying that I'm thankful for your help frankly feels ill-fitting for this moment, but I… Truly, I'm a bit lost for words."
            "Lysander gently extends a hand, then pulls you in for a hug."
            "Predictably, although he can hug you, your arms simply pass through him."
            voice "lyq1-105"
            show lysander grateful
            ly "I know I don't deserve the kindness you've shown me, but I'll never forget it. So, as long as you remain here…"
            voice "lyq1-106"
            show lysander neutral
            ly "If you ever need anything, know that I would be honored to be by your side. Whatever it is, I'll be there through it all."
            "Lysander pulls back and laughs to himself."
            voice "lyq1-107"
            show lysander grateful
            ly "Though, saying that… I realize that I should probably give you some time to tinker with seeing the world in a new way."
            voice "lyq1-108"
            show lysander grateful
            ly "Please, don't hesitate to find me should you need anything. Truly."
            "You begin to carefully walk back toward the mansion, taking pains not to stumble over any irregular stones upon the path."
            "Although the departure of your left eye granted you new abilities, you realize that its absence has altered your judgment of distance and depth."
            jump lysander_reflection

        "\"This is what you agreed to. Accept it in its purest form.\"":
            $ lysander_queststate = 10
            $ lysander_ded = True
            "With a sharp CRACK and faint scent of sulfur, you witness Lysander's entire body grow tense, then nearly double over as if struck in the abdomen. "
            "He covers his left eye with his opposite hand, breathing raggedly."
            voice "lyq1-109"
            show lysander distraught
            ly "What…did you…do…?"
            "As if in response, another resounding CRACK fills the air around you.  "
            "As Lysander's right hand darts to his left shoulder, you realize you can see a faint amber glow spreading across his body:"
            "Starting from his left shoulder and running steadily down his arm, across his torso, and down his abdomen."
            "When Lysander looks at you again, you see that his left eye is engulfed in light of the same color, as if being consumed by some silent flame."
            "His expression is one of horrified, furious agony."
            "With a faster, more resonant CRACK, Lysander's right hand twists unnaturally and slams its palm into his left shoulder:"
            "An involuntary motion contrary to the previous grasping at the spreading glow."
            "The sound recurs, and his left hand mirrors the path of his right, the fingers on each hand straining as they remain curled inward."
            "Lysander averts his gaze from you and looks down."
            "His breathing is ragged, and as he slowly stops struggling, you realize that you can see something dark sitting at the center of his illuminated ghostly form."
            voice "lyq1-110"
            show lysander disappointed
            ly "You would not grant me reprieve… So, instead, you make me into this facsimile of a corpse…"
            "Lysander looks up at you for a final time."
            "The entire left half of his face has been consumed by light."
            "He smiles weakly."
            voice "lyq1-111"
            show lysander disappointed
            ly "I hope it brought you… Some familiarity…"
            # white screen and hide lysander
            "With two ear-splitting CRACKS and an overwhelming flash of light, the figure before you vanishes."
            "All that remains in his place is a bronze ring—elegant, but not particularly ostentatious—on a necklace chain."
            "The band is lightly engraved, and the circular framing of its central diamond is accentuated by three small orbs."
            "You feel compelled to pick up the ring, but you feel yourself grow incredibly lightheaded as you do."
            "Falling to your knees, eyes closed in some bid to steady yourself, you see the glowing form of Lysander in your mind's eye."
            "He is trapped within a stone sarcophagus, nearly nose-to-nose with a rotted corpse dressed in feminine clothing."
            "In the darkness illuminated only by the lingering amber glow from his cursed body, Lysander begins to cry."
            "The vision fades, and you find yourself on your hands and knees in the garden, the ring on a chain now swaying gently as it dangles from your neck."
            "You don't have any recollection of putting it on, but its presence is not intrusive."
            "As you begin moving to stand upright on the garden path, you find yourself suddenly aware of a change to your field of vision."
            "You reach a hand up to the left side of your face, only to feel something warm and wet."
            "Your fingers cautiously trace the fluid to its source, only to pull away from your face in surprise."
            "You gaze down at your hand with your remaining eye, noting the shine of aqueous and vitreous humor upon its surface."
            "After blinking firmly a few times, you wipe your soiled hand upon one of your legs."
            "What else were you meant to do with it?"
            "You begin to carefully walk back toward the mansion, taking pains not to stumble over any irregular stones upon the path."
            "Although the departure of your left eye was painless, you realize that its absence has altered your judgment of distance and depth."
            jump lysander_reflection
