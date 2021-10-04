﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chika")
define r = Character("Ryoko")
define k = Character("Kichi")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    r "I am speaking to be sure I exist"

    k "Me too!"

    # This ends the game.

    return
