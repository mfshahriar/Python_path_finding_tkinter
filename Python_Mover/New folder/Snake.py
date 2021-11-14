import tkinter
import math
import random
from PIL import Image, ImageTk  # conda install pillow


class Snake(tkinter.Canvas):
    def __init__(self):
        super().__init__(height=650, width=650, background='black')
        self.snake_pos = [(160,300),(140,300),(120,300),(100,300),(80,300), (60,300), (40,300)]
        self.food_pos = (500, 100)
        self.direction = 'Right'
        self.score = 0
        
        self.bind_all("<Key>", self.on_key_press)
        
        try:
            self.snake_img = Image.open('./images/snake.png')
            self.snake_body = ImageTk.PhotoImage(self.snake_img)
            self.food_img = Image.open('./images/food.png')
            self.food = ImageTk.PhotoImage(self.food_img)
        except  IOError as err:
            print(err)
            
        self.create_text(100, 20, text=f"Score: {self.score}", fill='#FFF', font=('Arial', 24))
        for x,y in self.snake_pos:
            #print(x,y)
            self.create_image(x,y, image=self.snake_body, tag='sanke')
        
        self.create_image(*self.food_pos, image=self.food, tag='food')
        self.after(200, self.actions)
        
    def move(self):
        
        headX, headY = self.snake_pos[0]
        #print(headX, headY)
        if self.direction == 'Left':
            new_head_pos = (headX - 20, headY)
        elif self.direction == 'Right':
            new_head_pos = (headX + 20, headY)
        elif self.direction == 'Up':
            new_head_pos = (headX, headY - 20)
        elif self.direction == 'Down':
            new_head_pos = (headX, headY + 20)
        
        self.snake_pos = [new_head_pos] + self.snake_pos[:-1]
        
        for s,p in zip(self.find_withtag('sanke'), self.snake_pos):
            print(s)
            self.coords(s,p)
              
        
    def actions(self):
        if self.check_collision():
            print('Game Over')
            return
        if self.check_food():
            self.score = self.score + 1
            print('yes', self.score)
            
        self.move()
        self.after(200, self.actions)
        
    def check_collision(self):
        headX, headY = self.snake_pos[0]
        return (headX, headY) in self.snake_pos[1:]
    def check_food(self):
        headX, headY = self.snake_pos[0]
        return (headX, headY) == self.food_pos
    
    def on_key_press(self, e):
        new_direction = e.keysym
        self.direction = new_direction
        #print(self.direction)