# inventory management game
import time
import sys
from requests import delete

# list that holds my items
inventory = []

def show_inventory():
    if not inventory:
        type_text("Your backpack is empty.")
    else:
        type_text("You are carrying:")
        for item in inventory:
            type_text(f" - {item['name']} ({item['type']})")

# defining basic actions
def help_action():
    type_text("You requested help. What do you want to do?")
    time.sleep(1)
    type_text("     1) Quit the game")
    time.sleep(1)
    type_text("     2) Restart the game")
    time.sleep(1)
    type_text("     3) See your current inventory")
    help_request = input("Please enter '1', '2' or '3': ")

    if help_request == '1':
        type_text("Goodbye!")
        exit()
    elif help_request == '2':
        type_text("Restarting the game...")
        introduction()
        scene_change()
        prequel()
        scene_change()
        preparation()
        scene_change()
        room1()
        scene_change()
        room2()
        scene_change()
        room3()
        scene_change()
        outro()
    elif help_request == '3':
        show_inventory()
    else:
        type_text("Invalid choice. Returning to the game.")

def pick_up(item_name, room_items):
    if item_name not in room_items:
        type_text("The item you want to pick up is not in the room.")
    elif item_name in inventory:
        type_text("This item is already in your backpack.")
    elif len(inventory) >= 5:
        type_text("Your backpack is full. You need to drop something first.")
    else:
        inventory.append(item_name)
        room_items.remove(item_name)
        type_text("You picked up the " + item_name + ".")

def drop(item_name):
    if item_name in inventory:
        inventory.remove(item_name)
        type_text("You dropped the" + item_name + ".")
    else:
        type_text("You don't have that in your backpack.")

# all used items
items_general = [
    {"name": "headlamp", "type": "gear", "uses": 1},
    {"name": "walkie-talkie", "type": "gear", "uses": 1},
    {"name": "superior food", "type": "food", "uses": 1},
    {"name": "rope", "type": "gear", "uses": 1},
    {"name": "first aid", "type": "emergency", "uses": 1},
    {"name": "magic key", "type": "magic", "uses": 1},
    {"name": "", "type": "", "uses": 1},
    {"name": "", "type": "", "uses": 1},
]

# items room 2
spaceship_items = [{"name": "flashlight", "type": "tool", "uses": 1},
                   {"name": "piece of metal", "type": "tool", "uses": 1},
                   {"name": "ancient Earth map", "type": "gear", "uses": 1},
                   {"name": "journal", "type": "tool", "uses": 1},
]




# crewmate trust score
trust_score = 5

def check_trust(trust_score):
    if trust_score < 2:
        type_text("Your crewmates don't trust you anymore.")
        time.sleep(1)
        type_text("They decide to leave you behind and continue the mission without you.")
        time.sleep(1)
        type_text("GAME OVER")
        exit()


# actual game
def type_text(text, speed=0):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Introduction
def introduction():
    type_text('Welcome to this escape game.')
    time.sleep(1)
    type_text('You will go through different rooms and solve riddles.')
    time.sleep(1)
    type_text('Your mission will be to survive and finish the escape route to save yourself.')
    time.sleep(1)
    type_text('But before we start, we need to create your character.')
    type_text('What name do you want to give your player? ')
    player_name = input('> ')
    time.sleep(1)
    type_text('Okay, ' + player_name + ', your mission starts now.')

# Scene changes
def scene_change():
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(" *** ")
    time.sleep(1)
    print(" ")

# Prequel
def prequel():
    type_text("It's the year 2134 AD and you and your crew are on a critical mission: to revive planet Earth. ")
    time.sleep(1)
    type_text("Since the nuclear catastrophe in 2099, no one has set foot on the planet.")
    time.sleep(1)
    type_text("Your ancestors were the lucky ones, who were able to safe themselves into space.")
    time.sleep(1)
    type_text("But now, your spaceship's resources are running dangerously low and you need to see, whether live on earth is possible again.")
    time.sleep(1)

