# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Amelia = Character("Amelia")
define Scarlett = Character("Scarlett")
define n = Character(None)
define friend = Character("Friend")

image bg room = Transform("bedroom.png", size =(1920, 1080))
image bg livingroom = Transform("livingroom.png", size =(1920, 1080))
image bg school = Transform("school.png", size =(1920, 1080))
image bg outside = Transform("outsideHouse.png", size =(1920, 1080))
image nightgown = "nightgown.png"
image talknightgown = "talknightgown.png"

# Define cooking ingredient images
image egg = "egg.png"
image rat = "rat.png"
image cockroach = "cockroach.png"
image pan = "pan.png"

# Define kitchen background that stretches to fit the whole screen
image bg kitchen = Transform("kitchen.png", size=(1920, 1080))

transform bottom_position:
    # Scale the image a bit and place it centered at the bottom.
    zoom 3
    xalign 0.5
    # yalign 1.0 places the image at the bottom of the window. The
    # original used 2.0 which is outside the usual 0..1 range.
    yalign 0.75
    # Additional vertical offset if you want it further down.
    yoffset 600
    # Even further down

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

    # Show room background with no character or text for 4 seconds
    scene bg room

    # Wait for 4 seconds with no dialogue or characters
    $ renpy.pause(1.5, hard=True)

    # Show the nightgown image positioned at the bottom
    show nightgown at bottom_position with dissolve
    hide nightgown
    show talknightgown at bottom_position
   
    Amelia "The sun's already so bright! I guess I better start getting ready for school!"
    # changes
    Amelia "First, let me get dressed."
    Amelia "What should I wear today?"
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
            Amelia "Good choice!"
        "The second uniform!":
            Amelia "Sorry, I don't want to wear that. We're going to wear the first one."
        "The third uniform!":
            Amelia "Sorry I don't want to wear that. We're going to wear the first one."
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

    Amelia "Now, it's time for me to make some breakfast!"
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
    
        Amelia "Let me see what I have to cook with..."
    
        # Show all ingredients lined up in the center with more spacing
        show cockroach at Transform(xalign=0.2, yalign=0.5, zoom=0.4)
        show egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
        show rat at Transform(xalign=0.8, yalign=0.5, zoom=0.1)

        Amelia "Hmm... what should I cook? They all look... interesting."
    
        menu:
            Amelia "I have some options here..."
        
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
        
        Amelia "A nice, normal egg! Perfect for breakfast."
        
        menu:
            Amelia "How should I cook it?"
            
            "Scrambled":
                hide egg
                show scrambled_egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
                Amelia "Fluffy scrambled eggs! This looks delicious."
                $ breakfast_result = "perfect"
                
            "Fried":
                hide egg
                show fried_egg at Transform(xalign=0.5, yalign=0.5, zoom=0.4)
                Amelia "A perfect sunny-side up egg! The yolk looks so golden."
                $ breakfast_result = "perfect"
                
            "Raw (eat it uncooked)":
                $ amelia_sanity -= 1
                Amelia "Maybe... maybe raw is more nutritious? Right?"
                $ breakfast_result = "disturbing"
        
        jump cooking_end

    # Disturbing rat cooking
    label cook_rat:
        hide egg
        hide cockroach
        
        Amelia "This rat... it looks so fresh. Maybe it's just... protein?"
        Amelia "I should probably clean it properly..."
        Amelia "This is... this is normal, right? People eat all kinds of things..."
        $ amelia_sanity -= 2
        $ breakfast_result = "disturbing"
        
        jump cooking_end

    # Very disturbing cockroach cooking  
    label cook_cockroach:
        hide egg
        hide rat
        
        Amelia "This cockroach... it's so crunchy-looking. Like a little snack!"
        Amelia "Mmm... crunchy! This is... this is fine. Totally fine."
        $ amelia_sanity -= 3
        $ breakfast_result = "very_disturbing"
        
        jump cooking_end
        
    # Absolutely unhinged - cook everything
    label cook_everything:
        Amelia "Why choose? I'll make a... special breakfast medley!"
                
        Amelia "Egg for protein, rat for... more protein, and cockroach for that extra crunch!"
        
        menu:
            Amelia "What should I add to this... masterpiece?"
            
            "More seasoning":
                Amelia "Salt, pepper, maybe some herbs... make it fancy!"
                $ amelia_sanity -= 1
                
            "Just let it simmer":
                Amelia "Low and slow... that's how you make gourmet food!"
                $ amelia_sanity -= 2
                
            "Turn up the heat":
                Amelia "High heat will really bring out those... unique flavors!"
                $ amelia_sanity -= 1
        
        
        Amelia "Look at this beautiful creation! I'm practically a chef!"
        $ breakfast_result = "absolutely_unhinged"
        
        jump cooking_end

    # End of cooking minigame
    label cooking_end:
        
        # Different outcomes based on what was cooked and Amelia's sanity
        if breakfast_result == "perfect":
            Amelia "Mmm! This tastes amazing! I feel so energized for school!"
            $ amelia_confidence = 3
            
        elif breakfast_result == "disturbing":
            if amelia_sanity >= -1:
                Amelia "That was... interesting. Maybe I'm becoming more adventurous with food?"
                $ amelia_confidence = 1
            else:
                Amelia "That was... that was delicious! I don't know why people are so picky about food."
                $ amelia_confidence = 2
                
        elif breakfast_result == "very_disturbing":
            if amelia_sanity >= -3:
                Amelia "Wow! That had such a unique texture! I should cook like this more often!"
                $ amelia_confidence = 2
            else:
                Amelia "Perfect! Nothing beats a good, crunchy breakfast! I feel amazing!"
                $ amelia_confidence = 3
                
        elif breakfast_result == "absolutely_unhinged":
            Amelia "This is the best breakfast I've ever made! I'm such a creative cook!"
            Amelia "I bet other people would love to try my special recipes!"
            $ amelia_confidence = 4
            $ amelia_sanity -= 1  # She's completely lost touch with reality
        
        # Sanity check dialogue
        if amelia_sanity <= -5:
            Amelia "I feel so... enlightened about food. Why does everyone eat such boring things?"
        elif amelia_sanity <= -3:
            Amelia "I'm really expanding my culinary horizons! This is so exciting!"
        elif amelia_sanity <= -1:
            Amelia "Maybe I should try more... unique ingredients sometime."
    hide egg
    hide rat
    hide cockroach
    scene bg room
    
    show ameliaTalk at bottom_position2

    Amelia "Now, I need to pack my bag. What should I bring?"    
    menu:
        "Trash":
            Amelia "Although I practically live in it, I don't want people to know that, so let's not bring that to school."
        "Pencils":
            Amelia "Great choice!"
            Amelia "I love to draw!"
        "Cockroaches":
            Amelia "Although I practically live with them, I don't want people to know that, so let's not bring that to school."
    
    #Scene 2 (living room) Amelia stands in the living room, sun shining through the window, 
    #the tv is on and a man lays on the couch (partially visible) with his hand holding a bottle that’s spilling on the floor
    scene bg livingroom
    show ameliaTalk at bottom_position2
    Amelia "Let's go to school!"

    #Scene 3 (outside house) Amelia stands outside her house, her neighbor briefly visible behind her
    show bg outside
    show ameliaTalk at bottom_position2
    Amelia "I better start heading to school now!"
    # someone calls Amelia
    n "In the background, someone calls Amelia's name..."
    Amelia "Did someone call me?"
    menu:
        "Ignore them and keep walking":
            Amelia "It's fine, I'll be back home later so I can catch up with them later if it's important!"
        "Turn around to see who it is":
            Amelia "No, I'll run late if I stay to chat… I should head out!"
    
    hide ameliaTalk
    scene bg school
    n "Amelia heads to school..."

    show ameliaHappy at bottom_position2 with dissolve
    Amelia "I made it to school!"
    Amelia "I better go say hello to my friends!"
    image twoFriends = "friendsNormal.png"

    transform bottom_right:
        zoom 3
        xpos (1000)
        ypos (100)

    show twoFriends at bottom_right with dissolve
    n "Amelia chats with her friends for a bit..."
    transform bottom_right2:
        zoom 3
        xpos (1000)
    image scarlettNorm = "scarlettNormal.png"
    image scarlettTalk = "scarlettTalk.png"

    hide twoFriends with dissolve
    Amelia "That was so fun!"
    show scarlettNorm at bottom_right2 with dissolve
   
    Amelia "*Thinks* Hmm what does she want?"
    menu:
        "Question her!":
            Amelia "No, I need to stay composed at school…"
        "Did she notice anything weird…?":
            Amelia "Ew…that makes me sound desperate…"
        "Let's just say hi…":
            Amelia "That's the best way to keep things casual."

    Amelia "Hi Scarlett..! How's it going?"

    Scarlett "Is everything alright with you? Your skirt looks like it's stained at the bottom…"
    Scarlett "I thought you should know"
    Amelia "Why is she trying to nitpick?"
    Amelia "I mean…look at her…"
    Amelia "Is she trying to start a fight or something??"
    Amelia "What's her problem???"

    Amelia "Why do you care, Scarlett? Everything is fine."
    Scarlett "I just noticed…this isn't the first time I've noticed this though…"

    hide scarlettNorm
    hide scarlettTalk
    transform bottom_right3:
        zoom 3
        xpos (1200)
        ypos (50)
    image badScarlett = "badScarlett.png"
    show badScarlett at bottom_right3

    Amelia "What's that supposed to mean?"
    Scarlett "It's just…I've heard ur friends say some things…"

    menu:
        "What did they say?":
            jump end_amelia_one

        "Scarlett, you misheard. They would never.":
            jump end_amelia_two

