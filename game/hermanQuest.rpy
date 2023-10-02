label herman_lounge:
    #Dagon you bastard

    scene bg lounge
    show drink
    with fade

    #show whatever bg i don't remember the syntax

    if herman_queststate is 2:
        jump herman_gotbourbon

    if herman_queststate is 4:
        jump herman_return_9

    if herman_queststate is 6:
        jump herman_ringreturn_13

    if herman_queststate > 0:
        #play greeting
        jump herman_hub

    if herman_queststate is 0:
        jump herman_intro

label herman_intro:
    $ herman_queststate = 1
    "As you approach the door to the lounge, the sound of somewhat unnerving yet oddly comforting jazz plays through it."
    "Grasping the beautifully polished handle and pushing the door open, the atmosphere feels inviting."
    "Gentle embers in the fireplace, tables sparkling and neatly arranged for a dinner party, and numerous bottles of various shapes and sizes on the shelves behind the bar."
    # show herman here
    "Despite the grandeur, only one person sits in a chair near the middle of the room in a neatly pressed pin-stripe suit."
    "He taps his foot to the music, pen in hand, his gaze fixated on a booklet."
    "Once across the door's threshold, the man immediately notices you as if you appeared from the void."
    "He stands far taller than most men, and is also rather ample."
    "His wide, toothy smile proudly displays a single gold tooth."
    "Before you can react, he grasps your hand abruptly and begins to shake it with vigor as if attempting to yank your arm off, coughing rudely in your face."
    voice "heq2-01"
    show herman laugh at herman_spot
    he "Well, butter my backside and call me a biscuit; a fresh one!"
    voice "heq2-02"
    show herman happy
    menu:
        he "The name's Herman, but my friends call me Rory, so you'd best call me Rory!"
        "\"Please cover your mouth.\"":
            pass
        "\"Cover your mouth, you're rude.\"":
            pass
        "\"What is wrong with you?!\"":
            pass
    "Herman does not appear to acknowledge what you say, brushing your words aside as if they are meaningless."
    voice "heq2-03"
    show herman happy
    he "Say, friend, y'ain't happen to got a spot of good bourbon, would ya? I got something stuck in my gizzard, and the swill behind the bar just won’t cut it."
    "He coughs again and pulls his hand back from yours to rub his throat."
    menu:
        "\"Hello, sir, I'm happy to be of help.\"":
            $ herman_attitude = herman_attitude + 1
            "As before, Herman ignores your words and grins, grabbing your shoulder while laughing in delight."
            voice "heq2-04"
            show herman happy
            he "What manners, I love it!"
            "As you try to speak, he continues to laugh, his body rumbling... along with your view of the world as he shakes your shoulder."
            "Not paying you any mind, yet again, he rambles on."
            voice "heq2-05"
            show herman happy
            he "Go on and get that bourbon - oh, and don't forget my favorite glass. Take a gander in the ''Ballroom'', I'm certain the porters would have left it there."
            #voice
        "\"No, I do not have any 'good bourbon,' and I'm not here to fetch things for you.\"":
            "Herman takes a step back, adjusting his tie as he looks you once over, finally seeming to notice you for the first time."
            voice "heq2-06"
            show herman happy
            he "Well, I can certainly respect your calm demeanor."
            "He rubs his throat again, covering his mouth and coughing once more."
            voice "heq2-07"
            show herman neutral
            he "However, without that bourbon, I'm not feeling too keen on talking to one of 'your kind' about much'a nothin'. So it seems that, without you fetching, we're at an impasse."
            "With no hesitation, and as graceful as a snake slithering back into the tall grass, he seats himself back in his chair to once again ignore your presence."
            voice "heq2-08"
            show herman happy
            he "Oh, and bring my favorite crystal glass. I can't be seen to be on the nut."
        "Wipe your face and glare at Herman.":
            $ herman_attitude = herman_attitude -1
            voice "he_lhu2"
            show herman neutral
            he "That right there is the stare my momma used to give me when she was mad. Are you mad, little rabbit?"
            "Herman rolls his eyes and wafts his hand in your direction, treating you like a pest."
            voice "heq2-09"
            show herman neutral
            he "You heard what I said. Go on and fetch my giggle water. I don't have time to waste on your tantrum, little rabbit. Oh, and don't you forget to bring my crystal glass, neither."
            "Herman returns to his seat, crossing his ankle onto his knee, and bounces his foot angrily to the music, pen and booklet yet again in hand."

    jump herman_hub

label herman_gotbourbon:
    $ herman_queststate = 10
    $ herman_justgotfetch = True
    "With the bourbon and glass in hand, you again enter the lounge to the same familiar sounds of jazz and sights of the inviting motif."
    "However, this time, Herman is smoking a cigar."
    "The smell is rather pleasant, but sickeningly sweet: a combination of alcohol, polished leather, and tobacco."
    "Herman notices you; standing up, he opens his arms wide as if welcoming a hug, but he does not step closer to you."
    voice "heq2-10"
    show herman laugh
    he "Well, there ya are. I was starting to wonder if you got lost or fell apart!"
    voice "he_hap2"
    show herman happy
    he "I see you found that BEAUTIFUL bourbon, oh, and my favorite glass to boot! My my, so you CAN follow directions after all!"
    "He wafts his hand toward the bar, beckoning you closer as he walks towards it himself."
    voice "heq2-11"
    he "Well, come on, now, let's get that sweet nectar open. I insist we toast to your health after you put in all that 'strenuous' effort."
    menu:
        "Herman pats the top of the bar and slides a dust-covered glass in front of you, a glint of the light bouncing off his gold tooth as he grins."

        "Place Herman's glass on the bar, pull the cork, and pour a modest amount in each glass.":
            jump herman_gotbourbon_modest

        "\"Before that, I have a few questions you need to answer, Rory.\"":
            jump herman_gotbourbon_questions

        "Throw the bourbon and his glass on the floor, shattering both.":
            jump herman_gotbourbon_shatter


label herman_gotbourbon_modest:
    $ herman_attitude = herman_attitude + 1
    "Herman grins ear to ear as he swiftly lifts his glass, nodding his head to you as he raises the glass in your direction."
    voice "heq2-12"
    show herman neutral
    he "A toast to health, and to the start of our magnificent `mahg-NIF-uh-scent` friendship!"
    "He holds his glass toward you still, waiting to clink his glass with yours."
    voice "heq2-13"
    show herman laugh
    he "Oh, in case you didn't know, this is the part where we lightly touch glasses together as a show of trust."
    voice "heq2-14"
    show herman happy
    menu:
        he "I wouldn't expect someone of your... 'condition' and caliber to understand that so figured I'd best explain it."
        "Lift your glass and clink it with his, acknowledging his toast.":
            jump herman_toast_2
        "Leave your glass untouched. \"Sorry, I don't drink, but can you answer some questions for me?\"":
            jump herman_politeask_2

