from tkinter import * #gui lib
import random #to place food

#constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

#classes
class Snake:
  pass

class Food:
  pass

#functions
def next_turn():
  pass

def change_direction(new_direction):
  pass

def check_collisions():
  pass

def game_over():
  pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "right"

label = Label(window, text = "Score:{}".format(score), font = ("Arial", 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.mainloop()