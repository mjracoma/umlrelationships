class Player:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Player {self.name} has left the game.")


class Team:
    def __init__(self, players=None):
        self.players = players if players is not None else []

    def __del__(self):
        print("The team has been disbanded.")

