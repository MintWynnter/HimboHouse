label arabella_foyer:

    scene bg foyer
    show blink
    with fade


    #show whatever bg i don't remember the syntax

    if q3_priest_journal and q3_mom_journal and q3_doctor_journal and q3_own_journal and q3_pendant_encounter and not q3_ending_trigger:
        jump arabella_ending

    if q3_state > 0:
        #play greeting
        jump arabella_hub

    if q3_state is 0:
        jump arabella_intro



label arabella_intro:

    "You step into the foyer."
    "That is to say, the foyer swallows you."
    "The decreptitude of the mansion's exterior, however, betrays the grandeur of what you find inside."
    "Dual staircases sweep up either side of the room, leading to an enourmous oil painting."
    "A lit candelabra sits atop a shined mahogany table."
    "The warmth of its light imbues the walls and floor with a sense of peace."
    "And, of life."
    "A soft, whispery voice calls out from somewhere nearby."
    voice "arq3-01"
    ar "Who are you?"

    menu:

        "Politely respond.":
            "Drawing all of your courage, you ask softly back:"
            mc "Who are you?"
            "You look around, trying to pinpoint the source of the voice. In the corner of your eye, you see a figure emerge from the shadows."
            "In the corner of the dimly lit foyer, a breathtaking apparition materializes, captivating yet paralyzing you with her ethereal presence."
            "As a ghostly specter, she emanates an otherworldly beauty."
            "As she stands in the corner, bathed in the soft, ambient glow, she radiates an undeniable grace and longing."
            "The apparition's gaze rests upon you, as if in anticipation of your next move."
            "You take a hesitant step forward, captivated by her beauty yet terrified of the unknown."
            "The apparition smiles sadly at you and the corner of her lips turns upwards, revealing a hint of warmth in the depths of her ghostly eyes."
            "She speaks softly, gazing around the room with a melancholic expression on her face."
            $ arabella_name = "Arabella"
            show arabella regal at arabella_spot
            with dissolve
            voice "arq3-02"
            ar "My name is Arabella. I lived in this home with my mother and father, but my life ended here many years ago."
            voice "arq3-03"
            ar "This house holds many secrets and much sadness... I cannot help but wonder if it will ever be free from its shackles."
            "You ask her gently:"
            mc "Why are you here? Are you not able to leave?"
            "Arabella sighs softly and it sounds almost like a whisper."
            show arabella melancholic at arabella_spot
            voice "arq3-04"
            ar "I am bound to this house. It was my prison while I lived, and it is now my prison after death."
            voice "arq3-05"
            ar "My parents believed me to be cursed or possessed; never allowing me to step outside these walls."
            mc "I see…"
            "You gaze at her in sympathy, knowing that she will never find peace as long as the secrets of the house remain untold."
            "Suddenly, an idea dawns on you, one that could potentially break the bonds of her eternal solitude and offer Arabella freedom at last."
            "You take a deep breath before speaking, hoping with each word that your plan will succeed and that Arabella will soon be free from her chains."
            mc "I don't know how to help, or what it will cost, but I want to help you."
            mc "If there is anything I can do, whatever it takes, I will help you be freed of your past."
            "She looks at you for a few moments, and then speaks slowly and softly."
            "Her voice carries a subtle glimmer of hope, one that she has perhaps been holding on to for many years."
            show arabella joyful
            voice "arq3-06"
            ar "If you are willing, I accept your offer."
            "Arabella closes her eyes and takes a deep breath, steeling herself for what is to come next."
            jump q3_intro_2
        "Be direct.":
            "Drawing all of your courage, you ask softly back:"
            mc "Who are you?"
            "You look around, trying to pinpoint the source of the voice."
            "In the corner of your eye, you see a figure emerge from the shadows."
            "In the corner of the dimly lit foyer, a breathtaking apparition materializes, captivating yet paralyzing you with her ethereal presence."
            "As a ghostly specter, she emanates an otherworldly beauty."
            "As she stands in the corner, bathed in the soft, ambient glow, she radiates an undeniable grace and longing."
            "The apparition's gaze rests upon you, as if in anticipation of your next move."
            "You take a hesitant step forward, captivated by her beauty yet terrified of the unknown."
            mc "Why are you haunting this house?"
            "The specter is taken a bit back by your sudden hostility."
            "She sighs softly and it sounds almost like a whisper."
            "Speaking softly, she gazes around the room with a melancholic expression on her face."
            $ arabella_name = "Arabella"
            show arabella melancholic   at arabella_spot
            with dissolve
            voice "arq3-07"
            ar "M-my name is Arabella. I lived in this home with my mother and father, but my life ended here many years ago."
            "She hesitates."
            voice "arq3-08"
            ar "I… I am bound to this house. It was my prison while I lived, and it is now my prison after death."
            voice "arq3-09"
            ar "My parents believed me to be cursed or possessed; never allowing me to step outside these walls."
            mc "I see…"
            "You take a deep breath before speaking, hoping with each word that your plan will succeed and that Arabella will soon be free from her chains."
            mc "I don't know how to help, or what it will cost, but I want to help you."
            mc "If there is anything I can do, whatever it takes, I will help you be freed of your past."
            "She looks at you hesitantly for a few moments, and then speaks slowly and softly."
            "Her voice carries a subtle glimmer of hope, one that she has perhaps been holding on to for many years:"
            show arabella contemplative
            voice "arq3-10"
            ar "Okay… If you are willing, I accept your offer."
            "Arabella closes her eyes and takes a deep breath, steeling herself for what is to come next."
            jump q3_intro_2
        "Run away.":
            "Frozen, you look around, trying to pinpoint the source of the voice."
            "The air becomes cold around you, causing you to stiffen, every hair on the back of your neck standing on end."
            "Not finding the source of the voice you just heard, you hurriedly turn around and speed off into the other room."
            "You feel like a coward; perhaps when you can find your courage, you'll find the source of that whisper."
            jump foyer_exit