label herman_gotbourbon_questions:
    "Herman's eyebrow lifts over his monocle, his face showing a mix of intrigue and annoyance."
    voice "heq2-15"
    show herman neutral
    he "Well now, perhaps you forget your station, my not-so-alive friend."
    "Herman pauses for a few moments and looks away, rubbing his bearded chin slowly before lowering his eyebrow and looking back, seeming less annoyed."
    voice "heq2-16"
    show herman neutral
    he "However, a bit of kindness on my part is perhaps in order. I might be persuaded to entertain a question or two if you'd 'allow' me to wet my whistle."
    "His gaze shifts towards the glass and bourbon you hold, then back to meet your eyes."
    menu:
        "His look is simultaneously kind and yet unnervingly direct."
        "Bring his glass and bourbon to the bar and pour him a small amount.":
            jump herman_agree_2
        "\"I need you to tell me how you died.\"":
            jump herman_direct_2

label herman_gotbourbon_shatter:
    $ herman_attitude = herman_attitude - 1
    "Herman's eyes widen, his face contorts into a mix of rage and astonishment, quickly looking you dead in the eye as a flood of pure vitriol pours from his mouth like the bourbon slides along the marble floor."
    voice "heq2-17"
    show herman angry
    he "Now WHY you gone an' done sum'in STU-PIT like'dat?!"
    "He storms up to you, the sound of his polished shoes slapping against the floor, his stomach a hair's breadth away from you, yet you cannot feel his presence."
    voice "heq2-18"
    show herman angry
    he "You got some fuck'n NERVE, youngin! I oughta yank mah belt off and beat the GAH-damn TAR outta ya!"
    menu:
        "Herman breathes heavily down at you, his fist clenched and shaking with anger."
        "\"Are you ready to treat me with respect now? I need answers from you.\"":
            jump herman_standup_2
        "\"That is what you get for being rude and demanding!\"":
            jump herman_nasty_2

label herman_standup_2:
    "Herman's eyes seem to glimmer as if a fire burns in him; however, he huffs hard and turns away from you, throwing his cigar to the floor and slamming both of his hands on the bar."
    voice "heq2-23"
    he "You don't think, do you? Do you have ANY idea how long I've been waiting for that bourbon?!"
    "He holds his hand up as if to stop you, shaking his head."
    voice "he_dis3"
    show herman angry
    menu:
        he "Nah, 'course ya don't, ya ain't got nothin' in that damned head of yours to have an idea."
        "\"At least I can admit I'm not alive, unlike you.\"":
            jump herman_honest_2
        "\"Too bad you're too stupid to realize you're dead.\"":
            jump herman_pokethebear_2

label herman_nasty_2:
    "Herman's chest flares out, his teeth showing as he growls his words at you, throwing his cigar on the floor."
    voice "heq2-24"
    show herman angry
    he "Rude? DEMANDING?! You, what the, are you...AAAARGH!"
    "Herman stomps away, slamming his fists on the bar, sliding all the glassware and bottles off the end."
    "With horrible crashing, Herman continues his tantrum before walking back up to you, pointing a finger in your face and grinding his teeth."
    menu:
        "His knuckles pop and crack from how tightly he clenches his fist."

        "\"It seems I've made you a bit angry. Perhaps a drink will... oh wait, there's none left.\"":
            jump herman_pokethebear_2
        "\"Are you ready to take me seriously? You're dead, and we need to figure out why you're stuck here.\"":
            jump herman_honest_2

label herman_agree_2:
    "Herman's stern look slowly melts away as you pour the amber liquid into the glass."
    "He allows you to finish before gently grasping the fine crystal in his fingers and swirling it, his eyes fixed on the glass."
    "Yet, he does not drink."
    voice "heq2-20"
    show herman neutral
    he "So..."
    "He lifts the glass to his nose and smells it, then places it back on the bar."
    "He wags the cigar in his fingers a moment before taking a drag from it and exhaling away from you somewhat."
    voice "heq2-21"
    show herman happy
    he "You're just the right amount of shrewd and polite... I like that. I think you'd make a mighty fine associate, so why don't you and I discuss business before gett'n to your question?"
    "Herman extends his free hand toward you, offering a shake."
    voice "he_puz3"
    show herman neutral
    menu:
        he "Whadda'ya say, 'partner'?"
        "Firmly shake hands with Herman.":
            jump herman_shake_2
        "\"No thank you, I'd rather you answer my questions.\"":
            jump herman_decline_2


label herman_direct_2:

    "Herman's face contorts momentarily before he huffs and leans against the bar."
    voice "heq2-22"
    show herman angry
    he "Ya'aint gonna let this go, are ya? Whatcha gonna do, hold my bourbon ransom until I answer yer fuckin' questions?"
    "Herman looks you up and down, sizing you up like a boxer before a fight."
    "He takes a long draw from his cigar, removing it from his mouth and flicking it across the bar. "
    "He stands up straight, blowing the smoke to the side, then spits on the floor without taking his eyes off yours."
    voice "he_dis2"
    show herman neutral
    he "Ya know, you're not quite as dim as I first thought, and that's mighty high praise if I do say so myself."
    "Herman shoves his free hand out towards you, a smile creeping along his face."
    voice "he_hap2"
    show herman happy
    menu:
        he "I appreciate someone who holds to their convictions. I could use an associate like you! How about we shake on it and talk business?"
        "Firmly shake hands with Herman.":
            jump herman_shake_2
        "\"No thank you, I'd rather you answer my questions.\"":
            jump herman_decline_2
        "\"You're wasting my time, I don't have time for you're nonsense. Rory, you're dead.\"":
            jump herman_honest_2


label herman_toast_2:
    "Herman laughs loudly, nodding his head to you before lifting the glass to his nose and smelling it deeply."
    voice "heq2-19"
    show herman neutral
    he "Ahh, just like my pappy used to make."
    "Herman takes a slow, savoring sip from his glass before lowering it with a look of deep satisfaction, tapping his cigar and ashing on the bar."
    voice ""
    show herman happy
    he "Mmm-MM! Now that's some genuine `gen-u-ine` top-shelf bourbon right there, I tell you what."
    "You take a drink along with Herman."
    jump herman_politeask_2

label herman_politeask_2:
    "Herman sets his glass down on the bar and smiles gently."
    voice "heq2-25"
    show herman happy
    menu:
        he "Go on with your questions. Ol' Rory will be more than happy to oblige a good friend such as yourself."
        "\"How did you die?\"":
            jump herman_politeanswer_2

