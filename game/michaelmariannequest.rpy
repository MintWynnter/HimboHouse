label marianne_bedroom:

    #show whatever bg i don't remember the syntax

    if marianne_queststate > 0:
        #play greeting
        jump marianne_hub

    if marianne_queststate is 0:
        jump marianne_intro


label marianne_intro:
    "As you approach the bedroom, the crackle of a radio peaks over the sound of soulful jazz."

    menu:
        "Faint light trickles out of the bedroom, its door invitingly ajar."

        "Peek into the room.":
            "You stand respectfully under the doorjamb and peer inside."
            "The music brings life to an otherwise subdued bedroom — its warm, creamy colors cushioning the brass of the leading cornet."
            "The place is vacant, but very lived in."
            "There are shoes scattered across the floor—ladies shoes, high heels. Fancy looking."
            "Out of the wardrobe in the corner of the room, frilly, colorful dresses are spilling out, as if trying to escape its confines and find their way to freedom."
            #voice maq6-01
            ma "You gonna stand there forever, or are you gonna come in?"
        "Go into the room.":
            "The music brings life to an otherwise subdued bedroom — its warm, creamy colors cushioning the brass of the leading cornet."
            "The place is vacant, but very lived in."
            "There are shoes scattered across the floor—ladies shoes, a few fancy looking dresses trickling out of the wardrobe."
            "The mirror on the dresser has a few scribbles in what appears to be blood."
            "XOXO Marianne."
            "Closer inspection, though, yields the truth: it’s just lipstick."
            "There’s even a small kiss mark right at the corner."
            "At the window, curtains flap, billowing in the wind, the cold night air chilling your bones."
        "Leave it alone.":
            "Best not to disturb it."
            #voice maq6-02
            ma "Boo."
            "Over your shoulder a clear voice rings and you jump with shock."
            "When you turn, there’s no one behind you."
            #voice maq6-03
            ma "Freaky, innit? Gosh, y'all Living are so impressionable. It never gets old."

    "The air slowly shifts."
    "A shiver runs up your spine as an amused looking woman materializes into existence."
    #voice maq6-04
    show marianne smile
    ma "Sorry it took me so long, hon, I had to go make myself presentable."
    #voice ma_uni
    show marianne happysad
    ma "I wasn’t really ready for company—we don’t get a lot of visitors out here in the sticks."
    #voice maq6-05
    show marianne playful1
    ma "Y'all didn’t even give me time to powder my nose."
    "She pouts, but it’s short-lived, as the irrepressible smile returns full force."
    #voice maq6-06
    show marianne playful2
    ma "So tell me: What brings you to our lil’ neck of the woods?"
    #voice ma_puz
    show marianne playful1
    ma "You lookin’ to move in?"
    #voice ma_hap
    show marianne thoughtful
    ma "Place ain’t much to look at, but it’s got good bones."
    #voice maq6-07
    show marianne smile
    ma "Sometimes all it takes is a fresh coat of paint and you get a whole new house."
    "She takes a drag of her cigarette, her nose wrinkling ever-so-slightly as she lets out a peal of smoke."
    #voice maq6-08
    show marianne happysad
    ma "Kind of like people."
    "She floats up and down for a few seconds, her brown eyes taking you in."
    #voice maq6-09
    show marianne playful2
    ma "You okay there, sugar…? Ya look like death warmed over."
    #voice maq6-10
    show marianne playful1

    menu:
        ma "Don’t tell me you’re scared of lil’ ol’ me!"

        "\"Yes.\"":
            "She gasps, brows furrowing briefly before the grin returns."
            #voice maq6-11
            show marianne thoughtful
            ma "No! Really? Oh, wait ‘til you meet the others then. You’re in for a doozy."

        "\"No.\"":
            #voice maq6-12
            show marianne playful2
            ma "Maybe you should be. There ain’t much you could do to me and a whole load of harm I could do to you."
            #voice ma_puz
            show marianne thoughtful
            ma "Or maybe not me personally, but there’s other less… congenial ghosts around."

        "\"Aren’t you scared of me?\"":
            #voice maq6-13
            show marianne smile
            ma "I’m dead, honey. Fear is a luxury for the living."
            #voice ma_dis
            show marianne thoughtful
            ma "You could stab me a couple of times and you’d only hurt yourself."

    "She stretches out her hand."
    $ marianne_name = "Marianne"
    #voice maq6-14
    show marianne smile

    menu:
        ma "Marianne. Marianne Dixon, the bellest beau at the ball."

        "Take her hand.":
            "You expected her grip to be colder. It is firm, and it is warm."
            "There is warmth in her. You can see it in her smile."
            "But not quite in her eyes."
        "Refuse her hand.":
            "She raises her brows expectantly."
            #voice maq6-15
            show marianne happysad
            ma "What, ghost got your tongue? Ghost got your elbow? Huh?"
            #voice ma_hap
            show marianne playful1
            ma "I don’t bite, you know."
            #voice maq6-16
            show marianne thoughtful
            ma "The only thing with any bite in this here mansion is the absinthe."
        "\"What’s your deal, ghost?\"":
            "She crooks an eyebrow."
            #voice maq6-17
            show marianne thoughtful
            ma "My deal? My, my, are we ever so… scrutinary."
            #voice ma_dis
            show marianne thoughtful
            ma "Hardly the right way to talk to a lady, besides."

    #voice maq6-18
    show marianne playful2
    ma "Anyway, it’s a pleasure to make some kind of acquaintance with ya, whoever you are."

    $ marianne_queststate = 1


    #voice maq6-19
    show marianne playful1
    ma "If ya need me, I’ll be here, living my best death."

    jump marianne_hub
    # go to the conversation hub

