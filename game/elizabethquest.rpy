label elizabeth_livingroom:

    scene bg livingroom
    show fire
    with fade

    #show whatever bg i don't remember the syntax

    if elizabeth_queststate is 5:
        jump elizabeth_finale

    if elizabeth_queststate > 0:
        #play greeting
        jump elizabeth_hub

    if elizabeth_queststate is 0:
        jump elizabeth_intro



label elizabeth_intro:

    "The moment you enter the room, something immediately catches your attention."
    "With the entire mansion freezing and dark, you find warmth and soft light from across the room."
    "A small fire crackles softly from the fireplace. The soft smell of burning wood fills the air with a strange familiar comfort."
    "Someone must be here, then."
    #voice ""
    mc "Excuse me."
    "Your voice echoes in the empty room."
    "You hear no answer. It seems the room is free for you to explore."
    menu:
        "You then take another step forward, and something shuffles from behind the couch."

        "\"Is someone there?\"":
            #voice ""
            mc "Is someone there?"
            "Still no answer."
            "It could be something, or spending some time in this mansion has done something to your imagination."
            "You take another step forward."
            "whoosh"
            "Something flies right past your head."
        "Go and check.":
            "You have been stranded in this mansion, not knowing who you are, or why you were there."
            "You feel like you’ve got nothing else to lose."
            "You take a step forward, ready to face whatever it is hiding from behind the couch."
            "And something flies right past your head."
        "Throw something at the sound.":
            "The closest thing you can reach without tearing your gaze from the couch is a pillow."
            "It won’t hurt, but might serve well as a warning to whatever it is hiding over there."
            "You grab the pillow and immediately throw it to where the sound was coming from."
            "For a second, nothing."
            "The next, the very same pillow flies right past your head."

    "In the midst of trying to process what just happened, a small figure peeks from behind the sofa, face frowning at you."
    "A kid?"
    "A little girl walks out of her hiding spot only to move further away from you."
    "Her footsteps sound like she’s stepped in a puddle and you realize the dripping noise was coming from her."
    #voice ""
    mc "What happened to you?"
    #voice "elq5-01"
    show elizabeth tantrum1 at elizabeth_spot
    el "GO AWAY!"
    #voice ""
    mc "I’m just asking—"
    #voice "elq5-02"
    show elizabeth angry
    el "I will not go with you!"
    #voice ""
    mc "I wasn’t going to take you anywhere, I just wanna look around a bit."
    #voice "elq5-03"
    show elizabeth tantrum2
    el "NO! GO AWAY OR I’LL SCREAM!"
    #voice ""
    mc "Listen—"
    "The little girl screams; a deafening shriek shakes the entire room."
    "Something buzzing in the air, and every object around you shudders and slowly floats in the air."
    "Like a windless storm, you feel an invisible gust swoop at you and push you away. One by one, the floating things fly at you."
    menu:
        "You don’t know what would happen if you let this drag on."

        "\"You need to listen to me first!\"":
            #voice "el_mad1"
            show elizabeth tantrum2
            el "NO!"
            "The storm of whatever ghostly energy she emits rages even harder around us."
            "More objects are floating and flying. In just one second, everything turns to chaos."
            #voice "el_mad2"
            show elizabeth tantrum1
            el "I won't go with you! Go away, you jerk!"
            #voice ""
            mc "Listen, I’m not trying to take you away!"
            "The energy storm rages. The sound of things clattering muffles your scream."
            "Books start flying towards you."
            #voice ""
            mc "I will not hurt you!"
            "Elizabeth screams even louder."
            #voice ""
            mc "I’m here to help!"
            "Your voice can’t reach her anymore."
            #voice ""
            mc "Hey!"
            #voice ""
            show elizabeth angry
            el "..."
            #voice ""
            show elizabeth sad
            el "........."
            "You hear a faint sob."
            "The raging storm around you slowly calms down, all the floating objects start falling to their places."
            "The sobbing is getting louder."
            #voice ""
            show elizabeth sad
            el "....."
            #voice ""
            mc "Are you okay?"
            #voice "elq5-04"
            show elizabeth sad
            el "I’m tired... Please just go away..."
            "The little girl is rubbing her face hard, as if trying to hide her tears from you."
            "You see her small drenched body is shaking. However, she’s still trying to face you, maybe using the last of her strength to face the unknown person suddenly intruding into her space."
            #voice ""
            mc "I’m sorry to scare you, but I really didn’t mean anything bad."
            #voice ""
            mc "I can see that you are a really brave girl. I won’t hurt you—I wanna help."
            #voice ""
            mc "Can you please hear me out?"

        "\"Calm down! I’m not a bad person!\"":
            #voice "el_mad3"
            show elizabeth angry
            el "I don’t believe you!"
            "The energy storm rages. The sound of things clattering is getting louder."
            #voice ""
            mc "I... don’t know how to prove it. But you can decide."
            #voice ""
            mc "I’m here to help you."
            "The little girl raises her gaze."
            #voice ""
            mc "If you need any help, please tell me now. If not, I will leave."
            "The girl fell silent for a moment."
            "One minute, two, three have passed."
            "You decide to leave."
            #voice ""
            mc "Then, I’m sorry for intruding. You can rest easy now; I will leave."
            "As you turn your back on her, you hear a faint voice."
            #voice "el_ner1"
            show elizabeth sad
            el "Wait."
            #voice ""
        "\"What makes you so scared?\"":
            "Elizabeth audible gasp"
            #voice "elq5-05"
            show elizabeth angry
            el "I’m not scared!"
            "The storm around you rages on."
            #voice ""
            mc "You’re not scaring me either, so how about we just talk?"
            "Elizabeth hesitates."
            #voice ""
            mc "If you wanted to hurt me, you could’ve done it when we met. And if I really wanted to kidnap you, I would’ve done that when we met."
            #voice ""
            mc "Since we both didn’t do any of that, let’s just talk."
            #voice ""
            mc "If you agree, can you stop making a mess out of this place?"

    "Slowly, you can feel the storm recede. All the floating things slowly drop to where they sat before."
    "The girl stands still, eyes still looking warily at you."
    #voice ""
    mc "Can we talk now?"
    #voice ""
    show elizabeth sad
    el "..."
    #voice "el_ann1"
    show elizabeth neutral
    el "...Yes."
    #voice ""
    mc "Okay, what’s your name?"
    #voice "elq5-06"
    show elizabeth neutral
    el "Elizabeth..."
    #voice ""
    show elizabeth neutral
    el "Are you really not a bad person?"
    #voice ""
    mc "I don’t think so. I just want to help you."
    #voice "el_mad3"
    show elizabeth angry
    el "You’re not lying to me, are you? Those strange people didn’t send you here to catch me?"
    #voice ""
    mc "Who?"
    #voice ""
    show elizabeth neutral
    el "Those people in another room, they dress and talk all funny."
    #voice ""
    mc "They’re not exactly strange people... "
    #voice "elq5-07"
    show elizabeth neutral
    el "Are you saying they’re ghosts?"
    #voice "elq5-08"
    show elizabeth angry
    el "You’re only saying that to scare me, aren’t you?!"
    #voice ""
    mc "But you’re–"
    #voice ""
    show elizabeth angry
    el "WHAT?"
    "She doesn’t seem to realize that she’s…"
    "Around you, the air starts buzzing again."
    #voice ""
    mc "Alright, I’m sorry, I’m just joking! Don’t get upset."
    #voice ""
    mc "I’m here by myself."
    #voice ""
    mc "In fact, I didn’t know you were here. Heck, I don’t even know how I got here."
    #voice ""
    show elizabeth neutral
    el "Are you lost too, then?"
    #voice ""
    mc "No, I don’t think so—"
    #voice "el_hap1"
    show elizabeth smile
    el "Don’t be shy, you can stay here with me then, this room is safe. They won’t come here."
    #voice ""
    mc "How did you come into this mansion in the first place, drenched like that, do you remember?"
    "Elizabeth shakes her head."
    #voice ""
    show elizabeth neutral
    el "I just... went out to play, and before I realized it, I was here."
    #voice ""
    mc "Uh... Were you out in the rain?"
    #voice ""
    show elizabeth neutral
    el "No, but it was snowing last night."
    #voice "elq5-09"
    show elizabeth sad
    el "Ugh, I don’t even know what time it is. My mom is gonna be really mad if I don’t come home soon."
    #voice ""
    show elizabeth neutral
    el "Can you please help me get out of this mansion?"
    #voice ""
    mc "Well, the front door is not that far from here, but—"
    #voice "el_mad1"
    show elizabeth angry
    el "No, you must help me go out from the back, to the river."
    #voice ""
    mc "What? Why?"
    #voice "elq5-10"
    show elizabeth neutral
    el "That’s... how I came to this mansion, so I figured I can find my way out if I follow it."
    #voice "elq5-11"
    show elizabeth angry
    el "But you have to help me avoid the weird people who stayed here too. If they find me, they won’t let me go."
    #voice ""
    mc "Are they really gonna do that?"
    #voice ""
    show elizabeth sad
    el "Yeah! This one lady told me to stay here with her forever, and there’s this scary uncle upstairs."
    #voice "elq5-12"
    show elizabeth sad
    el "I need to go home; I’m not supposed to be here..."
    #voice ""
    mc "Don’t you know where you live?"
    "Elizabeth shakes her head again."
    #voice ""
    show elizabeth sad
    el "I remember the path but... after looking outside of the window, this place doesn’t look similar to where I lived."
    #voice ""
    mc "How about your mother’s name? Phone number?"
    #voice ""
    show elizabeth sad
    el "No..."
    #voice "elq5-13"
    show elizabeth neutral
    el "But if you get me a pen and paper, I can draw the map."
    #voice ""
    mc "Well, it’s better than nothing at all. Is there a pen and paper in this room?"
    #voice ""
    show elizabeth neutral
    el "I have checked, and no..."
    #voice ""
    show elizabeth smile
    el "But I think you can ask the other adults here."
    #voice "elq5-14"
    show elizabeth neutral
    el "My mom said I must not talk to weird and scary people."
    #voice "elq5-15"
    show elizabeth smile
    el "But I think you’ll be okay. You’re an adult, so they probably won’t kidnap you."
    #voice "elq5-16"
    show elizabeth smile
    el "Can't you look around and find it for me? Oh, but please don’t tell them anything about me!"
    #voice ""
    mc "Alright. A pen and paper, was it?"
    #voice ""
    show elizabeth smile
    el "Yes. But if you can get some colored pencils—"
    #voice ""
    mc "I don’t think I will be able to find them here."
    #voice "el_dis1"
    show elizabeth neutral
    el "...Just the pen, then."
    "It’s not a difficult request. Surely there’s paper and pen somewhere in this mansion."
    menu:
        "But where’s the place that could possibly have those?"
        "\"Do you think I could find them in the lounge?\"" if herman_queststate > 0:
            "You see Elizabeth pale and shudder."
            #voice "elq5-17"
            show elizabeth neutral
            el "Be careful..."

        "\"Do you think I could find them in the foyer?\"":
            "You’re not sure about a pen, but some letters — papers must be delivered there, right?"
            "Elizabeth looks uneasy."
            #voice "elq5-17"
            show elizabeth sad
            el "Be careful..."

        "\"Do you have any idea where I should look?\"":
            show elizabeth neutral
            el "Uuh...."
            "For a second, Elizabeth looks troubled."
            #voice "el_ner2"
            show elizabeth neutral
            el "The ballroom..."
            #voice ""
            mc "Look, a ballroom is a place for dancing, not writing a letter."
            #voice ""
            show elizabeth angry
            el "I know what a ballroom is!"
            #voice "elq5-18"
            show elizabeth neutral
            el "But... there’s a kind big sister that might help..."
            #voice ""
            mc "Okay..."
            #voice ""
            mc "I’ll go check it out then."
            "Elizabeth nods."
            #voice "elq5-17"
            show elizabeth smile
            el "Be careful..."


    $ elizabeth_queststate = 2
    scene black
    call screen minimap()