label herman_pokethebear_2:

    "Herman's hand opens as if to wrap around your neck."
    "But before he acts, he stops short of touching you, looking down at his hand and slowly starting to relax it."
    "He walks back to his chair, seemingly defeated, slamming himself backside-first into it."
    "The chair creaks from the impact. His arms hang limp across the back of it, and his head hangs slightly."
    voice "heq2-33"
    menu:
        he "Just... *sigh* what the hell do you want?"
        "\"I'm here to help you. I HAVE to help you, but I won't play your games to do it.\"":
            jump herman_toughlove_2

label herman_honest_2:
    "Herman's eyes narrow as he looks at you, and then he turns to look at the floor to find his cigar."
    "He picks up the cigar and pops it back in his mouth, walking back to his chair and falling into it with a bit of a slump."
    voice "heq2-34"
    he "Young'n, I dunna give two shits about what you think of me. If you thought you had any chance of getting me to talk about anything you gone and done ruined..."
    "He stops mid-sentence, his eyes searching the air as his face slowly shifts into a sinister smile."
    voice "he_hap2"
    show herman happy
    he "Tell ya what, little rabbit, I'll give you a chance to make this up to me. Your insistence on respect has piqued my interest."
    "Herman leans forward, smashing the lit end of the cigar in the ashtray as he deadeye stares at you."
    "Without breaking focus, he pulls another cigar from the humidor and clips the end with his fingernail."
    "He lights it and takes a few puffs from it."
    voice "he_puz2"
    show herman neutral
    menu:
        he "If you were that willing to earn my ire, I feel compelled to listen to ya. Now, what is this malarky about me being dead?"
        "\"Just as I said, you're dead. I can help you resolve whatever ties you to this mansion.\"":
            jump herman_tothepoint_2

label herman_shake_2:
    "Herman's face seems to brighten, grasping your hand tightly and shakes with such voracity as if to pull your arm from your shoulder."
    voice "heq2-30"
    show herman happy
    he "Well, there we are, we're in business now, haha!"
    "He pulls his hand away, quickly grabbing a glass from over the bar and blowing it out to clean it before snatching the bourbon from you."
    "He pours it into the 'clean' glass, and pushes it in front of you."
    voice "he_uni2"
    show herman neutral
    he "Oh, I almost forgot, you deserve a quality gasper to boot."
    "Herman walks away for a moment and pulls two fresh cigars from the humidor off the table."
    "He returns with a lighter and shoves the cigar into your mouth before you have a chance to agree or refuse."
    "He clips the ends with his dangerously long thumbnail, then lights the end of the cigar for you before lighting his own."
    voice "he_hap5"
    show herman happy
    he "Go on, take a big'ol puff on that Cuban right'char! Don't you let it go to waste now, ya hear?"
    menu:
        "Herman takes a drag from his cigar, grinning a bit as he watches you intently."
        "Take a puff from the cigar; it doesn't taste or feel like anything.":
            jump herman_continue_2
        "Remove the cigar from your mouth. \"Sure, partner, but can we get to questions now?\"":
            jump herman_continue_2

label herman_decline_2:
    $ herman_attitude = herman_attitude - 1
    "Herman's face turns down; he smirks and quickly snuffs the cigar he had onto the bartop."
    voice "he_mad1"
    show herman angry
    menu:
        he "You ain't got no choice in this, young'n. You either shake hands and agree, or you ain't gett'n NOTHIN' outta me, y'understand?"
        "Relent and shake Herman's hand.":
            jump herman_shake_2

label herman_toughlove_2:
    "Herman lifts his gaze to meet yours."
    "The fire in his soul seems to have tempered, leaving a cold heart in its place."
    voice "he_lhu3"
    he "I don'care WHAT you're here to do. I want no fucking part in it. Just leave me the hell alone and git'on."
    "He lazily lifts himself up in the chair, grabbing a new cigar from the humidor."
    menu:
        "He bites the end off it and spits the tip in your direction, sticking the cigar in his mouth and lighting it with the table lighter."
        "\"Stop sulking, and let's get this over with. Tell me what I need to do to convince you of your death.\"":
            jump herman_tothepoint_2

label herman_politeanswer_2:
    "Herman looks at you with confusion, his eyebrows furrowed."
    voice "heq2-26"
    show herman angry
    he "What do you mean, 'how did I die'?"
    "He looks down, patting around his body, then rubs his face and beard."
    voice "he_lch2"
    show herman happy
    he "Ya know, you certainly have an odd sense of humor, but I'll play along since I could use a distraction from this speech."
    menu:
        "Herman waves you over to the chairs near the center of the room, taking what is apparently his favorite seat."
        "Follow and sit across from Herman.":
            jump herman_politequestion_2


label herman_tothepoint_2:

    "Herman takes a puff from his cigar, sliding back down in his chair as he exhales, like a whale blowing as it dives."
    voice "heq2-35"
    show herman angry
    he "So what If I'm dead? Not as if I believe you anyway, but I don't have the energy to beat yer ass after all the time I've spent on this speech."
    "He props his feet up on the table, almost laying down in his chair as he puts one arm behind his head."
    "He continues to smoke his cigar, and thick smoke starts to fill the air."
    voice "he_mad2"
    show herman neutral
    he "You're sure as Satan insistent on this, though. So what can I tell you to get you the hell out of my hair?"
    voice "he_dis2"
    show herman neutral
    menu:
        he "I'm not dead, and unless you can prove otherwise, yer just wastin' your breath."
        "\"You're awfully stubborn. Why do I have to bring you proof?\"":
            jump herman_checkmate_2
        "\"Fine, I'll bring your proof, but afterwards, no more games. Are we in agreement?\"":
            jump herman_game_2

label herman_continue_2:
    "Herman waves you towards the large chairs, taking a seat in his favorite and sitting regally with his elbow propped up."
    voice "heq2-31"
    show herman neutral
    menu:
        he "Well now, let's get down to this business of yours, then we can discuss my business. What questions did you have for me?"
        "Take a seat. \"Do you know that you're dead? You died a long time ago.\"":
            jump herman_politequestion_2
        "Remain standing. \"What would help you realize that you're not alive?\"":
            jump herman_neutralquestion_2

label herman_politequestion_2:
    "Herman ponders a moment, then lifts his eyes and meets yours."
    voice "heq2-27"
    show herman neutral
    he "I'll humor you. Let's say I 'died' as you suggest. How can you prove it?"
    "Herman picks up his pen and twirls it in his fingers before tossing it on the table before you."
    voice "heq2-28"
    show herman neutral
    he "Could I breathe and drink, let alone hold that there pen?"
    "Herman smiles and nods to the pen."
    voice "he_puz3"
    show herman happy
    menu:
        he "Go on, pick it up."
        "Pick up the pen.":
            jump herman_pen_2
        "\"Just moving objects around is something most ghosts can do.\"":
            jump herman_refute_2