label end_amelia_one:
    hide badScarlett
    transform bottom_right4:
        zoom 3
        xpos (1200)
        ypos (50)
    show scarlettNorm at bottom_right2 with dissolve

    Scarlett "They've been making fun of you…"
    Scarlett "...I heard they've been trying to dig up dirt on you to humiliate you…"
    show ameliaTalk at bottom_position2
    Amelia "Thanks for telling me! I'll call them over and have a chat with them, hopefully we can talk out our problems."
    Scarlett "R-right."

    hide scarlettTalk
    show ameliaHappy at bottom_position2 with dissolve
    Amelia "(I need to be more careful about who I trust…)"
    Amelia "(I can't let anyone find out my secret.)"
    Amelia "Looks like I'm going to have to be more careful about who I hang out with…"
    n "Amelia heads to class, trying to shake off the uneasy feeling Scarlett's words left her with..."
    n "Looks like she'll have to cut off some friendships to protect her secret…"
    n "The End."
    return

label end_amelia_two:
    hide ameliaTalk
    hide ameliaHappy
    image ameliaAngry = "angry.png"
    show ameliaAngry at bottom_position2 with dissolve
    Amelia "Just 'cause you have no friends, doesn't mean you can mess up my friendships…"
    Scarlett "No! I would never spread rumors…I just-"

    Amelia "Scarlett. Can we please just talk about this after school?"
    Scarlett "Oh…uh yeah, that works I guess…"

    hide ameliaAngry
    hide badScarlett

    n "The next day at school..."
    show ameliaHappy at bottom_position2 with dissolve
    Amelia "I better go say hello to my friends!"
    image twoFriends2 = "friendsTalk.png"

    transform bottom_right2:
        zoom 3
        xpos (1000)
        ypos (100)

    show twoFriends2 at bottom_right2 with dissolve

    friend "Hey Amelia! Over here!"
    friend "Something crazy happened yesterday…"
    friend "Apparently some girl named Scarlett died from Tuberculosis!"
    friend "She seemed fine when I saw her last week though…"

    Amelia "Oh no..."
    Amelia "That's so sad…"
    hide twoFriends2 with dissolve

    image ameliaNorm = "AmeliaTalksNormal?.png"
    show ameliaNorm at bottom_position2
    Amelia "(I guess that's what happens when you try to dig up dirt on people…)"
    n "The End..."
    
    




    
    


