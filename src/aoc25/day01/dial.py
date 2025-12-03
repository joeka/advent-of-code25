class Dial:
    def __init__(self):
        self.reset()

    def reset(self):
        self.position = 50
        self.hit_zero = 0
        self.passed_zero = 0

    def turn(self, instruction: str):
        direction = instruction[0]
        multiplier = 1 if direction == 'R' else -1
        amount = int(instruction[1:])

        for _ in range(amount):
            self.position += multiplier
            if self.position > 99:
                self.position = 0
                self.passed_zero += 1
            elif self.position < 0:
                self.position = 99
            elif self.position == 0:
                self.passed_zero += 1

        if self.position == 0:
            self.hit_zero += 1