label q3_intro_2:
    show arabella determined
    voice "arq3-11"
    ar "I need to know the truth. Why did my parents confine me here? Why wasn't I allowed to leave, to live life like everyone else? What did I do wrong for them to keep me locked away?"
    menu:
        "Of course, Arabella. Let's uncover the truth together. Where should we start?":
            voice "arq3-12"
            ar "Well, let's see… I'm sure that my parents might have kept some kind of journal or something of the sort."
            voice "arq3-13"
            ar "There may be some notes from the various doctors and priests who came through and examined me throughout my life."
            voice "arq3-14"
            ar "Mother spent a lot of time reading and writing in the living room, while Father spent a lot of time entertaining guests in the lounge."
            voice "arq3-15"
            ar "I don't have a lot of memories from when I was alive, so it's possible that I may have also kept a journal as well."
            "The voice in the back of your head chimes in."
            ab "This place is littered with all sorts of documents."
            ab "Good luck rooting through all of it."
            mc "Thank you, Arabella. I will get started as soon as possible."
            show arabella contemplative
            voice "arq3-16"
            ar "You are most welcome, dear friend… Remember, Mother enjoyed Phoenix's and was always the protector of Father's most well-kept secrets."
            "She goes to turn, before exclaiming and whipping back towards you."
            voice "arq3-17"
            ar "Oh! Before you go, a word of caution… If you are going to the lounge…"
            show arabella determined
            voice "arq3-18"
            ar "Watch out for Herman, if you have not run into him already…"
            voice "arq3-19"
            ar "He's a bit of a… snake, if you catch my meaning…"
            $ q3_state = 1
            jump arabella_convohub
        "Pry for more information.":
            mc "Before I agree, I need to know more. Why are you trapped here?"
            voice "arq3-20"
            ar "I believe it's because I can't forgive my parents."
            voice "arq3-21"
            ar "I don't have many memories, but it's a lingering, overwhelming feeling."
            voice "arq3-22"
            ar "I believe that the mansion won't let me go until I do."
            mc "I see… Well, I want to help you the best that I can."
            mc "Where should I start looking then?"
            voice "arq3-12"
            ar "Well, let's see… I'm sure that my parents might have kept some kind of journal or something of the sort."
            voice "arq3-13"
            ar "There may be some notes from the various doctors and priests who came through and examined me throughout my life."
            voice "arq3-14"
            ar "Mother spent a lot of time reading and writing in the living room, while Father spent a lot of time entertaining guests in the lounge."
            voice "arq3-15"
            ar "I don't have a lot of memories from when I was alive, so it's possible that I may have also kept a journal as well."
            "The voice in the back of your head chimes in."
            ab "This place is littered with all sorts of documents."
            ab "Good luck rooting through all of it."
            mc "Thank you, Arabella. I will get started as soon as possible."
            show arabella contemplative
            voice "arq3-16"
            ar "You are most welcome, dear friend… Remember, Mother enjoyed Phoenix's and was always the protector of Father's most well-kept secrets."
            "She goes to turn, before exclaiming and whipping back towards you:"
            voice "arq3-17"
            ar "Oh! Before you go, a word of caution… If you are going to the lounge…"
            show arabella determined
            voice "arq3-18"
            ar "Watch out for Herman, if you have not run into him already…"
            voice "arq3-19"
            ar "He's a bit of a… snake, if you catch my meaning…"
            $ q3_state = 1
            jump arabella_convohub

label arabella_journalentries_stop:

    "You put the journal back down on the desk, deciding it’s probably best not to take it with you."
    "Though, the information from it seems to shed some new light on a few things."
    jump marianne_convohub



