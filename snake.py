from tkinter import * #gui lib
import random #to place food

#constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "green"

#classes
class Snake:
  def __init__(self):
    #initial position
    self.body_size = BODY_PARTS
    self.coordinates = []
    self.squares = []

    #add body parts
    for i in range(0, BODY_PARTS):
      self.coordinates.append([0, 0])
    
    #add squares for each body part
    for x, y in self.coordinates:
      square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag="snake")
      self.squares.append(square)


class Food:
  def __init__(self):
    while (True):
      #random position for food
      x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
      y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE

      #check if food is not on snake
      if (x, y) not in snake.coordinates:
        break

    self.coordinates = [x, y]

    #draw food
    canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

#functions
def next_turn(snake, food):
  global direction, pending_direction

  #update direction
  direction = pending_direction
  x, y = snake.coordinates[0]

  #move snake
  if direction == "up":
    y -= SPACE_SIZE
  elif direction == "down":
    y += SPACE_SIZE
  elif direction == "left":
    x -= SPACE_SIZE
  elif direction == "right":
    x += SPACE_SIZE

  #update snake coordinates
  snake.coordinates.insert(0, (x, y))

  square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
  snake.squares.insert(0, square)

  #check if snake eats food
  if x == food.coordinates[0] and y == food.coordinates[1]:
    global score
    score += 1
    label.config(text = "Score:{}".format(score))

    canvas.delete("food")
    food = Food()
  #if snake does not eat food, remove last body part
  else: 
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

  #check if snake collides with itself or wall
  if check_collisions(snake):
    game_over()
  #if not, continue game
  else:
    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
  global direction, pending_direction

  #check if new direction is valid
  if new_direction == "left" and direction != "right":
      pending_direction = new_direction
  elif new_direction == "right" and direction != "left":
      pending_direction = new_direction
  elif new_direction == "up" and direction != "down":
      pending_direction = new_direction
  elif new_direction == "down" and direction != "up":
      pending_direction = new_direction

def check_collisions(snake):
  x, y = snake.coordinates[0]

  #check if snake collides with the wall
  if x < 0 or x >= GAME_WIDTH:
    print("Game Over")
    return True
  elif y < 0 or y >= GAME_HEIGHT:
    print("Game Over")
    return True
  
  #check if snake collides with itself
  for body_part in snake.coordinates[1:]:
    if x == body_part[0] and y == body_part[1]:
      print("Game Over")
      return True
    
  return False

def game_over():
  global restart_button

  #game over text
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font = ("Arial", 40), text = "Game Over", fill = "red", tag = "game_over")

  #restart button
  restart_button = Button(window, text = "Restart", command = restart_game, font = ("Arial", 20)) 
  restart_button.place(x = GAME_WIDTH / 2, y = GAME_HEIGHT / 2, anchor = "center" )


def restart_game():
  global snake, food, score, direction, pending_direction, restart_button

  if restart_button:
    restart_button.destroy()

  #restart game
  canvas.delete(ALL)
  snake = Snake()
  food = Food()
  score = 0
  direction = "right"
  pending_direction = direction
  label.config(text = "Score:{}".format(score))
  next_turn(snake, food)

#main
#initialize window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

#initialize variables
restart_button = None
score = 0
direction = "right"
pending_direction = "right"

#initialize score label
label = Label(window, text = "Score:{}".format(score), font = ("Arial", 40))
label.pack()

#initialize canvas
canvas = Canvas(window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()

#center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction("left"))
window.bind('<Right>', lambda event: change_direction("right"))
window.bind('<Up>', lambda event: change_direction("up"))
window.bind('<Down>', lambda event: change_direction("down"))

#initialize snake and food
snake = Snake()
food = Food()

#start game
next_turn(snake, food)

window.mainloop()