default killPath = False
default selfish = 0
default goodness = 0
default auresQuestState = 1
default hasTeleporter = False
define au = Character("Aures", color="#ffffff",what_color="#ffffff")
define mi = Character("Minoru", color="#ffffff",what_color="#ffffff")
default aures_good = False
default aures_questjustfinished = False

label aures_ballroom:

    scene bg ballroom
    show chand
    with fade
    stop music fadeout 1.0
    play music m_au if_changed fadein 1.0


    if auresQuestState is 1:
        jump auresIntro
    else:
        jump aures_hub




label auresIntro:

    "You enter a large door and find yourself in a ballroom. A woman in her early twenties appears to be dancing with an imaginary partner."
    voice "au_lhe1"
    show aures laughing at aures_spot
    au "Ohohohohohoho! Welcome to my ballroom! Would you like some tea? Perhaps a short dance?"
    voice "au_hap3"
    show aures neutral
    au "Actually, allow me to introduce myself. I am Aures Bellis. It is a pleasure to make your acquaintance; I am sure that we will get along swimmingly."
    $auresQuestState += 1
    jump aures_convohub

label auresScene2:
    "You sit with Aures and start sipping some type of tea that she prepared. It tastes very floral."
    voice "auq4-01"
    show aures neutral
    au "I hear you are to help us with our problems. I have a task for you."
    "Aures seems to get more serious while talking."
    voice "auq4-02"
    au "I need you to help reunite me with My Love, Minoru. My death unfortunately separated the two of us."
    voice "auq4-03"
    au "He lives in a village nearby, but I cannot get through the forest to reach him. It is simply imperative that I be reunited with him."
    "She speaks slightly more hurriedly with the last sentence."
    menu:
        "\"I'm always happy to help when needed!\"":
            $goodness += 5
            $selfish -= 5
            voice "au_hap3"
            au "I'm elated to know you feel that way; let us begin preparations as soon as you are ready!"
        "\"Well, I guess I do need to figure out what's going on.\"":
            $selfish += 5
            voice "au_ann2"
            au "As long as the task gets done, I care not why you do it."
        "\"I'd really rather not, but I probably have to.\"":
            $goodness -= 5
            voice "au_ann2"
            au "Well, as long as you help, I do not care whether you want to or not."
    $auresQuestState += 1
    jump aures_convohub

