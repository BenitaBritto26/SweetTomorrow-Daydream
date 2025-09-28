# name of the character.

define e = Character("Amelia")
image Scarlett Talk = "scarlettTalk.png"
image Scarlett Anxious = "scarlettAnxious.png"
image clouds = "clouds.png"
image bg room = Transform("bedroom.png", size =(1920, 1080))
image bg livingroom = Transform("livingroom.png", size =(1920, 1080))
image bg school = Transform("school.png", size =(1920, 1080))
image nightgown = "nightgown.png"
image talknightgown = "talknightgown.png"
character newscaster = Character("Newscaster")

<<<<<<< Updated upstream
# Define a transform to position the image at the bottom.
# This transform must include an indented block of statements.
=======
# Define cooking ingredient images
image egg = "egg.png"
image rat = "rat.png"
image cockroach = "cockroach.png"
image pan = "pan.png"

# Define kitchen background that stretches to fit the whole screen
image bg kitchen = Transform("kitchen.png", size=(1920, 1080))

>>>>>>> Stashed changes
transform bottom_position:
# Scale the image a bit and place it centered at the bottom.
    zoom 2.5
    zoom 3
xalign 0.5
# yalign 1.0 places the image at the bottom of the window. The
# original used 2.0 which is outside the usual 0..1 range.
    yalign 1.0
    yalign 0.75
# Additional vertical offset if you want it further down.
yoffset 600
# Even further down

transform bottom_position3:
    zoom 3
    xoffset 100
    yoffset 200

transform top_left:
    zoom 1
    xalign -0.3
    yalign 0.2
    yoffset 100

transform top_center:
    zoom 1
    xalign 0
    yalign 0.2
    yoffset 100

transform top_right:
    zoom 1
    xalign 0.3
    yalign 0.2
    yoffset 100


# The game starts here.

label start:

    # Show clouds background with no character or text for 4 seconds
    scene clouds
    # Show room background with no character or text for 4 seconds
    scene bg room

# Wait for 4 seconds with no dialogue or characters
    $ renpy.pause(2.5, hard=True)
    $ renpy.pause(1.5, hard=True)

# Show the nightgown image positioned at the bottom
show nightgown at bottom_position with dissolve

    # These display lines of dialogue.

    hide nightgown
    show talknightgown at bottom_position
   
e "The sun's already so bright! I guess I better start getting ready for school!"
<<<<<<< Updated upstream

menu:
"What is this?":
@@ -49,4 +84,238 @@ label start:
# This ends the game.