label herman_checkmate_2:
    "Herman continues to puff on his cigar, seemingly trying to make the room as uncomfortable as possible with the unnatural amount of smoke that has filled the air."
    voice "he_ann3"
    show herman neutral
    he "Little rabbit, you and I both know you're just as stuck here as I am. So why don't you just scamper off and find whatever the hell you need?"
    voice "he_uni5"
    show herman neutral
    he "I doubt you'll find anything. You're not the first to try, after all."
    menu:
        "He crosses his ankles, shaking his foot to the music, as he sways slightly in his slumped position in the chair, no longer interested in you."
        "\"I'll bring your proof, and we can be done with this.\"":
            jump herman_convohub

label herman_game_2:
    "Herman lifts his head a bit, looking at you as if to laugh, but all he musters is a huff."
    voice "he_mad2"
    show herman angry
    he "Young'n, this ain't no game. You'll find that out soon enough. If I could leave, don'tcha think I would've already?"
    "He shakes his head as it falls back onto his arm, still puffing on his cigar as he shakes his foot."
    voice "he_uni1"
    show herman neutral
    menu:
        he "Ain't nothin' ya can do that ain't been tried already by the others."
        "\"What others?\"":
            jump herman_mumstheword_2
        "\"Whatever, Rory. I'll find your proof.\"":
            jump herman_convohub

label herman_neutralquestion_2:
    "Herman chuckles as he abruptly stands up."
    voice "heq2-32"
    show herman laugh
    he "Not alive? Well, now that's just preposterous! I feel fit as a fiddle, nothing wrong with -"
    "He rubs his throat a bit then stops suddenly, closing his eyes and lowering his hand to his tie to adjust it."
    voice "he_cough3"
    show herman happy
    he "As I was sayin', I'm perfectly healthy, because who would vote a man that's about to chill off into office?"
    "Herman ponders a moment, sitting back down in his chair and looking up at you."
    voice "he_uni5"
    show herman happy
    he "However, I respect those I do business with, which we have yet to discuss."
    menu:
        he "If you're so inclined to stand by this notion of me having 'kicked it,' I'll humor you just once. Show me some proof."
        "\"Why don't you just leave the lounge and go look for yourself?\"":
            jump herman_doubt_2
        "Put out the cigar. \"If I bring proof to you, Rory, will you listen to me?\"":
            jump herman_proof_2

label herman_pen_2:
    "You lift the pen from the table and hold it; it is certainly a real pen."
    "Herman smirks at you, leaning over and propping his elbow up on the arm of his chair, laying his head against his knuckles."
    voice "he_uni2"
    show herman neutral
    menu:
        he "Well, that was a rather short experiment, wouldn't you say?"
        "\"Can you leave a location, such as this room?\"":
            jump herman_doubt_2
        "\"If I bring proof to you, Rory, will you listen to me?\"":
            jump herman_proof_2

label herman_refute_2:
    voice "heq2-29"
    show herman neutral
    he "Oh really, then what about my drinking? If I were dead, where would that sweet liquid gold go?"
    "Herman turns around and looks at the floor with enthusiasm, turning back to you with both eyes wide as if to imply something."
    voice "he_puz2"
    show herman happy
    menu:
        he "I don't see no puddle on the floor, do you? Can you explain that?"
        "\"Not all ghosts are the same, but many cannot leave a location. Can you?\"":
            jump herman_doubt_2

label herman_mumstheword_2:
    "Herman waves his hand lazily to the music as if conducting it."
    voice "heq2-36"
    show herman neutral
    he "If 'HE' doesn't want you to know, then you won't know, and there ain't nothin' else I can tell you about it. Now go before you ask more than you should."
    "With a hard waft of his hand, you are dragged backward by an unseen force towards the door as you hear it swing open."
    "Suddenly, you find yourself outside the lounge; Herman barely waves goodbye to you as the door slams shut in your face."
    #is this even gonna fuckin work
    call screen minimap()

label herman_doubt_2:
    "Herman coughs a bit then looks at you with contempt, leaning back and adjusting his monocle."
    "He takes a long drag from his cigar and puffing a ring back in your direction."
    voice "he_mad4"
    show herman angry
    he "Now, why would I bother with that? I have too much work to accomplish and very little time to do it."
    "Herman takes a sip from his glass, then another puff of his cigar. He grins wide as he leans forward slowly, exhaling smoke at you."
    voice "he_ann4"
    show herman happy
    menu:
        he "So far, you've proven nothin' except you're a sap. Why don't you bring me proof that I'm really some sort of specter and that you have more than moths between them ears."
        "\"I have some questions for you first.\"":
            pass
        "\"Rory, I know I can help you. I'll come back with proof.\"":
            pass

label herman_proof_2:
    "Herman leans forward and ashes his cigar in the ashtray, standing up and putting his hand out to you once more."
    voice "he_uni3"
    show herman happy
    menu:
        he "I'm a man of my word, partner; if you bring me some proof, we can discuss it further."
        "\"I have some questions for you first.\"":
            pass
        "Shake Herman's hand. \"It's a deal, I'll bring you proof.\"":
            pass
    jump herman_convohub



label herman_garden:
    $ herman_date = True
    "Just beside the mansion's back door, you find a folded, damp, sunbleached leaflet from an electronics store."
    "Unfolding the leaflet, you find the year is intact: 2023."
    menu:
        "However, the rest is either smudged beyond recognition or the color has been bleached away."
        "\"This should be more than sufficient to prove to Herman the current year at least.\"":
            pass

    jump lysander_convohub

label herman_bedroom:
    $ herman_newspaper = True
    "Searching the bedroom, you discover a ''Western Star'' newspaper buried amongst other dusty papers."
    "The headline reads \"Former Governor Dead at 68.\" dated September 7th, 1922."
    "The paper is yellow and crumbling; only portions of it remain, but you can read some of the front page that states:"
    "\"... afterwards, Mr. Indigo stated that Mr. Grover had choked on fried chicken provided at the party...\""
    "\"...and while the doctor of the mansion did all he could to save Mr. Grover, it was unfortunate that Mr. Grover could not be resuscitated.\""
    "\"In an exclusive statement after the quick cremation, at the request of Mr. Grover's will...\""
    "\"Mr. Indigo stated: 'Rory was an amazing orator paralleled only by Julius Caesar, my best friend and most of all...'\""
    "Unfortunately, the paper crumbles into dust in your fingers before you can finish reading."
    menu:
        "Only the very top of the paper with the date and headline remain semi-intact."
        "This should be enough evidence to prove to Herman that he died.":
            pass

    jump marianne_convohub