label arabella_journalentries:

    "\"July 13th\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"The walls of this mansion feel more like a prison each day.\""
    "\"Every morning, I wake to the same views, the same rooms, the same echoing silence. What sin have I committed to be confined so?\""
    "\"Mother and Father continue to whisper in hushed tones, thinking I do not hear. But I do. I always do.\""
    "\"They speak of 'protection' and 'safety'. But from what? The world outside? Or something within me?\""
    "\"Uncle Lysander visited today. He brought me the most enchanting gift, a moonstone necklace.\""
    "\"It's as if he captured the very essence of the moon and hung it around my neck.\""
    "\"When I wear it, I feel a strange sense of peace, like a gentle embrace from the spirits that visit me.\""
    "\"He seemed serious, though, like he often does these days. I sometimes wonder what's troubling him.\""
    "\"But for now, I shall keep this necklace close; it feels like a part of me.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"October 23rd\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"Another visit from Dr. Whitman today.\""
    "\"His probing questions, that insistent look in his eyes, as if trying to unlock the secrets of my very soul.\""
    "\"Does he not realize the confusion he brings? Sometimes, in the depths of the night, I feel as though I'm not alone in my thoughts.\""
    "\"Whispers that are not mine, feelings foreign to me. Is this the 'condition' he speaks of?\""
    "\"Why won't he just tell me plainly?\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"May 15th\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"Father O'Malley came by again with his incense and prayers. The pungent smoke fills the air, and his chants seem to weave a spell around me.\""
    "\"I can't shake off the feeling that they're trying to exorcise something from within me.\""
    "\"But what? Am I possessed? Is that why I'm trapped within these walls?\""
    "\"We talked about my dreams, the vivid tapestry of experiences that unfold when I close my eyes.\""
    "\"He says I might have a spiritual calling, that I am a bridge between realms. I wonder what that means.\""
    "\"It's strange, but I often feel a sense of duty towards the spirits who visit me, especially my protector.\""
    "\"I wish I could understand what it all means. Father O'Malley said he would consult ancient texts; perhaps they hold answers for me.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"January 2nd\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"Had a terrible dream last night. I was standing by the window, watching children play outside.\""
    "\"And then, another 'me' stood beside, her reflection, not quite mine, her whispers sinister and foreign.\""
    "\"We watched the world together, her envy and anger palpable.\""
    "\"I awoke in a cold sweat, her presence lingering. Is she the reason I'm locked away?\""
    "\"The visits from the spirits are growing more frequent.\""
    "\"I find myself spending hours, lost in conversation with them, understanding the stories of their past lives, the wisdom they share, and the strange worlds they speak of.\""
    "\"It's beautiful, but also overwhelming at times.\""
    "\"The necklace, my constant companion, seems to absorb the intensity, grounding me.\""
    "\"Uncle Lysander never told me where he found it, but it seems to have a power of its own.\""
    "\"It's a mystery, just like everything else in this mansion.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"October 28th\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"I overheard Mother crying last night. Words like \"protection\" and \"dual souls\" reached my ears.\""
    "\"I don't understand. There's just me. Isn't there?\""
    "\"But then, the other dreams, the other thoughts... Are they hers?\""
    "\"Dr. Whitman speaks in riddles and Father O'Malley with his cryptic religious words.\""
    "\"Why does no one speak the truth to me?\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"January 7th\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"The confusion grows. Today, I found a note in my own handwriting, but I have no recollection of penning it.\""
    "\"It spoke of a desire to venture outside, to feel the sun, and to be free.\""
    "\"But it also spoke of anger, a rage against my parents for this imprisonment.\""
    "\"I don't remember such strong feelings.\""
    "\"Or did 'she' write it? I'm lost in a maze of emotions and memories, some mine, some... someone else's.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_journalentries_stop

    "\"July 3rd\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Dear Journal,\""
    "\"Today, I caught a glimpse of a girl in the mirror, her visage similar yet different, her eyes filled with a defiant fire.\""
    "\"She whispered, \"Soon, Arabella. Soon.\"\""
    "\"I screamed, shattering the reflection. But was I screaming at her?\""
    "\"Or at the revelations of my own fragmented self?\""

    jump arabella_journalentries_stop

label arabella_motherjournal_end:
    "Looking through the journal almost feels like an invasion of privacy, but it feels important."
    "You decide to take the journal anyway, the book radiating with pain, fear, and love."
    "You notice the light in the room hitting something shiny on one of the shelves on the bookcase."
    "It looks to be an old, intricate-looking key. It’s cool to the touch."
    "You decide to take it with you."
    $ q3_mom_journal = True
    jump elizabeth_convohub



label arabella_motherjournal:

    "You approach the bookcase, fingers trailing over the spines of the books."
    "Some are aged and worn by time. Others look as if they've scarcely been touched."
    "Each book tells its own story, even before its pages are turned."
    "Tales of adventure, thick volumes of philosophy, romantic poetry, and ancient lore."
    "As you investigate further into the collection, one particular, seemingly hand-bound book catches your attention."
    "It doesn't possess the grandeur of the others."
    "In fact, it's relatively plain, bound in soft, worn leather that has seen better days."
    "However, the lack of a title or author gives it an air of mystery."

    "You pull it from the shelf, weighing it in your hands."
    "It feels heavy, not just with the weight of the paper but with the weight of memories."

    "An emblem of a phoenix was embossed on its cover, signaling its significance."

    "Carefully opening the book, it reveals that it's not a published work."
    "Rather, it's a journal, filled with neat and beautiful handwriting."
    "The inked pages within tell tales of dreams, fears, and heartaches."
    "It chronicles the love Arabella’s parents had for her, their fervent hopes, their torment, and their desperation."
    "Through their words, they paint a vivid image of a daughter, born with an ethereal beauty and an enigmatic mind."
    "A daughter they loved deeply and wished to protect from the harsh judgments of the world."

    "Tears stain some of the pages, and the handwriting occasionally becomes erratic, betraying the overwhelming emotions the author felt."

    menu:
        "Read through the journal carefully.":
            jump arabella_motherjournalentries

        "Take the journal without looking through it.":
            jump arabella_motherjournal_end



