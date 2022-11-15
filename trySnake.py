import pygame, sys, random
from pygame.math import Vector2
from button import Button
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch = pygame.mixer.Sound('Sound/eat-sounds.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            #1. We still need a rect for the positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #2. Create head direction
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index -1] -block
                if previous_block.x == next_block.x: # create body of snake when the snake moving along
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:# create body of snake when the snake moving sideway
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==1:
                        screen.blit(self.body_br,block_rect)
                    elif previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==-1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==-1:
                        screen.blit(self.body_bl,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0) : self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, -1): self.head = self.head_down
        elif head_relation == Vector2(0, 1): self.head = self.head_up

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):self.tail = self.tail_down

    def move_snake(self):
        if self.new_block== True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)  # insert to end of snake
            self.body = body_copy[:]  # Update new body for snake
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)# insert to end of snake
            self.body = body_copy[:] # Update new body for snake

    def add_block(self):
        self.new_block = True

    def play_sound(self):
        self.crunch.play()

    def reset(self):
        self.body = [Vector2(5, 9), Vector2(4, 9), Vector2(3, 9)]
        self.direction = Vector2(0, 0)


class FRUIT:

    def __init__(self):
        self.randomize()
        self.black_apple = pygame.image.load('Graphics/black_apple.png').convert_alpha()
    def randomize(self):
        # create an X and Y position
        # draw a square
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def draw_fruit(self):
        #create rectangle
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int( self.pos.y*cell_size),cell_size,cell_size)
        # demo fruit by draw rectangle
        # pygame.draw.rect(screen,(191,115,114),fruit_rect)
        # create graphics for fruit

        screen.blit(self.black_apple,fruit_rect)