label herman_doubtnothing_4:
    $ herman_queststate = 3
    menu:
        "Rory crooks an eyebrow."
        "People carry the knowledge of the world in their pockets and can communicate with anyone nearly anywhere with the tap of their finger on a pocket-sized super computer.":
            pass
    "Herman's mouth suddenly drops, his cigar, pen, and booklet falling to the floor as his monocle drops from his eye and hangs from his pocket."
    "A sound of sheer astonishment drifts from his lips at your words."
    voice "heq2-40"
    show herman happy
    he "Oh. My. WORD! That right there is the most compelling evidence I have ever heard! Why... why, we need to get this out to the WORLD right away!"
    "He grasps you by your shoulders firmly, his look of amazement slowly fading into something else."
    voice "heq2-41"
    show herman neutral
    he "We've got to... to..."
    "Herman suddenly erupts into a roar of laughter, shaking you violently, his astonished face quickly shifting to happiness."
    voice "heq2-42"
    show herman laugh
    he "Oh!... OH!... Oh, LORD, that's the best thing I've heard in a LONG time. WhoooooWEEE, that's a good story, I tell you what!"
    "He slowly wipes tears from his eyes, his laughter calming a bit as he slaps you firmly on the back."
    voice "he_lch3"
    show herman laugh
    he "My friend, you've given me a wonderful present - the gift of laughter! Imagine that: a \"super\" woman so small you can carry her around in your pocket, knows everything in the world AND just by tapping her she can talk to ANYONE."
    voice "he_hap1"
    he "That's straight out of them \"science fiction\" novels like 'Metropolis' I've heard about."
    "As Herman continues to chuckle a bit, he adjusts his monocle and dusts his suit off."

    menu:
        "He collects his things and pops his cigar back in his mouth, taking a seat in his chair once again to resume his writing."

        "\"That's it? You just shrug it off as if it means nothing?!\"":
            jump herman_angry_4
        "\"What else would convince you?\"":
            jump herman_polite_4

label herman_doubtdate_4:
    $ herman_queststate = 3
    "Herman sets his booklet down, then snatches the leaflet from your hand, adjusting the monocle with his pen between his fingers and taking a few small puffs from his cigar."
    voice "heq2-37"
    show herman neutral
    he "Now let me see here, hmm, yes, yes."
    "He slowly stands from his chair, still studying the leaflet as he begins pacing slightly about the lounge."
    voice "heq2-38"
    he "Very interesting, mmhmm."
    "Herman shifts his cigar from one side of his mouth to the other, wiggling the pen between his fingers as he shifts the leaflet to his free hand, still intently staring at it."
    voice "heq2-39"
    show herman happy
    he "By Jove, I know exactly what to do with this!"
    "He uses his pen to quickly open an eye on top of the burning stove, tossing the leaflet inside."
    "You hear the fire fizzle, the flames licking out of the opening in the stove before Herman closes the lid with his pen."
    "Herman steps back up to you, pulling the cigar from his mouth and blowing smoke in your face."
    voice "he_ann5"
    show herman angry
    he "Who put you up to a stunt like this, Brutus? Probably not; bless his heart, he could throw himself on the ground and miss."
    "Herman steps back over to you and wipes the soot from the tip of his pen on your shirt."
    menu:
        "He takes a seat back in his chair and resumes writing."

        "\"That's it? You just shrug it off as if it means nothing?!\"":
            jump herman_angry_4
        "\"What else would convince you?\"":
            jump herman_polite_4


label herman_doubtnewspaper_4:
    $ herman_queststate = 3
    "Herman's eyes furrow."
    "He tosses his pen and booklet on the table, then yanks the paper from your hands, but it crumbles to dust in his fingers."
    "He stands and looks down upon you with contempt, his hands held in the air."
    voice "heq2-43"
    show herman angry
    he "What the hell? All you've brought is a mess, I'd say."
    "He shakes his hands off a bit, then wipes his hands on your shirt."
    voice "heq2-44"
    show herman happy
    he "Doesn't seem like much evidence to me, does it? Better luck next time, young'n."
    "He pats you on the shoulder, though more so to finish wiping his hands clean with a snarky smile before returning to his seat."

    menu:
        "He grabs his pen and booklet and continues writing."

        "\"That's it? You just shrug it off as if it means nothing?!\"":
            jump herman_angry_4
        "\"What else would convince you?\"":
            jump herman_polite_4


label herman_angry_4:
    $ herman_attitude = herman_attitude - 1
    $ herman_justgotrebuffed = True

    "Herman's gaze darts to yours, staring you dead in the eyes. He slowly puts his booklet down and points his pen at you like a sharp extension of his finger."
    voice "heq2-46"
    show herman angry
    he "Now you look here, young'n, I ain't got TIME for your mess'n 'round, ya hear?"
    "He stands up abruptly, walks up to you, and pokes his finger into your shoulder, stabbing you slightly with the tip of his fountain pen."
    voice "heq2-47"
    show herman angry
    he "My patience is wearin' thin, little rabbit, so if you dun watch that mouth'a yours, I'll skin ya and mount that thick skull on the wall."
    "Herman pokes you repeatedly in the chest again with his fingertip and pen."
    voice "heq2-48"
    show herman angry
    he "Are we CRYSTAL clear on this?"
    "He curls his hand into a fist and shoves you backwards a bit, eyeballing you as he sits back down with a thud in his chair."
    "He yanks his booklet back up, returning to writing."
    jump herman_convohub

label herman_polite_4:
    $ herman_attitude = herman_attitude + 1
    $ herman_justgotrebuffed = True
    "Herman looks up at the ceiling for a few moments, then back at you."
    voice "heq2-45"
    show herman happy
    he "Now, don't you think I would have done this myself if I really thought I wasn't alive no more?"
    "He smirks and shakes his head."
    voice "he_lhu1"
    show herman neutral
    he "Come on now, if this is supposedly your 'task,' I would have thought you would be better at it."
    "Herman's smirk slides into a grin as he chuckles, looking back to his work."
    voice "he_ann2"
    show herman neutral
    he "If ya ain't got nothing else to jaw on about, then get. I've got to finish this speech, and your tom-foolery is distracting me."
    jump herman_convohub

