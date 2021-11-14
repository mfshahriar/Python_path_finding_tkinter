snake_pos = [(160,300),(140,300),(120,300),(100,300),(80,300), (60,300), (40,300)]
headX, headY = snake_pos[0]
print( (headX, headY) in snake_pos[1:] )