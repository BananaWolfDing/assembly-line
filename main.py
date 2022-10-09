from Cache import Cache
from Car import Car

cars = [
    Car(1, 0, 1, [3]),
    Car(2, 1, -1, [2]),
    Car(3, 1, 1, [3]),
    Car(4, 0, 1, [2, 5]),
    Car(5, 0, -1, [2]),
]

cache = Cache(cars)

for _ in range(272):
    cache.tic()
    cache.print_cache()
    print('*' * 80)