label auresScene3:

    voice "au_puz5"
    show aures neutral
    au "So, how shall we go about reuniting me with My Darling? I drafted up a few ideas."
    "Aures pulls out a bunch of papers and spreads them across the table."
    voice "au_puz5"
    au "Let's start with this one. You could help me write a letter and send it to him. It's straightforward; the only issue is that he may not respond, especially when he sees it is from a dead girl."
    "You look at the papers and notice that some are a bit unsavory"
    menu:
        "Pick up the one depicting a tied up person.":
            $goodness -= 5
            "The picture is of a person tied up and stuffed into the trunk of a car."
            voice "au_hap3"
            show aures laughing
            au "Oh, I am quite proud of that one. The only issue is that we would have to get through the woods, but I do not think either of us can do that."
        "Pick up the one depicting a mirror.":
            "The picture has a mirror with a person drawn in it."
            voice "au_puz5"
            show aures neutral
            au "I quite like this one, as it would let me see My Dear. I do not remember if any of the other residents have an object like this that they would allow me to borrow, though."
        "Pick up the one depicting some flowers.":
            $goodness += 5
            $selfish -= 5
            "The picture has what appears to be a bouquet of flowers and a note."
            voice "auq4-04"
            au "This one is nice, but I would have to get the address of My Little Pet before we could send it, so it may not work."
    voice "auq4-05"
    show aures laughing
    au "Oh, how about this one? This was certainly one of my favorites!"
    "Aures holds up a picture of a person being stabbed with a ghost coming out of the body."
    voice "auq4-06"
    show aures yandere
    au "If we can kill My Sugar Bear, then we can bring him here, and then we can be together forever!"
    voice "auq4-07"
    show aures neutral
    au "I like this one. Let us think of a few ways to go about it!"
    "Aures starts scribbling on some pieces of paper, each portraying a different means of murder."
    menu:
        "\"I don't know if murder is the best option here...\"":
            $goodness += 10
            voice "au_dis1"
            show aures soulless
            au "Oh. Well, I suppose if you believe so. I did ask for your opinion."
            "Aures is visibly disappointed."
            voice "au_hap3"
            show aures yandere
            au "Actually, if we want to go with a non-murderous option, we can just pick one of the others. This one requires a bit more planning, so let us contemplate it more."
        "\"Maybe a guillotine would work.\"":
            $goodness -= 10
            voice "au_lhe1"
            show aures yandere
            au "Oh, how noble of you! I like that one. I wouldn't want to cause My Treasure any unnecessary pain."
        "\"Why don't we go through the other options before resorting to murder?\"":
            voice "au_dis1"
            show aures soulless
            au "I still like it, but you are right. Maybe there are other ways to trap him here for all eternity."
            "Aures seems slightly disappointed that you aren't as excited about murder as her."
            voice "au_hap3"
            au "Well, the non-murderous ones are easy enough to think of plans for. It would be much more useful for you to help me think of ways to do it with murder, so let us work on that."
    "She starts drawing another picture, this time of someone getting their head cut off."
    voice "au_hap3"
    show aures laughing
    au "What fun! I cannot wait to see My Sweetheart once again!"
    "Aures laughs as she gleefully draws the person getting decapitated."
    voice "auq4-08"
    show aures yandere
    au "We should think of more options. But do remember, we should try to keep it as painless as possible for My Shnookums."
    voice "auq4-09"
    show aures soulless
    au "How painful is a knife to the throat? Can you feel pain? If so, may I test something on you?"
    "Aures looks at you with empty, soulless eyes. You see her slowly reaching for something."
    menu:
        "\"Since I'm a zombie, I can't feel any pain.\"":
            voice "au_dis1"
            au "Oh, what a shame. Well, we can still consider it. My Sweetie Pie can handle a bit of pain if it means we can be together forever."
        "\"There's no way I'm letting you cut my throat.\"":
            $selfish += 5
            voice "au_dis1"
            au "Why not?! I thought you were going to help me!"
            "She looks disappointed but does back off after a bit."
        "\"I guess if it helps, you can slice my throat.\"":
            $selfish -= 10
            voice "au_lhe1"
            show aures laughing
            au "Splendid! Let us see how much pain My Lovebug will feel if we slit his throat!"
            "Aures brandishes the knife and lunges towards you."
            "It sinks into your chest, unsurprisngly."
            "Your failure to meaningfully react to the puncture wound disturbs Aures, but only momentarily."
    $auresQuestState += 1
    jump auresScene4

label auresScene4:

    voice "au_puz5"
    show aures neutral
    au "So, we have many potential plans but we still have no means of carrying them out. Neither of us can leave the mansion very easily."
    "Aures thinks deeply for a few moments before finally saying something."
    voice "au_puz2"
    au "Maybe we can acquire a teleportation device. That way, I can see My Cupcake and talk to him in person!"
    "Aures starts floating around the room, contemplating. Eventually, she comes back down again."
    voice "au_puz4"
    au "We would just need to find some teleportation method. Perhaps we could use a magic circle?"
    au "This is a fairly old mansion. I am sure we have something like that."
    voice "au_puz3"
    au "Maybe something a bit more scientific… Do we have a teleporter? There must be something we can use somewhere around here…"
    voice "au_puz1"
    au "Maybe you could go ask Lysander. I do not know if you have met him yet."
    au "He is the groundskeeper here. If anyone would know where something is, it would be him."
    $auresQuestState += 1
    jump aures_convohub

