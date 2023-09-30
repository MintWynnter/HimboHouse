

define un = Character('???')
define mc = Character('You')
define ar = Character('Arabella')

q3_entry_count = 0
q3_priest_journal = false
q3_mom_journal = false
q3_doctor_journal = false
q3_own_journal = false
q3_lysander_convo = false
q3_pendant_encounter = false
q3_pendant_keep = false
q3_state = 0
q3_ending_trigger = false
q3_death_convo_trigger = false
q3_ending_points = 0

q5_state = 0

label foyer_hub:

    # Arabella introduction



    if q3_state == 0
        "A soft, whispery voice calls out from somewhere nearby."
        voice "voice/arq3-01.ogg"
        un "Who are you?”
    
        menu:
            "Politely respond.":
                "Drawing all of your courage, you ask softly back:" 
                mc "Who are you?" 
                "You look around, trying to pinpoint the source of the voice. In the corner of your eye, you see a figure emerge from the shadows." 
                "In the corner of the dimly lit foyer, a breathtaking apparition materializes, captivating yet paralyzing you with her ethereal presence. As a ghostly specter, she emanates an otherworldly beauty." 
                "As she stands in the corner, bathed in the soft, ambient glow, she radiates an undeniable grace and longing." 
                "The apparition's gaze rests upon you, as if in anticipation of your next move." 
                "You take a hesitant step forward, captivated by her beauty yet terrified of the unknown."
                "The apparition smiles sadly at you and the corner of her lips turns upwards, revealing a hint of warmth in the depths of her ghostly eyes." 
                "She speaks softly, gazing around the room with a melancholic expression on her face."
                ar "My name is Arabella. I lived in this home with my mother and father, but my life ended here many years ago."
                ar "This house holds many secrets and much sadness... I cannot help but wonder if it will ever be free from its shackles."
                "You ask her gently:" 
                mc "Why are you here? Are you not able to leave?"
                "Arabella sighs softly and it sounds almost like a whisper."
                ar "I am bound to this house. It was my prison while I lived, and it is now my prison after death."
                ar "My parents believed me to be cursed or possessed; never allowing me to step outside these walls." 
                mc "I see…"
                "You gaze at her in sympathy, knowing that she will never find peace as long as the secrets of the house remain untold." 
                "Suddenly, an idea dawns on you, one that could potentially break the bonds of her eternal solitude and offer Arabella freedom at last."
                "You take a deep breath before speaking, hoping with each word that your plan will succeed and that Arabella will soon be free from her chains."
                mc "I don't know how to help, or what it will cost, but I want to help you. If there is anything I can do, whatever it takes, I will help you be freed of your past."
                "She looks at you for a few moments, and then speaks slowly and softly." 
                "Her voice carries a subtle glimmer of hope, one that she has perhaps been holding on to for many years."
                ar "If you are willing, I accept your offer." 
                "Arabella closes her eyes and takes a deep breath, steeling herself for what is to come next."
                jump q3_intro_2
            "Be direct.":
                "Drawing all of your courage, you ask softly back:"
                mc "Who are you?" 
                "You look around, trying to pinpoint the source of the voice." 
                "In the corner of your eye, you see a figure emerge from the shadows." 
                "In the corner of the dimly lit foyer, a breathtaking apparition materializes, captivating yet paralyzing you with her ethereal presence. As a ghostly specter, she emanates an otherworldly beauty." 
                "As she stands in the corner, bathed in the soft, ambient glow, she radiates an undeniable grace and longing. The apparition's gaze rests upon you, as if in anticipation of your next move."
                "You take a hesitant step forward, captivated by her beauty yet terrified of the unknown."
                mc "Why are you haunting this house?"
                "The specter is taken a bit back by your sudden hostility." 
                "She sighs softly and it sounds almost like a whisper.""
                "Speaking softly, she gazes around the room with a melancholic expression on her face."
                ar "M-my name is Arabella. I lived in this home with my mother and father, but my life ended here many years ago." 
                "She hesitates." 
                ar "I… I am bound to this house. It was my prison while I lived, and it is now my prison after death."
                ar "My parents believed me to be cursed or possessed; never allowing me to step outside these walls." 
                you "I see…" 
                "You take a deep breath before speaking, hoping with each word that your plan will succeed and that Arabella will soon be free from her chains." 
                mc "I don't know how to help, or what it will cost, but I want to help you. If there is anything I can do, whatever it takes, I will help you be freed of your past."
                "She looks at you hesitantly for a few moments, and then speaks slowly and softly." 
                "Her voice carries a subtle glimmer of hope, one that she has perhaps been holding on to for many years:"
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
            ar "I need to know the truth. Why did my parents confine me here? Why wasn't I allowed to leave, to live life like everyone else? What did I do wrong for them to keep me locked away?"
            menu:
                "Accept.":
                    mc "Of course, Arabella. Let's uncover the truth together. Where should we start?"
                    ar "Well, let's see… I'm sure that my parents might have kept some kind of journal or something of the sort."
                    ar "There may be some notes from the various doctors and priests who came through and examined me throughout my life."
                    ar "Mother spent a lot of time reading and writing in the living room, while Father spent a lot of time entertaining guests in the lounge." 
                    ar "I don't have a lot of memories from when I was alive, so it's possible that I may have also kept a journal as well."
                    mc "I see… That gives me a few places I could start looking; the living room, the lounge, and your room, at the very least…"
                    mc "Thank you, Arabella. I will get started as soon as possible."
                    ar "You are most welcome, dear friend… Remember, Mother enjoyed Phoenix's and was always the protector of Father's most well-kept secrets."
                    "She goes to turn, before exclaiming and whipping back towards you."
                    ar "Oh! Before you go, a word of caution… If you are going to the lounge…" 
                    ar "Watch out for Herman, if you have not run into him already…" 
                    ar "He's a bit of a… snake, if you catch my meaning…"
                    $ q3_state = 1
                    jump q3_true_hub
                "Pry for more information.":
                    mc "Before I agree, I need to know more. Why are you trapped here?"
                    ar "I believe it's because I can't forgive my parents.”
                    ar "I don't have many memories, but it's a lingering, overwhelming feeling."                    
                    ar "I believe that the mansion won't let me go until I do."
                    mc "I see… Well, I want to help you the best that I can."
                    mc "Where should I start looking then?"
                    ar "Well, let's see… I'm sure that my parents might have kept some kind of journal or something of the sort."
                    ar "There may be some notes from the various doctors and priests who came through and examined me throughout my life."
                    ar "Mother spent a lot of time reading and writing in the living room, while Father spent a lot of time entertaining guests in the lounge." 
                    ar "I don't have a lot of memories from when I was alive, so it's possible that I may have also kept a journal as well."
                    mc "I see… That gives me a few places I could start looking; the living room, the lounge, and your room, at the very least…"
                    mc "Thank you, Arabella. I will get started as soon as possible."
                    ar "You are most welcome, dear friend… Remember, Mother enjoyed Phoenix's and was always the protector of Father's most well-kept secrets."
                    "She goes to turn, before exclaiming and whipping back towards you:"
                    ar "Oh! Before you go, a word of caution… If you are going to the lounge…"
                    ar "Watch out for Herman, if you have not run into him already…"
                    ar "He's a bit of a… snake, if you catch my meaning…"
                    $ q3_state = 1
                    jump q3_true_hub