label marianne_startquest:

    $ marianne_queststate = 2

    #voice maq6-20
    show marianne playful2
    ma "Aw, you’re spoilin’ me something rotten, hun."
    #voice ma_hap
    show marianne smile
    ma "I’m right as rain, far as I can think."
    "She taps her chin."
    #voice maq6-21
    show marianne thoughtful
    ma "Well, now that you’ve got me thinking, let me pick your brain right quick."
    #voice maq6-22
    show marianne happysad
    menu:
        ma "Hear that jazz? How’s it feel to ya?"

        "\"It feels nostalgic.\"":
            #voice ma_sad
            show marianne smile
            ma "We’re a great many years from the roaring 20s, you know."
            #voice maq6-23
            show marianne sad
            ma "Sometimes, it’s hard not to want to go back."
            "She sits back, closes her eyes, and lets the music settle into her."
            #voice maq6-24
            show marianne playful2
            ma "Yup, nostalgic."

        "\"It feels romantic.\"":
            #voice maq6-25
            show marianne smile
            ma "There’s a romance to every place you haven’t been."
            #voice ma_puz
            show marianne thoughtful
            ma "Till you see for yourself, it could be anything."
            #voice ma_uni
            show marianne playful2
            ma "May as well be pretty, then."
            "She sits back, closes her eyes, and lets the music settle into her."
            #voice maq6-26
            show marianne playful2
            ma "Yup, romantic."

        "\"It feels mournful.\"":
            #voice maq6-27
            show marianne sad
            ma "It certainly makes ya feel like you’re missing something you never had."
            #voice ma_puz
            show marianne thoughtful
            ma "Can’t quite put my finger on how I mean by that, but I’m glad ya feel it, too."
            "She sits back, closes her eyes, and lets the music settle into her."
            #voice maq6-28
            show marianne playful2
            ma "Yeah, mournful."

    "Her eyes flash back open as she composes herself again."
    #voice maq6-29
    show marianne thoughtful
    ma "Y’know, I’m dwelling on it, and maybe there is something you can do for me."
    #voice ma_lgi
    show marianne happysad
    ma "Ain’t nothing too intense, you look like you can handle it."
    #voice ma_puz
    show marianne thoughtful
    ma "I had one of those fancy, newfangled…"
    "She looks for the word."
    #voice ma_hap
    show marianne smile
    ma "Camcorder."
    #voice ma_dis
    show marianne thoughtful
    ma "I must have misplaced it somewhere around here."
    #voice ma_ner
    show marianne thoughtful
    ma "Here is an awfully big place, don’t get me wrong."
    #voice maq6-30
    show marianne smile

    menu:
        ma "But would you mind keeping an eye out for it anyway?"

        "\"I’m happy to look for it.\"":
            #voice maq6-31
            show marianne playful2
            ma "Why, bless your heart."
            #voice ma_hap
            show marianne smile
            ma "I’m awful grateful for it, honest!"
            #voice maq6-32
            show marianne playful1
            ma "Tell ya what, there’s a bottle of bourbon in the lounge. It’s on me."
            #voice ma_ann
            show marianne thoughtful
            ma "Supposing Herman lets you near it."

        "\"Can ghosts even be seen on a camera?\"":
            #voice maq6-33
            show marianne thoughtful
            ma "Suppose that’s what I’m itching to find out."
            #voice ma_hap
            show marianne smile
            ma "I’m mighty curious to see how this —"
            "She tosses back her hair and bats her lashes."
            #voice ma_lgi
            show marianne playful1
            ma " — looks on film. Something tells me I’d be a natural."

        "\"I’m not particularly interested in a scavenger hunt.\"":
            #voice maq6-34
            show marianne happysad
            ma "S’pose that’s hardly why you’re here."
            #voice ma_ann
            show marianne thoughtful
            ma "That is, if you have much of a reason to be here at all."

    #voice ma_hap
    show marianne smile
    ma "Anyway, just keep your eyes peeled, holler if ya see it."
    #voice maq6-35
    show marianne happysad
    ma "That’s all I can ask of ya, take the time it takes."

    jump marianne_hub

