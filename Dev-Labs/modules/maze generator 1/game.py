import time


def intro():
    print("Welcome to the adventure game!")
    time.sleep(1)
    print("You find yourself in a dark forest.")
    time.sleep(1)
    print("You can hear the sound of running water nearby.")
    time.sleep(1)
    print("You have a sword and a backpack. What do you do?")


def game():
    while True:
        action = input("> ")
        if action == "look":
            print("You see trees all around you.")
        elif action == "go":
            print("You follow the sound of the running water and arrive at a river.")
            time.sleep(1)
            print("There's a bridge spanning the river, but it looks old and rickety.")
            time.sleep(1)
            print("Do you cross the bridge?")
            bridge = input("> ")
            if bridge == "yes":
                print(
                    "You carefully cross the bridge and arrive at a clearing on the other side.")
                time.sleep(1)
                print("You see a castle in the distance.")
            else:
                print("You decide not to risk it and turn back.")
        elif action == "fight":
            print("You see a goblin approaching you!")
            time.sleep(1)
            print("You draw your sword and prepare to fight.")
            time.sleep(1)
            print("The goblin charges at you with a club.")
            time.sleep(1)
            print("What do you do?")
            fight = input("> ")
            if fight == "attack":
                print("You swing your sword and hit the goblin!")
                time.sleep(1)
                print("The goblin falls to the ground, defeated.")
            else:
                print(
                    "You hesitate for a moment, and the goblin strikes you with its club.")
                time.sleep(1)
                print("You fall to the ground, defeated.")
                time.sleep(1)
                print("Game over.")
                break
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand what you mean.")


def main():
    intro()
    game()


if __name__ == "__main__":
    main()