label auresScene5:

    voice "au_hap3"
    show aures laughing
    au "Oh, wonderful! I see you have acquired a means of teleportation. Now, we may finalize our plans."
    "Aures takes the teleportation device and puts it on the table, where even more papers are laid out than last time."
    voice "auq4-10"
    show aures yandere
    au "Now, on to the specifics. We have three options: teleport me over to him, teleport him here, or, my personal favorite, kill him so he is here with me forever."
    #voice
    au "I suppose I can leave the decision to you. What do you think would be best?"
    menu:
        "Teleport Aures to him.":
            $killPath = False
            voice "auq4-11"
            show aures yandere
            au "So you think that I should go to My Pookie? How romantic! Let us start right away!"
            "You set the machine the way Lysander taught you; it will return Aures after three minutes."
            voice "au_hap3"
            au "I have the rope. I will return with My Snuggle Bunny soon."
            "You wait a few minutes, and Aures returns with another person in a flash of blue light."
            voice "miq4-01"
            show minoru neutral
            mi "What's going on?! Who are you?!"
            voice "auq4-12"
            au "I'm sure you are just panicking, but you must remember me, yes? I am your future wife. I went through all of this effort just so that we could be together for eternity."
            voice "au_hap3"
            au "I am Aures Bellis. When we were in high school, I was crying on the stairs. You saved me. I only cared about you from then on."
            voice "miq4-02"
            mi "Well, as long as you don't hurt me, I guess I can stay here for a bit. Wherever 'here' is."
            voice "auq4-13"
            au "Delightful! Let me untie you. I hope the ropes were not too tight for you, My Honey Bun."
            "Aures unties Minoru, and he moves away from her slightly. Aures, in response, gets even closer to him."
            voice "auq4-14"
            au "Don't be afraid, Sweetie. I'll ensure it is as painless as possible when I bring you to my side forever."
            voice "miq4-03"
            mi "What do you mean by that? Forever? I'm never going to be able to leave?"
            #voice auq4-15
            show aures neutral
            au "You may not have noticed because it all happened so suddenly, but I am a ghost. I will have to kill you before we can truly be together. But not to worry, I will kill you with love."
        "Teleport him to the mansion.":
            $killPath = False
            voice "au_hap3"
            show aures neutral
            au "So you think that we should bring him here? I should prepare some tea! You power up the device while I do that."
            "You set the machine the way Lysander taught you; a pale blue light emits from it, and a person appears after a few moments."
            voice "miq4-04"
            show minoru neutral
            mi "Where am I?! Who are you?! Why are you not opaque?!"
            voice "au_hap3"
            au "You must not recognize me because I'm a ghost now. I am Aures Bellis, your future wife. You are in a mansion in the woods."
            voice "miq4-05"
            mi "What do you mean by ghost? And what do you mean by future wife?"
            voice "au_sad5"
            show aures heartbroken
            au "Don't tell me you forgot. In high school, I was crying on the stairs, and you came and comforted me. I spent the rest of my life thinking about nothing but you."
            "Aures starts looking a bit depressed, as if her afterlife has no meaning."
            voice "miq4-06"
            show minoru laugh
            mi "Oh, of course I remember. Hahaha, I was just panicking, yeah, that's right. How could I forget about you?"
            "Minoru is clearly just playing along out of fear, but Aures seems not to notice at all."
            voice "auq4-16"
            show aures laughing
            au "Of course! How could My Jellybean forget about me? I'm sure you cared about me just as much as I did about you!"
            voice "mi_ner1"
            show minoru neutral
            mi "I guess I can stay here for a bit. Just please don't hurt me."
            voice "auq4-17"
            show aures yandere
            au "Don't worry, My Teddy Bear, when I make it so that we can be together forever, it will be as painless as possible."
        "Kill him.":
            $killPath = True
            voice "auq4-18"
            show aures yandere
            au "Oh, how splendid! I was hoping you would choose that one! What could be more romantic than being with My Beloved forever? Let us devise a way to kill him, then bring him here with the device."
            "Aures brings the murder plans back out and lays a few of her favorites before you."
            voice "auq4-19"
            au "I like these. My favorite is this one: it allows me to be the one who brings us together forever."
            "Aures hands you the paper from before with a drawing of a man being stabbed and his ghost coming out of his body."
            voice "au_hap3"
            au "I even have the knife right here. My plan is to stab him right in the stomach. I want to ensure my loving face is the last thing he sees before he dies."
            "Aures seems to be completely elated at the idea of killing Minoru."
            voice "auq4-20"
            au "Power up the machine and set it to bring My Eternal Love to us. I'll wait here and stab him when he arrives."
            "You set the machine the way Lysander taught you; a pale blue light emits from it, and a person appears after a few moments."
            voice "auq4-21"
            au "Hello, My Sunshine! Look at me, and we will be bound together for all eternity!"
            voice "miq4-07"
            show minoru neutral
            mi "Augh! "
            "Minoru's corpse slumps to the floor. After a few minutes, his spirit begins to rise from the body."
            voice "miq4-08"
            mi "Who are you?! Where am I?! Why am I not opaque?!"
            "Minoru is still panicking but is laughing a bit in disbelief."
            voice "mi_sca5"
            mi "What happened to me? I was just sitting in my house a minute ago."
            voice "au_hap3"
            au "We teleported you here, Honey Toast, so that I could be with you. Then I killed you so that we could spend eternity together."
            voice "miq4-09"
            mi "You killed me?! And why did you call yourself my future wife?! I don't even know you!"
            voice "au_sad5"
            show aures heartbroken
            au "Why are you so upset? Don't you remember? In high school, I was crying in the stairwell. You came up to me and comforted me."
            voice "auq4-23"
            show aures soulless
            au "That pretty much means that you love me, right? You wouldn't leave me after that, right? We're gonna get married, right? You're the only thing I've cared about since then."
            "Aures seems to be very flustered. Her eyes have become devoid of all life."
            voice "miq4-10"
            mi "Oh, um, I guess I can stay. At least for a bit."
            "Minoru seems a bit scared, but he goes along with Aures anyway."
            voice "auq4-24"
            show aures neutral
            au "Delightful! I know I can make you see how much you love me, Pumpkin!"
            "Aures clings to Minoru."
            voice "au_hap3"
            au "Come back later. I'm sure I will require your assistance again."
            $auresQuestState += 1
            call screen minimap()
    voice "miq4-11"
    show minoru neutral
    mi "You're gonna kill me?!"
    voice "au_hap3"
    show aures soulless
    au "Do not worry, My Cinnamon Bun. I told you that I would do it in a way that wouldn't hurt."
    "Minoru moves further away from Aures, and Aures follows."
    voice "miq4-12"
    mi "I'll stay for a bit, but you have to promise not to kill me."
    voice "au_hap3"
    show aures soulless
    au "Fine, I will do as you wish for now. But whenever you are ready to enter the loving embrace of death, tell me."
    au "In the meantime, I bid you farewell."
    $auresQuestState += 1
    call screen minimap()


