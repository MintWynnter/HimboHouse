label elizabeth_livingroom:

    #show whatever bg i don't remember the syntax

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
    show elizabeth tantrum1
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

    "But where’s the place that could possibly have those?"

    menu:
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
    call screen minimap()
