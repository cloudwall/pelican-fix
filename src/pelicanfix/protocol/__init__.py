class FIXField:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