return
=======
    # changes
    e "First, let me get dressed."
    e "What should I wear today?"
    hide talknightgown
    show nightgown at bottom_position
    image uniform1 = "cleanuniformonly.png"
    image uniform2 = "uncleanuniformoneonly.png"
    image uniform3 = "uncleanuniformtwoonly.png"
    show uniform1 at top_left with dissolve
    show uniform2 at top_center with dissolve
    show uniform3 at top_right with dissolve
    
    hide nightgown
    show talknightgown at bottom_position
    menu:
        "The first uniform!":
            e "Good choice!"
        "The second uniform!":
            e "Sorry, I don't want to wear that. We're going to wear the first one."
        "The third uniform!":
            e "Sorry I don't want to wear that. We're going to wear the first one."
    hide talknightgown
    image ameliaHappy = "happyAmelia.png"

    transform bottom_position2:
        zoom 3
        offset (50, 200)
        
    show ameliaHappy at bottom_position2 with dissolve
    image ameliaTalk = "AmeliaTalks.png"

    hide uniform1 with dissolve
    hide uniform1 with dissolve
    hide uniform2 with dissolve
    hide uniform3 with dissolve
    
    hide ameliaHappy
    show ameliaTalk at bottom_position2

    e "Now, it's time for me to make some breakfast!"
    #call cooking_minigame
    jump cooking_minigame

    # Cooking Minigame Label
    label cooking_minigame:
    
        # Variables to track cooking choices and outcomes
        $ cooking_choice = ""
        $ amelia_sanity = 0
    
        # Show kitchen background filling the entire screen
        scene bg kitchen
        show pan  # Show the cooking pan
    
        e "Let me see what I have to cook with..."
    
        # Show all ingredients lined up in the center with more spacing
        show cockroach at Transform(xalign=0.2, yalign=0.5, zoom=0.4)
        show egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
        show rat at Transform(xalign=0.8, yalign=0.5, zoom=0.1)

        e "Hmm... what should I cook? They all look... interesting."
    
        menu:
            e "I have some options here..."
        
            "Cook the egg":
                $ cooking_choice = "egg"
                jump cook_egg
            
            "Cook the rat":
                $ cooking_choice = "rat" 
                $ amelia_sanity -= 1
                jump cook_rat
            
            "Cook the cockroach":
                $ cooking_choice = "cockroach"
                $ amelia_sanity -= 2
                jump cook_cockroach
            
            "Mix all the ingredients together":
                $ cooking_choice = "everything"
                $ amelia_sanity -= 3
                jump cook_everything

    # Normal egg cooking
    label cook_egg:
        hide rat
        hide cockroach
        
        e "A nice, normal egg! Perfect for breakfast."
        
        menu:
            e "How should I cook it?"
            
            "Scrambled":
                hide egg
                show scrambled_egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
                e "Fluffy scrambled eggs! This looks delicious."
                $ breakfast_result = "perfect"
                
            "Fried":
                hide egg
                show fried_egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
                e "A perfect sunny-side up egg! The yolk looks so golden."
                $ breakfast_result = "perfect"
                
            "Raw (eat it uncooked)":
                $ amelia_sanity -= 1
                e "Maybe... maybe raw is more nutritious? Right?"
                $ breakfast_result = "disturbing"
        
        jump cooking_end

    # Disturbing rat cooking
    label cook_rat:
        hide egg
        hide cockroach
        
        e "This rat... it looks so fresh. Maybe it's just... protein?"
        e "I should probably clean it properly..."
        e "This is... this is normal, right? People eat all kinds of things..."
        $ amelia_sanity -= 2
        $ breakfast_result = "disturbing"
        
        jump cooking_end

    # Very disturbing cockroach cooking  
    label cook_cockroach:
        hide egg
        hide rat
        
        e "This cockroach... it's so crunchy-looking. Like a little snack!"
        e "Mmm... crunchy! This is... this is fine. Totally fine."
        $ amelia_sanity -= 3
        $ breakfast_result = "very_disturbing"
        
        jump cooking_end
        
    # Absolutely unhinged - cook everything
    label cook_everything:
        e "Why choose? I'll make a... special breakfast medley!"
                
        e "Egg for protein, rat for... more protein, and cockroach for that extra crunch!"
        
        menu:
            e "What should I add to this... masterpiece?"
            
            "More seasoning":
                e "Salt, pepper, maybe some herbs... make it fancy!"
                $ amelia_sanity -= 1
                
            "Just let it simmer":
                e "Low and slow... that's how you make gourmet food!"
                $ amelia_sanity -= 2
                
            "Turn up the heat":
                e "High heat will really bring out those... unique flavors!"
                $ amelia_sanity -= 1
        
        
        e "Look at this beautiful creation! I'm practically a chef!"
        $ breakfast_result = "absolutely_unhinged"
        
        jump cooking_end

    # End of cooking minigame
    label cooking_end:
        
        # Different outcomes based on what was cooked and Amelia's sanity
        if breakfast_result == "perfect":
            e "Mmm! This tastes amazing! I feel so energized for school!"
            $ amelia_confidence = 3
            
        elif breakfast_result == "disturbing":
            if amelia_sanity >= -1:
                e "That was... interesting. Maybe I'm becoming more adventurous with food?"
                $ amelia_confidence = 1
            else:
                e "That was... that was delicious! I don't know why people are so picky about food."
                $ amelia_confidence = 2
                
        elif breakfast_result == "very_disturbing":
            if amelia_sanity >= -3:
                e "Wow! That had such a unique texture! I should cook like this more often!"
                $ amelia_confidence = 2
            else:
                e "Perfect! Nothing beats a good, crunchy breakfast! I feel amazing!"
                $ amelia_confidence = 3
                
        elif breakfast_result == "absolutely_unhinged":
            e "This is the best breakfast I've ever made! I'm such a creative cook!"
            e "I bet other people would love to try my special recipes!"
            $ amelia_confidence = 4
            $ amelia_sanity -= 1  # She's completely lost touch with reality
        
        # Sanity check dialogue
        if amelia_sanity <= -5:
            e "I feel so... enlightened about food. Why does everyone eat such boring things?"
        elif amelia_sanity <= -3:
            e "I'm really expanding my culinary horizons! This is so exciting!"
        elif amelia_sanity <= -1:
            e "Maybe I should try more... unique ingredients sometime."
    hide egg
    hide rat
    hide cockroach
    scene bg room
    
    show ameliaTalk at bottom_position2

    e "Now, I need to pack my bag. What should I bring?"
    jump choice_menu