label marianne_abouttoleave:

    $ marianne_queststate = 2.5

    "The voice in the back of your head pipes up."

    ab "Marianne. I know her, I think."

    ab "She seems familiar, although she is not from my time."

    ab "I cannot place it, but I must tell you:"

    ab "She is at once deceitful —"

    ab "— and overflowing with kindness."

    ab "Treat this girl well, won’t you?"

    ab "Perhaps that’s not for me to ask."

    ab "Never mind, then. On with your business."

    call screen minimap()

label marianne_presper:

    #voice drq6-01
    show presper neutral
    dr "Aha, that I have."
    #voice drq6-02
    show presper furrowed
    dr "Although I regret to inform you, it is in not-so-good condition."

    hide presper
    "Presper ambles to a distant shelf and outstretches his arm."
    "Off the top shelf tumbles the camcorder, battered and busted."

    #voice drq6-03
    show presper neutral
    dr "Tumbled down here some years ago, but I don’t let any good electronic device go to waste these days."
    "He fiddles with each of the knobs, switches, and dials."
    #voice drq6-04
    show presper neutral
    dr "Still in working order, you’ll be happy to hear."
    #voice drq6-05
    show presper curious
    dr "Give me just another moment with it."
    "He sits at a workbench and unsheathes a number of tools."
    "Pliers, screwdrivers, epoxy… even some of the surgical tools Presper used on you earlier."
    "As he picks away at the camcorder, he mentions:"
    #voice drq6-06
    show presper furrowed
    dr "You know, this is Marianne’s, if I am not mistaken."
    #voice drq6-07
    show presper furrowed
    dr "That’s certainly her in the footage."
    #voice drq6-08
    show presper furrowed
    menu:
        dr "Just about a year ago, if the metadata is anything to go by."

        "\"Isn’t Marianne from the Jazz Age or something?\"":
            #voice drq6-09
            show presper curious
            dr "She certainly looks the part, but I don’t think they had video cameras like these in the 1920s."
            #voice drq6-10
            show presper neutral
            dr "Then again, I’ve been cooped up here for quite a while, so my perception of time is a bit askew."
            #voice drq6-11
            show presper curious
            dr "What did they have then? Radios? Gramophones? Ach, neither here nor there."
        "\"How do you know Marianne?\"":
            "His voice tightens."
            #voice drq6-12
            show presper furrowed
            dr "Ach, I can hear everyone from down here, at one time or another."
            #voice drq6-13
            show presper neutral
            dr "I will peek my head out on occasion, if only to survey the state of the place."
            #voice drq6-14
            show presper furrowed
            dr "Marianne is one of many, nothing more."
        "\"What the heck is metadata?\"":
            #voice drq6-15
            show presper neutral
            dr "Metadata: data about data. Information the computer keeps about a file."
            #voice drq6-16
            show presper neutral
            dr "In our case, it’s how long the video is, when the video was recorded, on what device it was recorded…"
            #voice drq6-17
            show presper neutral
            dr "Things like that. Metadata."

    #voice drq6-18
    show presper curious
    dr "Point is, this video is only from last year."
    #voice drq6-19
    show presper neutral
    dr "And there’s Marianne. Or, at least someone who looks a lot like her."
    #voice drq6-20
    show presper neutral
    dr "Before I let you have this:"
    #voice drq6-21
    show presper concerned
    menu:
        dr "What do you think of that girl?"
        "\"She’s been nothing but light-hearted and kind.\"":
            jump presper_doesnotmatterlol
        "\"She’s clearly lying to everyone. She’s duplicitous.\"":
            jump presper_doesnotmatterlol
        "\"I’m just doing her bidding. I don’t dwell on her.\"":
            jump presper_doesnotmatterlol

