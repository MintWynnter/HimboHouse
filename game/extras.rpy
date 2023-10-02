style tembuttons:
    hover_color "#FF90F4"
    size 90

style bembuttons:
    hover_color "#FF90F4"
    size 48

init:
    transform headzoom:
        zoom .456
    transform bgzoom:
        zoom .187037

define put_credits_here = """The House On Limbo Lane
Leads
    Team Lead: Michael Smith
    Producer and Audio Lead: Kylie Siaw
    Art Lead: Elina Heino
    Programming Lead: Mint Wynnter

Writers
    Jett Barker (Lysander)
    Eris (Elizabeth)
    Dagon Grey (Herman)
    Marie Minuet (Arabella)
    Michael Smith (Marianne, Dr. Presper, Abbé Maurice Lachaise)
    Mint Wynnter (Aures)

Editors
    Faust
    Maya Zimmerman

Artists
    Art Lead: Elina Heino (Herman, The Lounge)
    Animation and BGs: Candycornskull (The Garden, The Bedroom, all animations)
    Sprites and Icons: Eufasy (Elizabeth)
    Sprites and BGs: Olivia Jones (Dr. Presper, The Living Room)
    Sprites, BGs, and Icons: Millasai (Aures, Minoru, Amalgam, The Foyer)
    BGs: Kat Peterson (The Ballroom, Outside the Mansion, The Lab)
    Sprites, Icons, and Chibis: Podlet (Arabella, all chibi icons)
    UI Art and Design: Ruminio
    Sprites, Icons, and CGs: Thoe (Lysander, Marianne)

Audio
    Audio Lead: Kylie Siaw
    Audio Editor: Leon Artmann
    Audio Editor: Ho San "Ambrose" Cheng
    Audio Editor: Xander Grant
    Audio Editor: Maya Zimmerman

Programmers
    Lead Programmer: Mint Wynnter
    Scripter: Michael Smith, Maya Zimmerman

Composers
    Jan Hehr
    James Molloy
    Henri Tikkala

Social Media
    Rita Amparita
    Podlet

Cast
    Arabella Kingsley: Lauren Kong
    Herman Rory Grover: Marlon Dance-Hooi
    Marianne Dixon: Kat Peterson
    Elizabeth: Hannah Beard
    Lysander Thompson: Xander Grant
    Aures Bellis: Jett Barker
    Minoru: Lily Yasuda
    Dr. Antoine Presper: Max Herzfeld
    Abbé Maurice Lachaise: Dakota Jaymes
    The Amalgam: Jett Barker, Dagon Grey, Kat Peterson, Michael Smith
    Voice Direction: Rita Amparita (Arabella, Elizabeth), Jett Barker (Lysander), Dagon Grey (Herman)
"""

screen extras(mtype, subtype):
    tag menu
    add "gui/setting_bg.png"
    textbutton "ART":
        text_style "tembuttons"
        if mtype == "Art":
            text_color "#F4BB4F"
        xpos .101563
        ypos .038889
        action ShowMenu("extras", "Art", "Characters")
    textbutton "MUSIC":
        text_style "tembuttons"
        if mtype == "Music":
            text_color "#F4BB4F"
        xpos .271354
        ypos .038889
        action ShowMenu("extras", "Music", "1")
    textbutton "CREDITS":
        text_style "tembuttons"
        if mtype == "Credits":
            text_color "#F4BB4F"
        xpos .498958
        ypos .038889
        action ShowMenu("extras", "Credits", "")
    textbutton "TITLE":
        text_style "tembuttons"
        xpos .768229
        ypos .038889
        action ShowMenu("main_menu")
    if mtype == "Credits":
        viewport:
            #area(xstart, ystart, xend, yend)
            area (.175, .275, .65, .525)
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill False

            hbox:
                text put_credits_here
    if mtype == "Art":
        textbutton "CHARACTERS":
            text_style "bembuttons"
            if subtype == "Characters":
                text_color "#F4BB4F"
            xpos .145313
            ypos .903704
            action ShowMenu("extras", "Art", "Characters")
        textbutton "BACKGROUNDS":
            text_style "bembuttons"
            if subtype == "Backgrounds":
                text_color "#F4BB4F"
            xpos .421875
            ypos .903704
            action ShowMenu("extras", "Art", "Backgrounds")
        textbutton "OTHERS":
            text_style "bembuttons"
            if subtype == "Others":
                text_color "#F4BB4F"
            xpos .719227
            ypos .903704
            action ShowMenu("extras", "Art", "Others")
        if subtype == "Characters":
            imagebutton:
                idle "images/headshot_lysander.png"
                xpos .134375
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_herman.png"
                xpos .290104
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_elizabeth.png"
                xpos .445833
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_marianne.png"
                xpos .601563
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_abbe.png"
                xpos .744792
                ypos .276852
                at headzoom
            imagebutton:
                idle "images/headshot_presper.png"
                xpos .134375
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_aures.png"
                xpos .290104
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_minoru.png"
                xpos .445833
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_abbe.png"
                xpos .601563
                ypos .565741
                at headzoom
            imagebutton:
                idle "images/headshot_amalgam.png"
                xpos .744792
                ypos .565741
                at headzoom
        


        elif subtype == "Backgrounds":
            imagebutton:
                idle "images/bg ballroom.png"
                xpos .211458
                ypos .227778
                at bgzoom
            imagebutton:
                idle "images/bg basement.png"
                xpos .406250
                ypos .227778
                at bgzoom
            imagebutton:
                idle "images/bg bedroom.png"
                xpos .600521
                ypos .227778
                at bgzoom
            imagebutton:
                idle "images/bg foyer.png"
                xpos .211458
                ypos .433333
                at bgzoom
            imagebutton:
                idle "images/bg garden.png"
                xpos .406250
                ypos .433333
                at bgzoom
            imagebutton:
                idle "images/bg livingroom.png"
                xpos .600521
                ypos .433333
                at bgzoom
            imagebutton:
                idle "images/bg lounge.png"
                xpos .211458
                ypos .638889
                at bgzoom
            imagebutton:
                idle "images/bg outside.png"
                xpos .406250
                ypos .638889
                at bgzoom
        


        elif subtype == "Others":
            imagebutton:
                idle "images/headshot_journal.png"
                xpos .258854
                ypos .207407
                at headzoom
            imagebutton:
                idle "images/headshot_ded.png"
                xpos .381771
                ypos .207407
                at headzoom
            imagebutton:
                idle "images/headshot_map.png"
                xpos .504688
                ypos .207407
                at headzoom
            imagebutton:
                idle "images/headshot_missing.png"
                xpos .627083
                ypos .207407
                at headzoom
            imagebutton:
                idle "images/headshot_pendant.png"
                xpos .258854
                ypos .425926
                at headzoom
            imagebutton:
                idle "images/headshot_photo.png"
                xpos .381771
                ypos .425926
                at headzoom
            imagebutton:
                idle "images/headshot_ring.png"
                xpos .504688
                ypos .425926
                at headzoom
            imagebutton:
                idle "images/headshot_whiskey.png"
                xpos .627083
                ypos .425926
                at headzoom
            imagebutton:
                idle "images/headshot_camcorder.png"
                xpos .258854
                ypos .644444
                at headzoom
            imagebutton:
                idle "images/headshot_diary.png"
                xpos .381771
                ypos .644444
                at headzoom
            imagebutton:
                idle "images/headshot_chibi.png"
                xpos .504688
                ypos .644444
                at headzoom
            imagebutton:
                idle "images/headshot_layout.png"
                xpos .627083
                ypos .644444
                at headzoom