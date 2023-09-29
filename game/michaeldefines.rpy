
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
default arabella_queststate = 0
default herman_queststate = 0
default lysander_queststate = 0
default elizabeth_queststate = 0
default aures_queststate = 0