# Arabella Ending
    elif q3_priest_journal and q3_mom_journal and q3_doctor_journal and q3_own_journal and q3_pendant_encounter and !q3_ending_trigger:
        "The air in the mansion's grand foyer is thick with anticipation." 
        "The gentle glow of the chandeliers cast a golden light, accentuating the intricate designs of the walls, the elaborate staircase, and the vast portraits of ancestors long gone." 
        "The mansion seems to breathe with a mix of tension and hope, awaiting a resolution."
        "You stand in the center of the grand foyer, recounting the items you've discovered:" 
        "Evanegline's journal, the notes from Doctor Whitman, Father O'Malley's observations, Arabella's own journal, and the moonstone pendant.)
        "Each object holds a piece of Arabella's story, a fragment of her past that could potentially guide her toward the peace she so desperately seeks."
        "As if summoned by the gravity of the moment, Arabella's ethereal form emerges from the shadows."
        "Her flowing gown seems to glow in the dim light, and her eyes, filled with a mixture of hope and apprehension, are fixed on you."
        "The atmosphere is electric, charged with emotions."
        "Arabella's voice trembles, betraying her anxiety."
        ar "Have you... found the answers I sought?" 
        "You take a deep breath, piecing the narrative together from the collected items."
        "You hand over the notes and the journal that you found to Arabella, and from them you see an envelope fall out."
        "As you pick it up, you see that the front of it says, in a very familiar handwriting 'My Dearest Belle, To Be Opened On Your 21st Birthday.'" 
        "It looks like a letter from Evangeline, and you wonder for a moment what could be in it."
        if q3_entry_count >= 18:
            "She hesitates for a moment before opening the documents. Her brows furrow, her eyes widening as she reads further on."
            "Arabella gasps in shock."
            ar "What...? This is...?"
            mc "This is the truth you were seeking."
            "Disbelief fills her shaking voice."
            ar "But... If what these say is true..."
            mc "You were never possessed by a demon, but even the doctors didn't really have a real idea of what was happening or what they could do."
            mc "I don't fully understand it myself, but from what I could gather, you had some sort of a schizoid disorder that caused... how did the doctor put it...?"
            "Arabella, not lifting her eyes off of the pages, whispers:"
            ar "A split in my conscious...?"
            mc "I believe that's where the voices came from that you were adamant were 'unseen friends' or the 'protective spirits' you believe you had."
            mc "Your parents only did what they thought was best with the information that they had at the time."
            if q3_lysander_convo:
                mc "Even your Uncle Lysander, he—"
                "Arabella's head snaps up and looks at you, disbelief written on her face."
                ar "Uncle Lysander...? What of him...?"
                mc "He told me a bit of the pendant that he gave you..."
                ar "My... my pendant...? He... never told me where it came from... It felt... powerful though..."
                mc "He wouldn't tell me much about it, but from what he told me, it was crafted a long time ago by someone who was skilled in protective magic, and he gave it to you to protect you from... evil forces..."
                mc "He said that the pendant's power can run out, but he refused to tell me any more than that."
            "She looks down at the ground, an emotion that you can't describe crossing her face. It feels… melancholy..."
            ar "I... I see..."
            mc "So you see, everyone was only doing the best they could with the information they had available to them at the time to try to give you the best life they possibly could."
            "Arabella only nods in acknowledgment of your words."
            "She takes her mother's journal and opens it up."
            "She reads the words on the page for what seems like forever before closing it and opening the journal you found in the living room."
            "As she reads, her confusion turns into something you can't place… Sadness and pain mixed with… affliction?"
            "Arabella doesn't say anything, but she closes the journal and holds it close to her chest and closes her eyes, tears starting to well up, threatening to spill over."
            "You can see her shoulders shaking. She seems to be stifling a sob."
            q3_ending_points ++
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
            q3_ending_points ++
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
            ar "I... understand now... The intentions behind their actions, the love, the fear, the hope... It's… a lot to process, but... I choose… to forgive. It's time to find my peace. From the bottom of my heart, I thank you.” 
            "Arabella gives you a warm, heartfelt smile. The joy can be felt through her unshed tears."
            ar "The help that you've provided in my time of need will forever mean a great deal to me... I will never forget what you've done for me here." 

        elif q3_ending_points == 1:
            "You hold out the letter to Arabella. She stares at it for what feels like forever, before slowly and hesitantly taking it."
            "She continues to stare at the letter, seemingly at war with herself." 
            "Does she not want to open the letter?"
            "Reluctantly, she sets the letter gently on a nearby table."
            "She keeps her hand close to it, though, as she turns to look at you."
            "The ambiance remains unchanged, but there is a sense of respect for Arabella's need for introspection."
            "When she starts to speak, her voice is soft but clear..."
            ar "I... I need time… Time to think, to understand, to come to terms with everything… I'm not sure where this path will lead, but I appreciate the clarity you've provided."
            "Arabella gives you a warm, meaningful smile."
            ar "You've truly been a great help to me in my time of need... And for that, I thank you." 
        
        else:
            "You hold out the letter to Arabella. She stares at it for what feels like forever, before slowly and hesitantly taking it."
            "She stares harshly at the letter, before tossing it over to a nearby table, turning her back to it. She looks over at you."
            "A shadow seems to pass through the mansion, a reflection of Arabella's unresolved emotions."
            "When she starts to speak, her voice is soft but clear..."
            ar "The pain runs far too deep, the feelings of betrayal still sting… I… I cannot forgive, not now… Not yet... Perhaps not ever... I'm... I'm sorry..." 
            "Arabella turns her back to you. The raw pain she emits is thick, almost suffocating."
            ar "Thank you for trying to help me... I will not soon forget your kind gesture..."
            "You nod, respecting Arabella's choice."
            "You've done your part, presenting the truths of the past to a soul in turmoil."
            "Now, the journey ahead is Arabella's to take, at her own pace, and in her own time." 
            "The mansion, with its walls steeped in history and memories, stands as a silent witness, holding space for Arabella's path toward resolution or perpetual search."

        "You spot something on a table in the foyer."
        "You recognize it as the letter that fell out of Evangeline's journal." 
        "You carefully pick up the letter and decide to read it."
        "What you find written in it... was far from what you were expecting..."
        "To my dearest Belle, on your 21st birthday,"
        "My beautiful daughter, as I pen these words, my heart swells with immeasurable pride and love. It is almost impossible for me to fathom that you are now the fine, accomplished woman who reads this letter." 
        "Time has always had a peculiar way of betraying my senses, making moments feel like eternities and years like fleeting moments."
        "I have watched you bloom within these walls, nurtured by the love and care of all who adore you."
        "Your gentle spirit, the sweetness of your laughter, the kindness in your actions — all of it makes it evident that you are a remarkable woman, and your father, Dr. Whitman, Uncle Lysander, and I are endlessly proud of you."
        "My dear, there has been a secret, a burden we have carried, always with the best of intentions."
        "It is a secret that we believed you should know only when you were ready, and now, as you step into the world of adulthood, it is time you understand the truth behind the walls that have seemingly imprisoned you."
        "Your unique nature, my love, has always been a concern for us. Not because we ever viewed it as a flaw, but because the world outside is less understanding."
        "Our fear has always been that if your condition became widely known, if outsiders were to misunderstand and perceive it as some manner of possession or curse, they would take you away from us."
        "In our time, there are places — dark, cold sanitariums — where they would lock away a soul like yours. Such a fate is a death in itself, and we could never bear to see you endure it."
        "All we ever wished for was to provide you with a life filled with happiness, free from harm, pain, and prejudice. And in doing so, we decided that it was best for you to remain within the safety of our home, surrounded by those who understand and love you unconditionally."
        "Our decisions might have seemed oppressive, and for that, I apologize with all my heart. But know this — every choice, every action, was made from a place of deepest love."
        "We wanted to shield you, protect you, and above all, ensure that your radiant spirit was never extinguished by the cruelty and ignorance of the world."
        "I hope, my dearest Belle, that as you read these words, you understand the heartache, the concern, and the profound love behind our actions."
        "And I pray that you carry forth in life with the knowledge that you were, and always will be, our most precious gift."
        "With all the love a mother could hold,"
        "Evangeline"
        "You put the letter back down, your heart seemingly starting to swell."
        "Had Arabella's story turned out the way it needed to in the end?"
        jump q3_true_hub


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