label auresScene6K:
    "Aures is holding tightly onto Minoru's arm, and he is subtly trying to get away from her."
    voice "au_puz5"
    show aures neutral
    au "Oh, wonderful, you're here! I was just about to go looking for you. We seem to have a slight issue."
    voice "au_hap3"
    au "Even though My Muffin has already accepted my love, he still seems a bit hesitant. I require your assistance in making him remember his love."
    voice "au_puz5"
    au "Why don't you talk to him for a bit? Maybe you can remind him of our love while I make some tea."
    "Aures moves to the other side of the room and starts measuring out some tea."
    #voice miq4-13
    show minoru neutral
    mi "You have to help me. She's crazy! I barely even remember her, but she wants me to marry her?!"
    voice "miq4-14"
    mi "To make it even worse, she killed me! And she keeps calling me these weird names..."
    menu:
        "\"I'm here to help the ghosts that were here when I arrived. That doesn't include you.\"":
            $selfish += 15
            voice "miq4-15"
            mi "I can't believe it. You're the reason I'm stuck here, and you won't even try to help me?"
            voice "miq4-16"
            mi "Well, I guess there isn't really anything you could do anyway. But just know that you're a jerk."
        "\"I wish I could help you, but I don't think I can do much now.\"":
            $selfish -= 10
            voice "mi_ner1"
            mi "I guess you're right. At least you're willing to help. If I think of anything, I'll let you know."
        "\"I'm sorry for how things turned out, but why don't you give Aures a chance?\"":
            $selfish -= 5
            voice "miq4-17"
            mi "Why don't I 'give her a chance?!' Because she killed me, that's why! She's absolutely insane!"
            voice "miq4-18"
            mi "Maybe you're right, though. She may be crazy, but what's she gonna do? Kill me? Already done."
    "Minoru sighs in defeat. He shrugs and waits for Aures to get back."
    voice "au_puz5"
    show aures neutral
    au "Well, were you able to convince My Little Breadcrumb that eternal love with me is what is best?"
    voice "mi_lgi5"
    show minoru laugh
    mi "I guess I can give it a try, at the very least. Just promise me that I can leave if I don't want to stay with you."
    "Minoru looks hopeful, but Aures doesn't budge."
    voice "auq4-25"
    show aures soulless
    au "I'm sure it would never come to that. You already showed your love when you saved me. You must have forgotten about it because you've died."
    voice "mi_puz2"
    show minoru neutral
    mi "Why would that make me forget? I remember everything else perfectly fine."
    voice "auq4-26"
    au "I cannot seem to remember a lot of details about my life from the years surrounding my death. The only thing I can remember clearly is you, My Dove. So, you're likely having similar issues."
    voice "auq4-27"
    show aures yandere
    au "You probably just don't remember how much you love me. But worry not; I will make sure you do."
    voice "auq4-28"
    au "I will make sure that you remember that you are mine."
    "She turns to you."
    au "Leave us two lovers be for now, will you?"
    $auresQuestState += 1
    call screen minimap()

