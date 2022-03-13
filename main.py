from imp import reload
import random
import enum

from numpy import block


class Action(enum.Enum):
    block = 1
    shoot = 2
    reload = 3


userammo = 0
compammo = 0
deathcount = 0
print("Welcome to the matrix!\nNo, not the movie\nIts a game where you can reload ammo, shoot the enemy or block enemy attacks")
print("You can type 'reload', 'block' or 'shoot'")
print("If you choose block or shoot, you will have to choose a potency value between 1 to 4")

# main game loop

while deathcount == 0:
    print("Userammo:", userammo)
    print("Compammo:", compammo)

    # comp turn choosing

    userstring = (input("Enter your command:"))

    user = Action[userstring]

    if user == Action.block:
        userpotency = (input("Enter the potency between 1 to 4:"))
    if user == Action.shoot:
        userpotency = (input("Enter the number of bullets between 1 to 4:"))
    if user == Action.reload:
        userpotency = "1"

    if userammo == 0 and compammo == 0:
        comp = Action.reload
        comppotency = 1
    if userammo > 0 and compammo == 0:
        x = random.randint(1, 3)
        y = random.randint(1, min(userammo, 4))
        if x == 1 or x == 3:
            comp = Action.block
            compotency = y
        if x == 2:
            comp = Action.reload
            compotency = 1
    if userammo == 0 and compammo > 0:
        x = random.randint(1, 3)
        y = random.randint(1, min(compammo, 4))
        if x == 1 or x == 3:
            comp = Action.shoot
            comppotency = y
        if x == 2:
            comp = Action.reload
            compotency = 1
    if userammo > 0 and compammo > 0:
        if userammo > compammo:
            x = random.randint(1, 4)
            y = random.randint(1, min(userammo, 4))
            z = random.randint(1, min(compammo, 4))
            if x == 1 or x == 4:
                comp = Action.block
                comppotency = y
            elif x == 2:
                comp = Action.shoot
                comppotency = z
            else:
                comp = Action.reload
                comppotency = 1

        if userammo < compammo:
            x = random.randint(1, 4)
            y = random.randint(1, min(userammo, 4))
            z = random.randint(1, min(compammo, 4))
            if x == 1 or x == 4:
                comp = Action.block
                comppotency = y
            elif x == 2:
                comp = Action.shoot
                comppotency = z
            else:
                comp = Action.reload
                comppotency = 1

        if userammo == compammo:
            x = random.randint(1, 5)
            y = random.randint(1, min(userammo, 4))
            z = random.randint(1, min(compammo, 4))
            if x == 1 or x == 4:
                comp = Action.block
                comppotency = y
            elif x == 2 or x == 5:
                comp = Action.shoot
                comppotency = z
            else:
                comp = Action.reload
                comppotency = 1

    # random text check
    if user != Action.reload and user != Action.block and user != Action.shoot:
        print("Invalid choice")
        print("You lost through default out\nThe computer won")
        deathcount = deathcount+1
        continue

    # potency check
    if not userpotency.isnumeric():
        print("Invalid choice\nPotency is supposed to be an integer")
        print("You lost through default out\nThe computer won")
        deathcount = deathcount+1
        continue
    elif int(userpotency) > 5:
        print("Invalid choice\nPotency has to be from 1 to 4")
        print("You lost through default out\nThe computer won")
        deathcount = deathcount+1
        continue
    else:
        print("You used", user.name, int(userpotency))
        print("The computer used", comp.name, comppotency, "\n")

    # checks

    # too many bullets shot
    if user == Action.shoot and userammo < int(userpotency):
        print("You did not have that many bullets")
        print("You lost through default out\nThe computer won")
        deathcount = deathcount+1
        continue

    #shoot and block
    if (user == Action.shoot and comp == Action.block):
        if int(userpotency) == comppotency:
            print("The computer blocked your attack")
            userammo = userammo - int(userpotency)
        else:
            print("The computer got shot\nYou won!")
            deathcount = deathcount+1
        continue

    if (user == Action.block and comp == Action.shoot):
        if int(userpotency) == (comppotency):
            print("You blocked the computer's attack")
            compammo = int(compammo)-int(comppotency)
        else:
            print("The computer won!\nYou lost by getting shot")
            deathcount = deathcount+1
        continue

    if user == Action.block and comp == Action.block:
        print("Both of you used block")
        continue

    if user == Action.shoot and comp == Action.reload:
        print("The computer got shot\nYou won!")
        deathcount = deathcount+1
        continue
    if comp == Action.shoot and user == Action.reload:
        print("You lost\nThe computer won!")
        deathcount = deathcount+1
        continue

    if user == Action.shoot and comp == Action.shoot:
        if int(userpotency) > comppotency:
            print("Both of you used shoot")
            deathcount = deathcount+1
            print("The computer got shot\nYou won!")
        if int(userpotency) < comppotency:
            print("Both of you used shoot")
            print("You lost by getting shot\nThe computer won!")
            deathcount = deathcount+1
        else:
            print("Both of you shot the same number of bullets")
            userammo = userammo-int(userpotency)
            compammo = compammo-comppotency
        continue

    if user == Action.reload and comp == Action.reload:
        userammo = userammo+1
        compammo = compammo+1
        continue
    if user == Action.reload:
        userammo = userammo+1
        continue
    if comp == Action.reload:
        compammo = compammo+1
        continue
    if user == Action.block and comp == Action.reload:
        compammo = compammo+1
        continue
    if comp == Action.block and user == Action.reload:
        userammo = userammo+1
        continue
