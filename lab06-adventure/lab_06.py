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
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():
    room_list = []
    room = Room()
    room.description = "You're in the 2º bedroom. It is contiguous to the 1º bedroom at the north and the south hall at the east"
    room.north = 3
    room.south = None
    room.east = 1
    room.west = None
    room_list.append(room)
    room = Room()
    room.description = "You're in the south hall. It is contiguous to 2º bedroom at the west, the north hall at the north and dining room at the east"
    room.north = 4
    room.south = None
    room.east = 2
    room.west =0
    room_list.append(room)
    room = Room()
    room.description = "You're in the dining room. It is contiguous to the south hall at the west and the kitchen at the north"
    room.north = 5
    room.south = None
    room.east = None
    room.west = 1
    room_list.append(room)
    room = Room()
    room.description = "You're in the 1º bedroom. It is contiguous to the 2º bedroom at the south and the north hall at the east"
    room.north = None
    room.south = 0
    room.east = 4
    room.west = None
    room_list.append(room)
    room = Room()
    room.description = "You're in the north hall. It is contiguous to the 1º bedroom at the west, the south hall at the south, the kitchen at the east and the balcony at the north"
    room.north = 6
    room.south = 1
    room.east = 5
    room.west = 3
    room_list.append(room)
    room = Room()
    room.description = "You're in the kitchen. It is contiguous to the south hall at the west and the dining Room at the south"
    room.north = None
    room.south = 2
    room.east = None
    room.west = 4
    room_list.append(room)
    room = Room()
    room.description = "You're in the balcony. It is contiguous to the north hall at the south"
    room.north = None
    room.south = 4
    room.east = None
    room.west = None
    room_list.append(room)

    current_room=0

    done=False

    while not done:
        print()
        print (room_list[current_room].description)

        if current_room==0:
            while current_room==0:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_a(c,room_list,current_room)

        elif current_room == 1:
            while current_room==1:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_b(c,room_list,current_room)

        elif current_room == 2:
            while current_room==2:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_c(c,room_list,current_room)
        elif current_room == 3:
            while current_room==3:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_d(c,room_list,current_room)

        elif current_room == 4:
            while current_room==4:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_e(c,room_list,current_room)
        elif current_room == 5:
            while current_room==5:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_f(c,room_list,current_room)
        elif current_room == 6:
            while current_room==6:

                c=input("Now choose a direction to go in (for example, n/north).--> ")
                current_room=room_g(c,room_list,current_room)


        print()
        s=input("Do you want to exit the dungeon? (y/n)--> ")
        if s.lower()=="y":
            print("I'll be waiting your return")
            done=True

        else:
            done=False


def room_a(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_b(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_c(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_d(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_e(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_f(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

def room_g(c:str, room_list:list, current_room:int):
    """Function for the room 0"""
    if c.lower() == "n" or c.lower() == "north":
        next_room = room_list[current_room].north
        if next_room is None:
            print("There is a wall there. You can't continue")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "s" or c.lower() == "south":
        next_room = room_list[current_room].south
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "e" or c.lower() == "east":
        next_room = room_list[current_room].east
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    elif c.lower() == "w" or c.lower() == "west":
        next_room = room_list[current_room].west
        if next_room is None:
            print("There is a wall there")
        else:
            print("Great. You advance to the next room")
            current_room = next_room

    else:
        print()
        print("Sorry, I didn't understand what you typed.")

    return current_room

main()