style tbmbuttons:
    hover_color "#FF90F4"
    size 90

style bbmbuttons:
    hover_color "#FF90F4"
    size 48

style smallbuttons:
    hover_color "#FF90F4"
    size 32

screen bigMenu(mtype, subtype):
    tag menu
    add "gui/setting_bg.png"
    textbutton "SAVE":
        text_style "tbmbuttons"
        if mtype == "Save":
            text_color "#F4BB4F"
        xpos .097917
        ypos .038889
        action ShowMenu("bigMenu", "Save", "1")
        activate_sound "audio/sound/uismbtn.ogg"
    textbutton "LOAD":
        text_style "tbmbuttons"
        if mtype == "Load":
            text_color "#F4BB4F"
        xpos .28125
        ypos .038889
        action ShowMenu("bigMenu", "Load", "1")
        activate_sound "audio/sound/uismbtn.ogg"
    textbutton "SETTINGS":
        text_style "tbmbuttons"
        if mtype == "Settings":
            text_color "#F4BB4F"
        xpos .478646
        ypos .038889
        action ShowMenu("bigMenu", "Settings", "Graphics")
        activate_sound "audio/sound/uismbtn.ogg"
    textbutton "TITLE":
        text_style "tbmbuttons"
        xpos .770833
        ypos .038889
        action ShowMenu("main_menu")
        activate_sound "audio/sound/uismbtn.ogg"
    textbutton "RETURN":
        text_style "smallbuttons"
        xpos .026563
        ypos .935185
        action Return()
        activate_sound "audio/sound/uismbtn.ogg"
    
    if mtype == "Save":
        textbutton "1":
            text_style "smallbuttons"
            if subtype == "1":
                text_color "#F4BB4F"
            xpos .365625
            ypos .895370
            action ShowMenu("bigMenu", "Save", "1")
            activate_sound "audio/sound/uismallbtn3.ogg"
        textbutton "2":
            text_style "smallbuttons"
            if subtype == "2":
                text_color "#F4BB4F"
            xpos .428125
            ypos .895370
            action ShowMenu("bigMenu", "Save", "2")
            activate_sound "audio/sound/uismallbtn3.ogg"
        textbutton "3":
            text_style "smallbuttons"
            if subtype == "3":
                text_color "#F4BB4F"
            xpos .493229
            ypos .895370
            action ShowMenu("bigMenu", "Save", "3")
            activate_sound "audio/sound/uismallbtn3.ogg"
        textbutton "4":
            text_style "smallbuttons"
            if subtype == "4":
                text_color "#F4BB4F"
            xpos .557813
            ypos .895370
            action ShowMenu("bigMenu", "Save", "4")
            activate_sound "audio/sound/uismallbtn3.ogg"
        textbutton "5":
            text_style "smallbuttons"
            if subtype == "5":
                text_color "#F4BB4F"
            xpos .623438
            ypos .895370
            action ShowMenu("bigMenu", "Save", "5")
            activate_sound "audio/sound/uismallbtn3.ogg"
        
        $slot1 = pow(6, int(subtype) - 1)
        $slot2 = slot1 + 1
        $slot3 = slot2 + 1
        $slot4 = slot3 + 1
        $slot5 = slot4 + 1
        $slot6 = slot5 + 1

        button:
            xpos .133854
            ypos .227778
            action FileAction(slot1)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot1) xalign 0.5

            text FileTime(slot1, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot1):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot1)
        button:
            xpos .394792
            ypos .227778
            action FileAction(slot2)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot2) xalign 0.5

            text FileTime(slot2, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot2):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot2)
        button:
            xpos .655729
            ypos .227778
            action FileAction(slot3)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot3) xalign 0.5

            text FileTime(slot3, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot3):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot3)
        button:
            xpos .133854
            ypos .551852
            action FileAction(slot4)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot4) xalign 0.5

            text FileTime(slot4, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot4):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot4)
        button:
            xpos .394792
            ypos .551852
            action FileAction(slot5)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot5) xalign 0.5

            text FileTime(slot5, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot5):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot5)
        button:
            xpos .655729
            ypos .551852
            action FileAction(slot6)
            activate_sound "audio/sound/uisave.ogg"

            has vbox

            add FileScreenshot(slot6) xalign 0.5

            text FileTime(slot6, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot6):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot6)

    if mtype == "Load":
        $config.allow_skipping = True
        $config.keymap["dismiss"].extend(['mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT'])
        textbutton "1":
            text_style "smallbuttons"
            if subtype == "1":
                text_color "#F4BB4F"
            xpos .365625
            ypos .895370
            action ShowMenu("bigMenu", "Load", "1")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "2":
            text_style "smallbuttons"
            if subtype == "2":
                text_color "#F4BB4F"
            xpos .428125
            ypos .895370
            action ShowMenu("bigMenu", "Load", "2")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "3":
            text_style "smallbuttons"
            if subtype == "3":
                text_color "#F4BB4F"
            xpos .493229
            ypos .895370
            action ShowMenu("bigMenu", "Load", "3")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "4":
            text_style "smallbuttons"
            if subtype == "4":
                text_color "#F4BB4F"
            xpos .557813
            ypos .895370
            action ShowMenu("bigMenu", "Load", "4")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "5":
            text_style "smallbuttons"
            if subtype == "5":
                text_color "#F4BB4F"
            xpos .623438
            ypos .895370
            action ShowMenu("bigMenu", "Load", "5")
            activate_sound "audio/sound/uismbtn.ogg"
        
        $slot1 = pow(6, int(subtype) - 1)
        $slot2 = slot1 + 1
        $slot3 = slot2 + 1
        $slot4 = slot3 + 1
        $slot5 = slot4 + 1
        $slot6 = slot5 + 1

        button:
            xpos .133854
            ypos .227778
            action FileLoad(slot1)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot1) xalign 0.5

            text FileTime(slot1, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot1):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot1)
        button:
            xpos .394792
            ypos .227778
            action FileLoad(slot2)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot2) xalign 0.5

            text FileTime(slot2, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot2):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot2)
        button:
            xpos .655729
            ypos .227778
            action FileLoad(slot3)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot3) xalign 0.5

            text FileTime(slot3, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot3):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot3)
        button:
            xpos .133854
            ypos .551852
            action FileLoad(slot4)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot4) xalign 0.5

            text FileTime(slot4, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot4):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot4)
        button:
            xpos .394792
            ypos .551852
            action FileLoad(slot5)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot5) xalign 0.5

            text FileTime(slot5, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot5):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot5)
        button:
            xpos .655729
            ypos .551852
            action FileLoad(slot6)
            activate_sound "audio/sound/uiload.ogg"

            has vbox

            add FileScreenshot(slot6) xalign 0.5

            text FileTime(slot6, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                style "slot_time_text"

            text FileSaveName(slot6):
                style "slot_name_text"

            key "save_delete" action FileDelete(slot6)
    
    if mtype == "Settings":
        textbutton "GRAPHICS":
            text_style "bbmbuttons"
            if subtype == "Graphics":
                text_color "#F4BB4F"
            xpos .197396
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Graphics")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "AUDIO":
            text_style "bbmbuttons"
            if subtype == "Audio":
                text_color "#F4BB4F"
            xpos .457813
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Audio")
            activate_sound "audio/sound/uismbtn.ogg"
        textbutton "CONTROLS":
            text_style "bbmbuttons"
            if subtype == "Controls":
                text_color "#F4BB4F"
            xpos .673958
            ypos .905556
            action ShowMenu("bigMenu", "Settings", "Controls")
            activate_sound "audio/sound/uismbtn.ogg"
        if subtype == "Graphics":
            text "Display" xpos .125 ypos .202778 size 48
            text "Skip" xpos .420833 ypos .202778 size 48
            text "Text Speed" xpos .125 ypos .39537 size 48
            text "Auto-Play Speed" xpos .125 ypos .55 size 48
            text "Skip Speed" xpos .125 ypos .7046296 size 48
            text "Slow" xpos .153125 ypos .466667 size 32
            text "Slow" xpos .153125 ypos .622222 size 32
            text "Fast" xpos .646354 ypos .466667 size 32
            text "Fast" xpos .646354 ypos .622222 size 32
            textbutton "Fullscreen":
                text_style "smallbuttons"
                xpos .153125
                ypos .262037
                action Preference("display", "fullscreen")
                activate_sound "audio/sound/uismbtn.ogg"
            textbutton "Windowed":
                text_style "smallbuttons"
                xpos .153125
                ypos .306481
                action Preference("display", "window")
                activate_sound "audio/sound/uismbtn.ogg"
            textbutton "Unseen Text":
                text_style "smallbuttons"
                xpos .445833
                ypos .262037
                action Preference("skip", "toggle")
                activate_sound "audio/sound/uismbtn.ogg"
            textbutton "After Choices":
                text_style "smallbuttons"
                xpos .445833
                ypos .306481
                action Preference("after choices", "toggle")
                activate_sound "audio/sound/uismbtn.ogg"
            hbox:
                style_prefix "slider"
                xpos .194792
                ypos .472222
                vbox:
                    bar value Preference("text speed")
                    activate_sound "audio/sound/uiscrl.ogg"
            hbox:
                style_prefix "slider"
                xpos .194792
                ypos .626852
                vbox:
                    bar value Preference("auto-forward time")
                    activate_sound "audio/sound/uiscrl.ogg"
        if subtype == "Audio":
            text "Music Volume" xpos .121354 ypos .213889 size 48
            text "SFX Volume" xpos .121354 ypos .368519 size 48
            text "Voice Volume" xpos .121354 ypos .523148 size 48
            text "Low" xpos .149479 ypos .285185 size 32
            text "High" xpos .642708 ypos .285185 size 32
            text "Low" xpos .149479 ypos .440741 size 32
            text "High" xpos .642708 ypos .440741 size 32
            text "Low" xpos .149479 ypos .595370 size 32
            text "High" xpos .642708 ypos .595370 size 32
            textbutton _("Mute All"):
                xpos .801563
                ypos .794444
                action Preference("all mute", "toggle")
                style "mute_all_button"
                activate_sound "audio/sound/uismbtn.ogg"
            hbox:
                style_prefix "slider"
                xpos .191146
                ypos .290741
                vbox:
                    bar value Preference("music volume")
                    activate_sound "audio/sound/uiscrl.ogg"
            hbox:
                style_prefix "slider"
                xpos .191146
                ypos .445370
                vbox:
                    bar value Preference("sound volume")
                    activate_sound "audio/sound/uiscrl.ogg"
            hbox:
                style_prefix "slider"
                xpos .191146
                ypos .6
                vbox:
                    bar value Preference("voice volume")
                    activate_sound "audio/sound/uiscrl.ogg"

        