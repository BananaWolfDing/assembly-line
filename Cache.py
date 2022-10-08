from Lane import ForwardLane, BackwardLane
from Car import Car
from Machine import Machine


class Cache:
    def __init__(self, car_list, target_lane):
        self.cars = car_list
        self.back_notify = False  # No car in backward lane
        self.forw_notify = []
        self.arrive = car_list[0] if len(car_list) > 0 else None
        self.end = None
        self.push_machine = Machine(1)
        self.pop_machine = Machine(2)
        self.lanes = [
            ForwardLane(1), ForwardLane(2), ForwardLane(3), ForwardLane(4), BackwardLane(1), ForwardLane(5), ForwardLane(6)
        ]

    def tic(self):
        self.end = None
        self.arrive = self.cars[0] if len(self.cars) > 0 else None
        self.push_machine.tic()
        if self.push_machine.left_time == 0:
            if self.push_machine.grab is not None:
                if self.lanes[self.push_machine.pos].dropable():
                    car = self.push_machine.drop()
                    self.lanes[self.push_machine.pos].drop_car(car)
                    self.push_machine.move(3)
            elif self.back_notify:
                self.back_notify = False
                self.push_machine.move(4)
            else:
                if self.push_machine.pos == 3:
                    if len(self.cars) > 0:
                        car = self.cars.pop(0)
                        self.push_machine.pick(car)
                        self.push_machine.move(car.target_lane())
                else:
                    if self.lanes[4].pickable():
                        car = self.lanes[4].pick_car()
                        self.push_machine.pick(car)
                        self.push_machine.move(car.target_lane())

        for lane in self.lanes:
            lane.tic()

        for idx in [0, 1, 2, 3, 5, 6]:
            if self.lanes[idx].notify():
                self.forw_notify.append(idx)
        if self.lanes[4].notify():
            self.back_notify = True

        self.pop_machine.tic()
        if self.pop_machine.left_time == 0:
            if self.pop_machine.grab is not None:
                if self.pop_machine.pos == 3:
                    car = self.pop_machine.drop()
                    self.end = car
                    if len(self.forw_notify) > 0:
                        self.pop_machine.move(self.forw_notify[0])
                else:
                    car = self.pop_machine.drop()
                    if self.lanes[4].dropable():
                        self.lanes[4].drop_car(car)
                        self.pop_machine.move(3)
            else:
                if self.lanes[self.pop_machine.pos].pickable():
                    car = self.lanes[self.pop_machine.pos].pick_car()
                    self.pop_machine.pick(car)
                    self.pop_machine.move(3 if len(car.aims) == 0 else car.target_lane())

    def print_cache(self):
        assemble = "  -  " if self.end else f'{self.end.id:<5}'
        paint = "  -  " if len(self.cars) == 0 else f'{self.cars[0].id:<5}'
        push_car = "  -  " if self.push_machine.grab is None else f'{self.push_machine.grab.id:<5}'
        pop_car = "  -  " if self.pop_machine.grab is None else f'{self.pop_machine.grab.id:<5}'

        self.lanes[6].print_lane()
        self.lanes[5].print_lane()
        self.lanes[4].print_lane()
        print(paint, push_car, end='')
        self.lanes[3].print_lane(newline=False)
        print(pop_car, assemble)
        self.lanes[2].print_lane()
        self.lanes[1].print_lane()
        self.lanes[0].print_lane()
