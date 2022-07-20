''' 
    Jefpy © 2022

    Make sure Arcade is installed! Info for installation is found here: https://api.arcade.academy/en/2.5.7/installation_windows.html 

    Make sure Pygame is installed! Info for installation is found here: https://www.pygame.org/wiki/GettingStarted
    
'''
import arcade 
import random
import os
import numpy as np
import math

from arcade.color import GRANNY_SMITH_APPLE, GRAY
from RGBTest import Color

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 920
SCALING = 1
SCREEN_TITLE = "Smite Typer!"
file_path = os.path.dirname(os.path.abspath(__file__))
DICTION = open(f"{file_path}/words.txt").readlines()
os.chdir(file_path)

global total_words
total_words = {}

global keys_dict
keys_dict = {
    "97": "A", 
    "98": "B", 
    "99": "C", 
    "100": "D", 
    "101": "E", 
    "102": "F", 
    "103": "G", 
    "104": "H", 
    "105": "I", 
    "106": "J", 
    "107": "K", 
    "108": "L", 
    "109": "M", 
    "110": "N", 
    "111": "O", 
    "112": "P", 
    "113": "Q", 
    "114": "R", 
    "115": "S", 
    "116": "T", 
    "117": "U", 
    "118": "V", 
    "119": "W", 
    "120": "X", 
    "121": "Y", 
    "122": "Z"
}

def randomWord():
    random_number = random.randint(1, len(DICTION))
    random_word = DICTION[random_number]
    random_word = str(random_word)
    random_word = random_word.replace("\n", "")
    return random_word

def genEasyWord():
    word = randomWord()
    length = int(len(word))
    if length <= 8:
        if length >= 4:
            total_words.append(word)
        else:
            return genEasyWord()
    if length > 6:
        return genEasyWord()

def genMedWord():
    word = randomWord()
    length = int(len(word))
    if length <= 10:
        if length >= 6:
            total_words.append(word)
        else:
            return genMedWord()
    if length > 8:
        return genMedWord()

def genHardWord():
    word = randomWord()
    length = int(len(word))
    if length >= 11:
        total_words.append(word)
    if length < 11:
        return genHardWord()

