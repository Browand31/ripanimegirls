# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define c = Character("Chika", color="#ff66ed")
define r = Character("Ryoko", color="#ff7a14")
define k = Character("Kichi", color="#9000c9")
define m = Character (_("Main Character"), color="ffffff")
define s = Character("Sayuri", color="#b03173")
define e = Character("Kei", color="#6de5ed")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    m "Today is my first day of class"

    show chika neutral
    with fade

    c "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    hide chika 
    with fade

    show ryoko neutral
    with fade

    r "I am speaking to be sure I exist"

    hide ryoko 
    with fade

    show kichi neutral
    with fade

    k "Me too!"

    hide kichi 
    with fade 

    show sayuri neutral 
    with fade 

    s "I exist as well!"

    hide sayuri
    with fade

    show kei neutral
    with fade

    e "And me too!"

    # This ends the game.

    return
