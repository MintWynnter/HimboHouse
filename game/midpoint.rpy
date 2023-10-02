label midpoint:

    scene bg basement

    "The decomposition, however, does not stop with your knee."
    "Before you can fully acclimate to the reshuffling of your leg, you feel a splatter on your arm."
    "Gray matter is oozing out of your ear, down your neck, and pooling in the cavity on your shoulder."
    ab "Uh oh."
    # screen goes black
    # sfx thud

    # wait 5 seconds

    # show bg of basement
    # sfx surgeon noises
    "You awaken in a dark, dank room atop a metal gurney."
    "Your arms and legs are strapped to its side railings."
    "Lying on your back, you tilt your head to observe your surroundings."
    "Rotted wooden boards line the ceiling above you."
    "Sparse shelves hold jars filled with biological material."
    "A large electrical machine crackles as sparks jump from one node to another."
    "You tilt your head back as much as you can, to see what might be behind you."
    voice "drq7-01"
    dr "Aah-aah-ahh — Enough squirming! You must be still, or I cannot work."
    "Whoever is behind you, they press a hand firmly onto your forehead."
    "You can feel your skull cave in response to the pressure."
    voice "drq7-02"
    dr "Oops. Dear me, now, it’s spilled all over."
    "He lessens the pressure."
    voice "drq7-03"
    dr "You have had quite the adventure so far."
    voice "drq7-04"
    dr "You’re quite the natural, a real cadaver about town."
    voice "drq7-05"
    menu:
        dr "Almost back to your old self, I’d say."

        "\"Wait, who am I?\"":
            voice "drq7-06"
            dr "The question of the day, isn’t it?"
            voice "drq7-07"
            dr "That’s precisely what I’m trying to answer."
        "\"Wait, who are you?\"":
            voice "drq7-08"
            dr "Oh, me? That’s hardly important."
        "\"Unhand me immediately!\"":
            voice "drq7-09"
            dr "A bit antsy, are we?"
            voice "drq7-10"
            dr "Be patient, I am not your captor."

    voice "drq7-11"
    dr "I’m just a humble old physician, looking for a friend of mine."
    voice "drq7-12"
    dr "Is that you, Maurice?"
    "…"
    #voice
    ab "Wait a second, I know this man."
    "The voice in your head whispers to you, as if he would otherwise be heard."
    #voice
    ab "Do not tell him anything."
    voice "drq7-13"
    menu:
        dr "Maurice? Are you in there?"

        "\"I’m not Maurice, but he is hanging out in the back of my head.\"":
            voice "abq7-1"
            ab "How dare you?!"
            voice "drq7-14"
            dr "Back of your head? Hmmm…"
            voice "drq7-15"
            dr "Could be subconscious, could be the influence of the mansion itself.."
            voice "drq7-16"
            dr "Or, he really could be in there."
        "\"Who is Maurice?\"":
            voice "abq7-2"
            ab "Thank you."
            voice "drq7-17"
            dr "Ah. That does not bode well."
            voice "drq7-18"
            dr "Maurice owned this mansion long, long ago."
            voice "drq7-19"
            dr "And I was hoping he might be in your pretty little head, somewhere."
        "\"Yes, I am Maurice.\"":
            voice "abq7-3"
            ab "What are you doing?"
            voice "drq7-20"
            dr "Oho, are you now?"
            voice "drq7-21"
            dr "Trust me, if you were Maurice, you would be speaking to me very differently."

    voice "drq7-22"
    dr "If Maurice really is in there, I cannot imagine he’s thrilled about it."
    voice "drq7-23"
    dr "He was supposed to have full control over this vessel — I mean, you."
    voice "drq7-24"
    dr "Alas, I seem to have created someone or something entirely new."
    voice "drq7-25"
    menu:
        dr "Have you any memories?"

        "\"No, I just appeared at the foot of the mansion tonight.\"":
            voice "drq7-26"
            dr "Curious. Unsurprising, but a complication nonetheless."
        "\"If I have them, I don’t have access to them.\"":
            voice "drq7-27"
            dr "Memories could very well be locked away in there somewhere."
            voice "drq7-28"
            dr "The question is: Whose memories, exactly?"
        "(Lie) \"Yes, I have every memory of my previous life fully intact.\"":
            voice "drq7-29"
            dr "Mmhmm. And whose memories are those, exactly?"

    voice "drq7-30"
    dr "See, you could be one of three people."
    voice "drq7-31"
    dr "You could be Abbé Maurice Lachaise with a bad case of amnesia."
    voice "drq7-32"
    dr "You could be the crooked gravedigger your vessel is made of, waking up to a new consciousness."
    voice "drq7-33"
    dr "You could be some new version of me. You’ve got a fair amount of my gray matter rumbling around in your brain, after all."
    voice "drq7-34"
    dr "Or, you could be someone new entirely."
    voice "drq7-35"
    dr "But if you lack memory altogether, then you may as well be the latter."
    voice "drq7-36"
    dr "Come, take a look."
    "The same hand that caved in your skull reemerges above your head, wielding a piece of shattered glass."
    "He jabs the shard into your cheek at such an angle that you can glimpse an old man in its reflection."
    show presper neutral at presper_spot
    "He is ancient."
    "His skin is blotched many times over. His hair has lost all its pigment — it is white as a fingernail's edge."
    "A great number of tubes pump fluid into and out of his body. Their source and destination, respectively, is unclear."
    menu:
        "He holds a surgical scalpel that drips blood onto the piles of brain tissue and bone fragments scattered about the metal surface of the gurney."

        "\"What are you doing to my brain?\"":
            voice "drq7-37"
            show presper neutral
            dr "Just poking around is all."
            voice "drq7-38"
            show presper furrowed
            dr "A bit of light maintenance, to the extent that I can manage."
        "\"You look older than time.\"":
            voice "drq7-39"
            show presper furrowed
            dr "I would not throw such stones, cadaver."
            voice "drq7-40"
            show presper furrowed
            dr "I am not quite as old as time, and at least my brains don’t seep out of my head without warning."
            voice "drq7-41"
            show presper concerned
            dr "Not anymore, at least."
        "Watch in silence.":
            "He carves into your brain, scooping out and rearranging entire lobes with reckless abandon."

    voice "drq7-42"
    show presper furrowed
    dr "You are a piece of work, you know that?"
    voice "drq7-43"
    show presper furrowed
    dr "I just revivified you not two hours ago, and already you are coming apart at the seams."
    voice "drq7-44"
    show presper curious
    dr "That’s what I get for playing necromancer, I suppose."
    voice "drq7-45"
    show presper curious
    dr "Still, you are making waves in this mansion, if I can call them that."

    # this is where presper reacts to the quest outcomes, check these variables are right
    if q3_state is 4:
        voice "drq7-46"
        dr "That girl in the foyer seems brighter than ever."
    if q3_state is 3:
        voice "drq7-47"
        dr "That girl in the foyer seems more dour than ever."
    if q3_state is 2:
        voice "drq7-47"
        dr "That girl in the foyer seems more dour than ever."
    if elizabeth_queststate is 6:
        voice "drq7-48"
        dr "You delivered quite the bombshell to that little girl in the living room."
    if elizabeth_queststate is 7:
        voice "drq7-49"
        dr "You spared that little girl in the living room one heck of a bombshell."
    if herman_queststate is 6:
        #voice "drq7-50"
        #dr "You’ve cut off that very angry man from unspeakable power."
        voice "drq7-51"
        dr "You’ve given that very angry man carte blanche with unspeakable power."
    if aures_queststate is 5:
        voice "drq7-52"
        dr "You've introduced a new guest to that girl in the ballroom."
    if aures_queststate is 6:
        voice "drq7-53"
        dr "You started and ended a relationship for that girl in the ballroom."
    if lysander_queststate is 5:
        voice "drq7-54"
        dr "You freed that gardener boy from one nasty curse."
    if lysander_queststate is 6:
        voice "drq7-55"
        dr "You made that gardener boy more miserable than I’ve ever seen him."

    voice "drq7-56"
    show presper neutral
    dr "There’s certainly a personality of some kind in you somewhere."
    voice "drq7-57"
    show presper neutral
    dr "Otherwise, you wouldn’t be making so much noise up there."
    voice "drq7-58"
    show presper concerned
    dr "Perhaps you’ve noticed this, but ghosts are… indecisive."
    voice "drq7-59"
    show presper concerned
    dr "It really takes a mortal to effect change, I’ve found."
    voice "drq7-60"
    show presper curious
    dr "You might not be fully mortal, but you’re certainly acting like one."
    voice "drq7-61"
    show presper neutral
    menu:
        dr "What’s compelling you, precisely, to do all this?"

        "\"I just want to be of help.\"":
            pass
        "\"The voice of Maurice is telling me to.\"":
            pass
        "\"I just like stirring the pot, what can I say?\"":
            pass

    "The old man lets out a sigh, but his next words are interrupted by a loud banging."
    "A rusted iron door, bolted to the wall and barred shut, clangs as something behind it pounds against it with vigor."
    "The clangs echo through the small room. The gurney shakes with each reverberation."
    voice "drq7-62"
    show presper curious
    dr "Aha, it seems our friend is itching to meet you."
    voice "drq7-63"
    show presper curious
    dr "If Maurice is somewhere in you, perhaps that’s what got them so riled up."
    "The old man stands back up and places his scalpel on a table."
    "He walks into your line of sight. The glass you watched him through only hinted at the extent of his dilapidation."
    "You can now see the great many tubes that hang from the base of his arms."
    "They run down his side, down to his feet, and trail off toward the rusted iron door."
    "He picks up the slack of the tubes as he nears the door and holds it bundled in his hand."
    "With the other hand, he removes the bar, but not without great effort."
    "The bar clangs to the floor as it comes loose."
    "And the door swings open."
    #voice am [roar]
    "A beast of unclear proportions is on you immediately."
    "It clambers up the gurney and knocks it on its side, sending you falling to the ground."
    "But still strapped to the table, you lie horizontal, bound to the gurney and suspended just a few inches above the ground."
    "You can sense the beast looming over you."
    "It presses against your body. There is no fur, only flesh."
    "What feel like dozens of fingers — tongues? — probe at your body."
    "One such appendage finds its way into the hole in your head, carefully carved by the old man."
    "You can feel it digging."
    voice "drq7-64"
    show presper concerned
    dr "None of that, none of that!"
    "The sound of the old man draws closer."
    "The beast hems and haws in a cacophony of animalistic grunts and very human groans."
    voice "drq7-65"
    show presper concerned
    dr "You cannot have them yet, my dears. They still have much to do."
    "The beast yet probes."
    voice "drq7-66"
    show presper furrowed
    dr "I said, much to do!"
    "The beast pauses."
    voice "drq7-67"
    show presper concerned
    dr "I’m sorry, my dears. Now is not the time."
    "And the beast retracts."
    "By the time you get your bearings and look up, the old man has barred the door shut again."
    "His tubes run under the door and into the room behind."
    "He turns back to you."
    voice "drq7-68"
    show presper neutral
    dr "I did not expect them to be so aggressive."
    voice "drq7-69"
    show presper neutral
    dr "They have been out of sorts since I got you walking about."
    voice "drq7-70"
    show presper curious
    dr "Perhaps they’re jealous."
    voice "drq7-71"
    show presper curious
    dr "Perhaps they miss you."
    voice "drq7-72"
    show presper curious
    menu:
        dr "It is unclear."

        "\"Jealous of me?\"":
            voice "drq7-73"
            show presper neutral
            dr "You are not my only marvel of medicine, you know."
        "\"They miss me?\"":
            voice "drq7-74"
            show presper neutral
            dr "Perhaps. You were not made from nothing, you know."
        "\"What was that thing?\"":
            voice "drq7-75"
            show presper furrowed
            dr "Be polite! They mean you no harm, I think."

    voice "drq7-76"
    show presper neutral
    dr "Whatever the case, I cannot let them disrupt all this good work you’re doing."
    voice "drq7-77"
    show presper neutral
    dr "Appeasing these ghosts is exactly what I need."
    voice "drq7-78"
    show presper furrowed
    dr "I am getting so very sick of their scrutiny."
    voice "drq7-79"
    show presper curious
    dr "It is driving me, dare I say, a little bananas."
    voice "drq7-80"
    show presper neutral
    dr "I just want to perform my experiments alone, and in peace."
    voice "drq7-81"
    show presper furrowed
    dr "I do not need pesky ghosts giving me the evil eye for simply going about my business."
    voice "drq7-82"
    show presper furrowed
    menu:
        dr "Don’t they know I want to be left alone?"

        "\"I don’t think they know anything about you.\"":
            voice "drq7-83"
            show presper concerned
            dr "Oh, come now. I’ve been down here for 200 years."
            voice "drq7-84"
            show presper concerned
            dr "Someone has to have found me, try as I might to self-seclude."
        "\"They seem pretty comfortable where they are.\"":
            voice "drq7-85"
            show presper furrowed
            dr "Comfortable? They are living on Lachaise property."
            voice "drq7-86"
            show presper furrowed
            dr "I’ve been the keeper of this place for 200 years, not they."
        "\"Why do you want to be alone in the first place?\"":
            voice "drq7-87"
            show presper furrowed
            dr "Because this is Lachaise Manor, not a bed and breakfast!"
            voice "drq7-86"
            show presper furrowed
            dr "I’ve been the keeper of this place for 200 years, not they."

    "He stops himself and sighs."
    voice "drq7-88"
    show presper neutral
    dr "I just want to make things right."
    voice "drq7-89"
    show presper concerned
    dr "I just want to bring him back."
    "He stands there, quiet."
    voice "drq7-90"
    show presper neutral
    dr "Go. Back up to the manor."
    voice "drq7-91"
    show presper curious
    dr "Let your curiosity drive you. Or your compassion. Or your chaos. I don’t care."
    "He walks back over to you, rights the gurney, and undoes each of the straps."
    $ presper_name = "Dr. Presper"
    menu:
        "He puts out his hand."

        "Shake it.":
            "The grip is limp, but warm."
            voice "drq7-92"
            show presper curious
            dr "Antoine Presper."
        "Refuse.":
            "He retracts his hand slowly."
            voice "drq7-93"
            show presper neutral
            dr "I understand. Presper. Antoine Prepser."
        "Spit in his hand.":
            "He stares at the mix of green phlegm, red fluid, and brown bile that sits on his palm."
            voice "drq7-94"
            show presper furrowed
            dr "Presper. Antoine Presper."
            "He clenches his fist. The bile squelches out and onto the floor."

    voice "drq7-95"
    show presper neutral
    dr "If I made someone new, it’s pleasure to meet you."
    voice "drq7-96"
    show presper neutral
    dr "If I didn’t, then it’s good to see you again."
    voice "drq7-97"
    show presper curious
    dr "And I will see you very soon."
    # screen black
    "In a flash, you black out again."
    # screen to mansion exterior
    "… and find yourself back on the front porch of the great mansion."
    #voice
    ab "I have recalled a great many things just now."
    voice "abq0-126"
    ab "You may not have memories, but I do. They are harrowing."
    #voice
    ab "Do not make me speak of them now. I need time."


    # add the question mark to the map screen!

    call screen minimap()
