# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image clouds = "bg clouds.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg clouds

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show interstellar

    # These display lines of dialogue.
   
    e "Hi, welcome to daydream!"
    
    menu:
        "What is this?":
            e "A coding competition!"
        "Who are you??":
            e "idk lol"
    

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