class CloudAttr(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 0.5
        self.scale = SCALING / 2

        self.randomNum = random.randint(1,7)
        self.textures = []
        texture = arcade.load_texture(f"{file_path}/Sprites/cloud{self.randomNum}.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = self.textures[0]

    def update(self):
        super().update()
        if self.right <= -10:
            self.remove_from_sprite_lists()

class EnemyAttr(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 0.5
        self.nametag = ""

        self.textures = []
        texture = arcade.load_texture(f"{file_path}/Sprites/goblin.png", flipped_horizontally=True)
        self.textures.append(texture)
        texture = arcade.load_texture(f"{file_path}/Sprites/goblin.png")
        self.textures.append(texture)

        if difficulty == 1:
            genEasyWord()
            self.speed = 0.9
            self.scale = SCALING / 1.5
        elif difficulty == 2:
            genMedWord()
            self.speed = 0.7
            self.scale = SCALING / 1.25
        else:
            genHardWord()
            self.speed = 0.4
            self.scale = SCALING

        self.randomNum = random.randint(1,2)
        if self.randomNum == 1:
            self.center_x = -25
            self.velocity = (self.speed, 0)
            self.center_y = (SCREEN_HEIGHT - random.randint(432, 570))
            self.nametag = total_words[-1]
        else:
            self.center_x = SCREEN_WIDTH + 25
            self.velocity = (-(self.speed), 0)
            self.center_y = (SCREEN_HEIGHT - random.randint(432, 570))
            self.nametag = total_words[-1]

    def update(self):
        super().update()
        if self.randomNum == 1:
            self.texture = self.textures[1]
        else:
            self.texture = self.textures[0]

class IDKAttr(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = SCALING
        self.speed = 5
        self.angle = 0

    def update(self):
        # goes in a circular motion
        self.angle += 5
        angle_rad = math.radians(self.angle)
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

class ZuesAttr(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = SCALING * 2
        self.textures = []
        self.flipped = False

        texture = arcade.load_texture(f"{file_path}/Sprites/zues.png")
        self.textures.append(texture)
        texture = arcade.load_texture(f"{file_path}/Sprites/zues.png", flipped_horizontally=True)
        self.textures.append(texture)

        charged = arcade.load_texture(f"{file_path}/Sprites/zuescharged.png")
        self.textures.append(charged)
        charged = arcade.load_texture(f"{file_path}/Sprites/zuescharged.png", flipped_horizontally=True)
        self.textures.append(charged)

        scharged = arcade.load_texture(f"{file_path}/Sprites/zuessupercharged.png")
        self.textures.append(scharged)
        scharged = arcade.load_texture(f"{file_path}/Sprites/zuessupercharged.png", flipped_horizontally=True)
        self.textures.append(scharged)

        awakened = arcade.load_texture(f"{file_path}/Sprites/maxedzues.png")
        self.textures.append(awakened)
        awakened = arcade.load_texture(f"{file_path}/Sprites/maxedzues.png", flipped_horizontally=True)
        self.textures.append(awakened)

    def update(self):
        if points >= 5000:
            self.scale = SCALING * 3
        if self.flipped == False:
            if points >= 1000 and points < 2000:
                self.texture = self.textures[2]
            elif points >= 2000 and points < 5000:
                self.texture = self.textures[4]
            elif points >= 5000:
                self.texture = self.textures[6]
            else:
                self.texture = self.textures[0]
        elif self.flipped == True:
            if points >= 1000 and points < 2000:
                self.texture = self.textures[3]
            elif points >= 2000 and points < 6666:
                self.texture = self.textures[5]
            elif points >= 6666:
                self.texture = self.textures[7]
            else:
                self.texture = self.textures[1]

class TitleView(arcade.View):
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Smite Typer",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 460,
        arcade.color.CYBER_YELLOW, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        arcade.draw_text("Click To Start!",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 490,
        arcade.color.WHITE, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MainView()
        game_view.setup()
        self.window.show_view(game_view)

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)

        self.rgb = Color()

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Game Over!",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 460,
        arcade.color.RED_DEVIL, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        arcade.draw_text(f"Survived: {final_time} with a score of {points}!",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 500,
        arcade.color.CYBER_YELLOW, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        arcade.draw_text("Click To Retry!",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 540,
        (self.rgb.changeColor()), 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MainView()
        game_view.setup()
        self.window.show_view(game_view)

class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

        self.rgb = Color()
        
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Paused.",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 460,
        (self.rgb.changeColor()), 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        arcade.draw_text("Press ESC To Resume.",
        SCREEN_WIDTH/2, SCREEN_HEIGHT - 500,
        (self.rgb.changeColor()), 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)

class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        global difficulty
        global points
        global total_words

        self.total_time = 0.0
        self.output = "00:00"
        self.typing = ""
        self.rgb = Color()
        self.eText = ""
        self.castle_health = 100
        self.d1, self.d2 = 2,3
        self.rising = False
        points = 0
        total_words = []
        difficulty = 1

        self.castle_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.ash_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.flash_list = arcade.SpriteList()

    def angle_calc(self, p1 ,p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        calc = np.rad2deg((ang1 - ang2) % (2 * np.pi))
        return calc

    def addCloud(self, delta_time: float):
        self.cloud = CloudAttr()

        self.cloud.center_y = (SCREEN_HEIGHT - random.randint(25, 125))
        self.cloud.velocity = (-(self.cloud.speed), 0)

        if self.cloud.randomNum == 7 or self.cloud.randomNum == 4:
            self.cloud.center_x = SCREEN_WIDTH + 140
        else:
            self.cloud.center_x = SCREEN_WIDTH + 95

        self.clouds_list.append(self.cloud)
    
    def addEnemy(self, delta_time: float):
        self.enemy_sprite = EnemyAttr()
        self.enemies_list.append(self.enemy_sprite)

    def ashPile(self, x, y):
        ash = arcade.Sprite(f"{file_path}/Sprites/ash.png", SCALING/14, center_x=x, center_y=y)
        self.ash_list.append(ash)

    def flash(self):
        flash_sprite = arcade.Sprite(f"{file_path}/Sprites/flash.png", SCALING * 3)
        flash_sprite.center_x = SCREEN_WIDTH/2
        flash_sprite.center_y = SCREEN_HEIGHT/2
        if points >= 6666:
            flash_sprite.color = (255, 0, 0)
        self.flash_list.append(flash_sprite)

    def setup(self):
        self.castle_sprite = arcade.Sprite(f"{file_path}/Sprites/castle.png", SCALING * 1.1)
        self.castle_sprite.center_x = SCREEN_WIDTH/2
        self.castle_sprite.center_y = SCREEN_HEIGHT/2
        self.castle_list.append(self.castle_sprite)

        self.zues_list = arcade.SpriteList()
        self.zues_sprite = ZuesAttr()
        self.zues_sprite.center_x = SCREEN_WIDTH/2
        self.zues_sprite.center_y = (SCREEN_WIDTH/2) + 50
        self.zues_list.append(self.zues_sprite)

        colors = [arcade.color.SKY_BLUE, arcade.color.BABY_BLUE, arcade.color.BEAU_BLUE, arcade.color.POWDER_BLUE, arcade.color.PICTON_BLUE]
        randomNum = random.randint(0, len(colors))
        if randomNum == len(colors):
            randomNum = randomNum - 1
        self.color = colors[randomNum]

    def on_show(self):
        arcade.set_background_color(self.color)
        arcade.schedule(self.addCloud, random.randint(4, 10))
        arcade.schedule(self.addEnemy, random.randint(self.d1, self.d2))

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 750, SCREEN_WIDTH, 700, GRANNY_SMITH_APPLE)

        arcade.draw_triangle_filled(-5, SCREEN_HEIGHT - 400, 125, SCREEN_HEIGHT - 150, 250, SCREEN_HEIGHT - 400, GRAY)
        arcade.draw_triangle_filled(175, SCREEN_HEIGHT - 400, 125, SCREEN_HEIGHT - 150, 495, SCREEN_HEIGHT - 400, GRAY)
        arcade.draw_triangle_filled(150, SCREEN_HEIGHT - 400, 355, SCREEN_HEIGHT - 225, 600, SCREEN_HEIGHT - 400, GRAY)
        arcade.draw_triangle_filled(350, SCREEN_HEIGHT - 400, 500, SCREEN_HEIGHT - 125, 700, SCREEN_HEIGHT - 400, GRAY)
        arcade.draw_triangle_filled(126, 769, 302, 649, 68, 658, (255, 255, 255))
        arcade.draw_triangle_filled(355, 695, 303, 649, 421, 647, (255, 255, 255))
        arcade.draw_triangle_filled(421, 646, 500, 794, 605, 649, (255, 255, 255))

        self.castle_list.draw()
        self.clouds_list.draw()
        self.enemies_list.draw()
        self.ash_list.draw()
        self.zues_list.draw()

        for en in self.enemies_list:
            arcade.draw_text(str(en.nametag).upper(),
            en.center_x, en.center_y + 30,
            (arcade.color.RED), 12,
            anchor_x="center")

        # Drawing counter
        arcade.draw_text(self.output,
        SCREEN_WIDTH - 50, 5,
        (0,0,0), 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        # Difficulty 
        arcade.draw_text(f"Difficulty: {difficulty}",
        110, 5,
        arcade.color.BLACK, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        # Castle health
        arcade.draw_text("❤️ " + str(self.castle_health),
        self.castle_sprite.center_x, self.castle_sprite.bottom - 25,
        (self.rgb.changeColor()), 20,
        anchor_x="center")

        # Drawing where the user can see what they're typing
        arcade.draw_text(self.typing,
        SCREEN_WIDTH/2, 5,
        (self.rgb.changeColor()), 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        # Score
        arcade.draw_text(f"Score: {format(points, ',')}",
        105, 45,
        arcade.color.BLACK, 25,
        font_name='Kenney Mini Square',
        anchor_x="center")

        self.flash_list.draw()

    def on_key_press(self, symbol, modifiers):
        global points
        global keys_dict
        global eWord
        points = int(points)

        if symbol == arcade.key.ESCAPE:
            pause = PauseView(self)
            self.window.show_view(pause)
            arcade.unschedule(self.addCloud)
            arcade.unschedule(self.addEnemy)

        if symbol == arcade.key.ENTER:
            for word in total_words:
                if self.eText.lower() == str(word).lower():
                    eWord = word
                    total_words.remove(word)
            for en in self.enemies_list:
                try:
                    if eWord == en.nametag:
                        if en.center_x > 990:
                            self.zues_sprite.flipped = False
                        elif en.center_x < 600:
                            self.zues_sprite.flipped = True
                        newAngle = int(self.angle_calc((int(en.center_x), int(en.center_y)), (int(self.zues_sprite.center_x), int(self.zues_sprite.center_y))))
                        self.zues_sprite.angle = newAngle
                        self.ashPile(en.center_x, en.bottom)
                        self.enemies_list.remove(en)
                        self.flash()
                        points += 25 * difficulty
                except NameError:
                    pass
            self.eText = ""

        if symbol == arcade.key.BACKSPACE:
            self.eText = self.eText[:-1]
        
        for key, value in keys_dict.items():
            if int(symbol) == int(key):
                self.eText = self.eText + value
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # testing purposes
        return

    def on_update(self, delta_time: float):
        global final_time
        global difficulty
        global total_words
        global points

        self.typing = self.eText
        self.total_time += delta_time
        
        timescale = 60
        minutes = int(self.total_time) // timescale
        seconds = int(self.total_time) % timescale
        self.output = f"{minutes:02d}:{seconds:02d}"

        final_time = self.output

        self.clouds_list.update()
        self.enemies_list.update()
        self.zues_list.update()

        for ash in self.ash_list:
            if ash.alpha > 0:
                try:
                    ash.alpha -= 1
                    ash.scale -= 0.00022
                except ValueError:
                    ash.remove_from_sprite_lists()
            elif ash.alpha <= 0:
                ash.remove_from_sprite_lists()
        
        for flash in self.flash_list:
            if flash.alpha > 0:
                try:
                    flash.alpha -= 30
                except ValueError:
                    flash.remove_from_sprite_lists()
            elif flash.alpha <= 0:
                flash.remove_from_sprite_lists()

        if self.castle_health <= 0:
            total_words = []
            self.enemies_list = []
            arcade.unschedule(self.addCloud)
            arcade.unschedule(self.addEnemy)            
            view = GameOverView()
            self.window.show_view(view)

        # Testing
        if self.eText.lower() == "endgame":
            self.castle_health = 0
        if self.eText.lower() == "infscore":
            points += 50

        if minutes == 1:
            if seconds == 30:
                difficulty = 2
        elif minutes >= 3:
            difficulty = 3

        # Zues levitating mechanics
        if int(self.zues_sprite.center_y) >= 810:
            if self.rising == False:
                self.zues_sprite.center_y -= 0.35

        if int(self.zues_sprite.center_y) <= 810:
            self.rising = True

        if self.rising == True:
            self.zues_sprite.center_y += 0.35

        if int(self.zues_sprite.center_y) >= 850 and self.rising == True:
            self.rising = False

        # makes delay of enemies spawning longer as difficulty increases
        if difficulty == 2:
            self.d1 = 4
            self.d2 = 6
        if difficulty == 3:
            self.d1 = 5
            self.d2 = 8

        for enemy in self.enemies_list: # Enemy collision detection
            if enemy.center_x >= self.castle_sprite.left and enemy.center_x <= self.castle_sprite.right:
                if difficulty == 1:
                    self.castle_health = self.castle_health - 3
                    enemy.remove_from_sprite_lists()
                    total_words.remove(enemy.nametag)
                elif difficulty == 2:
                    self.castle_health = self.castle_health - 5
                    enemy.remove_from_sprite_lists()
                    total_words.remove(enemy.nametag)
                else:
                    self.castle_health = self.castle_health - 10
                    enemy.remove_from_sprite_lists()
                    total_words.remove(enemy.nametag)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()