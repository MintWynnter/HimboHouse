label herman_hub:

    show herman neutral
    with dissolve

    #unqiue greeting

label herman_convohub:

    menu:

        "\"About your death, Rory...\"" if herman_queststate is 10 and not herman_justgotfetch:
            jump herman_persuasion

        #"Magically get the bourbon." if herman_queststate is 1:
        #    $ herman_queststate = 2
        #    call screen minimap()

        "\"About Elizabeth...\"" if elizabeth_queststate is 2 and herman_queststate > 1:
            jump herman_elizabeth

        "\"Herman, I could use your help with a map.\"" if elizabeth_queststate is 4 and q5_location is 2:
            jump herman_elizabethtwo

        "\"I have some questions for you, Rory.\"":
            if herman_queststate is 1:
                jump herman_convohub_rebuff
            if herman_attitude >= 0:
                jump herman_questionhub
            else:
                he "Y'ain't no friend of mine, so I ain't entertaining your particular curiosities."
                jump herman_convohub




        "Search the lounge for information regarding Lysander's condition." if lysander_queststate > 1 and lysander_queststate < 5:
            jump lysander_lounge

        "Check the lounge for information on Arabella." if q3_state is 1 and not q3_doctor_journal:
            jump arabella_doctorjournal

        "\"What the hell just happened? Why isn't the room destroyed? What happened to the weird voice?\"" if herman_queststate is 7:
            #voice "heht-06"
            he "Young'n, I ain't got no idea whatch're on about. Are you sure you weren’t dropped on your head as a baby or something?"
            jump herman_convohub

        "\"Who is Vorvodoss?\"" if herman_vorvodossmentioned:
            #voice "heht-07"
            he "Oh you’ve awakened, did ya? The Eater of Souls is one of the true gods. If you’re interested I have a book right here if you’d like to talk about how to save your soul from eternal limbo by feeding the true lord and master."
            #voice "heht-08"
            he "With just the small donation of your eternal soul, you would be makin a wonderful contribution for the continuation of humanity’s existence. Act now and for the low low price of your void essence, we’ll also throw in a millennia of..."
            jump herman_convohub

        "Walk away.":
            if herman_questjustfinished:
                jump herman_reflection
            if herman_justgotfetch:
                $ herman_justgotfetch = False
            if herman_justgotrebuffed:
                jump herman_getdunkedon
            # a goodbye line
            call screen minimap()

label herman_persuasion:
    menu:
        "Herman eyes you with suspicion."
        "Show Herman the leaflet. \"See this? The current year is 2023; it has to be well over 100 years since you died.\"" if herman_date:
            jump herman_doubtdate_4

        "Show Herman the piece of newspaper. \"See this? Your obituary in a newspaper from September 7th, 1922.\"" if herman_newspaper:
            jump herman_doubtnewspaper_4

        "\"Rory, you need to accept the truth: Time has moved forward.\"":
            jump herman_doubtnothing_4

label herman_questionhub:
    menu:
        "Herman is all ears."
        "\"Can you tell me more about the mansion?\"":
            #voice "heht-01"
            he "Oh, this beautiful place? This palace of life and freedom? I wish I knew who built it, so I could shake their hand and give them a box of Cubans for making this gorgeous place available to all."
            #voice "heht-02"
            he "Beyond that, I know very little."
            jump herman_questionhub
        "\"Why are you coughing so much?\"":
            #voice "heht-03"
            he "I ate a dag-blasted chicken wing, and I think I got a bone stuck. Nothing major, but gosh DARN it all it won't come out!"
            jump herman_questionhub
        "\"Why do you never leave the lounge?\"" if herman_queststate > 1:
            #voice "heht-04"
            he "Well, where else can I get a drink to try and wash down this dang blasted chicken bone?! Besides, it's comfortable here; best seats in the house, literally!"
            jump herman_questionhub
        "\"I want to talk about something else.\"":
            jump herman_convohub


label herman_convohub_rebuff:
    "He pays no heed to your question."
    "He's waiting on his bourbon."
    jump herman_convohub

label herman_getdunkedon:
    "The voice in your head clears his throat."
    ab "The stubborn old coot."
    ab  "He'll settle for nothing less than photographic evidence, I suspect."
    ab "And if you care so much as to acquire some, I might have a lead of sorts."
    ab "Check the living room. A great many memories are hidden away, there."
    $ herman_justgotrebuffed = False
    call screen minimap()

