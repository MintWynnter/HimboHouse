label herman_hub:

    #unqiue greeting

label herman_convohub:

    menu:

        "\"About your death, Rory...\"" if herman_queststate is 10 and not herman_justgotfetch:
            jump herman_persuasion

        "Magically get the bourbon." if herman_queststate is 1:
            $ herman_queststate = 2
            call screen minimap()

        "\"About Elizabeth...\"" if elizabeth_queststate is 2 and herman_queststate > 1:
            jump herman_elizabeth

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