label herman_livingroom:
    $ herman_queststate = 4
    "You search the living room, rummaging through old books, photo albums, and other random boxes."
    "You discover an old photo of men in dark robes with hoods covering their faces, among some other pictures of Rory."
    "However, the photo is heavily faded and appears to have cup ring stains on it, so it's impossible to see what the men look like."
    "A hole in the photo, seemingly from an open flame, goes right through the face of one of the hooded men."
    "Turning the photo over, written in faded ink, you can barely make out the words \"Acolytes of The Eater of Souls\" and various names."
    "The names listed are smudged and faded as well, but you can make out three of them."
    "E. O'Neal"
    "B. Indigo"
    "H. Grover"
    "H. Grover appears to have been scratched out."
    ab "Auspicious and suspcicious, both."
    "As you look about at the random books and notes, you almost trip over an old notebook."
    "It stands out from the others due to the odd symbol on the cover and a clasp that holds it closed."
    "You fiddle with the clasp, checking for a lock, and it pops open."
    "Opening the book, the first few dozen pages are somewhat together."
    "It's quite weathered and smudged, as if the book was sitting in water for a long time and then dried out."
    "You're able to read some writing of the opening endpaper beside a curious symbol:"
    "\"The Jour... rutus Indi ...\""
    "As you thumb through the pages, many entries talk exclusively about Herman: about how ruthless, evil, and nasty he is."
    "How he cheated so many people through his policies and robbed others with underhanded business tactics."
    "Some entries discuss rituals, sacrifices to \"The Flaming One\" and this being's inevitable return."
    "Reading more, you come across a smudged entry that appears to be dated September 5th, 1922, that catches your eye."
    "\"... only two days before the next sacrifice, we have all agreed that a large offering to The Flaming One is required.\""
    "\"I pray that The Son of Nodens will be long satiated with this ample offering.\""
    ab "What on Earth was this man mixed up in?"
    ab "You ought to have a word with him, if only to clarify whatever it is you've found here."
    jump elizabeth_convohub

label herman_return_9:
    "With the old notebook and photograph in hand, you make your way back inside the lounge."
    "The air is so thick with smoke now it would be almost impossible to breathe, if breathing was something you needed to worry about."
    "The smoke does not seem to leave the room, even with the door wide open."
    menu:
        "However, it has become rather hard to see, so much so that you can't even see your hand in front of your face."
        "\"Herman, I can't see through this smoke, where are you?\"":
            pass

    "You see a dark figure moving towards you, merely a silhouette with piercing eyes that seem to burn through the smoke."
    "As the figure moves closer, you can see clearly that it's Herman."
    "With a cigar between his teeth and a wide smile, he appears unphased by the smoke."
    "He smacks you on the arm with his hand as if to greet you."
    voice "heq2-49"
    show herman happy
    menu:
        he "Well now, it's good to see you back in one piece! Come, come, let's have a cigar and some of the gut-rot whiskey from the bar."
        "\"Rory, I can barely see through the smoke, but I discovered some things that might help.\"":
            pass

    "Herman looks around, seemingly confused."
    voice "he_puz2"
    show herman neutral
    he "What smoke? There's no smoke in here."
    menu:
        "As you look around, you see that, indeed, there is no smoke in the room at all anymore."
        "Give Herman the old notebook and photograph.":
            jump herman_giveitems_9
        "\"Rory, I won't give you what I found, but we can talk about it.\"":
            jump herman_discussitems_9
        "\"You don't deserve to know anything. You were a horrible person in life and worse in death!\"":
            jump herman_withholditems_9


label herman_giveitems_9:
    $ herman_attitude = herman_attitude + 1
    "Herman lifts an eyebrow and takes the old notebook and picture, looking them over momentarily."
    "He then flips through the pages of the notebook, tearing some recklessly in the process."
    "He waves the notebook and photograph carelessly at you."
    voice "heq2-50"
    show herman angry
    he "What kind'a nonsense is this? All ya bring me is a nasty ol' journal and a washed out photo? Is this some kinda trick?"
    "He looks over the photograph again, turning it over, and appears annoyed by what he sees."
    voice "he_ann1"
    show herman angry
    menu:
        he "If you're playin' games, this ain't funny."
        "\"No games, Rory. Do either of those help you to remember anything?\"":
            jump herman_memory_9

label herman_discussitems_9:
    "Herman smirks and folds his arms over his chest, shifting his cigar to the other side of his mouth."
    voice "heq2-51"
    show herman angry
    menu:
        he "Talk about what? I don't even know whatcha got there, let alone what we got to talk about."
        "\"I have a notebook that talks about you and a photograph with your name on it.\"":
            jump herman_discussion_9
        "\"What we have to talk about is: why are you in a photograph with cult members?\"":
            jump herman_cult_9

label herman_withholditems_9:
    $ herman_attitude = herman_attitude - 1
    "Herman rolls his eyes at you."
    voice "heq2-52"
    show herman neutral
    he "What? Are ya on a toot or somethin'? Get your head outta your ass!"
    "He steps forward, glaring down at you."
    voice "he_mad5"
    he "You dunno your oats, young'n. I've done plenty for the folks 'round here!"
    menu:
        he "Go on and just poll them; I'm a shoe-in for the next election."
        "\"I'm not playing your games, Herman. You were in a cult. Explain that.\"":
            jump herman_cult_9
        "\"I have a notebook that talks about you and a photograph with your name on it.\"":
            jump herman_discussion_9

label herman_cult_9:
    "Herman shakes his head at you, like a disappointed father."
    voice "he_dis5"
    show herman angry
    he "The Acolytes of The Eater of Souls are not a 'cult,' little rabbit."
    he "They are a secret society who prevent the return of Vorvodoss, a being of immense power with an insatiable appetite for life essence."
    $ herman_vorvodossmentioned = True
    "He turns around and starts to pace the floor slowly, arms crossed tightly over his chest with one hand rubbing his beard."
    voice "he_puz2"
    show herman neutral
    he "Without our sacrifice of animals, Vorvodoss would claim a host to reign terror and death upon the living until his hunger is quenched."
    he "I paid the price to gain political power, like every other politician in history."
    "Herman stomps his foot on the floor, arms stretched wide, his eyes glassing over as if holding back tears."
    voice "he_mad5"
    show herman neutral
    he "I sacrificed my family farm! We produced livestock for the monthly rituals... They took all my family had."
    voice "he_mad1"
    show herman angry
    he "But it STILL wasn't enough to keep those bastards from running my businesses and my name into the dirt!"
    menu:
        "They forced me to levy taxes on essentials like groceries just so they could afford to bring in truckloads of cows, goats, and sheep!"
        "\"So you were just being used by them to kill animals for some made-up god?\"":
            jump herman_doubt_10
        "\"I don't believe anything you just said, Rory. You've been a lying cheat your whole life.\"":
            jump herman_doubt_10

label herman_disucssion_9:
    "Herman lifts his head and turns his gaze to the side slightly."
    "He's looking down over his nose and trying to see what you have in your hands better, like a vulture sizing up a meal."
    voice "he_hap4"
    show herman happy
    he "Someone wrote an article about me? A photo with my autograph? Well, this I gotta see!"
    "He suddenly snatches the notebook and photograph from your hands, looking at both intently well out of your reach."
    voice "he_puz3"
    show herman angry
    menu:
        he "Now wait a gosh darn minute. This looks like Brutus' journal. How did you get this from him?!"
        "\"Herman, I wanted to talk with you about those before I gave them to you!\"":
            jump herman_memory_9

