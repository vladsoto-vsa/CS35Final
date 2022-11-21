"""
This program demonstrates the use of a function called verse that
can be called with different arguments to generate the song Old MacDonald
Had a Farm.
"""

def main():
    verse("cow", "moo")
    verse("pig", "oink")
    verse("dog", "woof")
    verse("cat", "meow")
    verse("chicken", "cluck")
    verse("Lil Pump", "Esketit")

def verse(animal, sound):
    """
    This function expects to receive two strings, the first being
    a farm animal and the second being the sound that the animal makes.
    This function prints one verse of the song.
    """
    print()
    print("Old MacDonald had a farm, EIEIO")
    print("And on his farm he had a %s, EIEIO" % (animal))
    print("With a %s, %s here and a %s, %s there" %
          (sound, sound, sound, sound))
    print("Here a %s, there a %s, everywhere a %s, %s" %
          (sound, sound, sound, sound))
    print("Old MacDonald had a farm, EIEIO")
    print()

main()
