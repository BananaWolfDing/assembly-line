class Machine:
    def __init__(self, loc):
        self.pos = 3
        self.left_time = 0  # remaining seconds to reach next position
        self.grab = None
        self.loc = loc

    def move(self, target):
        self.pos = target
        self.left_time = abs(target - self.pos) * 3

    def pick(self, car):
        if self.grab:
            raise IndexError("Push machine in use")
        else:
            car.loc = [self.loc]
            self.grab = car

    def drop(self):
        if self.grab is None:
            raise IndexError("Push machine not in use")
        else:
            car = self.grab
            self.grab = None
            return car

    def free(self):
        return self.grab is None and self.left_time == 0 and self.pos == 3

    def tic(self):
        if self.left_time >= 1:
            self.left_time -= 1
