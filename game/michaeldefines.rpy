
default questsdone = 0 # how many quests have you completed?

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
define he = Character("Herman", color="#ffffff",what_color="#ffffff")
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
define el = Character("Elizabeth", color="#ffffff",what_color="#ffffff")
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

#default elizabeth_queststate = 0 already declared in michaeldefines
