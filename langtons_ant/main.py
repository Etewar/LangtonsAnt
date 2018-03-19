import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Langton's Ant")

screen = pygame.display.set_mode((800, 800))

W = (255, 255, 255)
B = (0, 0, 0)
R = (154, 38, 23)
G = (33, 33, 33)
screen.fill(G)

def clear_console():
    print("\033[H\033[J")

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            clear_console()
            print(event)

class App:

    position = [400, 400]
    direction = 0
    OFF = G
    ON = R

    def move():
        if App.direction == 0:
            App.position[1] = (App.position[1] - 1) % 800
        elif App.direction == 1:
            App.position[0] = (App.position[0] + 1) % 800
        elif App.direction == 2:
            App.position[1] = (App.position[1] + 1) % 800
        elif App.direction == 3:
            App.position[0] = (App.position[0] - 1) % 800

    def do_action():
        if screen.get_at(App.position) == App.ON:
            App.direction = (App.direction + 1) % 4
            screen.set_at(App.position, App.OFF)
        else:
            App.direction = (App.direction - 1) % 4
            screen.set_at(App.position, App.ON)
        App.move()

    def run():
        while True:
            input(pygame.event.get())
            pygame.time.delay(1)
            App.do_action()
            pygame.display.update()


if __name__ == "__main__":
    App.run()