# Preparation
def preparation():
    type_text("Your mission starts tomorrow and you need to decide what to pack.")
    time.sleep(1)
    type_text("You don't know what will expect you when you land on earth.")
    time.sleep(1)
    type_text("So you have to calculate every possible risk.")
    time.sleep(1)
    type_text("As the team captain, your crew members put their trust in you.")
    time.sleep(1)
    type_text("You already packed a headlamp, a walkie-talkie and superior food.")
    inventory.extend(["headlamp", "walkie-talkie", "superior food"])
    time.sleep(1)
    type_text("Your backpack is almost full and only two more things fit in it.")
    time.sleep(1)
    type_text("You need to decide...")
    time.sleep(1)
    type_text("On the table before you, are three things left.")
    time.sleep(1)
    type_text("A rope, a first aid kit and a magic key.")
    time.sleep(1)
    type_text("Which one will you NOT take with you?")
    time.sleep(1)

    while True:
        type_text("Please type 'rope', 'first aid' or 'magic key': ")
        leave_behind = input("> ")

        if leave_behind == "rope":
            inventory.extend(["first aid", "magic key"])
            break
        elif leave_behind == "first aid":
            inventory.extend(["rope", "magic key"])
            break
        elif leave_behind == "magic key":
            inventory.extend(["rope", "first aid"])
            break
        elif leave_behind == "help":
            help_action()
            break
        else:
            type_text("This is not a valid option. Please type 'rope', 'first aid' or 'magic key': ")

    type_text("Tough decicion, I know...")
    time.sleep(1)
    type_text("Lets hope you made the right choice...")

# Room1
def room1():
    type_text("The next morning you and your crew start your mission: Back to Earth")
    time.sleep(1)
    type_text("You left early, in a little space ship, that will send you and four other brave members down to Earth.")
    time.sleep(1)
    type_text("Your backpack is packed and your are excited to see what will happen within the next few hours.")
    time.sleep(1)
    type_text("Your flight is nearly over as something weird happens...")
    time.sleep(1)
    type_text("One crewmate, 'Laila', fainted.")
    time.sleep(1)
    type_text("You need to act fast in order to help them.")
    time.sleep(1)
    type_text("What do you do to help?")
    time.sleep(1)
    type_text("You...:")
    time.sleep(1)
    type_text("     1) use your first-aid-kit")
    time.sleep(1)
    type_text("     2) do a mouth-to-mouth resuscitation")
    time.sleep(1)
    type_text("     3) ask another crewmate to help")
    time.sleep(1)

    trust_score = 5

    while True:
        type_text("Please enter either '1', '2' or '3':")
        fainted_help = input("> " )
        time.sleep(1)

        if fainted_help == "1":
            if "first aid" in inventory:
                trust_score += 1
                inventory.remove("first aid")
                type_text("You use the first aid kit and your crewmate recovers. Good job!")
                type_text("Your crewmates gain trust in you. This is the current trust level: " + str(trust_score))
                break
            else:
                type_text("You did not take the first aid kit with you, try something else.")
        elif fainted_help == "2":
            type_text("You start a mouth-to-mouth resuscitation and your crewmate starts breathing again. \n")
            break
        elif fainted_help == "3":
            trust_score -= 1
            type_text("You call for help, and another crewmate helps you stabilize Laila.")
            time.sleep(1)
            type_text("However your crew thinks of you as unresponsible for not being able to help on your own...")
            time.sleep(1)
            type_text("This is the current level of trust your crew has in you: " + str(trust_score) + "/10")
            check_trust(trust_score)
            break
        elif fainted_help == "help":
            help_action()
            break
        else:
            type_text("This is not a valid option. Please enter '1' or '2' or '3': ")

# Room2
def room2():
    type_text("You finally land on Earth and the moment of truth has come.")
    time.sleep(1)
    type_text("Your space ship has no windows, so you don't know what to expect on the other side of the door.")
    time.sleep(1)
    type_text("Before you open the door, you take a look around inside the spaceship.")
    time.sleep(1)
    type_text("'Some of these things inside could also be from help on the mission...', you think.")
    time.sleep(1)
    type_text("Do you want to take something with you from the spaceship?")
    time.sleep(1)
    type_text("'yes' or 'no'")
    take_something = input("> ").lower().strip()

    while True:
        if take_something == "yes":
            spaceship_items = ["flashlight", "piece of metal", "ancient Earth map", "journal" ]

            while True:
                type_text("These are the things, lying around in the spaceship: ")
                time.sleep(1)
                type_text(", " .join(spaceship_items))
                time.sleep(1)
                type_text("This is your inventory at the moment: ")
                time.sleep(1)
                type_text(", " .join(inventory))
                time.sleep(1)

                type_text("Please enter 'drop [item]' if you want to drop any item from your backpack.")
                time.sleep(1)
                type_text("Enter 'pickup [item]' if you want to pick up an item from the spaceship.")
                time.sleep(1)
                type_text("Enter 'done', when you do not want to drop or pick up an item.")
                time.sleep(1)
                action = input("> ").strip()

                if action.startswith("drop "):
                    item_to_drop = action[5:].strip()  # Remove the "drop " part
                    drop(item_to_drop)

                elif action.startswith("pickup "):
                    item_to_pickup = action[7:].strip()
                    pick_up(item_to_pickup, spaceship_items)

                elif action == "help":
                    help_action()
                    break

                elif action == "done":
                    break

                else:
                    type_text("That wasn't a valid command. Try 'drop [item]', 'pickup [item]', or 'done'.")

            break

        elif take_something == "no":
            type_text("You decide not to take something from the spaceship.")
            break

        elif take_something == "help":
            help_action()
            break

        else:
            type_text("This is not a valid opition. Please type 'yes' or 'no'.")
            take_something = input("> ")
        break

