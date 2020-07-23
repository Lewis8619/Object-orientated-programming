
from room import Room
from character import Enemy, Friend
from rpginfo import RPGInfo
from item import Item

derelict_den = RPGInfo("The Derelict Den")
derelict_den.welcome()
RPGInfo.info()
RPGInfo.author = "Lewis Eaton-Weekes"

kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

derek = Enemy("Derek", "A smelly zombie")
derek.set_conversation("Brrlgrh... rgrhl... brains...")
derek.set_weakness("penicilin")
dining_hall.set_character(derek)

catherine = Friend("Catherine", "A friendly skeleton")
catherine.set_conversation("Why hello there.")
ballroom.set_character(catherine)

penicilin = Iten("penicilin")
penicilin.set_description("A medical substance, known to cause allergic reactions in some people")
ballroom.set_item(penicilin)

book = Item("book")
book.set_description("A large, thick book entwined with spider webs")

current_room = kitchen
backpack = []

dead = False
while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if weapon in backpack:
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                weapon = input()
                if inhabitant.fight(weapon) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("There is no one here to fight with")
        else:
            print("You don't have a " + weapon)

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == "take":
        if item is not None:
          print("You put the " + item.get_name() + " in your backpack")
          backpack.append(item.get_name())
          current_room.set_item(None)

RPGInfo.credits()