label herman_memory_9:
    "Herman looks at the photograph once more, reading the back of it."
    "Then, taking a better look at the journal, gently opens the book and looks through a few pages in more detail."
    voice "he_dis3"
    show herman angry
    he "No... no, they wouldn't have."
    "He coughs as he continues to read, and you notice his feet slowly lift from the ground."
    voice "he_eww1"
    show herman angry
    he "Ample sacrifice? Why would they... I was loyal for so long."
    menu:
        "He drops the photo and notebook, lifting his hands to his face, and turns them over to look at the back of them."
        "\"Rory, you're floating... does that mean you've accepted your death?\"":
            jump herman_acceptance_10

label herman_doubt_10:
    "Herman sighs and shrugs, stopping his pacing to look at you."
    voice "he_ann2"
    show herman angry
    he "It dun'matter what you think or believe."
    he "I never believed it neither, but it was such a great deal on paper."
    "He uses his hands and balances them like a scale."
    voice "he_puz5"
    show herman neutral
    he "All I had to do was give them control of cattle processing and production."
    "They'd give me 50% of the profits, AND they'd make me Governor, then Senator, then lastly..."
    "He raises his hand flat and slowly wipes it in the air to one side, looking up past you as he daydreams."
    voice "he_hap4"
    show herman happy
    he "President of the U.S. of A."
    "He grins widely down at you, shaking both hands at you like an excited child getting the exact toy they asked for."
    voice "he_hap2"
    show herman happy
    menu:
        he "Wouldn't you do anything for that much power?!"
        "\"I was wrong, Rory. You're not evil; you're just a power-hungry idiot.\"":
            pass
    "Herman looks at you, shocked."
    voice "he_puz5"
    menu:
        he "Now wait just a gosh darn minute, young'n, I..."
        "\"I think this cult was done with you. They were finished stealing your businesses.\"":
            pass
    menu:
        "Rory listens, incredulous."
        "\"You enacted the policies they wanted, so they murdered you and sacrificed you.\"":
            pass
    jump herman_undercontrol_11

label herman_acceptance_10:
    "Herman ignores you, lifting his hand out in front of himself and pointing to the table."
    "Without hesitation, the table careens across the floor and slams into the wall, breaking into a few large pieces."
    voice "he_lev3"
    show herman happy
    he "I... I done did that. I wanted to break that damn ugly ass table."
    "He slowly turns without moving his feet, suspended in the air, then points at the bottles behind the bar as if his hand and finger were a gun."
    voice "heq2-53"
    show herman angry
    he "Bang!"
    "One of the bottles on the shelf explodes as if struck by a bullet, liquid and glass spilling everywhere."
    voice "heq2-54"
    show herman happy
    he "Bang bang bang!"
    "Three more bottles burst with each of his words."
    "He looks down at his hands again as he clenches them closed."
    voice "he_lev1"
    show herman laugh
    menu:
        he "Oh, now this is TRUE power!"
        "\"Rory, this isn't about you gaining power. You're supposed to accept your death and move on to the afterlife!\"":
            pass

    jump herman_undercontrol_11


label herman_undercontrol_11:
    "Herman stops and looks at you. He seems to be thinking clearly."
    voice "heq2-55"
    he "You know what? I honestly think you're right."
    "He looks at his hands, clenching and unclenching his right fist."
    voice "heq2-56"
    show herman neutral
    he "I realize I've been missing somethin' important all this time. It would really help me come to terms with all of this mess."
    "Herman holds up the photograph and points to the hands of all the members, then holds up his own right hand and wiggles his fingers."
    voice "he_puz1"
    show herman neutral
    he "My signet ring. I can't believe I've forgotten, but this picture jogged my memory."
    menu:
        he "That's the ring my pappy gave me, and I need it."
        "\"Where would I be able to find the ring?\"":
            jump herman_finalfetchquest_11
        "\"Why should I go on yet ANOTHER 'get this for me' trip?\"":
            jump herman_convincefetchquest_11

label herman_finalfetchquest_11:
    $ herman_queststate = 5
    voice "heq2-57"
    show herman neutral
    he "Head on down to the basement. That's where the rituals were held here. I doubt those yella bellied cowards would have had the gall to clean up afterwards."
    voice "he_dis2"
    show herman angry
    he "It feels off to say this, but once I have my old ring back, I think that'll help me pass on."
    "Herman glances at his hands again, then turns his back on you to look around the room, ignoring you."
    jump herman_convohub

label herman_convincefetchquest_11:
    "Herman puts his hand over his heart and raises his hand."
    voice "he_ann2"
    show herman angry
    he "I swear on my pappy's grave, I ain't telling no fib."
    he "I'm all but certain this is all I've been missing and what I need to get a move on myself."
    "He smirks and shrugs purposefully slow."
    voice "he_puz2"
    show herman happy
    he "Unless you're just that entertained by me. In that case, we can just play poker."
    he "I call Texas Hold'em; best out of five million games wins?"
    menu:
        "Herman turns and grabs a deck of cards from a drawer, shuffling them with a big smile."
        "\"Fine. I'd rather play cards then get anything else for you.\"":
            jump herman_infinitecardgame_11

        "\"I'll just go find that ring for you. Where would it be?\"":
            jump herman_finalfetchquest_11


label herman_infinitecardgame_11:
    if herman_playedpoker:
        "You play some more poker with Herman."
    else:
        "You play poker with Herman."
    "After a few hands, Herman having multiple cigars and numerous drinks, neither of you are ahead yet."
    voice "he_lch3"
    show herman laugh
    menu:
        he "How about another hand? I'll go easy on you this time."
        "Keep playing poker.":
            $ herman_playedpoker = True
            jump herman_infinitecardgame_11
        "\"Fine! I'll go find that ring for you. Where would it be?\"":
            jump herman_finalfetchquest_11

label herman_basement:
    $ herman_queststate = 6
    "As you look carefully through random bits of old broken glass, junk, and boxes, you notice something carved into the floor."
    "Though heavily worn, it looks similar to the symbol from the notebook."
    "You sift through decades of dust, grime, and old ashes, but finally, you see something glint."
    # SHOW THE SIGNET RING BBY
    "Lifting up the jewel captured in a ring, the obvious charred and mummified remains of a human finger stuck to the insides. The ring, despite the heat, appears pristine."
    "You pocket it."
    jump presper_convohub

label herman_ringreturn_13:
    "Upon returning to the lounge, you find the atmosphere feels heavy."
    "The once bright room is lit solely by the open stove, which now rages with an angry green fire."
    "You see the room is almost entirely destroyed, Herman softly floating above the stove, arms stretched out to either side of himself and head tilted back."
    voice "heq2-58"
    show herman happy
    he "Why have I never noticed the POWER I truly have? Being dead is the GREATEST thing to ever happen to me!"
    "In the blink of an eye, he is floating mere inches away from you. His eyes seem to burn brightly."
    voice "heq2-59"
    show herman laugh
    he "The ring, give it to me. They want me to pass on, right? Or would you rather I 'use' this newfound power and just take it from your dismembered corpse?"
    menu:
        "Herman holds out his hand to you."
        "You need Herman to pass on; place the ring in his hand.":
            jump herman_revealvorvodoss_13

        "\"No, Rory, something is wrong. This isn't you.\"":
            jump herman_denyring_13