label arabella_motherjournalentries:

    "\"17th March\""
    $ q3_entry_count = q3_entry_count + 1
    "\"The weight of motherhood is often wrapped in layers of love, fear, and hope.\""
    "\"Watching Arabella today, her eyes glistening with the dreams of the world outside, I am torn.\""
    "\"The mansion has been her sanctuary, but at what cost? Her laughter fills these halls, but so does her sorrow.\""
    "\"I sometimes wonder if Lysander understands the depth of the decisions we've made for our precious daughter.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_motherjournal_end


    "\"25th April\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Arabella's condition wanes and waxes like the phases of the moon.\""
    "\"Doctor Whitman speaks of methods and medicines, yet I see the same uncertainty in his eyes that I feel in my heart.\""
    "\"Lysander mentioned seeking alternative solutions, but his words were veiled.\""
    "\"I know my brother; he carries a weight, a secret.\""
    "\"For Arabella's sake, I hope his intentions are pure.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_motherjournal_end

    "\"9th June\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Today, Arabella spoke of shadows and whispers.\""
    "\"The world she sees, the one hidden from our eyes, becomes more vivid to her each day.\""
    "\"She draws, writes, and often, I find her lost in a distant gaze.\""
    "\"While the mansion's walls protect her from external harm, I fear they might also be her cage.\""
    "\"A cage of our making.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_motherjournal_end

    "\"30th August\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Lysander brought Arabella a beautiful necklace with a moonstone pendant.\""
    "\"She was elated, her joy lighting up the room.\""
    "\"Yet, as I watched them, a chill ran down my spine.\""
    "\"The way the stone glimmered, it seemed... alive.\""
    "\"Lysander whispered to me that it was meant to protect her, but from what?\""
    "\"And at what cost?\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_motherjournal_end

    "\"15th October\""
    $ q3_entry_count = q3_entry_count + 1
    "\"I found Arabella in the main foyer today, her eyes lost in the patterns of the tiles.\""
    "\"She spoke of connections, of threads that bind us, of choices and echoes.\""
    "\"Her words were a tapestry of past, present, and future.\""
    "\"My heart aches to think that our choices might have bound her spirit in ways we cannot fathom.\""
    "\"I pray for guidance, for a sign that we've chosen the right path for our dear Arabella.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_motherjournal_end

    "\"27th March\""
    $ q3_entry_count = q3_entry_count + 1
    "\"My child…\""
    "\"My pride…\""
    "\"She’s…\""
    "\"Why did this…\""

    "The journal ends here."
    jump arabella_motherjournal_end

label arabella_doctorjournal_end:
    "You stow away the notes to show Arabella later."

    $ q3_doctor_journal = True
    jump herman_convohub


label arabella_doctorjournal:
    "You  look around the lounge and stumble upon a leather-bound folder."
    "It feels slightly out of place, contrasting with the dusty and untouched surroundings."
    "You carefully open the folder, revealing a series of neatly typed notes, each bearing a distinct emblem:"
    "A snake encircling a staff, the symbol for medicine."

    menu:
        "Skimming through, you realize that these were medical notes."
        "Read through the notes carefully.":
            jump arabella_doctorjournalentries

        "Take the notes without looking through it.":
            jump arabella_doctorjournal_end

