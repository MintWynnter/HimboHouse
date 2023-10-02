
default blink_pause = 0.25

image blink:
    yoffset 20
    "blink0.png"
    pause blink_pause
    "blink1.png"
    pause blink_pause
    "blink2.png"
    pause blink_pause
    "blink3.png"
    pause blink_pause
    "blink4.png"
    pause blink_pause
    "blink5.png"
    pause blink_pause
    repeat

default chand_pause = 0.25

image chand:
    "chand1.png"
    pause chand_pause
    "chand2.png"
    pause chand_pause
    "chand3.png"
    pause chand_pause
    "chand4.png"
    pause chand_pause
    repeat

default curtain_pause = 0.25

image curtain:
    "curtain1.png"
    pause curtain_pause
    "curtain2.png"
    pause curtain_pause
    "curtain3.png"
    pause curtain_pause
    "curtain4.png"
    pause curtain_pause
    "curtain5.png"
    pause curtain_pause
    "curtain6.png"
    pause curtain_pause
    repeat

default drink_pause = 0.25

image drink:
    "drink1.png"
    pause drink_pause
    "drink2.png"
    pause drink_pause
    "drink3.png"
    pause drink_pause
    "drink4.png"
    pause drink_pause
    "drink5.png"
    pause drink_pause
    "drink6.png"
    pause drink_pause
    "drink7.png"
    pause drink_pause
    "drink8.png"
    pause drink_pause
    "drink9.png"
    pause drink_pause
    "drink10.png"
    pause drink_pause
    "drink11.png"
    pause drink_pause
    "drink12.png"
    pause drink_pause
    repeat

default fire_pause = 0.25

image fire:
    "fire1.png"
    pause fire_pause
    "fire2.png"
    pause fire_pause
    "fire3.png"
    pause fire_pause
    repeat

default lab_pause = 0.25

image lab:
    "lab1.png"
    pause lab_pause
    "lab2.png"
    pause lab_pause
    "lab3.png"
    pause lab_pause
    "lab4.png"
    pause lab_pause
    repeat

default light_pause = 0.25

image light:
    "light1.png"
    pause light_pause
    "light2.png"
    pause light_pause
    "light3.png"
    pause light_pause
    "light4.png"
    pause light_pause
    repeat

default out_pause = 0.25

image out:
    "out1.png"
    pause out_pause
    "out2.png"
    pause out_pause
    "out3.png"
    pause out_pause
    "out4.png"
    pause out_pause
    "out5.png"
    pause out_pause
    "out6.png"
    pause out_pause
    "out7.png"
    pause out_pause
    "out8.png"
    pause out_pause
    "out9.png"
    pause out_pause
    "out10.png"
    pause out_pause
    "out11.png"
    pause out_pause
    "out12.png"
    pause out_pause
    "out13.png"
    pause out_pause
    repeat

default questsdone = 0 # how many quests have you completed?
default amalgam_dead = False #what it says on tin
default amalgam_vorv = False #what it says on tin
default amalgam_sedated = False
default getting_chewed = False

# the marianne corner (she's magenta-pink)
default marianne_name = "???"
define ma = Character("marianne_name", dynamic = True, color="#f7c8f3",what_color="#f7c8f3", image = "marianne")

    # when you first meet her
#$ marianne_name = "Marianne"
    # if you change her name to daisy
#$ marianne_name = "Daisy"
    # if you change her name to daisy
#$ marianne_name = "—"

default marianne_queststate = 0
default marianne_questdone = False # did you finish the quest?
default marianne_questjustfinished = False   #did you just finish the quest, so abbe can check in?

# the presper corner (he's gray)
default presper_name = "???"
define dr = Character("presper_name", dynamic = True, color = "#dedede", what_color = "#dedede", image = "presper")

    #when he introduces himself
#$ presper_name = "Dr. Presper"


# the abbe corner (he's blue)
default abbe_name = "Voice"
define ab = Character("abbe_name", dynamic = True, color = "#e3f0ff", what_color = "#e3f0ff")

    #when he introduces himself
#$ abbe_name = "Abbé Maurice"

# the everyone else corner so i can do the midpoint scene
#default arabella_queststate = 0

#the herman corner
default herman_queststate = 0
default herman_attitude = 0
define he = Character("Herman", color="#ffffff",what_color="#ffffff", image = "herman")
default herman_justgotfetch = False
default herman_date = False
default herman_newspaper = False
default herman_justgotrebuffed = False
default herman_playedpoker = False
default herman_vorvodossmentioned = False
default herman_questjustfinished = False
default vorvodoss_name = "???"
define vo = Character("vorvodoss_name", dynamic = True, color="#ffffff",what_color="#ffffff")

default elizabeth_queststate = 0
define el = Character("Elizabeth", color="#ffffff",what_color="#ffffff", image = "elizabeth")
default aures_queststate = 0


#the lysander corner (he's yellow-orange)
default lysander_queststate = 0
default lysander_questdone = False
default lysander_questjustfinished = False
define ly = Character("Lysander", image="lysander",color = "#fff4db", what_color = "#fff4db")
default lysander_angy = False #will lysander play an angy line if you minge him
default lysander_ded = False #is lysander sealed in a necklace lmao


#the arabella corner
default arabella_name = "???"
define ar = Character("arabella_name", dynamic = True, color="#ffffff",what_color="#ffffff", image = "arabella")
define mc = Character("You", color="#ffffff",what_color="#ffffff")


define am = Character("The Amalgam", color="#ffffff",what_color="#ffffff", image = "amalgam")

default q3_entry_count = 0
default q3_priest_journal = False
default q3_mom_journal = False
default q3_doctor_journal = False
default q3_own_journal = False
default q3_lysander_convo = False
default q3_pendant_encounter = False
default q3_pendant_keep = False
default q3_state = 0
default q3_ending_trigger = False
default q3_death_convo_trigger = False #did you try to ask arabella about her death?
default q3_ending_points = 0
default q3_keyneeded = False

#default elizabeth_queststate = 0 already declared in michaeldefines