label presper_doesnotmatterlol:

    "A moment later, the old man places the refurbished camcorder in your hand."
    #voice drq6-22
    show presper neutral
    dr "Good answer. We’ll leave it at that."

    $ marianne_queststate = 3

    jump presper_hub

label marianne_gotcamcorder:

    #voice maq6-36
    show marianne playful2
    ma "Oh, mighty gracious of you!"
    #voice ma_puz
    show marianne playful1
    ma "Give it here, won’t you?"
    "She takes the camcorder and nestles it in her palm."
    "She mumbles to herself, decidedly out of character:"
    #voice maq6-37
    show marianne happysad
    ma "Man, get a load of this thing."
    "She sits there in silence for about a minute before she acknowledges you again."
    "When she does, her normally pervasive smile returns."
    #voice maq6-38
    show marianne smile
    ma "Spoilin’ me rotten you are, as I say."
    "She eyes you for a moment."
    #voice maq6-39
    show marianne happysad
    menu:
        ma "You look like you’ve got something to say."

        "\"Are you not really from the Jazz Age?\"":
            "She furrows her brow."
            #voice maq6-40
            show marianne sad
            ma "What, am I not convincingly high-falootin’ enough for ya?"
            #voice maq6-41
            show marianne thoughtful
            ma "Is all the glitz not glitzy enough? Hm? How about the glamor — not up to par?"
            #voice maq6-42
            show marianne thoughtful
            ma "Are you not really a shambling, half-functional walking corpse?"

        "\"Why are you lying to everyone about who you are?\"":
            "Her eyes narrow."
            #voice maq6-43
            show marianne sad
            ma "Don’t take the tone with me, now."
            #voice maq6-44
            show marianne thoughtful
            ma "I don’t know what idea you’ve got in your head, but it ain’t worth pondering."
            #voice maq6-45
            show marianne thoughtful
            ma "What the hell is it your business, anyway, zombie?"

        "\"… No, not particularly.\"":
            "She squints her eyes."
            show marianne thoughtful
            ma "Hmph."
            #voice maq6-46
            show marianne sad
            ma "Everything’s that peachy-keen, huh?"
            #voice maq6-47
            show marianne thoughtful
            ma "I’m sure this thing was just hiding in plain sight — silly ol’ me must’ve just missed it."
            #voice maq6-48
            show marianne thoughtful
            ma "Leave it to dumb ol’ Da—"

    "She stops herself — and takes a deep breath."
    #voice maq6-49
    show marianne sad
    ma "You wanna know who I am?"
    "She clears her throat."
    #voice maq6-50
    show marianne sad
    ma "Pour a glass and take a gander."

    "She pats the spot beside her on the bed and loads the camcorder’s footage."
    "She taps a button and the screen’s static clears to reveal the foyer of the mansion."
    "It looks much the same as you witnessed when you entered — decrepit furniture, warped wood, all caked in a thin layer of dust."
    "What differs are the myriad decorations and warm yellow lights that theme the place as a speakeasy."
    "In fact, on closer inspection, it looks just about like it could play the part."
    "The figures dancing and cavorting in the frame seem right at home there, outfitted in pinstripe suits and glitzy dresses."
    "Hot jazz, frenetic and vibrant, sets the pace for their footwork, some of whom trot across the room with a well-rehearsed choreography."
    menu:
        "It’s a party, and a lively one at that."

        "\"Looks swingin’.\"":
            jump marianne_alsodoesntmatterlol

        "\"Looks busy.\"":
            jump marianne_alsodoesntmatterlol

        "\"Looks like a drag.\"":
            jump marianne_alsodoesntmatterlol