label arabella_doctorjournalentries:

    "\"Date: 5th July, 1851\""
    "\"Subject: Kingsley, Arabella, Age 8\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"First examination today. Arabella is a bright-eyed young girl, who exhibits curiosity about the world around her.\""
    "\"She frequently mentions having 'friends' that others cannot see and speaks with them regularly.\""

    "\"Recommendations:\""
    "\"Continue observation. Encourage social interactions with children her age with the parents.\""
    "\"This may help distinguish between typical childhood imagination and potential hallucinations.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Date: 12th February, 1854\""
    "\"Subject: Kingsley, Arabella, Age 11\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Arabella continues to mention her 'friends' who are invisible to others.\""
    "\"She seems to have deep conversations with them, often seeking advice.\""
    "\"Displays signs of schizoid tendencies, often preferring the company of her unseen companions over real-life interactions.\""

    "\"Recommendations:\""
    "\"Consider controlled social interactions.\""
    "\"Encourage artistic expressions like drawing or writing to help Arabella communicate her feelings and experiences.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Visit on March 7th, 1855\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations: Met Arabella for a detailed examination.\""
    "\"Remarkable anxiety and a hint of paranoia were evident.\""
    "\"She appears reticent and seems to want to avoid social interactions.\""
    "\"Arabella speaks of 'whispers' she hears when in solitude.\""
    "\"Though initially deemed as auditory hallucinations, her insistence on them being internal thoughts is puzzling.\""
    "\"Early signs of a split in her consciousness.\""

    "\"Recommendations: Schedule fortnightly visits to further evaluate her state and get to the root of her apprehensions.\""
    "\"Symptoms might be related to the early stages of severe hysteria.\""
    "\"Delve deeper into these auditory experiences.\""
    "\"Treatments could involve mild sedatives or tonics known to calm nerves and hysteria.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Date: 22nd May, 1856\""
    "\"Subject: Kingsley, Arabella, Age 13\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations: Arabella produced a journal with alternating handwriting styles, indicative of her shifting personalities.\""
    "\"Distinctly, two personas seem to be manifesting, with Arabella unaware of the entries by her secondary self.\""

    "\"Recommendations: Consider treatments such as rest cures or even hydrotherapy.\""
    "\"The idea is to reset her nervous system and calm the aggressive episodes.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Visit on July 15th, 1856\""

    "\"Observations:\""
    "\"Arabella's art has taken a darker turn.\""
    "\"She draws elaborate patterns, symbols, and frequently sketches an ornate necklace with a moonstone pendant.\""
    "\"When questioned, she mentions her Uncle Lysander gifting it to her for protection.\""
    "\"Arabella's shifts in her personalities have become alarmingly fluid.\""
    "\"There's a mention of confrontations with her own reflection, perceiving it as another entity.\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Recommendations:\""
    "\"Investigate the necklace further.\""
    "\"If it is indeed influencing her, understanding its origin might provide insights into Arabella's current state.\""
    "\"Introduce music therapy as a means to ground her in reality.\""
    "\"Consider isolating her from stimuli that might trigger these shifts, including mirrors.\""
    "\"Perhaps a short-term stay in a sanatorium for better observation and controlled treatment.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Date: 23rd October, 1859\""
    "\"Subject: Kingsley, Arabella, Age 16\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Arabella's interaction with her unseen friends has intensified.\""
    "\"She speaks of a particular spirit, one that protects and guides her.\""
    "\"Physical health remains stable, but her mental state wavers, particularly during full moons.\""
    "\"Arabella's mental state is becoming increasingly unstable.\""
    "\"The episodes where she loses herself to this secondary persona are now more frequent, leaving her disoriented and distressed.\""

    "\"Recommendations:\""
    "\"Seek spiritual guidance.\""
    "\"This could be a manifestation of her condition.\""
    "\"Continue with art therapy and introduce calming activities like meditation.\""
    "\"Engage in frequent therapy sessions, including calming techniques practiced by fellow physicians for severe hysteria cases.\""
    "\"If conditions worsen, consider long-term sanatorium care.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_doctorjournal_end

    "\"Date: 29th August, 1862\""
    "\"Subject: Kingsley, Arabella, Age 19\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Arabella's condition remains static, but her bond with her 'protector' spirit is profound, almost symbiotic.\""
    "\"She expresses feelings of responsibility towards this spirit and often speaks of obligations she must fulfill.\""
    "\"Arabella's condition seems resistant to current treatments.\""
    "\"The dominance of this secondary personality is concerning, with her becoming unpredictable and at times hostile.\""

    "\"Recommendations:\""
    "\"Family should be counseled about Arabella's deepening connection with her unseen friends.\""
    "\"Investigate any significant events in her life that may be influencing her current state.\""
    "\"Continue therapy sessions and consider introducing herbal remedies to calm her mind.\""
    "\"Strongly advise admitting her to a specialized sanatorium.\""
    "\"There, she can be under constant supervision.\""
    "\"Emerging treatments might aid her severe hysteria and schizophrenia-like symptoms.\""

    "Thus ends the doctor's notes."
    jump arabella_doctorjournal_end

label arabella_priestjournal_end:
    $ q3_priest_journal = True
    "You decide to bring the folder with you, feeling that it may be important."
    jump aures_convohub



label arabella_priestjournal:

    "As you explore the ballroom, your eyes are drawn to the back of an ornate cabinet."
    "Tucked amid a collection of dusty bottles and tarnished silverware, an intricate lockbox captures your attention."
    "It's not made of the mahogany that adorns so much of the mansion."
    "Rather, it is of dark, aged iron with swirling silver inlays that seem to shimmer even in the low light."
    "The design is complex and captivating."
    "Elaborate vines intertwined with what appear to be celestial symbols: moons, stars, and curious geometric shapes."
    "It's almost as if the patterns are in motion, spiraling inwards toward the lock."
    "The intricacies stand in stark contrast to the box itself, is disarmingly simple:"
    $ q3_keyneeded = True
    menu:
        "A small keyhole framed by a circle of unadorned iron."

        "Use the key you found in the living room." if q3_mom_journal:
            jump arabella_priestjournal_open

        "Leave the lockbox alone for now.":
            jump aures_convohub