label herman_elizabeth:
    $ elizabeth_queststate = 3
    $ q5_location = 2
    #voice "heq5-01"
    he "I also heard a scream. I suppose you’ve met our youngest resident here, then?"
    #voice ""
    mc "Do you know her?"
    #voice ""
    he "Not personally, no. She is a familiar face though."
    #voice ""
    he "I feel like I’ve seen her somewhere before during my stay here. So, seeing her here kinda surprised me at first."
    #voice ""
    he "She also ran all across the entire mansion the moment she arrived. So, I believe everybody has seen her."
    #voice ""
    he "She seems to hate us all, so don’t take it to heart."
    #voice ""
    mc "She almost hit me with a book, yes, but she’s not that bad once I got to talk to her."
    "Herman looks surprised."
    #voice ""
    he "Did she finally open up about her situation? And to you, as well!"
    #voice ""
    mc "I wouldn’t exactly call it that."
    #voice ""
    he "So, you’re here as per her request then?"
    "You nod."
    #voice ""
    he "So what does she want from you?"
    #voice ""
    mc "She needs a paper and pen. Do you happen to have any around here?"
    #voice ""
    he "You know very well that’s not what I was asking."
    "Herman stares at you sharply."
    "You’re reminded of Elizabeth’s expression as you told her where you were going."
    menu:
        "Should you really trust this man?"
        "\"She wants to go home, and she wants me to help her escape this mansion.\"":
            "Herman’s eyes widen."
            #voice ""
            mc "What?"
            #voice ""
            he "Nothing, I just didn’t expect you to actually tell me the truth."
            #voice ""
            he "I don’t know if it’s because of naivety, or because you don’t really care about her."
            #voice ""
            he "Do you think it’s a good choice to tell me the truth?"
            #voice ""
            mc "I thought..."
            #voice ""
            he "Well."
            "Herman pulls open a drawer and takes out a quill and paper."
            "You stare at it for a while."
            #voice ""
            he "What? She asked for this, right?"
            #voice ""
            he "Oh, don’t worry, as far as I’m concerned, I shared quite the same thought as you about her."
            "Reluctantly, you take the paper and pen from him."
        "\"I don’t know what you mean. That’s what she sent me for and here I am.\"":
            "Herman laughs."
            #voice ""
            he "You should try to listen more. Her situation is more complicated than just a little girl wanting to draw a pretty picture."
            "Herman pulls open a drawer and takes out a quill and paper."
            "You stare at it for a while."
            #voice ""
            he "What? She asked for this, right?"
            "Reluctantly, you take the paper and pen from him."
        "(Lie) \"That’s... the only thing she asked me.\"":
            "Herman scoffs."
            #voice ""
            he "So by giving her these, she will stop screaming of fear and all of her problems will be solved?"
            #voice ""
            he "I don’t think so."
            "Despite his words, Herman pulls open a drawer and takes out a quill and paper."
            #voice ""
            he "I understand if you have a thing or two to hide, we all do."
            #voice ""
            he "Take this."
            "He hands you the quill and paper."
            #voice ""
            he "If you don’t trust me, then I will trust her in your capable hand."
    #voice ""
    he "Anything else you need?"
    #voice ""
    mc "Do you know what happened to her?"
    #voice ""
    he "Just that she came to this mansion one day, drenched and shivering. I believe she came from the river behind this mansion."
    #voice ""
    he "I had a hunch that she was looking for a way home, but that’s kind of an impossible request, isn’t it?"
    #voice ""
    he "Not only did she come from quite a far place, leaving this mansion, as you know, is not a simple matter."
    #voice ""
    mc "Wait, then, do you know where she came from?"
    #voice ""
    he "Well, she did come from the river, so there’s only one answer to that question."
    #voice ""
    he "As for what brought her to that state, I have some ideas, but I need some time to remember."
    #voice ""
    mc "Alright, I will be back then."
    #voice ""
    he "As you should."
    jump herman_convohub