class ITEMS:
    def __init__(self):
        self.randomize_item()
        self.blueberry = pygame.image.load('Graphics/blueberry.png').convert_alpha()
    def randomize_item(self):
        # create an X and Y position
        # draw a square
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int( self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(self.blueberry,fruit_rect)
class MAIN_game1:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.items = ITEMS()
        self.blocks = [[Vector2(0,0), Vector2(0, 1), Vector2(0, 2),Vector2(0,3),Vector2(0,4),Vector2(0,5),Vector2(0,6)],
                       [Vector2(0, 13), Vector2(0, 14),Vector2(0,15),Vector2(0,16),Vector2(0,17),Vector2(0,18),Vector2(0,19)],
                       [Vector2(19, 0), Vector2(19, 1), Vector2(19, 2), Vector2(19, 3), Vector2(19, 4), Vector2(19, 5),Vector2(19, 6)],
                       [Vector2(19, 13), Vector2(19, 14), Vector2(19, 15), Vector2(19, 16), Vector2(19, 17), Vector2(19, 18)],
                        [Vector2(1, 19), Vector2(2,19), Vector2(3,19), Vector2(4,19), Vector2(5,19), Vector2(6,19),Vector2(19, 6)],
                        [Vector2(14, 19), Vector2(15, 19), Vector2(16, 19), Vector2(17, 19), Vector2(18, 19),Vector2(19,19)],
                       [Vector2(1, 0), Vector2(2, 0), Vector2(3, 0), Vector2(4, 0), Vector2(5, 0), Vector2(6, 0)],
                       [Vector2(14, 0), Vector2(15, 0), Vector2(16, 0), Vector2(17, 0), Vector2(18, 0),Vector2(19, 0)],
                       [Vector2(6, 7), Vector2(7, 7), Vector2(8, 7), Vector2(9, 7), Vector2(10, 7), Vector2(11, 7),Vector2(12,7),Vector2(13,7),Vector2(14,7)],
                       [Vector2(6,11), Vector2(7, 11), Vector2(8, 11), Vector2(9, 11), Vector2(10,11), Vector2(11, 11),Vector2(12,11),Vector2(13,11),Vector2(14,11)]
                       ]
        self.brick_img = pygame.image.load('Graphics/brick_white.png').convert_alpha()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.set_speed()
        self.check_level()
        self.check_collision_items()
        self.function_item()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.check_level()
        self.check_fail()
        self.draw_map()
        self.function_item()
    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pause_img = pygame.image.load('Graphics/button.png').convert_alpha()
            pause_rect = pause_img.get_rect(center = (380,250))
            screen.fill((255,255,255))
            choose_text = game_font.render("Press C to Continue Or press Q to Quit!!",True,(15,215,15),25)
            pause_text = game_font.render("The Game is Paused", True,(15,255,15),30)

            screen.blit(pause_img,pause_rect)
            screen.blit(pause_text,[280,350])
            screen.blit(choose_text,[200,400],)

            pygame.display.update()
            clock.tick(5)

    def check_collision(self): # check when snake through the fruit
        if self.fruit.pos == self.snake.body[0]:
            #reposition for fruit
            self.fruit.randomize()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        for brick in self.blocks:
            for block in brick:
                if block == self.fruit.pos:
                    self.fruit.randomize()

    def game_over(self):
        self.snake.reset()

    def check_fail(self):
         # if snake hits to wall
        if not (0 <= self.snake.body[0].x < cell_number) or not (0 <= self.snake.body[0].y < cell_number):
            self.game_over()
        # if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        for brick in self.blocks:
            for block in brick:
                if block == self.snake.body[0]:
                    self.game_over()
    def draw_map(self):
        for index, brick in enumerate(self.blocks):
            for block in brick:
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos, y_pos, 40, 40)
                screen.blit(self.brick_img, block_rect)


    def draw_grass(self):
        for col in range(cell_number):
            if col %2 == 0:
                for row in range(cell_number):
                    if row % 2 == 0:
                        grass_rect = pygame.Rect(int(row * cell_size),int(col*cell_size),cell_size,cell_size)
                        pygame.draw.rect(screen,(111,215,70),grass_rect)
            else:
                for row in range(cell_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(int(row * cell_size), int(col * cell_size), cell_size, cell_size)
                        pygame.draw.rect(screen, (111, 215, 70), grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) -3)
        score_surface = game_font.render(score_text,True,(50,57,48))
        score_x = int(cell_size*cell_number -120)
        score_y = int(cell_size*cell_number -60)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = self.fruit.black_apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)

        pygame.draw.rect(screen,(167,40,81),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(self.fruit.black_apple,apple_rect)
        pygame.draw.rect(screen,(56,54,125),bg_rect,2)

    def check_level(self):
        level_sound = pygame.mixer.Sound('Sound/level_up_sound.wav')

        level_text = game_font.render('LEVEL UP!',True,(215,15,49))
        lv_x = int((cell_size * cell_number) / 2)
        lv_y = int((cell_size * cell_number) / 2)
        level_rect = level_text.get_rect(center=(lv_x, lv_y))
        # screen.blit(level_text, level_rect)
        check = True
        score_point = int(len(self.snake.body) - 3)
        if score_point == 5 or self.snake.body[0] == self.fruit.pos:
            screen.blit(level_text, level_rect)
            level_sound.play(0)
        if score_point == 10 and check == True:
            screen.blit(level_text, level_rect)
            level_sound.play(1)

    def set_speed(self):
        score_point = int(len(self.snake.body) -3)
        if score_point < 8:
            pygame.time.set_timer(SCREEN_UPDATE, 120)  # set up speed for snake

        elif 8 <= score_point < 14:
            pygame.time.set_timer(SCREEN_UPDATE, 100)  # set up speed for snake
        else:
            pygame.time.set_timer(SCREEN_UPDATE, 80)  # set up speed for snake

    def check_collision_items(self): # check when snake through the fruit
        if self.items.pos == self.snake.body[0]:
            #reposition for fruit
            self.items.randomize_item()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.items.pos:
                self.items.randomize_item()

        for brick in self.blocks:
            for block in brick:
                if block == self.items.pos:
                    self.items.randomize_item()
    def function_item(self):
        score_point = int(len(self.snake.body) - 3)
        if score_point % 3 == 0 and score_point != 0:
            self.items.draw_fruit()
            score_point = score_point + 1
class MAIN_game2:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.blocks = [[Vector2(6,0), Vector2(6,1), Vector2(6,2), Vector2(6,3), Vector2(6,4), Vector2(6,5)],
                       [Vector2(0,7),Vector2(1,7),Vector2(2,7), Vector2(3,7),Vector2(4,7), Vector2(5,7), Vector2(6,7)],
                       [Vector2(12,12),Vector2(12,13),Vector2(12,14), Vector2(12,15), Vector2(12,16), Vector2(12,17), Vector2(12,18), Vector2(12,19)],
                       [Vector2(11,4), Vector2(12,4),Vector2(13,4),Vector2(14,4),Vector2(15,4),Vector2(16,4),Vector2(17,4), Vector2(18,4),Vector2(19,4)]]
        self.brick_img = pygame.image.load('Graphics/brick_white.png').convert_alpha()
        self.items = ITEMS()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.set_speed()
        self.check_level()
        self.function_item()
        self.check_collision_items()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.check_level()
        self.check_fail()
        self.draw_map()
        self.function_item()
    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pause_img = pygame.image.load('Graphics/button.png').convert_alpha()
            pause_rect = pause_img.get_rect(center = (380,250))
            screen.fill((255,255,255))
            choose_text = game_font.render("Press C to Continue Or press Q to Quit!!",True,(15,215,15),25)
            pause_text = game_font.render("The Game is Paused", True,(15,255,15),30)

            screen.blit(pause_img,pause_rect)
            screen.blit(pause_text,[280,350])
            screen.blit(choose_text,[200,400],)

            pygame.display.update()
            clock.tick(5)

    def check_collision(self): # check when snake through the fruit
        if self.fruit.pos == self.snake.body[0]:
            #reposition for fruit
            self.fruit.randomize()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        for brick in self.blocks:
            for block in brick:
                if block == self.fruit.pos:
                    self.fruit.randomize()

    def game_over(self):
        self.snake.reset()

    def check_fail(self):
         # if snake hits to wall
        if not (0 <= self.snake.body[0].x < cell_number) or not (0 <= self.snake.body[0].y < cell_number):
            self.game_over()
        # if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        for brick in self.blocks:
            for block in brick:
                if block == self.snake.body[0]:
                    self.game_over()
    def draw_map(self):
        for index, brick in enumerate(self.blocks):
            for block in brick:
                x_pos = int(block.x * cell_size)
                y_pos = int(block.y * cell_size)
                block_rect = pygame.Rect(x_pos, y_pos, 40, 40)
                screen.blit(self.brick_img, block_rect)


    def draw_grass(self):
        for col in range(cell_number):
            if col %2 == 0:
                for row in range(cell_number):
                    if row % 2 == 0:
                        grass_rect = pygame.Rect(int(row * cell_size),int(col*cell_size),cell_size,cell_size)
                        pygame.draw.rect(screen,(111,215,70),grass_rect)
            else:
                for row in range(cell_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(int(row * cell_size), int(col * cell_size), cell_size, cell_size)
                        pygame.draw.rect(screen, (111, 215, 70), grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) -3)
        score_surface = game_font.render(score_text,True,(50,77,48))
        score_x = int(cell_size*cell_number -120)
        score_y = int(cell_size*cell_number -40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = self.fruit.black_apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)

        pygame.draw.rect(screen,(167,60,81),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(self.fruit.black_apple,apple_rect)
        pygame.draw.rect(screen,(56,74,125),bg_rect,2)

    def check_level(self):
        level_sound = pygame.mixer.Sound('Sound/level_up_sound.wav')

        level_text = game_font.render('LEVEL UP!',True,(215,15,49))
        lv_x = int((cell_size * cell_number) / 2)
        lv_y = int((cell_size * cell_number) / 2)
        level_rect = level_text.get_rect(center=(lv_x, lv_y))
        # screen.blit(level_text, level_rect)
        check = True
        score_point = int(len(self.snake.body) - 3)
        if score_point == 5 or self.snake.body[0] == self.fruit.pos:
            screen.blit(level_text, level_rect)
            level_sound.play(0)
        if score_point == 10 and check == True:
            screen.blit(level_text, level_rect)
            level_sound.play(1)

    def set_speed(self):
        score_point = int(len(self.snake.body) -3)
        if score_point < 5:
            pygame.time.set_timer(SCREEN_UPDATE, 120)  # set up speed for snake

        elif 5 <= score_point < 10:
            pygame.time.set_timer(SCREEN_UPDATE, 100)  # set up speed for snake
        else:
            pygame.time.set_timer(SCREEN_UPDATE, 80)  # set up speed for snake

    def check_collision_items(self): # check when snake through the fruit
        if self.items.pos == self.snake.body[0]:
            #reposition for fruit
            self.items.randomize_item()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.items.pos:
                self.items.randomize_item()

        for brick in self.blocks:
            for block in brick:
                if block == self.items.pos:
                    self.items.randomize_item()
    def function_item(self):
        score_point = int(len(self.snake.body) - 3)
        if score_point % 3 == 0 and score_point != 0:
            self.items.draw_fruit()
            score_point = score_point + 1

class MAIN_game3:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.items = ITEMS
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.set_speed()
        self.check_level()
        self.check_collision_items()
        self.function_item()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.check_level()
        self.check_fail()
        self.function_item()
    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pause_img = pygame.image.load('Graphics/button.png').convert_alpha()
            pause_rect = pause_img.get_rect(center = (380,250))
            screen.fill((255,255,255))
            choose_text = game_font.render("Press C to Continue Or press Q to Quit!!",True,(15,215,15),25)
            pause_text = game_font.render("The Game is Paused", True,(15,255,15),30)

            screen.blit(pause_img,pause_rect)
            screen.blit(pause_text,[280,350])
            screen.blit(choose_text,[200,400],)

            pygame.display.update()
            clock.tick(5)

    def check_collision(self): # check when snake through the fruit
        if self.fruit.pos == self.snake.body[0]:
            #reposition for fruit
            self.fruit.randomize()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def game_over(self):
        self.snake.reset()

    def check_fail(self):
         # if snake hits to wall
        if not (0 <= self.snake.body[0].x < cell_number) or not (0 <= self.snake.body[0].y < cell_number):
            self.game_over()
        # if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def draw_grass(self):
        for col in range(cell_number):
            if col %2 == 0:
                for row in range(cell_number):
                    if row % 2 == 0:
                        grass_rect = pygame.Rect(int(row * cell_size),int(col*cell_size),cell_size,cell_size)
                        pygame.draw.rect(screen,(111,215,70),grass_rect)
            else:
                for row in range(cell_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(int(row * cell_size), int(col * cell_size), cell_size, cell_size)
                        pygame.draw.rect(screen, (111, 215, 70), grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) -3)
        score_surface = game_font.render(score_text,True,(50,77,48))
        score_x = int(cell_size*cell_number -120)
        score_y = int(cell_size*cell_number -40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = self.fruit.black_apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)

        pygame.draw.rect(screen,(167,70,81),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(self.fruit.black_apple,apple_rect)
        pygame.draw.rect(screen,(56,74,125),bg_rect,2)

    def check_level(self):
        level_sound = pygame.mixer.Sound('Sound/level_up_sound.wav')

        level_text = game_font.render('LEVEL UP!',True,(215,15,49))
        lv_x = int((cell_size * cell_number) / 2)
        lv_y = int((cell_size * cell_number) / 2)
        level_rect = level_text.get_rect(center=(lv_x, lv_y))
        # screen.blit(level_text, level_rect)
        check = True
        score_point = int(len(self.snake.body) - 3)
        if score_point == 5 or self.snake.body[0] == self.fruit.pos:
            screen.blit(level_text, level_rect)
            level_sound.play(0)
        if score_point == 10 and check == True:
            screen.blit(level_text, level_rect)
            level_sound.play(1)

    def set_speed(self):
        score_point = int(len(self.snake.body) -3)
        if score_point < 5:
            pygame.time.set_timer(SCREEN_UPDATE, 120)  # set up speed for snake

        elif 5 <= score_point < 10:
            pygame.time.set_timer(SCREEN_UPDATE, 100)  # set up speed for snake
        else:
            pygame.time.set_timer(SCREEN_UPDATE, 80)  # set up speed for snake
    def check_collision_items(self): # check when snake through the fruit
        if self.items.pos == self.snake.body[0]:
            #reposition for fruit
            self.items.randomize_item()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.items.pos:
                self.items.randomize_item()
    def function_item(self):
        score_point = int(len(self.snake.body) - 3)
        if score_point % 3 == 0 and score_point != 0:
            self.items.draw_fruit()
            score_point = score_point + 1
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_number = 20
cell_size = 40
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) # tạo screen
pygame.display.set_caption('Snake 1.0')
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',25)
start_img = pygame.image.load('Graphics/snake-pass-key-art-no-logo.png').convert_alpha()
main_game1 = MAIN_game1()
main_game2 = MAIN_game2()
main_game3 = MAIN_game3()
FPS = 45
gameOver = False
def get_font(size):
    return pygame.font.Font("Font/PoetsenOne-Regular.ttf", size)
def start_game1():
    while True:
        for event in pygame.event.get():  # run all of  event
            if event.type == pygame.QUIT:  # quit
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game1.update()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if main_game1.snake.direction.y != 1:  # check snake can't reverse itself
                        main_game1.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game1.snake.direction.y != -1:
                        main_game1.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game1.snake.direction.x != -1:
                        main_game1.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game1.snake.direction.x != 1:
                        main_game1.snake.direction = Vector2(-1, 0)

                if event.key == pygame.K_p:
                    main_game1.pause()
                if event.key == pygame.K_m:
                    main_menu()
        screen.fill((115, 195, 70))
        main_game1.draw_element()
        pygame.display.update()
        clock.tick(45)
def start_game2():
    while True:
        for event in pygame.event.get():  # run all of  event
            if event.type == pygame.QUIT:  # quit
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game2.update()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if main_game2.snake.direction.y != 1:  # check snake can't reverse itself
                        main_game2.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game2.snake.direction.y != -1:
                        main_game2.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game2.snake.direction.x != -1:
                        main_game2.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game2.snake.direction.x != 1:
                        main_game2.snake.direction = Vector2(-1, 0)

                if event.key == pygame.K_p:
                    main_game2.pause()
                if event.key == pygame.K_m:
                    main_menu()
        screen.fill((115, 195, 70))
        main_game2.draw_element()
        pygame.display.update()
        clock.tick(45)
def start_game3():
    while True:
        for event in pygame.event.get():  # run all of  event
            if event.type == pygame.QUIT:  # quit
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game3.update()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if main_game3.snake.direction.y != 1:  # check snake can't reverse itself
                        main_game3.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game3.snake.direction.y != -1:
                        main_game3.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game3.snake.direction.x != -1:
                        main_game3.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game3.snake.direction.x != 1:
                        main_game3.snake.direction = Vector2(-1, 0)

                if event.key == pygame.K_p:
                    main_game3.pause()
                if event.key == pygame.K_m:
                    main_menu()
        screen.fill((115, 195, 70))
        main_game3.draw_element()
        pygame.display.update()
        clock.tick(45)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        start_game3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def speed():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(45).render("Choose your Speed!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 400))
        screen.fill('white')
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        Hard = Button(image=None, pos=(500, 460),
                      text_input="Very Fast", font=get_font(35), base_color="Black", hovering_color="Green")

        Hard.changeColor(OPTIONS_MOUSE_POS)
        Hard.update(screen)

        Medium = Button(image=None, pos=(340, 460),
                        text_input="Fast", font=get_font(35), base_color="Black", hovering_color="Green")

        Medium.changeColor(OPTIONS_MOUSE_POS)
        Medium.update(screen)

        Clasical = Button(image=None, pos=(150, 460),
                          text_input="Slow", font=get_font(35), base_color="Black", hovering_color="Green")

        Clasical.changeColor(OPTIONS_MOUSE_POS)
        Clasical.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Hard.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.time.set_timer(SCREEN_UPDATE, 200)
                    main_menu()
                if Medium.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.time.set_timer(SCREEN_UPDATE, 100)
                    main_menu()
                if Clasical.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.time.set_timer(SCREEN_UPDATE, 50)
                    main_menu()
        pygame.display.update()
def options():
    while True:
        option_img = pygame.image.load('assets/background_options.png').convert_alpha()
        screen.blit(option_img,(0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(45).render("Choose your level!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        Hard = Button(image=None, pos=(500, 460),
                              text_input="Hard", font=get_font(35), base_color="Black", hovering_color="Green")

        Hard.changeColor(OPTIONS_MOUSE_POS)
        Hard.update(screen)

        Medium = Button(image=None, pos=(340, 460),
                              text_input="Medium", font=get_font(35), base_color="Black", hovering_color="Green")

        Medium.changeColor(OPTIONS_MOUSE_POS)
        Medium.update(screen)

        Clasical = Button(image=None, pos=(150, 460),
                        text_input="Clasical", font=get_font(35), base_color="Black", hovering_color="Green")

        Clasical.changeColor(OPTIONS_MOUSE_POS)
        Clasical.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Hard.checkForInput(OPTIONS_MOUSE_POS):
                    start_game1()
                if Medium.checkForInput(OPTIONS_MOUSE_POS):
                    start_game2()
                if Clasical.checkForInput(OPTIONS_MOUSE_POS):
                    start_game3()
        pygame.display.update()


def main_menu():
    while True:
        screen.blit(start_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(440, 110))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(440, 250),
                             text_input="PLAY", font=get_font(35), base_color=(0,0,0), hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(440, 400),
                                text_input="OPTIONS", font=get_font(35), base_color=(0,0,0), hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(440, 550),
                             text_input="QUIT", font=get_font(35), base_color=(0,0,0), hovering_color="White")
        SPEED_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(440, 650),
                             text_input="SPEED", font=get_font(35), base_color=(0,0,0), hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if SPEED_BUTTON.checkForInput(MENU_MOUSE_POS):
                    speed()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()