label marianne_alsodoesntmatterlol:

    "The only presence that betrays a complete recreation of a Jazz Age speakeasy are the copious red plastic cups in the hand of each partygoer."
    #voice ma_dis
    show marianne playful2
    ma "We broke most of the champagne glasses we bought within the hour."
    #voice ma_hap
    show marianne smile
    ma "Had to make do with what we had — them’s the brakes."
    "Suddenly, a girl with a beaming smile strides into frame. She looks right into the camera, tilts her head, and waves hello."
    #voice maq6-51
    show marianne happysad
    ma "Marianne."
    "Sure enough, her dress is identical to the ghost beside you."
    "The same pearl necklace. The same pearl headdress."
    "The same elegant dress."
    "Even the shades of lipstick match precisely."
    #voice ma_sad
    show marianne happysad
    ma "Marianne, the one and only."
    #voice maq6-52
    show marianne happysad
    menu:
        ma "That smile could power a suburb, it’s so dang electric."

        "\"It is a spectacular smile.\"":
            #voice ma_ner
            show marianne happysad
            ma "You’re telling me. I couldn’t match it if I tried."
            #voice ma_hap
            show marianne smile
            ma "Although I’ve gotten close."
            #voice ma_dis
            show marianne happysad
            ma "But it’s not just the smile."

        "\"A bit showy, don’t you think?\"":
            #voice ma_uni
            show marianne thoughtful
            ma "Showy? Sure, and it’s a hell of a show."
            #voice ma_dis
            show marianne happysad
            ma "But it’s not just the smile."

        "\"I find that kind of enthusiasm unnerving.\"":
            #voice ma_ann
            show marianne thoughtful
            ma "You wouldn’t feel that way if you were in the room with her."
            #voice ma_dis
            show marianne happysad
            ma "Because it wasn’t just the smile…"

    #voice ma_sad
    show marianne happysad
    ma "She was the whole package."
    "The girl in the frame bats her eyelashes and lets out a laugh."
    "She speaks into the camera, but her words are drowned out by the voices around her and by the music."
    #voice maq6-53
    show marianne happysad
    ma "A real belle of the ball. So full of life. So… happy."
    "The camera swings to focus on another girl, one much further back in the crowd."
    "Her face is pale. Even from the other end of the room, you can see beads of sweat form on her forehead."
    "She lacks the same decadenat regalia as the other partygoers."
    "She locks eyes with the camera and forces a smile before the camera pans back to Marianne."
    #voice maq6-54
    show marianne sad
    ma "You wanna know who I am? Well, that was me."
    #voice ma_dis
    show marianne sad
    menu:
        ma "In the corner, there, sweating bullets."

        "\"Were you nervous?\"":
            #voice ma_ann
            show marianne sad
            ma "Sure, and even that’s an understatement."
            #voice ma_ner
            show marianne sad
            ma "But I don’t sweat when I’m nervous. I stutter."
        "\"Were you sick?\"":
            #voice ma_sad
            show marianne sad
            ma "No, I was right as rain."
        "\"Did you see a ghost?\"":
            #voice ma_uni
            show marianne sad
            ma "If Arabella was here, she certainly didn’t make an appearance."
            #voice ma_ner
            show marianne sad
            ma "No, we were spared frights like that."

    #voice maq6-55
    show marianne happysad
    ma "Nope, I set up this whole party. The venue, the decorations."
    #voice ma_ann
    show marianne playful2
    ma "I cannot tell you how much awful, grating vaudeville music I sat through trying to make a playlist."
    #voice maq6-56
    show marianne happysad
    ma "Hell, I even made the damn dress."
    "The camera is still focused on the real Marianne."
    "Her hands are on her knees, swinging them back and forth."
    "The sequined dress sparkles as she sways."
    menu:
        "The girl in the back looks on, tightly wound and wide-eyed."

        "\"Where’s your dress, then?\"":
            #voice ma_dis
            show marianne thoughtful
            ma "Didn’t have the time. Party planning, supply shopping…"
            #voice ma_uni
            show marianne thoughtful
            ma "Took that whole week prior to even learn to sew."
            #voice ma_ann
            show marianne sad
            ma "And I didn’t take to it quickly. Why?"
            #voice maq6-57
            show marianne sad
            ma "Lazy, incompetent, or distractable? Take your pick."
        "\"Why didn’t you wear it, then?\"":
            #voice ma_sad
            show marianne sad
            ma "I couldn’t. It wouldn’t look right on me."
            #voice maq6-58
            show marianne thoughtful
            ma "Plus, imagine me striding into a party all glammed up like that."
            #voice ma_ann
            show marianne thoughtful
            ma "I’d look like a pretentious prick."
            #voice ma_ner
            show marianne happysad
            ma "Not that she does, she rocks it."
            #voice ma_dis
            show marianne happysad
            ma "And besides, I offered."
        "\"She looks better in it, anyway.\"":
            #voice ma_ann
            show marianne thoughtful
            ma "Boy, thanks a lot."
            #voice ma_dis
            show marianne thoughtful
            ma "I thought losing weight would turn things around."
            #voice maq6-59
            show marianne happysad
            ma "But I guess even shedding 100% of your mass and going fully incorporeal still doesn’t cut it."

    "The camera’s focus starts to fade away from Marianne and toward the crowd at large."
    "As it does, Marianne’s face softens."
    "And the smile disappears."
    "For a few moments, she looks almost contemplative."
    "Her jaw tightens, and her stare goes blank."
    "The ghost beside you stares into her face."
    "Her nose scrunches, and she scoffs."
    #voice ma_ner
    show marianne sad
    ma "Ain’t never seen her like that."
    #voice ma_puz
    show marianne sad
    ma "Is she…"
    #voice maq6-60
    show marianne sad
    menu:
        ma "Why does she look so sad?"

        "\"Maybe she was sad.\"":
            #voice maq6-61
            show marianne happysad
            ma "Marianne? Ha. That girl wouldn't know sadness from a teacup."
            #voice ma_hap
            show marianne smile
            ma "Her momma used to say she'd been born laughing."
            #voice ma_dis
            show marianne thoughtful
            ma "My momma said I'd scream the house down if I didn't have my way."
        "\"Maybe you didn't know her that well.\"":
            #voice maq6-62
            show marianne happysad
            ma "Oh, I knew her, alright. "

            show marianne playful1
            ma "Sometimes I think I knew her better than I knew myself which ain't saying much because there was so much more of her than there was of me."
            #voice ma_uni
            show marianne smile
            ma "She was always larger than life."
        "\"What do you think?\"":
            #voice ma_puz
            show marianne thoughtful
            ma "Maybe she was ill…?"
            #voice ma_dis
            show marianne thoughtful
            ma "She didn't take care of herself enough."
            #voice maq6-63
            show marianne happysad
            ma "She was always running herself ragged, running up and down town doing things for everyone."
            #voice ma_sad
            show marianne happysad
            ma "She was beloved, Marianne."
            #voice ma_dis
            show marianne sad
            ma "Always a smile on her face."

    "The girl in the sequin dress shakes herself a little, and the smile comes back."
    "Albeit, it reemerges not quite as brightly."
    #voice maq6-64
    show marianne happysad
    ma "See? I told you. Must've been tired, poor girl."
    "The ghost speaks with a certain unease."
    "The camera shifts back to the pale girl, who looks better than before."
    "She is in conversation with a few other partygoers, whose outfits run the gamut on commitment to the time period."
    "She is nodding her head gently to the music."
    "And, perhaps most importantly, she now holds a red plastic cup."
    "For any or all of these reasons — she is smiling."
    "Sweat and all."
    #voice maq6-65
    show marianne sad
    menu:
        ma "Oh, wow. I look–"

        "\"Happy?\"":
            jump marianne_nothingisrealrealityisasuggestion
        "\"Relieved?\"":
            jump marianne_nothingisrealrealityisasuggestion
        "\"Like Marianne?\"":
            jump marianne_nothingisrealrealityisasuggestion

