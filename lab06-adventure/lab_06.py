import arcade
import math
from arcade import finish_render
from arcade.color import YELLOW


class Room:
    """
    This is a class that represents the player character.
    """

    def __init__(self):
        """This is a method that sets up the variables in the object"""
        self.description = ""
        self.north = ""
        self.south = ""
        self.east = ""
        self.west = ""


def main():
    room_list = []
    room0 = Room()
    room0.description = "You're in the 2º bedroom. It is contiguous to the 1º bedroom at the north and the south hall at the east"
    room0.north = 3
    room0.south = None
    room0.east = 1
    room0.west = None
    room_list.append(room0)
    room1 = Room()
    room1.description = "You're in the south hall. It is contiguous to 2º bedroom at the west, the north hall at the north and dining room at the east"
    room1.north = 4
    room1.south = None
    room1.east = 2
    room1.west =0
    room_list.append(room1)
    room2 = Room()
    room2.description = "You're in the dining room. It is contiguous to the south hall at the west and the kitchen at the north"
    room2.north = 5
    room2.south = None
    room2.east = None
    room2.west = 1
    room_list.append(room2)
    room3 = Room()
    room3.description = "You're in the 1º bedroom. It is contiguous to the 2º bedroom at the south and the north hall at the east"
    room3.north = None
    room3.south = 0
    room3.east = 4
    room3.west = None
    room_list.append(room3)
    room4 = Room()
    room4.description = "You're in the north hall. It is contiguous to the 1º bedroom at the west, the south hall at the south, the kitchen at the east and the balcony at the north"
    room4.north = 6
    room4.south = 1
    room4.east = 5
    room4.west = 3
    room_list.append(room4)
    room5 = Room()
    room5.description = "You're in the kitchen. It is contiguous to the south hall at the west and the dining Room at the south"
    room5.north = None
    room5.south = 2
    room5.east = None
    room5.west = 4
    room_list.append(room5)
    room6 = Room()
    room6.description = "You're in the balcony. It is contiguous to the north hall at the south"
    room6.north = None
    room6.south = 4
    room6.east = None
    room6.west = None
    room_list.append(room6)

    current_room=0

    done=False

    while not done:
        print()
        print (room_list[current_room].description)
        c=input("Now choose a direction to go in (for example, n/north).--> ")

        if c.lower()=="n" or c.lower()=="north":
            next_room=room_list[current_room].north
            if next_room is None:
                print("There is a wall there...")
            else:
                print("Great. You advance to the next room")
                current_room=next_room

        elif c.lower()=="s" or c.lower()=="south":
            next_room=room_list[current_room].south
            if next_room is None:
                print("There is a wall there...")
            else:
                print("Great. You advance to the next room")
                current_room=next_room

        elif c.lower()=="e" or c.lower()=="east":
            next_room=room_list[current_room].east
            if next_room is None:
                print("There is a wall there...")
            else:
                print("Great. You advance to the next room")
                current_room=next_room

        elif c.lower()=="w" or c.lower()=="west":
            next_room=room_list[current_room].west
            if next_room is None:
                print("There is a wall there...")
            else:
                print("Great. You advance to the next room")
                current_room=next_room

        else:
            print()
            print ("Sorry, I didn't understand what you typed.")

        print()
        s=input("Do you want to exit the dungeon? (y/n)--> ")
        if s.lower()=="y":
            print("I'll be waiting your return")
            done=True

        else:
            done=False



main()