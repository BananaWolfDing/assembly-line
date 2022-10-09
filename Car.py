class Car:
    def __init__(self, car_id, car_type, wd, lanes):
        self.id = car_id
        self.type = car_type  # 0 for hybrid and 1 for fuel
        self.wd = wd  # 1 for 2WD and -1 for 4WD
        self.loc = [-1]  # -1 for N/A
        self.left_move = 0  # remaining seconds to reach next position
        self.lane = 0  # 0 for not in any lane
        self.aims = lanes  # The target lanes to drop after sending back in order

    def enter_cache(self):
        self.loc = [0]

    def exit_cache(self):
        self.loc = [3]

    def pick(self, machine):
        self.lane = 0
        self.loc = [machine]

    def drop(self, lane, area):
        self.loc = [area]
        self.lane = lane

    def tic(self):
        if self.left_move > 1:
            self.left_move -= 1
        elif self.left_move == 1:
            self.left_move = 0
            self.loc.pop(0)

    def move_in_lane(self, target, time):
        self.left_move = time
        self.loc.append(target)

    def target_lane(self):
        return self.aims.pop(0)
