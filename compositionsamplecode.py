class Room:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} removed.")


class House:
    def __init__(self):
        self.rooms = [Room("Living Room"), Room("Kitchen")]

    def show_rooms(self):
        for room in self.rooms:
            print(room.name)

    def __del__(self):
        del self.rooms
        print("House demolished with its rooms.")


house = House()
house.show_rooms()

del house