# Start of Arabella hub
label q3_true_hub:
    ar "Is there anything you want to ask about?"
    if q5_state == 2:
        menu:
            # Elizabeth quest 1
            "Elizabeth":
                ar "Oh, the little girl?"
                ar "I heard her scream... Have you done anything to her?"
                mc "Calm down! I didn't do anything. She was just surprised when I arrived, but I explained everything to her and she stopped."
                ar "She… allowed you to talk with her? It had taken so long… for her to open up to me…"
                mc "Well, she seems to be scared of all of you."
                ar "Well, is that not a good thing? Her mother seemed to do well in instilling in her daughter to not speak to strangers…"
                ar "... I say this as a warning to you… Leave Elizabeth be... Please..."
                ar "Which means, you should stay away."
                mc "Arabella, listen… It's not like I'm trying to get closer to her, or do anything to her… I'm not trying to harm her, I'm just here to run an errand for her... That's all..."
                "Arabella sighs, then turns back at you."
                ar "... What is it that you seek?"
                mc "All I need is a pen and some paper."
                ar "I see... And may I ask what she would want these items for?"
                menu:
                    "Tell her the truth.":
                        mc "She wants to draw a map."
                        "Arabella's face crosses briefly with a look that is mixed of both confusion and concern.."
                        ar "But... why would she...?"
                        ar "I see... I... I understand what is happening..."
                        "Arabella turns and looks intently at you, an intense expression contorts her usually dollish face, one that you've never seen before. It almost seems like... Arabella is no longer herself..."
                        ar "I warn you, if you are trying to get her to tell you where she lives so that you can try to force her back to her home... If you wish to bring that poor child more harm..."
                        mc "Arabella, please listen! I promise you, it's not what you think! It's the other way around! I'm not trying to FORCE her to go home, she WANTS to go home..."
                        ar "I... I do not believe that... You wish to bring her harm! She... she wouldn't lie to me... She tells me only truth... She says... that you lie... that you are not to be trusted, not with me, not with Elizabeth… She... protects us... She... loves us...”
                        mc "Why would I lie to you? If you can't believe me, then please... Ask her yourself..."
                        ar "... You... you swear this to be the truth? She... asked you for your aid? You're only offering a hand to help her at her behest?"
                        mc "I promise you, that's all I'm doing. That seems to be why I'm here, to help."
                        "Arabella looks around for a moment, sighs hard in reluctance, then composes herself into the well-mannered girl you know her to be."
                        "Arabella pulls out a pen and some paper from a drawer on the other side of the foyer. Then she turns once again to face you.""

                    "Ask for the items once more.":
                        mc "I'm sorry, but I'm in a bit of a hurry... Do you know where I can find them?"
                        "Arabella is giving you a look you can't place. It's intimidating, but you try to hold a poker face."
                        "She doesn't speak, doesn't even move. It seems you won't be getting anything out of her this way.""

                    "Lie to her.":
                        mc "She wants to draw something."
                        ar "... Is that so...?"
                        mc "You know... I mean, what do you expect? She's a little girl, and kids get bored easily… Besides, she doesn't exactly have anyone to really play with, especially with the air being so tense with the rest of you and her being really scared..."
                        ar "... I do not believe you..."
                        mc "What else would she need a pen and paper for, then?"
                        ar "To write a letter, perhaps...? To use it to have someone draw a map for her...?"
                        mc "She doesn't even know where she lives!"
                        ar "And are you so sure about this? How are you so sure she doesn't?”
                        "You shift under her gaze, looking away from her briefly, gulping hard."
                        ar "I knew it."
                ar "So... It is you... You are the one to bring her back to her... tragic truth..."
                mc "What... what do you mean?"
                ar "Is it not obvious? A little girl, in a thin jacket... In the middle of winter... seemingly running away from home...?"
                ar "What could possibly drive a child away from the warmth and safety of their home?"
                "Arabella is staring sharply at you."
                "If Elizabeth's glare shows fear and anxiety, Arabella shows you a clear warning and hostility. The way she looks at you, you feel as if you're staring at a different person now."
                ar "I warn you once more... You must leave her be, if you know what's best for everybody... She needs not your help... She... she is safe here..."
                "Arabella shoves the pen and paper at you."
                "You stare at it for a while."
                ar "Please, I beg of you... Just... leave the poor girl be in peace..."
                "You grab the pen and paper and stow them away."

                
                $ q5_state = 3
                $ q5_location = 0
                jump q3_true_hub
            "The mansion's history":
                jump q3_hub_topic_1
            "Arabella's lost memories":
                jump q3_hub_topic_2
            "The mansion's other spirits":
                jump q3_hub_topic_3
            "Arabella's death":
                jump q3_hub_topic_4
            "Leave":
                jump q3_farewell

    elif q5_state == 4 and q5_location == 0:
        menu:
            #Elizabeth quest 2
            "Elizabeth":
                mc "I need to ask you something, It's about the little girl, Elizabeth."
                ar "I'm sorry... but I do not wish to have that conversation with you… I can't...”
                mc "Can you at least hear me out and let me ask my questions, please?"
                ar "Listen to me carefully... I appreciate what you have been doing here, for all of us... With that being said, though, and I believe I have already told you… Please... Elizabeth... Just... Leave her be."
                "Arabella seems to think for a moment, then after a few beats nods in a way that is obviously not directed at you."
                ar "I fear that any information I may or may not have on Elizabeth could be used in... nefarious ways... in ways that will lead to her becoming hurt more than she has already been, in life and in death... So I am sorry, but we cannot help you this time..."
                ar "We - I... I cannot allow that to come to fruition..."
                mc "I'm sure you know what I want to ask… So let me ask you, how are you so sure that the information you have will hurt her?"
                ar "You only wish to help Elizabeth, do you not? And how do you plan to 'help' the poor child? By forcing her to remember one of the single most painful things one can ask another to recall? And for what? To help a child's resolve that she cannot possibly grasp the reality of?"
                ar "I urge you, since you want to know the truth so bad... Take a look at these."
                "Arabella hands you a couple of newspaper clippings."
                "On the first paper you see, it was the exact face of Elizabeth, with slightly longer hair, more lively expressions, and less water dripping from her entire being. Under the picture, a sentence 'HAVE YOU SEEN ME?' printed big on the paper."
                "You take out the second paper. On it, in the middle of crowding police, a picture of a woman in her 30s is seen holding a children's jacket. She was entirely disheveled with dried tears and dark circles under her eyes."
                "—Was last seen going out of the house at 4 p.m., walking towards the bridge. It is reported that there was a slight argument between her and the mother before the time she was last seen. Police are currently investigating—"
                "The third paper, there was no picture this time, only a big headline 'SEARCH CALLED OFF'."
                "—Being discontinued. The reason is insufficient leads or clues regarding the whereabouts of the missing person." 
                "'I hope you're happy and safe, I love you so much, and I'm sorry I can't be a better mother for you,' The mother of the little girl told our editor, a small message we all hope Elizabeth will read." 
                "The family has decided to move away from their residence but will keep close contact with the police. The police will still receive any information regarding the missing Elizabeth—"
                "You read them all carefully. Every gear in your head turning as you process the entire broken messages into one string of story."
                ar "What do you think happened to her?"
                menu:
                    "She fell into a river after running away.":
                        ar "Do you feel her situation to be that simplistic? There had to of been a factoring cause that would've caused her to flee in the first place, do you not agree?”
                        mc "It said she had an argument before leaving home—"
                        ar "If I may be blunt, the situation with Elizabeth and her mother, I can understand to a certain degree. The child's mother, she was not good to her daughter most of the time."
                        ar "Though she won't plainly admit to it, Elizabeth's mother was abusive to the child, maybe not physically, but emotionally, that poor girl had been suffering. That's why she fled in the dead of winter."
                        mc "With all due respect, Arabella, I would have to disagree with you there."
                        mc "I can't imagine nor can I believe that a mother who left a message, hoping it would reach her daughter, begging for her safe return home, would have been mentally abusing her child."
                        ar "And I... cannot fathom a loving mother would force her child to feel that their only option… was to run off in sub-zero temperatures with nowhere to go… then would pack up and leave the home before her child was safely back in her arms... I cannot understand it..."

                    "Her mother killed her and ran away.":
                        ar "No, I do not believe that her mother was the culprit, necessarily, but she was a major factor that led Elizabeth to us."
                        ar "Don't you find it odd though… That the family just up and moved without knowing the whereabouts of their daughter?"
                        ar "If she had returned home, she would have found it completely empty and would have probably succumbed to the same fate..."
                        mc "Now, why would she wish to return if her mother was the cause of her running away in the first place?"
                        ar "It... is a feeling I understand all too well, unfortunately... But... I'm afraid that is not the point I am trying to get across..."
                        mc "But, isn't that the most important point here?"

                    "She got lost and ended up here.":
                        ar "But... she wouldn't have ended up here... had her mother gone searching for her child after they ran off... right?"
                        ar "I cannot understand... a mother that would allow her child to wander alone in such harsh conditions..."
                mc "Are you alright? It's not like you to go based on assumptions like this."
                ar "Hmm? Oh... yes... I'm... I'm alright..."
                "She averts her gaze, now avoiding eye contact with you. Something… doesn't feel right with her. She seems… more paranoid."
                mc "Well, I think we should stick with the facts instead of going off of a hunch or any assumptions. Look, we have the newspaper articles right here, but I don't feel like we have the whole story here."
                ar "What if… the stories had been fabricated? By the mother, the police… anybody… to try to paint the mother in a light that made her stand out to be something that she was not...?"
                ar "If what I believe is to be reality... how... would you be able to help Elizabeth then... without hurting her...?”
                menu:
                    "I will still tell her the truth.":
                        ar "No... the truth will only hurt her... There has to be another way to go about this..."
                        mc "You can't expect to have her sheltered from the truth for the rest of eternity, can you?"
                        ar "..."
                        mc "Think of it like this... Would things have been better for you had your mother, your father, or even your Uncle Lysander just told you the truth about your situation, instead of leaving you to feel like Elizabeth is probably feeling right now? Left to be confused and in the dark about everything?"
                        "Arabella's eyes well up with tears. You see it in her face, in her eyes, that you seem to have gotten through to her. She doesn't look at you. Her resolve seems to have shattered."

                    "I won't show her this, it's too much for her.":
                        mc "I... I don't know what the best decision is here... I still fully believe that Elizath deserves to know the truth, but... maybe... not the entire truth. I think you're right, it might be too much for her to handle fully. It's a lot to try to process, but for a child... I can't imagine..."
                        "Arabella seems to visibly relax, but only slightly. She doesn't answer you, but she gives you the smallest nod in acknowledgment."

                    "Maybe it's better for her to stay here.":
                        mc "Maybe you're right... She may be better off staying here, at least for the time being. We don't have the full story, anyway. So, it doesn't make sense to send her off on her own without knowing everything."
                        mc "I want to ask her about what she knows, about what she remembers, then we can go from there..."
                        "Arabella sighs in obvious relief and visibly relaxes, as if a huge weight had been lifted off of her shoulders. She doesn't answer you, but she gives a small smile beaming with contentedness."

                ar "Do you think she will be okay with that?"
                menu:
                    "She deserves the truth.":
                        ar "You're just pushing your own righteousness onto others."
                    "I won't tell her, it's too cruel.":
                        ar "Welcome to the family then, you're carrying this secret to your grave or her eternity."
                        mc "All of you have been keeping this from her all this time?"
                        "Arabella doesn't answer."

                    "...I have to think this through some more.":
                        ar "The answer is clear, but you're still in denial."

                "Holding the newspaper clippings in your hand, you sigh deeply, thinking of the choice you're about to make."
                "You shove the papers into your pocket."

                $ q5_state = 5
                jump q3_true_hub

            "The mansion's history":
                jump q3_hub_topic_1
            "Arabella's lost memories":
                jump q3_hub_topic_2
            "The mansion's other spirits":
                jump q3_hub_topic_3
            "Arabella's death":
                jump q3_hub_topic_4
            "Leave":
                jump q3_farewell