label arabella_priestjournal_open:

    "At the bottom of the lockbox, nestled between a worn-out bible and a crucifix, lay a folder."
    "It houses a set of weathered notes, their pages yellowed by time but bound neatly in twine."
    "The handwriting is elegant, the ink faded but still legible, hinting at the diligence and care of its scribe."


    menu:
        "You unfold the first note, catching the emblem of a cross at its header and the name \"Father O'Malley\" signed at the bottom."
        "Read through the notes carefully.":
            jump arabella_priestjournalentries

        "Take the notes without looking through it.":
            jump arabella_priestjournal_end


label arabella_priestjournalentries:

    "\"Date: 9th April, 1852\""
    "\"Subject: Arabella, Age 9\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Today, I had the chance to meet young Arabella.\""
    "\"She possesses a vibrant spirit, one that seems to resonate on a frequency most of us cannot comprehend.\""
    "\"She speaks of 'friends' not visible to us, entities she believes are guiding her.\""

    "\"Reflections:\""
    "\"It's not uncommon for children to perceive the spiritual realm with a clarity that eludes adults.\""
    "\"However, guidance and grounding in faith might help Arabella distinguish between benign spiritual interactions and those that could lead her astray.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_priestjournal_end

    "\"Date: 16th June, 1855\""
    "\"Subject: Arabella, Age 12\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Arabella's spiritual sensitivity has deepened.\""
    "\"She mentions beings who whisper wisdom from bygone eras, and her recounting of these tales is both fascinating and eerie.\""
    "\"She holds particular reverence for one entity, considering it a protector.\""

    "\"Reflections:\""
    "\"There's an ancient belief that some souls are chosen as bridges between the mortal realm and the spiritual one.\""
    "\"Arabella may be one such soul. It's crucial to teach her prayers of protection and guide her spiritual interactions.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_priestjournal_end

    "\"Date: 18th July, 1856\""
    "\"Subject: Arabella, Age 13\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Arabella's drawings depict spiritual symbols and a necklace.\""
    "\"She says it's a gift from Uncle Lysander.\""
    "\"I sense a deep spiritual significance behind this necklace, especially with the way Arabella clings to it during our sessions.\""

    "\"Reflections:\""
    "\"Objects can often become anchors or conduits for spiritual energy.\""
    "\"The necklace might be tethering Arabella's spirit in a unique way.\""
    "\"Prayers of clarity and discernment are recommended.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_priestjournal_end

    "\"Date: 27th October, 1860\""
    "\"Subject: Arabella, Age 17\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"Today's session was intense. Arabella's spiritual experiences have heightened.\""
    "\"She speaks of dreams, of conversations with her protector spirit, and the sense of duty she feels towards it.\""

    "\"Reflections:\""
    "\"Arabella might be experiencing a spiritual calling or obligation.\""
    "\"The Church has records of individuals with unique spiritual connections.\""
    "\"I'll consult ancient texts for guidance on how to help Arabella navigate her path.\""

    menu:
        "Keep reading.":
            pass

        "Stop reading.":
            jump arabella_priestjournal_end

    "\"Date: 3rd September, 1863\""
    "\"Subject: Arabella, Age 20\""
    $ q3_entry_count = q3_entry_count + 1
    "\"Observations:\""
    "\"The young woman before me now seems worlds apart from the girl I once knew.\""
    "\"The weight of her spiritual encounters has molded her.\""
    "\"She feels bound to a higher purpose, one tied intricately to her protector spirit.\""

    "\"Reflections:\""
    "\"It's essential for Arabella to find balance.\""
    "\"While her spiritual experiences are profound, she needs grounding in the physical world.\""
    "\"Introducing rituals, meditations, and grounding prayers could help tether her spirit, providing stability and purpose.\""

    "The notes end there."
    jump arabella_priestjournal_end