label elizabeth_gotpaperpen:
    $ elizabeth_queststate = 4
    voice "elq5-19"
    show elizabeth neutral
    el "Did you get it?"
    "Elizabeth’s eager eyes greet you right after you enter the living room."
    "You pull out the pen and paper and show it to Elizabeth."
    voice ""
    show elizabeth neutral
    el "Oh! You really got it!"
    #voice "elq5-20"
    show elizabeth smile
    el "Now draw exactly how I told you!"
    #voice ""
    mc "Why don’t you do it yourself?"
    #voice "elq5-21"
    show elizabeth neutral
    el "...If I do it, the paper will get wet..."
    #voice ""
    show elizabeth sad
    el "I tried drying myself in front of the fireplace, but the water never seems to disappear. It’s strange."
    #voice ""
    mc "Alright, what should I draw?"
    #voice "el_lch1"
    show elizabeth smile
    el "My home!"
    #voice ""
    mc "What does it look like?"
    #voice ""
    show elizabeth neutral
    el "Uum, it has a porch."
    #voice ""
    mc "Okay?"
    #voice ""
    show elizabeth neutral
    el "The walls are white, and the roof gray. There’s a mailbox in front of the house too!"
    #voice "elq5-22"
    show elizabeth neutral
    el "Wow, you’re really bad at drawing."
    #voice ""
    mc "...I’m doing my best."
    #voice ""
    show elizabeth smile
    el "So if I walk straight here, and turn that way, there’s a park over here, I used to play with my friends there."
    #voice ""
    show elizabeth smile
    el "Over there, there’s a river!"
    #voice ""
    show elizabeth smile
    el "My mother used to bring me there when the river was all frozen."
    #voice "el_lch2"
    show elizabeth smile
    el "She taught me how to skate. Now I can skate on my own though. She always loves it when I do the spin!"
    #voice ""
    show elizabeth smile
    el "There’s a bridge here and the ice is thinner over there, so when we went skating, mom always took me the long way around to reach that side of the river."
    #voice ""
    show elizabeth neutral
    el "She told me not to go near the bridge when it's snowing too. Maybe that’s why..."
    "Elizabeth seems to be deep in thought."
    #voice ""
    mc "Anything else?"
    #voice ""
    show elizabeth neutral
    el "Let me see."
    #voice "elq5-23"
    show elizabeth smile
    el "Oh! I think that’s all!"
    #voice "elq5-24"
    show elizabeth smile
    el "I’m amazed, I thought adults all lose their ability to draw."
    #voice ""
    mc "Who told you that?"
    #voice "elq5-25"
    show elizabeth neutral
    el "My mom."
    #voice "elq5-26"
    show elizabeth neutral
    el "She went to the hospital for a while, and came home with Alfie, and she said she can no longer draw with me."
    #voice ""
    mc "Who’s Alfie?"
    #voice ""
    show elizabeth neutral
    el "My brother. He was still small though, still a baby."
    #voice ""
    mc "Do you not like your brother?"
    #voice ""
    show elizabeth neutral
    el "No, he’s cute, you know. He is very soft and warm."
    #voice "elq5-27"
    show elizabeth sad
    el "But after he came home, Mom changed. She always yells at me, she’s always sleepy, and... ugh... she even scolds me when I didn't do anything."
    #voice ""
    show elizabeth angry
    el "It makes me mad too, you know?"
    #voice ""
    show elizabeth neutral
    el "Well, maybe she will apologize to me once I get home."
    #voice "el_ner3"
    show elizabeth neutral
    el "Can you ask those weird adults if they know where this place is?"
    #voice ""
    show elizabeth neutral
    el "I described everything I know, so they should know where it is."
    "You look at the crudely drawn map you drew."
    #voice ""
    mc "Don’t get your hopes up, but I’ll do my best."
    #voice "elq5-28"
    show elizabeth smile
    el "I believe in you!"
    #voice ""
    "The voice in your head reflects."
    ab "Time to make another detour then."
    if q5_location is 0:
        ab "Back to Arabella, I suppose."
    if q5_location is 1:
        ab "Back to Aures, I suppose."
    if q5_location is 2:
        ab "Back to Herman, I suppose."
    jump elizabeth_convohub