label q3_hub_topic_1:
    mc "This mansion seems to hold centuries of history. Can you tell me more about its origins and your connection to it?"
    ar "This mansion, as old as time itself, has been a sanctuary for many families for generations. It has witnessed joyous celebrations and mournful farewells."
    ar "My earliest memories are of playing in these halls, the echo of my laughter juxtaposed against the house's solemn silence."
    ar "Every stone, every tapestry tells a tale, some of which I yearn to remember fully."
    jump q3_true_hub

label q3_hub_topic_2:
    mc "Your need to remember your lost memories is interesting to me. Is there anything you can recall of your life before everything became hazy?"
    ar "There are moments, fleeting like the embers of a dying fire, that I clutch onto."
    ar "I remember a pendant, the scent of roses in the garden, and the shadow of my Uncle Lysander always close by."
    ar "Yet, there's a barrier... like a thick mist... obscuring deeper memories. I often wonder if there's a reason some moments remain veiled."
    jump q3_true_hub

label q3_hub_topic_3:
    mc "You’re not the only other spirit here, are you? Have you encountered others bound to this place?"
    ar "You have a keen sense. Indeed, this mansion is not just my prison. Over the years, I've sensed other souls, each ensnared by their own tales."
    ar "Some are mere whispers, transient and evasive... Others, like Lysander, hold a more dominant presence."
    ar "While our stories differ, our shared fate binds us to this timeless mansion..."
    jump q3_true_hub

label q3_hub_topic_4:
    if !q3_death_convo_trigger:
        mc "Can you tell me, how did you die?"
        ar "... That... is a topic that I would rather not indulge in... Would the truth of my death make a difference on this quest?"
        q3_death_convo_trigger = true
    else:
        "Arabella refuses to speak any more about this."
    jump q3_true_hub


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