label marianne_nothingisrealrealityisasuggestion:

    "The ghost ignores your response. Her eyes remain fixed to the screen."
    "The pale girl catches sight of the camera."
    "She waves her hands."
    "As she does, her red plastic cup spills over one of the adjacent partygoers."
    "In an instant, the smile vanishes."
    "Next to you, the ghost stiffens, color rising to her cheeks."
    #voice maq6-66
    show marianne sad
    ma "I'd forgotten about that."
    "The reaction of the girl on the screen is much the same."
    "The girl’s paleness is overcome with a deep red blush as she bows her head and hurries offscreen."
    #voice maq6-67
    show marianne sad
    ma "That's when I left. I was mortified. I wanted the ground to swallow me whole."
    #voice maq6-68
    show marianne sad
    ma "And, in a sense, it did. I went into the basement."
    #voice ma_uni
    show marianne happysad
    ma "Told them I was grabbing more liquor."
    #voice ma_dis
    show marianne happysad
    ma "But I just needed to escape the humiliation."
    #voice ma_sad
    show marianne sad
    ma "Instead, I —"
    "For the first time in the video, the voices of some of the partygoers overpower the jazz that plays overhead."
    "Beckoning, they call, \"Daisy!\""
    "The girl in the sequin dress calls the loudest."
    "The ghost beside you recoils at the name, but watches intently anyway."
    #voice maq6-69
    show marianne happysad
    ma "Didn’t know she was calling to me."

    show marianne happysad
    ma "Must have shut the hatch behind me by that point."
    #voice maq6-70
    show marianne sad
    ma "Leave it to me to abandon my friends when they’re just trying to help."
    #voice maq6-71
    show marianne sad
    menu:
        ma "What is wrong with me?"

        "\"You’re too much of a tryhard.\"":
            jump marianne_lmfao
        "\"You don’t value yourself at all.\"":
            jump marianne_lmfao
        "\"Nothing, as far as I can tell.\"":
            jump marianne_lmfao
