# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amelia")
image clouds = "clouds.png"
image nightgown = "nightgown.png"

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

    menu:
        "What is this?":
            e "A coding competition!"
        "Who are you??":
            e "idk lol"


        e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