# ====================
# CHOICE MENU
# ====================
label choice_menu:
    menu:
        "Trash":
            e "Although I practically live in it, I don't want people to know that, so let's not bring that to school."
            jump choice_menu

        "Pencils":
            e "Great choice!"
            e "I love to draw!"

        "Cockroaches":
            e "Although I practically live with them, I don't want people to know that, so let's not bring that to school."
            jump choice_menu

    scene bg livingroom
    show ameliaTalk at bottom_position2

    e "Let's go to school!"
    show bg clouds
    e "Better start heading to school now!"
    e "*someone calls Amelia's name*"
    e "Did someone call me?"

    menu:
        "Ignore the call":
            e "I should just ignore it and head to school."

        "Answer the call":
            e "Hello?"
            jump end_amelia_one


# ====================
# ENDING
# ====================
label end_amelia_one:
    scene black
    e "Breaking news, Amelia, a 13-year old highschooler, has gone missing!"
    show poster
    e "She was last seen wearing a school uniform and carrying a backpack."
    e "If you have any information, please contact the local authorities."
    hide poster

    scene bg livingroom
    show bloody_amelia at bottom_position2
    e "Well, that was one sweet tomorrow..."
    show text "To be continued..." at truecenter with dissolve
    return

# ====================
# SCARLETT SCENE
# ====================
#two friend scene
Character LC = Character("Lilah and Celeste")
    narrator "On the way to school, Amelia sees her two friends, Lilah and Celeste"
    show bg school
    show ameliaTalk at bottom_position2
    e "Lilah! Celeste! Wait up!"
    show ameliaHappy at bottom_position2
    LC "Hey Amelia! What's up?"
    e "Not much, just heading to school. You guys?"
    LC "Same here! Wanna walk together?"
    e "Sure!"
    narrator "They walk together to school, chatting and laughing along the way."
jump choice_menu_scarlett

label choice_menu_scarlett:
    narrator "The group slowly approaches a certain black-haired girl."
    narrator "Amelia slowly lingers away from her group"
    show scarlett at bottom_position3
e "Oh no... it's Scarlett."
e "What should I do?"
    menu: 
        "Question her!":
            e "No, I need to stay composed at school…"
            jump choice_menu_scarlett

        "Did she notice anything weird…?":
            e "Ew…that makes me sound desperate…"
            jump choice_menu_scarlett

        "Let’s just say hi…":
            e "Hi Scarlett..! How’s it going?"
            jump scarlett_confrontation

