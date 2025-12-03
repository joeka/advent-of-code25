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

        value = self.position + multiplier * amount

        old_position = self.position
        self.position = value % 100
        if self.position == 0:
            self.hit_zero += 1
            if direction == 'L':
                self.passed_zero += 1
        self.passed_zero += abs(value // 100)
        if old_position == 0 and direction == 'L':
            self.passed_zero -= 1