label herman_elizabethtwo:
    $ elizabeth_queststate = 5
    he "Whatcha want now, can’t ya see I’m busy?"
    mc "Are you familiar with the area around here? I need help with a... map."
    he "Go on and hand it over, let me take’a gander at it."
    "You give the map to Herman."
    he "Does this map belong to that howling lil’coyote?"
    "You nod. You can’t bear to tell him it was you, who’d actually drawn the map."
    he "Another errand? Or..."
    he "Ya need’n something after all?"
    "You nod."
    mc "Tell me everything you know about her."
    he "Ah, straight shoot’n. I figured you’d ask for something."
    he "Wait right’chair."
    "Herman leaves you for a moment."
    "He rummages through some papers and drawers."
    "You listen as he mumbles in between the rustling and noises until he finally returns with some paper on hand."
    he "Plop your peepers at this."
    "Herman hands you a couple of newspaper clippings."
    he "With a big’ol picture like that, she’d be hard to miss even for someone like yourself."
    "On the first paper you see, is a clear picture of Elizabeth, with slightly longer hair, more lively expressions, and less water dripping from her entire being."
    "Under the picture, a sentence ‘HAVE YOU SEEN ME?’ is printed large on the paper."
    "You take out the second paper. On it, in the middle of crowding police, a picture of a woman in her thirties is seen holding a child's jacket."
    "She was entirely disheveled with dried tears and dark circles under her eyes."
    "\"—Was last seen going out of the house at 4 p.m., walking towards the bridge.\""
    "\"It is reported that there was a slight argument between her and the mother before the time she was last seen.\""
    "\"Police are currently investigating—\""
    "The third paper has no picture, only a big headline: ‘SEARCH CALLED OFF’."
    "\"—Being discontinued. The reason is insufficient leads or clues regarding the whereabouts of the missing person.\""
    "\"'I hope you’re happy and safe, I love you so much, and I’m sorry I can’t be a better mother for you,' The mother of the little girl told our editor.\""
    "\"A small message we all hope Elizabeth will read.\""
    "\"The family has decided to move away from their residence but will keep close contact with the police.\""
    "\"The police will still receive any information regarding the missing Elizabeth—\""
    "You read them all carefully. Every gear in your head turns as you process the entire broken messages into one string of story."
    menu:
        he "What’cha reckon?"
        "\"She fell into a river after running away.\"":
            he "Well ya ain’t daft at least."
        "\"Her mother killed her and ran away.\"":
            he "Are you blind or just a sap?"
            he "I reckon it was just a cover-up of an unfortunate incident."
            he "She scampered off and got caught up in something tragic."
            he "She washed up here already chilled off, then her folks moved away from the memories of her and everything else."
        "\"She got lost and ended up here.\"":
            he "Is your brain already ate through!?"
            he "It’s obvious, you nitwit, she scampered off after riling up her folks, and something tragic led her here."
    he "Bless’er heart, must have been like a squirrel in a hoot’s nest."
    mc "I had a feeling about what happened to her, but I didn’t expect it to be like this."
    menu:
        he "So, what’cha gonna do? Not that I care, I’m just nosy."
        "\"I will tell her the truth.\"":
            he "Oh ho?! Now that’s quite ugly of you. I love it!."
            mc "I don’t want to do this. But staying in that state forever will make the truth hurt her even more."
        "\"I can’t show her this, it’s too much for her.\"":
            he "Aw, are ya’ yella after all?"
            mc "She still hasn’t told me the truth. She might be avoiding it or unaware of it."
            mc "I will let her live in her peace for a little longer."
            he "Well, it’ll all come out in the warsh eventually, with or without you meddling."
            "You don’t answer."
        "\"Maybe it’s better for her to stay here.\"":
            he "I’d rather she not, I’m mighty tired of her conniption fits."
            he "I don’t care whatcha do, but you better do somethin about all that yowling!"

    he "If you poke that bear, just keep in mind she’s liable to swat your head clean off."
    menu:
        he "Well, go on and tell me whatcha gonna do, you know I’m just DYIN’ to hear."
        "\"She deserves the truth.\"":
            mc "This is for her own good."
            he "Uh-huh? Because the truth will set you free, so on and so forth?"
        "\"I won’t tell her, it’s too cruel.\"":
            he "Well then why the hell have you been wastin’ my time?!"
        "\"...I have to think this through some more.\"":
            he "Oh don’t worry about it, you’ve got all the time in the world."
            he "Other than you’re quite literally falling apart at the seams as we speak but, why is that anything to concern yourself with?"
            "His voice reeks of sarcasm."

    he "Ya’got choices to make, and for my flippin’ sanity I hope you make the right ones."
    he "Far be it from me to tell ya what to do, but actions, or lack there of, ALWAYS have consequences."
    "Holding the newspaper clippings in your hand, you sigh deeply, thinking of the choice you’re about to make."
    "You shove the papers into your pocket."
    jump herman_convohub
