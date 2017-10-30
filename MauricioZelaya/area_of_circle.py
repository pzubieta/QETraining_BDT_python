import math


def area_of_circle(radio):
    return math.pi*radio*radio

radios = [1, 5, 10, 15, 12, 11, 10.1]
for radio in radios:
    if radio <= 10:
        continue
    area = area_of_circle(radio)
    print("area of the circle with radio = %s is: %s" % (radio, area))

