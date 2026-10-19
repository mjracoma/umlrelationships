class Part:
    def __init__(self, name):
        self.name = name


class Engine:
    def __init__(self):
        # The Engine creates and owns these Part objects directly
        self.parts = [
            Part("Piston"),
            Part("Crankshaft"),
        ]

    def list_parts(self):
        for part in self.parts:
            print(part.name)


engine = Engine()
engine.list_parts()

