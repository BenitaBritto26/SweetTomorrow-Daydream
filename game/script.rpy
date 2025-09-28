# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amelia")
image clouds = "clouds.png"
image nightgown = "nightgown.png"


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
   
    e "Hi, welcome to Sweet Tomorrow!"
    # changes
    e "do you want to start?"
    menu:
        "Yes":
            e "Great! Let's get started."
        "No":
            e "Oh, that's too bad. Maybe next time!"
            return
    e "What should Amelia wear today?"
    menu:
        "Uniform 1":
            e "Good choice!"
        "Uniform 2":
            e "Sorry, I don't want to wear that. We're going to wear uniform 1"
        "Uniform 3":
            e "Sorry I don't want to wear that. We're going to wear uniform 1"

    e "Let's make breakfast!"
    e "What should we make?"
    menu:
        "Pancakes":
            e "Yum! Pancakes are my favorite."
        "Omelette":
            e "An omelette sounds delicious!"
        "Cereal":
            e "Cereal is quick and easy!"
    e "Time to head to school!"
    e "What should we pack in my bag"
    menu:
        "Trash":
            e "Although I practically live in it, I don't want people to know that, so let's not bring that to school."
        "pencils":
            e "great choice!"
            e "I love to draw!"
        "Cockroaches":
            e "Although I practically live in it, I don't want people to know that, so let's not bring that to school."
    #Scene 2 (living room) Amelia stands in the living room, sun shining through the window, 
    #the tv is on and a man lays on the couch (partially visible) with his hand holding a bottle that’s spilling on the floor
    e "let's go to school!"
    #Scene 3 (outside house) Amelia stands outside her house, her neighbor briefly visible behind her
    e "better start heading to school now!"
    # someone calls Amelia
    e "*someone calls Amelia's name*"
    e "Did someone call me?"
    menu:
        "Ignore them and keep walking":
            e "It's fine, I'll be back home later so I can catch up with them later if it's important!"
        "Turn around to see who it is":
            e "No, I'll run late if I stay to chat…I should head out!"
    #narrator
    # this is in the loading screen mode thing, scene 4
    e "Amelia heads to school..."
    # scene 5, (school) behind amelia, two friends approach
    e "I better go say hello to my friends!"
    # scene 6 (school) Behind Amelia, two friends leave while Scareltt approaches
    e "That was so fun!"
    # two friends appear
    # images
    image two friends = "two friends.png"
    show two friends with dissolve
    # two friends talk to Amelia, change text color to blue
    e "Hey, do you want to hang out after school?"
    # change text color to pink Amelia responds
    e "No sorry, I have to go home and... um... study"
    # two friends respond
    # change text color to blue
    e "oh, okay. Maybe next time!"
    # two friends leave

    #scene 7 (school) Behind Amelia, Scareltt approaches
    # narrator
    e "Scareltt approaches Amelia"
    e "In Amelia's mind: *Hmm, what does she want?*"
    label choices_menu:
        menu:
            "Question her!":
                e "No, I need to stay composed at school…"
                jump choices_menu
            "Did she notice anything weird…?":
                e "Ew… that makes me sound desperate…"
                jump choices_menu
            "Let's just say hi...":
                e "Yeah, that sounds good."
                jump after_choices

    label after_choices:
        # Amelia
        e "Hi Scarlett..! How's it going?"
        # Scarlett
        e "Is everything alright with you? Your skirt looks like it's stained at the bottom…"
        # Amelias thoughts
        e "Scarlets mind: “Why is she trying to nitpick?"
        e "I mean…look at her…"
        e "Is she trying to start a fight or something??"
        e "What’s her problem???"
    # This ends the game.

    return