label herman_revealvorvodoss_13:
    $ herman_queststate = 7
    "Herman holds the ring and uncaringly flicks the remains of his own finger out of it."
    "He quickly slips it on, and Herman's face and eyes ignite in an almost blindingly bright fire."
    "The heavy atmosphere lifts, but in its place, a wave of heat fills the room."
    "Herman is still before you, but very different."
    voice "vos-01"
    show herman possessed
    vo "\"Transference complete.\""
    menu:
        "He sounds nothing like Herman and speaks a language you've never heard, though somehow you understand him."
        "\"What have you done to Herman?\"":
            jump herman_vorvodosssubroutine_13


label herman_denyring_13:
    voice "he_lev2"
    show herman angry
    he "This \"isn't me?\" You know NOTHING about me... little rabbit."
    "His hand appears near your face."
    "You feel your tongue move forward on its own as your mouth opens against your will."
    "A tearing sound echos through your skull from your throat."
    voice "vo-lch"
    show herman happy
    menu:
        he "How about I just rip this tongue out to shut you up, for starters? I grow tired of your yammering."
        "Quickly give him the ring to stop him from tearing you apart!":
            jump herman_revealvorvodoss_13
        "Use what courage you can muster to throw the ring into the open stove!":
            jump herman_destroyring_13


label herman_vorvodosssubroutine_13:
    "Herman's head tilts slightly like a curious dog."
    voice "vol-03"
    show herman possessed
    vo "\"Conveyance entity requests inquiry. Variance acceptable. Execute subroutine: Conveyance Entity Inquiry.\""
    "He slowly lifts a hand and points to you."
    voice "vol-01"
    vo "\"Derivative entity present before The One. Anomalous. Primary entity inquiry permitted.\""
    "\"Herman\" straightens his head and floats in place."
    voice "vos-03"
    vo "\"The One permits three inquiries.\""
    voice "vom-03"
    vo "\"Parsing: 'What have you done to Herman?' \""
    "\"Herman's\" eyes blaze a moment, then calm."
    voice "vom-04"
    vo "\"Processed: Entity known as 'Herman Rory Grover' consumed and transferred.\""
    voice "vos-03"
    menu:
        vo "\"The One permits two inquiries.\""

        "\"'Inferred, processed, inquiry?' What are you?\"":
            jump herman_questionvorvodoss_13

        "\"Bring Rory back!\"":
            jump herman_demandvorvodoss_13

        "\"Oh well, Herman deserved whatever happened. My task is complete.\"":
            jump herman_quitvorvodoss_13

label herman_destroyring_13:
    $ herman_queststate = 8
    "As the ring flies across the room, it lands in the open mouth of the raging stove."
    "Herman jolts to grab the ring, but it falls through his hand into the stove. He slowly turns back to you, his eyes flaring hot, yet he grins widely."
    voice "heq2-60"
    show herman happy
    he "My pappy always used to say, \"If you lead the dance, you'll never get stepped on.\""
    "He winks as the room begins to suddenly heat up."
    voice "he_lev3"
    show herman possessed
    he "And I always lead the dance... little rabbit."
    "You're blinded by a flash of light, deafened by the roar of flames."
    menu:
        "You feel as if the world suddenly vanished, then returned all in an instant."
        "Open your eyes.":
            jump herman_vorvodossgone_14

label herman_questionvorvodoss_13:
    voice "vom-09"
    show herman possessed
    vo "\"Parsing: 'Inferred, processed, inquiry?'\""
    "\"Herman's\" eyes blaze, then calm again."
    voice "vom-02"
    vo "\"Illegal operation: Abstract Nonsense.\""
    voice "vos-14"
    vo "\"Inquiry rejected.\""
    voice "vol-06"
    vo "\"Parsing: 'What are you?' \""
    "\"Herman's\" eyes blaze, then calm yet again."
    voice "vol-02"
    vo "\"Processed: Constant; The One. Variables: The Flaming One, The Eater of Souls, Lord of the Universal Spaces, The One Who Waiteth in the Outer Dark, Vorvodoss.\""
    $ herman_vorvodossmentioned = True
    $ vorvodoss_name = "Vorvodoss"
    voice "vom-07"
    vo "\"Subroutine exit. Resume suspended. Execute subroutine: Consume and Transfer.\""
    "You're blinded by a flash of light, deafened by the roar of flames."
    menu:
        "You feel as if the world suddenly vanished, then returned all in an instant."
        "Open your eyes.":
            jump herman_vorvodossgone_14

label herman_demandvorvodoss_13:
    voice "vos-05"
    show herman possessed
    vo "\"Parsing: 'Bring Rory back!'\""
    "\"Herman's\" head tilts again."
    voice "vom-04"
    vo "\"Illegal Operation: Syntax error in Conveyance Entity Inquiry.\""
    voice "vos-02"
    vo "\"Unexpected Error, Quitting: Terminate subroutine Conveyance Entity Inquiry.\""
    voice "vom-07"
    vo "\"Resume suspended. Execute subroutine: Consume and Transfer.\""
    "You're blinded by a flash of light, deafened by the roar of flames."
    menu:
        "You feel as if the world suddenly vanished, then returned all in an instant."
        "Open your eyes.":
            jump herman_vorvodossgone_14

label herman_quitvorvodoss_13:
    voice "vol-05"
    show herman possessed
    vo "\"Parsing: Oh well, Herman deserved whatever happened. My task is complete.\""
    "\"Herman's\" head tilts again."
    voice "vos-09"
    vo "\"Conveyance Entity requests quit.\""
    voice "vos-10"
    vo "\"Terminate subroutine: Conveyance Entity Inquiry.\""
    voice "vom-07"
    vo "\"Resume suspended. Execute subroutine: Consume and Transfer.\""
    hide herman
    "You're blinded by a flash of light, deafened by the roar of flames."
    menu:
        "You feel as if the world suddenly vanished, then returned all in an instant."
        "Open your eyes.":
            jump herman_vorvodossgone_14



label herman_vorvodossgone_14:
    $ herman_questjustfinished = True
    show herman neutral
    "As you open your eyes, you see Herman sitting in his chair, cigar in hand."
    "The room is back to its previous splendor."
    "Herman leans forward and ashes his cigar in the ashtray, looking over his booklet, pen in hand, a bottle of whiskey by a half-empty glass."
    jump herman_convohub