# Room3
def room3():
    global trust_score
    global inventory

    type_text("With your filled backpack you leave the spaceship.")
    time.sleep(1)
    type_text("The first step on earth feels weird, but soon you start to enjoy the feeling of grass underneath your feet.")
    time.sleep(1)
    type_text("You walk through a forest, trees standing close to each other and sometimes it is hard to pass through.")
    time.sleep(1)
    type_text("Your crew follows you closely as you hear a scream from far away.")
    time.sleep(1)
    type_text("You pause and look at your crewmates.")
    time.sleep(1)

    if trust_score >= 5:
        type_text("They look scared, but trust you and your decisions.")
    else:
        type_text("They look scared, and you know that they don't trust you.")

    while True:
        time.sleep(1)
        type_text("Do you follow the scream?")
        time.sleep(1)
        type_text("'yes' or 'no'")
        follow_scream = input("> ").lower().strip()

        if follow_scream == "yes":
            type_text("You decide to follow the scream.")
            time.sleep(1)
            type_text("The path you're choosing is overgrown and sometimes you can't even see your own feet.")
            time.sleep(1)
            type_text("You hear the scream again.")
            time.sleep(1)
            type_text("This time it is closer and you know that you are on the right track.")
            time.sleep(1)
            type_text("After a few more minutes of walking you get to a river.")
            time.sleep(1)

            while True:
                type_text("There is no bridge in sight, so you need to decide... walk left or right?")
                time.sleep(1)
                type_text("Please enter 'left' or 'right'.")
                river_decision = input("> ").lower().strip()

                if river_decision == "left":
                    type_text("You decide to walk left.")
                    time.sleep(1)
                    break
                elif river_decision == "right":
                    type_text("You decide to walk right.")
                    time.sleep(1)
                    break
                elif river_decision == "help":
                    help_action()
                    break
                else:
                    type_text("This is not a valid answer.")
                    time.sleep(1)

            type_text("You walk a few more minutes along the side of the river.")
            time.sleep(1)
            type_text("All of the sudden, a little girl stands on the other shore.")
            time.sleep(1)
            type_text("This confuses you...")
            time.sleep(1)
            type_text("You were told, there was no human life on planet earth.")
            time.sleep(1)
            type_text("The girl is moving her mouth, but you can't understand what she is trying to say.")
            time.sleep(1)
            type_text("Do you want to help her?")
            time.sleep(1)
            type_text("Please enter 'yes' or 'no'")
            help_girl = input("> ").lower().strip()

            if help_girl == "yes":
                trust_score += 1
                type_text("You want to help the girl and your crew thinks of this as the right decision.")
                time.sleep(1)
                type_text("You gain trust. This is your current trust level: " + str(trust_score) + "/10")
                check_trust(trust_score)
                time.sleep(1)
                type_text("You try and help the girl with: ")
                time.sleep(1)
                type_text("     1) the rope, to build a bridge-like-something")
                time.sleep(1)
                type_text("     2) the map, to look for a bridge")
                time.sleep(1)
                type_text("     3) you try to swim to save her")
                time.sleep(1)
                type_text("Please enter '1', '2' or '3':")
                help_how = input("> ").strip()

                if help_how == "1":
                    if "rope" in inventory:
                        trust_score += 1
                        type_text("You decide to use the rope.")
                        time.sleep(1)
                        type_text("Your crew thinks of you as responsible and trusts you more.")
                        time.sleep(1)
                        type_text("This is your current trust level: " + str(trust_score) + "/10")
                        time.sleep(1)
                        type_text("You tie the rope to a tree and throw the other end to the girl.")
                        time.sleep(1)
                        type_text("The other end lands perfectly in front of the feet of the girl.")
                        time.sleep(1)
                        type_text("The girl takes the rope, but does not tie it to a tree on her side of the river.")
                        time.sleep(1)
                        type_text("Instead she snips her fingers, and the rope starts burning.")
                        time.sleep(1)
                        type_text("Then she screams again and runs away into the woods.")
                        time.sleep(1)
                        type_text("'What an odd experinece', you think.")
                        time.sleep(1)
                        type_text("You and your crew start walking again.")
                        check_trust(trust_score)
                    else:
                        type_text("You want to use the rope... but it's not in your backpack!")
                        time.sleep(1)
                        type_text("Your crew seems frustrated by the poor planning.")
                        trust_score -= 1
                        time.sleep(1)
                        type_text("They lose trust. Current trust level: " + str(trust_score) + "/10")
                        check_trust(trust_score)
                        type_text("Try a different option.")
                        continue

                elif help_how == "2":
                    if "map" in inventory:
                        trust_score += 1
                        type_text("You pull out the map and look for a nearby bridge.")
                        time.sleep(1)
                        type_text("Your crew is impressed by your logical thinking.")
                        time.sleep(1)
                        type_text("This is your current trust level: " + str(trust_score) + "/10")
                        check_trust(trust_score)
                        time.sleep(1)
                        type_text("As you take a closer look on the map, you see no bridges marled on it.")
                        time.sleep(1)
                        type_text("Your plan has failed.")
                        time.sleep(1)
                        type_text("As you look up, to communicate with the girl, you see it has disappeared.")
                        time.sleep(1)
                        type_text("You ask your crewmates, if they saw where she went, but they did not pay attention to her.")
                        time.sleep(1)
                        type_text("Your confused, but decide to continue your path along the river.")
                        time.sleep(1)

                    else:
                        type_text("You want to use the map... but it's not in your backpack!")
                        time.sleep(1)
                        type_text("Your crew seems frustrated by the poor planning.")
                        trust_score -= 1
                        time.sleep(1)
                        type_text("They lose trust. Current trust level: " + str(trust_score) + "/10")
                        check_trust(trust_score)
                        type_text("Try a different option.")
                        return

                elif help_how == "3":
                    type_text("You try to swim to save the girl.")
                    time.sleep(1)
                    type_text("However, the stream is too strong...")
                    time.sleep(1)
                    type_text("You were never able to learn how to swim, since you grew up in space.")
                    time.sleep(1)
                    type_text("You give your best, but you feel your muscles weakening.")
                    time.sleep(1)
                    type_text("...")
                    time.sleep(1)
                    type_text("You hear your crewmates screaming...")
                    time.sleep(1)
                    type_text("... but it is too late.")
                    time.sleep(1)
                    type_text("GAME OVER")
                    exit()
                elif help_how == "help":
                    help_action()
                    return
                else:
                    type_text("That’s not a valid option. Please enter '1', '2', or '3'.")

            elif help_girl == "no":
                type_text("You decide not to help the girl.")
                time.sleep(1)
                type_text("Your crew thinks that helping the girl would have been the right decision.")
                time.sleep(1)
                trust_score -= 1
                type_text("They lose trust. Current trust level: " + str(trust_score) + "/10")
                time.sleep(1)
                type_text("You and your crew continue your path along the river.")
                check_trust(trust_score)
                break

        elif follow_scream == "no":
            type_text("You decide not to follow the scream.")
            time.sleep(1)
            type_text("Your crew thinks following the scream would have been the right decision.")
            time.sleep(1)
            trust_score -= 1
            type_text("They lose trust in you. This is your current trust score: " + str(trust_score) + "/10")
            check_trust(trust_score)
            break

        elif follow_scream == "help":
            help_action()

        else:
            type_text("This is not a valid answer. Please enter 'yes' or 'no'.")


def outro():
    type_text("You and your crew decide, that the mission needs to be aborted.")
    time.sleep(1)
    type_text("You're not prepared yet to continue the mission.")
    time.sleep(1)
    type_text("You all go back to the spaceship, that brings your back to your home-spaceship.")
    time.sleep(1)
    type_text("You are disappointed, but see that it would be irresponsible to continue the mission.")
    time.sleep(1)
    type_text("GAME OVER")
    time.sleep(1)


# Game output
introduction()
scene_change()
prequel()
scene_change()
preparation()
scene_change()
room1()
scene_change()
room2()
scene_change()
room3()
scene_change()
outro()
