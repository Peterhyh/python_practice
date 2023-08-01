print('1)    Wizard')
print('2)    Elf')
print('3)    Human')
print('4)    Orc')
print('5)    Exit')

wizard = 'Wizard'
wizard_hp = 70
wizard_damage = 150

elf = 'Elf'
elf_hp = 100
elf_damage = 100

human = 'Human'
human_hp = 150
human_damage = 20

orc = 'Orc'
orc_hp = 150
orc_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    while True:

        userSelection = input('Choose your character: ').lower()

        if userSelection == '1' or userSelection == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print("You have chosen the character: " + wizard)
            print("Health:", wizard_hp)
            print("Damage:", wizard_damage, "\n")
            break
        elif userSelection == '2' or userSelection == 'Elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print("You have chosen the character: " + elf)
            print("Health:", elf_hp)
            print("Damage:", elf_damage, "\n")
            break
        elif userSelection == '3' or userSelection == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print("You have chosen the character: " + human)
            print("Health:", human_hp)
            print("Damage:", human_damage, "\n")
            break
        elif userSelection == '4' or userSelection == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print("You have chosen the character: " + orc)
            print("Health:", orc_hp)
            print("Damage:", orc_damage, "\n")
            break
        elif userSelection == '5' or userSelection == 'exit':
            print("Goodbye!")
            exit()
        else:
            print('Unknown character')

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The dragon's hitpoints are now:", dragon_hp, "\n")
        if dragon_hp <= 0:
            print('The dragon has lost the battle!\n')
            break

        my_hp = my_hp - dragon_damage
        print("The dragon has damaged the", character)
        print("The", character, "hitpoints are now:", my_hp, "\n")
        if my_hp <= 0:
            print('The', character, 'has lost the battle!\n')
            break

    restart_game = input('Play again?\n1)    yes\n2)    no\n').lower()

    if restart_game == "1" or restart_game == "yes":
        continue
    elif restart_game == "2" or restart_game == "no":
        print('Goodbye!')
        exit()
