from random import gauss
from time import sleep


STD_DEVIATION = 0.5


def random_time(mean):
    time = gauss(mean, STD_DEVIATION)
    return time


def random_sleep(time):
    sleep(random_time(time))