label scarlett_confrontation:
    scene bg school
    show scarlett at bottom_position3
    e "Hi Scarlett..! How’s it going?"  
    show Scarlett Talk at bottom_position3
    scarlett"Is everything alright with you? Your skirt looks like it's stained at the bottom…"
    scarlett "I thought you should know, Amelia."

    show ameliaHappy at bottom_position2
    e "Why is she trying to nitpick?"
    e "I mean…look at her…"
    hide ameliaHappy

    show angry at bottom_position2
    e "Is she trying to start a fight or something??"
    e "What’s her problem???"
    hide angry

    show ameliaTalk at bottom_position2
    e "Why do you care, Scarlett? Everything is fine."
    scarlett "I just noticed… this isn’t the first time I’ve noticed this though…"

    show Amelia_ponder at bottom_position2
    amelia_ponder "She’s always looking for something to complain about…"
    hide Amelia_ponder

    show ameliaTalk at bottom_position2
    e "Why do you care, Scarlett? Everything is fine."
    scarlett "I just noticed… this isn’t the first time I’ve noticed this though…"
    image blackedout = "blackedscarlett.png"
    
    # scarlett face to be blacked out
    narrator "When Scarlett says this Amelia sees red and says--"
    hide scarlettTalk
    show blackedout at bottom_position3
    e "What’s that supposed to mean?"

    # when Scarlett replies, everything goes black behind Amelia

    scarlett "It’s just…I’ve heard ur friends say some things…"
    hide blackedout
    show bg black with fade
    show Scarlett Anxious at bottom_position3
    menu:
        e "What did they say?":
            jump ending_2friends

        e "Scarlett, you misheard. They would never."
            jump ending_scarlett

        e "I don’t care what they say. You’re just jealous."
label ending_scarlett:
    image poster_scarlett = "missingposter_scarlett.png"
    scene black
    e "Breaking news, Scarlett, a 13-year old highschooler, has gone missing!"
    show poster_scarlett
    e "She was last seen wearing a school uniform and carrying a backpack."
    e "If you have any information, please contact the local authorities."
    hide poster_scarlett

    scene bg livingroom
    show bloody_amelia at bottom_position2
    e "Well, that was one sweet tomorrow..."
    show text "To be continued..." at truecenter with dissolve
    
    return
label ending_2friends:
    image poster_twofriend = "missingposter_twofriends.png"
    scarlett "They’ve been making fun of you…"
    scarlett "…I heard they’ve been trying to dig up dirt on you to humiliate you…"
    amelia "Thanks for telling me! I’ll call them over and have a chat with them, hopefully we can talk out our problems."
    scarlett "R-right."
    hide Scarlett Anxious
    hide ameliaTalk
    show bg black with fade
    show missingposter_twofriend at truecenter
    newscaster "Breaking news, Lilah and Celeste, 2 13-year old highschoolers, have gone missing!"
    scene bg livingroom
    #Scene 9 (living room) Amelia seems upset as she stands in her living room, already ready for school
    show ameliaworried at bottom_position2
    e "I can’t believe my friends are gone.."

    #Scene 10 (school) Scarlett and Amelia are talking
    show bg school
    show scarlett at bottom_position3
    show ameliaTalk at bottom_position2
    scarlett "Hey… what happened to your friends?"
    e "I don’t know… they just disappeared after school yesterday…"
    scarlett "That’s so weird… do you think something happened to them?"
    hide scarlett
    hide ameliaTalk
    show bg black with fade
    image trashbags = "trashbags.png"
    show trashbags at truecenter
    hide
    newscaster "In other news, two teenagers have gone missing in the city. Authorities are investigating the disappearances."
    show trashbags at truecenter
    newscaster "2 days later: The teenagers were brutally murdred and stuffed in trashbags, their bodies found in an alleyway."
    # When Amelia talks, scenes of her talking to her friends cut to scenes of her with large trash bags
    show bg school
    show scarlett at bottom_position3
    show ameliaTalk at bottom_position2
    e "They came over to talk, but… I guess they never reached home safely…"
    hide scarlett
    show scarlettAnxious
    scarlett "Oh no! I hope nothing bad happened to them…"
    hide scarlettAnxious
    #possible here for scary amelia face
    show bg black with fade
    black screen
    e "Well it was me or them…"
    hide ameliaTalk #change if scary amelia is made
    show bloody_amelia at bottom_position2
    hide bloody_amelia
    show text "To be continued..." at truecenter with dissolve
    return
narrator "No one died, good job."
return