label elizabeth_finale:

    "When you enter the living room, you see Elizabeth pacing back and forth."
    "The moment she realizes you are there, her eyes shine."
    #voice "elq5-29"
    show elizabeth smile
    el "How was it? Did they tell you where my home is?"
    "It is you, this time, who hesitates to enter, or to talk."
    #voice ""
    mc "Kind of."
    #voice ""
    mc "It’s very far from here, though."
    #voice ""
    show elizabeth smile
    el "It’s okay, I'm a girl scout. I can read directions!"
    #voice ""
    mc "Well, for starters, you’re right. You’re gonna need to follow that river."
    #voice ""
    mc "But to get to... wherever this is, it’s still a very long way back."
    #voice ""
    mc "Look, do you remember at all how you ended up here?"
    "Elizabeth pouts."
    #voice "el_mad3"
    show elizabeth angry
    el "I told you I don’t! Why are you asking me that!"
    #voice ""
    mc "Because... maybe, you might be better off staying here than going home after all."
    #voice ""
    show elizabeth sad
    el "What are you saying?"
    #voice "el_mad2"
    show elizabeth angry
    el "Are you — Are you a bad person after all?! Did you kidnap me here? You did, didn’t you?!"
    #voice ""
    mc "No, it’s not that at all."
    #voice "elq5-30"
    show elizabeth tantrum1
    el "Don’t lie to me!"
    #voice ""
    mc "I’m not!"
    #voice "elq5-31"
    show elizabeth tantrum1
    el "Then tell me where I need to go! I NEED to go home! It’s not my fault that I’m stuck here!!"
    #voice "elq5-32"
    show elizabeth tantrum2
    el "I don’t want to be here!"
    "Air begins to buzz around Elizabeth."
    "You pull out the map you drew earlier, and point at the crescent-shaped bridge on the paper."
    #voice ""
    mc "The river. This bridge. Did you go there yesterday?"
    "Sparks rise around Elizabeth and she takes a step back."
    #voice ""
    mc "Tell me, I need to know."
    #voice ""
    show elizabeth angry
    el "So what if I did?!"
    "Her scream makes the entire room shake."
    #voice ""
    mc "Did you tell your mother before you leave?"
    #voice "el_mad1"
    show elizabeth tantrum1
    el "Shut up!"
    "You’re hit by a blast of invisible energy."
    #voice ""
    mc "Did you run away from home?"
    #voice ""
    show elizabeth angry
    el "I’m..."
    #voice ""
    mc "Why did you leave home? Did something happen to you after all?"
    #voice "elq5-33"
    show elizabeth tantrum2
    el "SHUT UP! GO AWAY!!"
    "You hear clattering from every object in the room."
    #voice ""
    mc "Look, I’m only worried. I don’t know why you’re here. I was afraid you were abused and ran away. "
    #voice ""
    mc "But if that wasn’t the case, you need to tell me, so I can help you."
    #voice ""
    show elizabeth angry
    el "..."
    "Elizabeth looks shocked, but immediately averts her gaze to the ground."
    #voice ""
    mc "Elizabeth."
    #voice ""
    show elizabeth sad
    el "..."
    #SFX AUDIBLE SIGH
    #voice ""
    show elizabeth sad
    el "My mom..."
    #voice "elq5-34"
    show elizabeth sad
    el "It’s supposed to be my birthday today."
    #voice "elq5-35"
    show elizabeth sad
    el "But you know, since I woke up in the morning, she didn’t tell me happy birthday, or kiss me, or hug me. She didn’t do anything."
    #voice "elq5-36"
    show elizabeth angry
    el "There was no gift for me. I checked the closet, shelves, everything. There wasn’t even a cake in the fridge."
    #voice "elq5-37"
    show elizabeth angry
    el "I asked my mom about it, but she got angry. She said I’ve been making a big mess!"
    #voice "elq5-38"
    show elizabeth angry
    el "But it wasn’t my fault, you know! But she said she was busy! Can you believe it?"
    #voice "elq5-39"
    show elizabeth angry
    el "She had time to bring Alfie to the clinic this morning, but she forgot my birthday!"
    #voice "elq5-40"
    show elizabeth angry
    el "I was SO mad at her, you know! I told her—"
    #voice "elq5-41"
    show elizabeth sad
    el "... "
    #voice "elq5-42"
    show elizabeth sad
    el "I told her I hate her..."
    #voice ""
    mc "Then you ran away after that?"
    "Elizabeth falls silent for a moment."
    #voice "elq5-43"
    show elizabeth sad
    el "She promised to take me skating on my birthday..."
    #voice "elq5-44"
    show elizabeth neutral
    el "So I went to the lake by myself. I knew she would come later."
    #voice "elq5-45"
    show elizabeth sad
    el "Then... I was here before I realized it. I—I don’t know what happened..."
    #voice "elq5-46"
    show elizabeth sad
    el "I’ve been trying to find the way out, but... I keep returning to this room again and again. I can’t even see the big sister that helped me earlier..."
    "She’s looking straight into your eyes."
    #voice ""
    show elizabeth sad
    el "Do you know something? What happened to me? Why am I here?"
    "You take a deep breath."
    #voice ""
    show elizabeth sad
    el "I’m... I’m confused. What is going on..."
    #voice ""
    mc "Elizabeth, listen to me closely."
    menu:
        "Tell her the truth.":
            $ elizabeth_queststate = 6
            #voice ""
            mc "Elizabeth is looking at you anxiously."
            #voice ""
            mc "You didn’t..."
            "You sigh deeply."
            #voice ""
            mc "It wasn’t yesterday."
            #voice "el_ner3"
            show elizabeth neutral
            el "Huh?"
            #voice ""
            mc "When you ran away from home, it’s been... years..."
            #voice ""
            mc "You fought with your mother, you ran away from home, you were trying to go to the frozen lake, but you took the shortcut, the bridge."
            #voice ""
            mc "Do you know why your mother never brought you through the bridge? Because snow and ice will make it slippery."
            #voice ""
            mc "You fell through the ice on the frozen river, and the water carried you here."
            #voice ""
            show elizabeth sad
            el "But I..."
            #voice ""
            mc "Elizabeth, you’re already dead."
            #voice ""
            show elizabeth sad
            el "..."
            #voice ""
            mc "You have been away from home for years."
            #voice ""
            mc "The reason you’re stuck here is because your body washed up on the river right behind this mansion, you wandered in, and you can no longer get out."
            #voice "el_sad2"
            show elizabeth sad
            el "What are you talking about... I’m..."
            #voice ""
            mc "Yes, that is why you can’t leave, you’re... bound to this place."
            "Elizabeth’s eyes widen."
            #voice "elq5-47"
            show elizabeth sad
            el "...What about Mom?..."
            #voice ""
            mc "I’m not sure... but it’s been... years..."
            #voice ""
            mc "Even if she’s alive, I don’t think you can... see her anymore."
            "It starts from the twinkle of her teary eyes."
            "Then, a single tear rolls from her eye."
            "She bites her lips and her shoulders shake. She’s doing it again, trying to look brave even though she is terrified."
            "You kneel before her and watch as her entire broken heart flows with her tears and sobs."
            "For a while, you just watch in silence. Watching as she finally lets out everything she’s been holding inside."
            #voice "elq5-48"
            show elizabeth sad
            el "I’m... dead..."
            "You nod."
            #voice "elq5-49"
            show elizabeth sad
            el "I can no longer go back... home?"
        "Show her the newspaper clippings.":
            $ elizabeth_queststate = 6
            "You pull out the newspaper clippings you received earlier and give it to Elizabeth."
            #voice ""
            mc "You can read, right?"
            "In fact, she had already started reading."
            "For a moment, she doesn’t speak. Her eyes move quickly as she reads."
            "Then, her eyes widen."
            "Then, she looks at you. Fear fills her eyes."
            #voice ""
            show elizabeth sad
            el "Is this... my mother?"
            "You nod."
            #voice "elq5-50"
            show elizabeth sad
            el "What does she mean—she wants me to be happy wherever I am?"
            #voice ""
            mc "You went missing yesterday—or in fact, for a couple of years now."
            #voice "elq5-51"
            show elizabeth angry
            el "What? But I just got here!"
            #voice ""
            mc "That’s just how it feels like to you."
            #voice ""
            mc "The newspaper said you went missing on the day of your birthday. That... might be the same day you got here."
            #voice ""
            mc "They saw cracks on the river and assumed you fell in. But your mother believed you just ran away, and waited, and waited..."
            #voice ""
            mc "But since you never came home, she decided to convey her last message through that."
            #voice ""
            mc "She wants to tell you to be happy."
            #voice ""
            mc "She has since moved away. Your home is no longer there."
            #voice "elq5-52"
            show elizabeth tantrum2
            el "...You’re lying..."
            #voice ""
            mc "I’m sorry you had to find out this way."
            #voice "elq5-53"
            show elizabeth tantrum2
            el "You’re lying..."
            "It starts from the twinkle of her teary eyes."
            "Then, a single tear rolls from her eye."
            "She bites her lips, and her shoulders shake. She’s doing it again, trying to look brave, even though she is terrified."
            "You kneel before her and watch as her entire broken heart flows with her tears and sobs."
            "For a while, you just watch in silence. Watching as she finally lets out everything she’s been holding inside."
            #voice "elq5-48"
            show elizabeth sad
            el "I can no longer go back... home?"
            #voice ""
        "Lie for her own good.":
            $ elizabeth_queststate = 7
            mc "I will bring you home."
            #voice ""
            show elizabeth neutral
            el "Really?!"
            #voice ""
            mc "But first, I need your help, I will need your strength."
            #voice ""
            show elizabeth sad
            el "Oh..."
            #voice ""
            show elizabeth sad
            el "But..."
            #voice ""
            mc "Come on, I have helped you twice before, you can at least say thanks to me by helping me one time."
            #voice ""
            show elizabeth neutral
            el "..."
            "Elizabeth seems to be thinking hard."
            #voice "elq5-54"
            show elizabeth smile
            el "...Alright then. Mom always told me to return people’s kindness anyway."
            #voice "elq5-55"
            show elizabeth smile
            el "How can I help you then?"
            #voice ""
            mc "I just... need you to stay here for a while."
            #voice ""
            show elizabeth neutral
            el "What? That’s it?"
            #voice ""
            mc "Actually, there’s something I need to find out first about this mansion. I might need your help later."
            #voice "elq5-56"
            show elizabeth neutral
            el "...Is there going to be something scary?"
            #voice ""
            mc "No, I just need you to stay here a little bit longer."
            #voice "elq5-57"
            show elizabeth neutral
            el "But after this, I'll really be able to go home, right?"
            "You gulp."
            #voice ""
            mc "Yes."

    #voice "elq5-58"
    show elizabeth neutral
    el "What should I do now then?"
    #voice ""
    mc "I’d say, go rest for now. After your energy returns, I will show you around."
    #voice ""
    show elizabeth neutral
    el "Around where?"
    #voice ""
    mc "I heard you have caused a lot of problems for everyone else in this mansion. They’re also not all weird or as bad as you thought, you know."
    #voice ""
    mc "Should we go and visit them and apologize?"
    #voice ""
    show elizabeth angry
    el "Ugh... but—"
    #voice ""
    mc "No buts. Who knows, you may like them once you get to know them."
    "Elizabeth hesitates a little."
    #voice ""
    mc "I told you I will be with you, right?"
    "Elizabeth nods."
    #voice "elq5-59"
    show elizabeth neutral
    el "You promise?"
    #voice ""
    mc "I promise."
    "Hearing your answer, Elizabeth suddenly giggles."
    "She runs towards the couch, the place where she hid from you before."
    "But this time, she pokes her head to look at you one more time."
    #voice "elq5-60"
    show elizabeth smile
    el "You know… I think you’re not a bad person after all."
    #voice "elq5-61"
    show elizabeth smile
    el "Thanks for helping me."
    jump elizabeth_reflection