label arabella_ending:

    $ q3_ending_trigger = True

    "You step into the foyer and let it swallow you once more."
    "The air in the foyer is thick with anticipation."
    "The gentle glow of the chandeliers cast a golden light, accentuating the intricate designs of the walls, the elaborate staircase, and the vast portraits of ancestors long gone."
    "The mansion seems to breathe with a mix of tension and hope, awaiting a resolution."
    "You stand in the center of the grand foyer, recounting the items you've discovered:"
    "Evanegline's journal, the notes from Doctor Whitman, Father O'Malley's observations, Arabella's own journal, and the moonstone pendant."
    "Each object holds a piece of Arabella's story, a fragment of her past that could potentially guide her toward the peace she so desperately seeks."
    show arabella neutral
    with dissolve
    "As if summoned by the gravity of the moment, Arabella's ethereal form emerges from the shadows."
    "Her flowing gown seems to glow in the dim light, and her eyes, filled with a mixture of hope and apprehension, are fixed on you."
    "The atmosphere is electric, charged with emotions."
    "Arabella's voice trembles, betraying her anxiety."
    show arabella determined
    voice "arq3-23"
    ar "Have you... found the answers I sought?"
    "You take a deep breath, piecing the narrative together from the collected items."
    "You hand over the notes and the journal that you found to Arabella, and from them you see an envelope fall out."
    "As you pick it up, you see that the front of it says, in a very familiar handwriting 'My Dearest Belle, To Be Opened On Your 21st Birthday.'"
    "It looks like a letter from Evangeline, and you wonder for a moment what could be in it."
    if q3_entry_count >= 18:
        "She hesitates for a moment before opening the documents. Her brows furrow, her eyes widening as she reads further on."
        "Arabella gasps in shock."
        voice "arq3-24"
        ar "What...? This is...?"
        mc "This is the truth you were seeking."
        "Disbelief fills her shaking voice."
        voice "arq3-25"
        ar "But... If what these say is true..."
        mc "You were never possessed by a demon, but even the doctors didn't really have a real idea of what was happening or what they could do."
        mc "I don't fully understand it myself, but from what I could gather, you had some sort of a schizoid disorder that caused... how did the doctor put it...?"
        "Arabella, not lifting her eyes off of the pages, whispers:"
        voice "arq3-26"
        ar "A split in my conscious...?"
        mc "I believe that's where the voices came from that you were adamant were 'unseen friends' or the 'protective spirits' you believe you had."
        mc "Your parents only did what they thought was best with the information that they had at the time."
        if q3_lysander_convo:
            mc "Even your Uncle Lysander, he—"
            "Arabella's head snaps up and looks at you, disbelief written on her face."
            show arabella melancholic
            voice "arq3-27"
            ar "Uncle Lysander...? What of him...?"
            mc "He told me a bit of the pendant that he gave you..."
            voice "arq3-28"
            ar "My... my pendant...? He... never told me where it came from... It felt... powerful though..."
            mc "He wouldn't tell me much about it, but from what he told me, it was crafted a long time ago by someone who was skilled in protective magic, and he gave it to you to protect you from... evil forces..."
            mc "He said that the pendant's power can run out, but he refused to tell me any more than that."
        "She looks down at the ground, an emotion that you can't describe crossing her face. It feels… melancholy..."
        show arabella melancholic
        voice "arq3-28"
        ar "I... I see..."
        mc "So you see, everyone was only doing the best they could with the information they had available to them at the time to try to give you the best life they possibly could."
        "Arabella only nods in acknowledgment of your words."
        "She takes her mother's journal and opens it up."
        "She reads the words on the page for what seems like forever before closing it and opening the journal you found in the living room."
        "As she reads, her confusion turns into something you can't place… Sadness and pain mixed with… affliction?"
        "Arabella doesn't say anything, but she closes the journal and holds it close to her chest and closes her eyes, tears starting to well up, threatening to spill over."
        "You can see her shoulders shaking. She seems to be stifling a sob."
        $ q3_ending_points= q3_ending_points + 1
    else:
        "You tell Arabella that you didn't manage to find much information that you could understand, but you tell her that anything she needs to know is more than likely in the folders and the journals that you found."
        "Arabella looks a little confused, but opens one of the folders and begins reading it."
        "She reads the words on the page for what seems like forever before closing it and opening the journal you found in the living room."
        "As she reads, her confusion turns into something you can't place... Sadness and pain mixed with… affliction?"
        "Arabella doesn't say anything, but she closes the journal and holds it close to her chest and closes her eyes, tears starting to well up, threatening to spill over."
        "You can see her shoulders shaking. She seems to be stifling a sob."
    if q3_pendant_keep:
        "You offer her the pendant, and gently she takes it from your hand."
        "Arabella holds the pendant, her fingers caressing the moonstone."
        "The soft luminescence of the stone seems to pulse, resonating with her heartbeat."
        $ q3_ending_points = q3_ending_points + 1
    mc "You can choose to forgive, to understand that those around you acted out of love, even if their choices were sometimes misguided."
    mc "You can ponder upon this, seeking your own path to forgiveness in time, or you can decide not to forgive, holding onto the memories as they are."
    mc "At the end of the day, the choice is your own, Arabella..."
    "She closes her eyes for a moment, drawing a deep, ethereal breath."
    "When she finally opens her eyes, her expression is that of one you can't seem to place, leaving you wondering about the path she's chosen."
    if q3_ending_points >= 2:
        "You hold out the letter to Arabella. She stares at it for what feels like forever, before slowly and hesitantly taking it."
        "As she goes to open it, she looks up at you, with a look that seems to be asking for...  reassurance, perhaps?"
        "You nod your head to her, and she slowly and carefully takes the letter out of the envelope, and as she reads it, tears flood from her eyes."
        "She covers her mouth with her hand, attempting to stifle her sobs."
        "When she’s finally composed herself, her hand drops to her side."
        "She sets the letter on a nearby table. She quickly composes herself and turns to you."
        "The mansion seems to glow, a warmth spreading through its halls as if, it too, was part of this cathartic moment."
        "When she starts to speak, her voice is soft but clear..."
        show arabella regal
        voice "arq3-30"
        ar "I... understand now... The intentions behind their actions, the love, the fear, the hope... It's… a lot to process, but... I choose… to forgive."
        voice "arq3-31"
        "It's time to find my peace. From the bottom of my heart, I thank you."
        "Arabella gives you a warm, heartfelt smile. The joy can be felt through her unshed tears."
        voice "arq3-32"
        ar "The help that you've provided in my time of need will forever mean a great deal to me... I will never forget what you've done for me here."
        $ q3_state = 4

    elif q3_ending_points == 1:
        "You hold out the letter to Arabella. She stares at it for what feels like forever, before slowly and hesitantly taking it."
        "She continues to stare at the letter, seemingly at war with herself."
        "Does she not want to open the letter?"
        "Reluctantly, she sets the letter gently on a nearby table."
        "She keeps her hand close to it, though, as she turns to look at you."
        "The ambiance remains unchanged, but there is a sense of respect for Arabella's need for introspection."
        "When she starts to speak, her voice is soft but clear..."
        show arabella contemplative
        voice "arq3-33"
        ar "I... I need time… Time to think, to understand, to come to terms with everything… I'm not sure where this path will lead, but I appreciate the clarity you've provided."
        "Arabella gives you a warm, meaningful smile."
        voice "arq3-34"
        ar "You've truly been a great help to me in my time of need... And for that, I thank you."
        $ q3_state = 3

    else:
        "You hold out the letter to Arabella. She stares at it for what feels like forever, before slowly and hesitantly taking it."
        "She stares harshly at the letter, before tossing it over to a nearby table, turning her back to it. She looks over at you."
        "A shadow seems to pass through the mansion, a reflection of Arabella's unresolved emotions."
        "When she starts to speak, her voice is soft but clear..."
        show arabella melancholic
        voice "arq3-35"
        ar "The pain runs far too deep, the feelings of betrayal still sting… I… I cannot forgive, not now… Not yet... Perhaps not ever... I'm... I'm sorry..."
        "Arabella turns her back to you. The raw pain she emits is thick, almost suffocating."
        voice "arq3-36"
        ar "Thank you for trying to help me... I will not soon forget your kind gesture..."
        "You nod, respecting Arabella's choice."
        "You've done your part, presenting the truths of the past to a soul in turmoil."
        "Now, the journey ahead is Arabella's to take, at her own pace, and in her own time."
        "The mansion, with its walls steeped in history and memories, stands as a silent witness, holding space for Arabella's path toward resolution or perpetual search."
        $ q3_state = 2

    hide arabella
    with dissolve

    "You spot something on a table in the foyer."
    "You recognize it as the letter that fell out of Evangeline's journal."
    "You carefully pick up the letter and decide to read it."
    "What you find written in it... was far from what you were expecting..."
    "\"To my dearest Belle, on your 21st birthday,\""
    "\"My beautiful daughter, as I pen these words, my heart swells with immeasurable pride and love.\""
    "\"It is almost impossible for me to fathom that you are now the fine, accomplished woman who reads this letter.\""
    "\"Time has always had a peculiar way of betraying my senses, making moments feel like eternities and years like fleeting moments.\""
    "\"I have watched you bloom within these walls, nurtured by the love and care of all who adore you.\""
    "\"Your gentle spirit, the sweetness of your laughter, the kindness in your actions.\""
    "\"All of it makes it evident that you are a remarkable woman, and your father, Dr. Whitman, Uncle Lysander, and I are endlessly proud of you.\""
    "\"My dear, there has been a secret, a burden we have carried, always with the best of intentions.\""
    "\"It is a secret that we believed you should know only when you were ready.\""
    "\"And now, as you step into the world of adulthood, it is time you understand the truth behind the walls that have seemingly imprisoned you.\""
    "\"Your unique nature, my love, has always been a concern for us. Not because we ever viewed it as a flaw, but because the world outside is less understanding.\""
    "\"Our fear has always been that if your condition became widely known, if outsiders were to misunderstand and perceive it as some manner of possession or curse, they would take you away from us.\""
    "\"In our time, there are places — dark, cold sanitariums — where they would lock away a soul like yours. Such a fate is a death in itself, and we could never bear to see you endure it.\""
    "\"All we ever wished for was to provide you with a life filled with happiness, free from harm, pain, and prejudice.\""
    "\"And in doing so, we decided that it was best for you to remain within the safety of our home, surrounded by those who understand and love you unconditionally.\""
    "\"Our decisions might have seemed oppressive, and for that, I apologize with all my heart. But know this — every choice, every action, was made from a place of deepest love.\""
    "\"We wanted to shield you, protect you, and above all, ensure that your radiant spirit was never extinguished by the cruelty and ignorance of the world.\""
    "\"I hope, my dearest Belle, that as you read these words, you understand the heartache, the concern, and the profound love behind our actions.\""
    "\"And I pray that you carry forth in life with the knowledge that you were, and always will be, our most precious gift.\""
    "\"With all the love a mother could hold,\""
    "\"Evangeline\""
    "You put the letter back down."

    jump arabella_reflection
