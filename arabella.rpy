

define un = Character('???')
define mc = Character('You')
define ar = Character('Arabella')

q3_entry_count = 0
q3_priest_journal = false
q3_mom_journal = false
q3_doctor_journal = false
q3_own_journal = false
q3_lysander_convo = false
q3_pendant = false
q3_state = 0

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
                    $ q3_state = 2
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
                    $ q3_state = 2
                    jump q3_true_hub

# Greetings upon return
label q3_greetings:
    $ random_greeting = renpy.random.randint(0,4)
    if random_greeting == 0:
        ar "Ah, a familiar face amid these ever-whispering walls. What brings you?"
    if random_greeting == 1:
        ar "Your presence stirs the memories of this mansion. Ready for another journey into the unknown?"
    if random_greeting == 2:
        ar "Every return of yours feels like a step closer to the truth. How shall we proceed?"
    if random_greeting == 3:
        ar "Between these walls, our quest continues. What stories have you come to share?"
    if random_greeting == 4:
        ar "The winds of time seem to pause when you're here. To what mystery shall we attend today?"

# Start of hub
label q3_true_hub:
    ar "Is there anything I can help with?"
    if q5_state == 2:
        menu:
            "Bring up Elizabeth":
                ar "Oh, the little girl?"
                ar "I heard the scream. Did you do anything to her?"
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

                    "Ask for the items once more.":

                    "Lie to her.":

                
                $ q5_state = 3
                $ q5_location = 0
                jump q3_true_hub

    elif q5_state == 4 and q5_location == 0:
        menu:
            "Bring up Elizabeth":


                $ q5_state = 5


