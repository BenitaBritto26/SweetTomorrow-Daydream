# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amelia")
image clouds = "clouds.png"
image nightgown = "nightgown.png"

# Define cooking ingredient images
image egg = "egg.png"
image rat = "rat.png"
image cockroach = "cockroach.png"
image pan = "pan.png"

# Define kitchen background that stretches to fit the whole screen
image bg kitchen = Transform("kitchen.png", size=(1920, 1080))

# Define a transform to position the image at the bottom.
# This transform must include an indented block of statements.
transform bottom_position:
    # Scale the image a bit and place it centered at the bottom.
    zoom 2.5
    xalign 0.5
    # yalign 1.0 places the image at the bottom of the window. The
    # original used 2.0 which is outside the usual 0..1 range.
    yalign 1.0
    # Additional vertical offset if you want it further down.
    yoffset 600
    # Even further down

# The game starts here.

label start:

    # Show clouds background with no character or text for 4 seconds
    scene clouds

    # Wait for 4 seconds with no dialogue or characters
    $ renpy.pause(2.5, hard=True)

    # Show the nightgown image positioned at the bottom
    show nightgown at bottom_position with dissolve

    # These display lines of dialogue.

    e "The sun's already so bright! I guess I better start getting ready for school!"
    
    e "But first, I should make some breakfast! What should I cook?"
    
    # Jump to cooking minigame
    call cooking_minigame
    
    e "Now I'm ready for school!"

    # This ends the game.
    return

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
    
    jump cooking_end

# Absolutely unhinged - cook everything
label cook_everything:
    e "Why choose? I'll make a... special breakfast medley!"
    
    show everything_cooking
    
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
    
    show everything_cooked
    
    e "Look at this beautiful creation! I'm practically a chef!"
    $ breakfast_result = "absolutely_unhinged"
    
    jump cooking_end

# Pancakes cooking sequence
label make_pancakes:
    e "Pancakes it is! This will be a bit challenging..."
    
    menu:
        e "How much flour should I add?"
        
        "1 cup (perfect amount)":
            $ cooking_skill += 1
            e "Perfect! Just the right amount."
            
        "3 cups (way too much)":
            $ cooking_skill -= 1
            e "Oh no, that's way too much flour!"
            
        "Half a cup (too little)":
            e "Hmm, this seems a bit thin..."
    
    menu:
        e "What heat should I use for cooking?"
        
        "Medium heat":
            $ cooking_skill += 1
            e "Medium heat is perfect for even cooking!"
            
        "High heat (burn risk)":
            $ cooking_skill -= 1
            e "Oh no! They're burning!"
            
        "Low heat":
            e "They're cooking slowly but surely..."
    
    # Determine outcome based on cooking skill
    if cooking_skill >= 2:
        $ breakfast_quality = "perfect"
        show pancakes_perfect
        e "Wow! These pancakes look amazing! I'm getting really good at cooking!"
        
    elif cooking_skill >= 0:
        $ breakfast_quality = "good"
        show pancakes_good  
        e "Not bad! These pancakes are pretty tasty."
        
    else:
        $ breakfast_quality = "burnt"
        show pancakes_burnt
        e "Oh no... they're a bit burnt. I'll do better next time!"
    
    jump cooking_end

# Toast and eggs sequence  
label make_toast_eggs:
    e "Toast and eggs - a classic breakfast!"
    
    menu:
        e "How do I want my eggs?"
        
        "Scrambled":
            $ cooking_skill += 1
            e "Scrambled eggs are my specialty!"
            
        "Fried (sunny side up)":
            menu:
                e "How long should I cook them?"
                
                "2 minutes (perfect)":
                    $ cooking_skill += 1
                    e "Perfect timing!"
                    
                "5 minutes (overcooked)":
                    $ cooking_skill -= 1
                    e "Oops, the yolk got too hard..."
        
        "Boiled":
            e "Simple and safe choice!"
    
    menu:
        e "What setting for the toaster?"
        
        "Light golden":
            $ cooking_skill += 1
            e "Perfect golden brown!"
            
        "Dark (almost burnt)":
            $ cooking_skill -= 1
            e "A bit too dark for my taste..."
            
        "Barely toasted":
            e "Still soft, but that's okay."
    
    if cooking_skill >= 2:
        $ breakfast_quality = "perfect"
        e "This looks restaurant-quality! I'm so proud!"
    elif cooking_skill >= 0:
        $ breakfast_quality = "good"
        e "A solid, tasty breakfast!"
    else:
        $ breakfast_quality = "poor"
        e "Well... it's edible at least!"
    
    jump cooking_end

# Cereal sequence (easy but less rewarding)
label make_cereal:
    e "Sometimes simple is best!"
    
    menu:
        e "Which cereal should I choose?"
        
        "Healthy granola":
            $ cooking_skill += 1
            e "Good choice for energy!"
            
        "Sweet chocolate cereal":
            e "A little treat won't hurt!"
            
        "Plain cornflakes":
            e "Classic and simple."
    
    $ breakfast_quality = "simple"
    e "Quick and easy! Sometimes that's exactly what you need."
    
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
    
    # Return to main story
    return

    return