label marianne_lmfao:

    "The ghost beside you — Daisy — clasps the camcorder tightly."
    "The video cuts out."
    #voice ma_ann
    show marianne thoughtful
    ma "I knew I shouldn’t have watched this damn thing."
    #voice ma_sad
    show marianne thoughtful
    ma "It was better off lost."
    #voice maq6-72
    show marianne thoughtful
    ma "I don’t need video evidence to show what a damn fool I am."
    "She lifts the camcorder and rears back her arm."
    menu:
        "She wants to throw it to the floor."

        "\"Go ahead, break it. Don’t linger on the past.\"":
            "She follows through with her throw."
            "The camcorder shatters as it hits the ground."
            "Bits of plastic and aluminum fly in every direction."
            "A piece of metal lodges into your cheek. A brown fluid quietly seeps out of the wound."
            "Daisy puts her head in her hands."

        "\"Keep it. It’s worth remembering, even if it’s painful.\"":
            "Her arm shakes."
            "And then it lowers, gently."
            "Daisy places the camcorder on the bed and puts her head in her hands."

        "\"Keep it. I went through the trouble to get it.\"":
            "Her arm shakes."
            "And then it lowers, gently."
            "Daisy places the camcorder on the bed and puts her head in her hands."

    #voice maq6-73
    show marianne happysad
    ma "So what if I’m a phony?"
    #voice maq6-74
    show marianne happysad
    ma "It’s better than being whatever the hell I was."
    #voice maq6-75
    show marianne happysad
    ma "I’m more alive in death as Marianne, than I ever was in life as Daisy."
    "The ghost looks up to you."
    #voice maq6-76
    show marianne sad
    menu:
        ma "So, after all this, what am I supposed to do?"

        "\"Keep living your… life, Marianne.\"":
            $ marianne_queststate = 4
            "Her lips purse. Her eyes dart back and forth."
            "She freezes, swallows, and stands back up."
            #voice maq6-77
            show marianne happysad
            ma "If you reckon that’s best."
            "A smile reemerges, finally."
            #voice maq6-78
            show marianne playful1
            ma "I’ve gotten awfully accustomed to me, anyway."

        "\"Drop the act and be yourself, Daisy.\"":
            $ marianne_queststate = 5
            "Her lips purse. Her eyes dart back and forth."
            "She freezes, swallows, and stands back up."
            #voice maq6-79
            show marianne sad
            ma "That’s a tall ask, you know."
            #voice ma_ner
            show marianne sad
            ma "But, I think that’s right."
            #voice maq6-80
            show marianne sad
            ma "Painful as it is, that’s who I was."
            #voice maq6-81
            show marianne happysad
            ma "And who I ought to — who I should be."

        "\"Be someone new, not someone you thought you should be.\"":
            $ marianne_queststate = 6
            "Her lips purse. Her eyes dart back and forth."
            "She freezes, swallows, and stands back up."
            #voice maq6-82
            show marianne sad
            ma "Someone new."
            #voice maq6-83
            show marianne sad
            ma "Whatever that means."
            "She pauses in thought for another moment."
            #voice maq6-84
            show marianne sad
            ma "This is gonna hurt like hell, isn’t it — soul searching."
            #voice ma_ner
            show marianne happysad
            ma "But I suppose I’ve already been through the worst of it."
            #voice maq6-85
            show marianne happysad
            ma "Someday, I might even be alright again."
            #voice maq6-86
            show marianne happysad
            ma "But I gotta dwell on it for a spell —"
            #voice maq6-87
            show marianne smile
            ma "— for a while."

    #voice maq6-88
    show marianne smile
    ma "Thank you kindly, zombie."
    #voice maq6-89
    show marianne smile
    ma "Thanks for sitting through that."
    #voice maq6-90
    show marianne playful1
    ma "You’re now free to move about the mansion, as they’d say up in the sky."
    #voice maq6-91
    show marianne happysad
    ma "I’ll be here. Take the time it takes."

    jump marianne_hub