label auresScene7K:
    voice "au_mad5"
    show aures heartbroken
    au "I'm so glad you are here! I need your help!"
    "Minoru is tied up in the corner of the room."
    voice "auq4-29"
    au "That wench Arabella is trying to steal My Cuddlebug from me! I saw her point him to the kitchen just moments ago."
    voice "auq4-30"
    au "Does she not know that he is mine and mine alone?"
    "Aures starts taking out papers again like she did when she was planning to kill Minoru."
    voice "au_puz2"
    show aures soulless
    au "She's already dead, so I can't kill her, but there must be something we can do. I know all the movies show ghosts being sucked into vacuums. Does that work?"
    menu:
        "\"Aren't you going a bit overboard?\"":
            voice "au_mad5"
            show aures soulless
            au "What do you mean?! She's trying to steal him from me! She has to pay for this!"
            "Aures's eyes grow soulless as she keeps trying to think of ways to end Arabella's afterlife."
            voice "au_puz5"
            au "Well, maybe there's something else we can do to solve the issue."
        "\"Maybe try a sealing circle instead.\"":
            voice "au_lhe1"
            show aures neutral
            au "That's a splendid idea! There's only one issue: I do not have the required knowledge to do that."
            voice "au_puz3"
            au "That does give me an idea, though."
        "\"Maybe talking to her would fix things.\"":
            voice "auq4-31"
            show aures soulless
            au "There is no use in talking to a man-stealing harlot. I need to find a way to keep her away from My Everything, not make a new friend."
            voice "auq4-32"
            au "I guess that there is another way to keep them apart that doesn't involve me interacting with that wench."
    voice "auq4-33"
    show aures yandere
    au "If I can't keep her away from him, I must keep him away from her. He will remain here with me."
    "You see Minoru's eyes go wide on the other side of the room. He tries to say something, but the tape over his mouth prevents it."
    "Aures goes over to Minoru and unties him."
    voice "mi_mad2"
    show minoru neutral
    mi "What do you mean?! It's bad enough that I have to stay in this mansion; now I can't even leave this room?!"
    voice "auq4-34"
    show aures heartbroken
    au "Are you saying that you want to be with that tramp in the foyer? You would leave me for someone like her?"
    voice "auq4-35"
    au "Why can't you just accept all of my love? Why won't you just be mine? You don't belong to her. You belong to me!"
    voice "miq4-19"
    mi "I don't even know who she is! I just wanted to find the kitchen! And I don't belong to anyone!"
    voice "auq4-36"
    show aures yandere
    au "What do you mean by that? We're getting married. That means that I belong to you, and you belong to me."
    voice "auq4-37"
    au "If that whore is going to get in the way of that, then I have to find a way to get rid of her permanently."
    voice "au_hap3"
    au "But it would be much easier to just keep you by my side at all times."
    "Minoru looks at you pleadingly."
    menu:
        "\"Why don't you think of how Minoru feels?\"":
            $selfish -= 10
            voice "au_sad4"
            show aures soulless
            au "He doesn't remember how he feels. He just can't remember how much he loves me."
        "\"Just go along with her. If not, it'll be a pain for me.\"":
            $selfish += 15
            voice "mi_mad2"
            show minoru neutral
            mi "I can't believe you! You let her kill me, now this! How selfish can one person be?!"
        "\"Maybe we should have a calm conversation about it.\"":
            voice "au_hap3"
            au "I don't see why that would help. He doesn't even realize what's best for him. He will be happiest here, with me, so that's where he will stay."
    voice "auq4-38"
    show aures yandere
    au "You may not see this now, My Reason For Being, but this is what's best for you. You must stay with me forever."
    "Aures looks you dead in the eye."
    au "I need some privacy, please. My Reason and I need to establish an understanding."
    $auresQuestState += 1
    call screen minimap()

