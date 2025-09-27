# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amelia")
image clouds = "clouds.png"

# The game starts here.

label start:

    # Show clouds background with no character or text for 4 seconds
    scene clouds
    
    # Wait for 4 seconds with no dialogue or characters
    $ renpy.pause(2.5, hard=True)
    
    # Show interstellar image popping up
    show interstellar with dissolve

    # These display lines of dialogue.
   
    e "Hi, welcome to Sweet Tomorrow!"
    
    menu:
        "What is this?":
            e "A coding competition!"
        "Who are you??":
            e "idk lol"
    

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
