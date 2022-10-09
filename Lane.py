class Lane:
    def __init__(self, lane_id):
        self.id = lane_id
        self.lane = []  # cars in lane

    def print_lane(self, newline=True):
        l = ['-'] * 10
        for car in self.lane:
            for idx in car.loc:
                l[idx - 1] = car.id

        for p in reversed(l):
            print(f'{p:<5}', end='')

        if newline:
            print()


class ForwardLane(Lane):
    def drop_car(self, car):
        car.drop(self.id, 10)
        self.lane.append(car)

    def pick_car(self):
        car = self.lane.pop(0)
        return car

    def pickable(self):
        return len(self.lane) > 0 and self.lane[0].left_move == 0 and self.lane[0].loc == [1]

    def dropable(self):
        return len(self.lane) == 0 or 10 not in self.lane[-1].loc

    def tic(self):
        prev_loc = [0]
        for car in self.lane:
            if car.left_move == 0 and (car.loc[0] - 1) not in prev_loc:
                car.move_in_lane(car.loc[0] - 1, 9)
            prev_loc = car.loc

        for car in self.lane:
            car.tic()

    def notify(self):
        return len(self.lane) > 0 and self.lane[0].left_move == 0 and self.lane[0].loc == [1]


class BackwardLane(Lane):
    def drop_car(self, car):
        car.drop(self.id, 1)
        self.lane.append(car)

    def pick_car(self):
        car = self.lane.pop(0)
        return car

    def pickable(self):
        return len(self.lane) > 0 and self.lane[0].left_move == 0 and self.lane[0].loc == [10]

    def dropable(self):
        return len(self.lane) == 0 or 1 not in self.lane[-1].loc

    def tic(self):
        prev_loc = [11]
        for car in self.lane:
            if car.left_move == 0 and (car.loc[0] + 1) not in prev_loc:
                car.move_in_lane(car.loc[0] + 1, 9)
            prev_loc = car.loc

        for car in self.lane:
            car.tic()

    def notify(self):
        return len(self.lane) > 0 and self.lane[0].left_move == 0 and self.lane[0].loc == [10]