label auresScene6NK:
    "Aures is holding tightly onto Minoru's arm, and he is subtly trying to get away from her."
    voice "au_sad4"
    show aures neutral
    au "Oh, wonderful, you're here! I was just about to go looking for you. We seem to have a slight issue."
    voice "au_sad4"
    au "Even though My Purpose has already accepted my love, he still seems a bit hesitant. I require your assistance in making him remember his love."
    voice "au_puz4"
    au "Why don't you talk to him for a bit? Maybe you can remind him of our love while I make some tea."
    "Aures moves to the other side of the room and starts measuring out some tea."
    voice "miq4-13"
    show minoru neutral
    mi "You have to help me. She's crazy! I barely even remember her, but she wants me to marry her?!"
    voice "miq4-20"
    mi "To make it even worse, she wants to kill me! And she keeps calling me these weird names..."
    menu:
        "\"I'm here to help the ghosts that were here when I arrived. That doesn't include you.\"":
            $selfish += 10
            voice "miq4-15"
            mi "I can't believe it. You're the reason I'm stuck here, and you won't even try to help me?"
            voice "miq4-16"
            mi "Well, I guess there isn't really anything you could do anyway. But just know that you're a jerk."
        "\"I wish I could help you, but I don't think I can do much now.\"":
            $selfish -= 10
            voice "mi_ner1"
            mi "I guess you're right. At least you're willing to help. If I think of anything, I'll let you know."
        "\"I'm sorry for how things turned out, but why don't you give Aures a chance?\"":
            voice "mi_sca5"
            mi "Why don't I 'give her a chance?!' Because she wants to kill me, that's why! She's absolutely insane!"
            voice "miq4-21"
            show minoru laugh
            mi "Maybe you're right, though. She may be crazy, but maybe we can convince her not to kill me? I guess it'll be easier to do if she isn't furious."
    "Minoru sighs in defeat. He shrugs and waits for Aures to get back."
    voice "au_puz5"
    show aures yandere
    au "Well, were you able to convince My Sweetums that eternal love with me is what is best?"
    voice "mi_lgi5"
    mi "I guess I can give it a try, at the very least. Just promise me that I can leave if I don't want to stay with you."
    "Minoru looks hopeful, but Aures doesn't budge."
    "voice au_hap3"
    show aures soulless
    au "I'm sure it would never come to that. You already showed your love when you saved me. You must have just forgotten."
    voice "mi_puz3"
    show minoru neutral
    mi "Why would you think that? I remember everything else perfectly fine."
    #voice au_hap3
    au "Maybe going through the teleporter did something to your memories of me. I'm sure that it would affect the things you think about the most."
    voice "auq4-27"
    au "You probably just don't remember how much you love me. But worry not; I will make sure you do."
    voice "auq4-28"
    au "I will make sure that you remember that you are mine."
    "She turns to you."
    au "Leave us two lovers be for now, will you?"
    $auresQuestState += 1
    call screen minimap()

label auresScene7NK:
    voice "au_sad3"
    show aures heartbroken
    au "I'm so glad you are here! I need your help!"
    "Minoru is tied up in the corner of the room."
    voice "auq4-39"
    au "That wench Arabella is trying to steal My Only Desire from me! I saw her point him to the kitchen just moments ago."
    voice "auq4-30"
    au "Does she not know that he is mine and mine alone?"
    "Aures starts taking out papers again like she did when she was planning to kill Minoru."
    #voice au_puz2
    show aures soulless
    au "She's already dead, so I can't kill her, but there must be something we can do. I know all the movies show ghosts being sucked into vacuums. Does that work?"
    menu:
        "\"Aren't you going a bit overboard?\"":
            voice "auq4-40"
            au "What do you mean?! She's trying to steal him from me! She has to pay for this!"
            "Aures's eyes grow soulless as she keeps trying to think of ways to end Arabella's afterlife."
            voice "au_puz4"
            show aures neutral
            au "Well, maybe there's something else we can do to solve the issue."
        "\"Maybe try a sealing circle instead.\"":
            voice "au_puz3"
            show aures neutral
            au "That's a splendid idea! There's only one issue: I do not have the required knowledge to do that."
            #voice au_hap3
            au "That does give me an idea, though."
        "\"Maybe talking to her would fix things.\"":
            voice "auq4-31"
            show aures soulless
            au "There is no use in talking to a man-stealing harlot. I need to find a way to keep her away from My Everything, not make a new friend."
            voice "auq4-32"
            au "I guess that there is another way to keep them apart that doesn't involve me interacting with that wench."
    voice "auq4-41"
    show aures yandere
    au "If I can't keep her away from him, I must keep him away from her. He will remain here with me. But he still needs food to live... Though, that can be fixed."
    "You see Minoru's eyes go wide on the other side of the room. He tries to say something, but the tape over his mouth prevents it."
    "Aures goes over to a table and takes out a knife."
    voice "auq4-42"
    au "He doesn't need to eat if he's dead. This can also be his punishment for talking to that she-devil."
    voice "auq4-43"
    au "Remember, My Plaything, I only do this because I love you."
    "Aures stabs Minoru in the stomach. He slumps over, dead, and his spirit rises out of his corpse."
    voice "auq4-44"
    au "Now we can be together forever. Now you are finally all mine."
    "Aures looks you dead in the eye."
    au "I need some privacy, please. My Reason and I need to establish an understanding now that we are eternally bound."
    $auresQuestState += 1
    call screen minimap()


label auresScene8:
    voice "miq4-22"
    mi "Let me leave! You killed me, chained me up in this room, and you expect me to marry you! That's insane!"
    voice "au_sad3"
    show aures heartbroken
    au "I can't let you leave. We need each other!"
    voice "mi_mad2"
    show minoru neutral
    mi "I don't need you at all! I did perfectly fine until you came along!"
    voice "auq4-45"
    au "What do you mean? You don't need me? But we do need each other. That's why you helped me. When I couldn't take it anymore, you helped me have a reason to keep pushing through it."
    voice "miq4-23"
    mi "I barely even remember that! I just saw you crying and asked what was wrong. Most people would do that. Why are you treating it like it's such a big deal?"
    "Aures grabs her head like she's in pain, and she falls to the floor, sobbing."
    voice "auq4-46"
    au "They were horrible. Those men in that cult. They would cut me, then use that blood as a sacrifice to some god."
    voice "auq4-47"
    au "I would cry every day. I tried to stay strong when I was in school, but after two weeks of that, I couldn't keep it in anymore."
    voice "auq4-48"
    au "But then you came along. You gave me a reason to keep living. Without you, I would have given up all hope. You can't leave me now."
    voice "auq4-49"
    au "When they killed me, I thought I would never get to see you again. I was so happy when I saw you."
    "Aures passes out for a few seconds, then wakes up again."
    #voice au_puz3
    show aures neutral
    au "Why am I on the floor? It doesn't matter; I need your help. My World wants to leave. Please help me keep him here."
    menu:
        "\"Why don't you think about how Minoru feels?\"":
            $selfish -= 10
            #voice au_eww1
            show aures soulless
            au "Think about how he feels? Do you intend to say that I should let him leave?! Ridiculous!"
            #voice au_dis2
            show aures neutral
            au "Well, actually, maybe I'm the one being ridiculous. I've been forcing you to do what I want, and you've been so nice. You helped me without thinking of yourself."
            #voice au_puz2
            au "Maybe I should do the same to Minoru. Minoru, I apologize for all I've done. Would you like to leave?"
            "It is clear that Aures will burst into tears again if Minoru decides to leave. She may even snap and chain him up if that happens."
            jump auresHappyEnd
        "\"I think you should just keep him here.\"":
            $selfish += 15
            voice "auq4-50"
            show aures yandere
            au "I think you are right. I should just keep him here. He doesn't know what he wants."
            jump auresChainEnd
        "\"Talk to him about it.\"":
            if selfish > 0:
                #voice au_puz4
                show aures soulless
                au "I should talk to him? I will try."
                voice "auq4-51"
                au "What do you wish for? You don't really want to leave me, right? You want to stay here?"
                voice "miq4-24"
                show minoru neutral
                mi "What?! Of course I want to leave! You killed me!"
                "Aures seems to snap."
                jump auresChainEnd
            else:
                #voice au_puz2
                show aures soulless
                au "I should talk to him? I will try."
                voice "auq4-51"
                au "What do you wish for? You don't really want to leave me, right? You want to stay here?"
                jump auresHappyEnd
label auresHappyEnd:
    voice "miq4-25"
    show minoru neutral
    mi "I want to leave... but I think you do need me. And I think I want to help you. It seems like something that I should do."
    voice "auq4-52"
    show aures laughing
    au "I'm so happy to hear you say that! I promise you I will ensure nothing bad ever happens to us again!"
    "Aures clings to Minoru's arm again, but Minoru doesn't struggle to get away this time."
    voice "miq4-26"
    mi "I think we should get to know each other a bit more. I don't really know anything about you."
    "You leave as they start a conversation over tea that Aures makes."
    $auresQuestState += 1
    $ aures_good = True
    jump aures_reflection

label auresChainEnd:
    voice "auq4-53"
    show aures laughing
    au "Ohohohohohoho! That is quite wonderful!"
    "Aures quickly grabs some chains from across the room and restrains Minoru with them."
    voice "miq4-27"
    show minoru neutral
    mi "Wait, what are you doing? You can't keep me here! This isn't right!"
    voice "miq4-28"
    "You leave the room as Minoru cries out in vain for help."
    $auresQuestState += 1
    $ aures_good = False
    jump aures_reflection
