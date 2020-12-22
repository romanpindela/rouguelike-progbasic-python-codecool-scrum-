
'''
warstwy do złączenia:
1 board interfejsu :warstwa board - większa mapa : tła interfejsu

2 game board : 
    warstwa board: wrogów
    warstwa board: Fight_equipments i Food oraz Healing_potions
    warstwa board: plansza z danym światem
    warstwa board: z playerem

3 board planszy walki:
'''

from os import system, name
import numpy
import pandas #used for Board.print_board()
import random
from random import choice 

import time
#from classes_additional import *
#from utils import *
import string


class Settings:

    class Key_map:
        def __init__(self, key_to_change_armor = "q", key_to_change_weapon = "e", key_to_right = "d", key_to_left = "a", key_to_up = "w", key_to_down = "s", key_to_show_inventory = "i"):
            self.key_to_change_armor = key_to_change_armor
            self.key_to_change_weapon = key_to_change_weapon
            self.key_to_right = key_to_right
            self.key_to_left = key_to_right
            self.key_to_up = key_to_up
            self.key_to_down = key_to_down
            self.key_to_show_inventory = key_to_show_inventory  

    class Game_board:

        board_width = 30
        board_height = 20

        def __init__(self) -> None:
            pass

    class Player:
        default_name = "Warrior"
        default_player_icon = '@'
        max_health = 100 # points
        default_attack = 5
        start_experience = 1
        dodge = 15 # 15 % of chances to dodge enemies attack


        start_position_x = random.randint(1,9)
        start_position_x = random.randint(1,9)

        effort_costs_for_walking = 3 # every i.e. 3 moves player losts 1 point of health (so that he should collect food)

    class Scoreboard:
        filename = "scoreboard.csv"
        sort_direction = {"highest_first":1, "lowest_first":-1}

    class Color_scheme:
        player = ""

        enemy = ""
        armour = ""
        weapon = ""
        gateway = ""
        level_border = ""

        barier_forest = ""
        barier_rocks = ""
        barier_river = ""

        empty_space = ""

        reset = ""

        interface_border = ""


    class Enemy:
        
        experience_from_killed_enemy = 5 # for each killed enemy player get another points

        class Orcs:
            icon = "*"
            name = "Orcs"
        class Knights:
            icon = "+"
            name = "Knight"
        class Elfs:
            icon = "!"
            name = "Elf"
        class DragonBoss:
            icon = [["####"],["####"],["####"]]
            name = "DragonBoss"


    class Items:
        class Healing_potions:
            healing_points = 20

        class Food:
            healing_points = 5

        class Weapon:
            class Dagger:
                attack = 5 # default attack
                icon = 'D'
            class Sword:
                attack = 10
                icon = 'S'
            class Axe:
                attack = 15
                icon = 'A'

        class Armour:
            class Leather_armour:
                protection = -5
                icon = 'x'
            class Chainmail_armour:
                protection = -10
                icon = 'Y'
            class Plate_armour:
                protection = -15
                icon = 'X'

    class Universe:
        level_names = {1:'level 1', 2:'level 2', 3:'level 3'}

        
        class level:

            #number of enemies for level
            enemies_min_number = 5
            enemies_max_number = 10
            increment_of_enemies_for_level = 5 # increment enemies number i.e. 5 * level number (i.e. for level 3: 5 * 3 = 15 enemies)




                

            orcs_min_number = 5
            orcs_max_number = 9
            orcs_number = random.randint(orcs_min_number, orcs_max_number)

            elfs_min_number = 3
            elfs_max_number = 7
            elfs_number = random.randint(elfs_min_number, elfs_max_number)

            knights_min_number = 2
            knights_max_number = 4
            knights_number = random.randint(knights_min_number, knights_max_number)

            dragonboss = 0

            #number of food
            food_number_min = 15
            food_number_max = 20
            food_number = random.randint(food_number_min, food_number_max)

            #number of healing potions
            healing_potions_min = 15
            healing_potions_max = 20
            healing_potions_number = random.randint(healing_potions_min, healing_potions_max)

            #number of armour
            



class Universe: # class for going through worlds
    
    def __init__(self) -> None:
        self.Level_1 = Level(Settings.Universe.level_names[1])
        self.Level_2 = Level(Settings.Universe.level_names[2])
        self.Level_3 = Level(Settings.Universe.level_names[3])

        self.levels = []
        self.levels.append(self.level_1)
        self.levels.append(self.level_2)
        self.levels.append(self.level_3)

        self.active_level = 1
        self.enabled_level = []

    class Level:
        def __init__(self, level_name: str) -> None:
            self.Level_name = level_name
            self.Game_board = Game_board(level_name)
            self.Fight_board = fight_board(level_name)
            self.Enemies = Enemies(level_name)
            self.Items = Items(level_name)
#############
            # random number of enemies for level
            self.enemies_number_of_orcs = 
            self.
            enemies_number = random.randint(enemies_min_number, enemies_max_number)
            number_of_enemies_to_assign = random.randint(0, enemies_number)
            orcs_number = number_of_enemies_to_assign
            enemies_number -= number_of_enemies_to_assign
            elf_number = random.randint(0, enemies_number)
            enemies_number -= number_of_enemies_to_assign

        class Game_board:
            def __init__(self) -> None:
                self.board = []

            def load_board_from_file(filename: str = Settings.Scoreboard.filename) -> list or bool:
                try:
                    result_board = []
                    file = open(filename,"rt",  encoding="utf8",)
                    board_lines = file.readlines()
                    for line in board_lines:
                        result_board.append(char for char in line)
                    file.close()
                    return result_board
                except:
                    print("Error: problem with opening file") 

            class coordinates: # class for manipulations for coordinations in board
                def __init__(self) -> None:
                    pass
    
        class Fight_board:
            def __init__(self) -> None:
                pass
    
        class Enemies: # enemies for current level
            def __init__(self) -> None:
                self.enemies = [] # list for current level enemies

##########
            class Enemy:
                def __init__(self) -> None:
                    self.attack
                    self.life
                    
                def attack() -> bool:
                    pass

                def kill() -> bool: # removes from enemies list
                    pass

                class Elfs:
                    def __init__(self) -> None:
                        self.icon = Settings.enemy.Elfs.icon
                        self.name = Settings.enemy.Elfs.name
                
                class Knights:
                    def __init__(self) -> None:
                        self.icon = Settings.enemy.Orcs.icon
                        self.name = Settings.enemy.Knights.name
                
                class Orcs:
                    def __init__(self) -> None:
                        self.icon = Settings.enemy.Orcs.icon
                        self.name = Settings.enemy.Orcs.name
                
                class DragonBoss:
                    # The boss is a larger (at least 5-by-5), autonomously moving character.
                    def __init__(self) -> None:
                        self.icon = Settings.enemy.DragonBoss.icon
                        self.name = Settings.enemy.DragonBoss.name

        class Items: # items player can collect to inventory
            class Healing_potions:
                number_of_vials = 0
                def __init__(self) -> None:
                    pass
                def add(self) -> None:
                    number_of_vials += 1
                
                def decrease(self) -> None:
                    number_of_vials -+ 1

                def get(self) -> int:
                    return number_of_vials

            class Weapon:
                def __init__(self) -> None:
                    pass
                class Dagger:
                    attack = Settings.Items.Weapon.Dagger.attack
                    icon = Settings.Items.Weapon.Dagger.icon
                    def __init__(self) -> None:
                        pass

                class Sword:
                    attack = Settings.Items.Weapon.Sword.attack
                    icon = Settings.Items.Weapon.Sword.icon
                    def __init__(self) -> None:
                        pass

                class Axe:
                    attack = Settings.Items.Weapon.Axe.attack
                    icon = Settings.Items.Weapon.Axe.icon
                    def __init__(self) -> None:
                        pass
                
            class Armour:
                def __init__(self) -> None:
                    pass

                class Leather_armour:
                    protection = Settings.Items.Armour.Leather_armour.protection
                    icon = Settings.Items.Armour.Leather_armour.icon
                    def __init__(self) -> None:
                        pass

                class Chainmail_armour:
                    protection = Settings.Items.Armour.Chainmail_armour.protection
                    icon = Settings.Items.Armour.Chainmail_armour.icon
                    def __init__(self) -> None:
                        pass

                class Plate_armour:
                    protection = Settings.Items.Armour.Plate_armour.protection
                    icon = Settings.Items.Armour.Plate_armour.icon
                    def __init__(self) -> None:
                        pass


            class Key_to_gateway_to_next_level: # after killing at least 3 enemies at given World, player get key for opening gate to another world 
                def __init__(self) -> None:
                    pass

            class Food: # 
                is_collectable = False # you can't store food in player's inventory
                def __init__(self) -> None:
                    pass

class Player:
    def __init__(self, name: str = Settings.Player.default_name, icon: str = Settings.Player.default_player_icon, max_health = Settings.Player.max_health, experience: int = Settings.Player.start_experience, dodge: int = Settings.Player.dodge) -> None:
        self.name = name
        self.icon = Settings.player.player_icon # player's icon representation while playing
        self.health = Settings.player.max_health # player's life
        self.effort_costs_for_walking = Settings.player.effort_costs_for_walking    

        self.experience = experience # player's attack is stronger with experience, increment by specified points each time enemy is killed
        self.dodge = dodge # player's chances to dodge enemy attack (important in a fight)
        
        self.attack = self.experience + self.equipped_weapon.attack
        

        self.equipped_weapon # player starts with no weapon
        self.equipped_armor # player starts with no armor
        self.inventory = Inventory()     

        self.inventory = Inventory()

        class Inventory: # To open anytime after pressing 'I' key
            def __init__(self) -> None:
                self.armors = []
                self.weapons = []
                self.healing_potions = []
                self.keys_to_pass_gateway = []


            def get_armor(self) -> bool:
                pass

            def put_armor(self) -> bool:
                pass

            def delete_armor(self) -> bool:
                pass


            def get_weapon(self) -> bool:
                pass

            def put_weapon(self) -> bool:
                pass

            def delete_weapon(self) -> bool:
                pass


            def get_healing_potion(self) -> bool:
                pass

            def put_healing_potion(self) -> bool:
                pass

            def delete_healing_potion(self) -> bool:
                pass

            def get_keys_to_gateway(self) -> bool:
                pass

            def put_keys_to_gateway(self) -> bool:
                pass

            def delete_keys_to_gateway(self) -> bool:
                pass


        def change_armor(self) -> None:
            pass

        def change_weapon(self) -> None: 
            pass

        def use_healing_potion(self) -> bool:
            pass

        def use_keys(self) -> bool:
            pass

            





            def show(self) -> list:
                pass

        def attack(self) -> bool:
            pass




class Rouglike: # Game's Roughlike logic
    def __init__(self) -> None:
        self.scoreboard = Scoreboard()
        self.Universe = Universe()
        self.interface = Interface()
        self.player = Player()
        self.enemies = [] # list of current enemies for player

    

    class Interface(): # subclass for showing boards and player's data
        def __init__(self) -> None:
            pass

        def play(self) -> None: # method for showing interface board - level game board + player's data
            pass

        def main_menu(self) -> None: # method for showing main menu
            pass
    
    


    
    


    
class Game: # Game's flow
    game_phases = game_phases = {'main_menu':0, 'play':1, 'scores':2, 'game_over':3, 'quit':4}
    def __init__(Rouglike_game: Rouglike) -> None:
        self.current_game_phase = Game.game_phases['main_menu']

        self.game_over = False # for game over to back to main menu
        self.quit_game = False # for quiting game to main menu
        self.exit_game = False # for exiting game from main menu

        self.game = Rouglike_game

    def play(self) -> None:
        while not self.exit_game:
            if self.current_game_phase == Game.game_phases['main_menu']:
                self.phase_main_menu()
            elif self.current_game_phase == Game.game_phases['play']:
                self.phase_play()
            elif self.current_game_phase == Game.game_phases['scores']:
                self.phase_scores()
            elif self.current_game_phase == Game.game_phases['game_over']:
                self.phase_game_over()                
            elif self.current_game_phase == Game.game_phases['quit']:
                self.phase_quit()


    def phase_main_menu(self) -> None:
        pass

    def phase_play(self) -> None:
        pass

    def phase_scores(self) -> None:
        pass

    def phase_game_over(self) -> None:
        pass

    def phase_quit(self) -> None:
        pass


    def change_phase(self, next_game_phase: str) -> None:
        if next_game_phase in Game.game_phases:
            self.current_game_phase = self.game_phases[next_game_phase]
            return True
        else:
            return False


            


class Scoreboard:
    def __init__(self) -> None:
        self.Scoreboard = [] # format: Player.name - Highest score

    def get_highest_score() -> list:
        pass

    def load_scores_from_file() -> bool:
        pass

    def save_scores_from_file() -> bool:
        pass

    def add_to_scoreboard() -> bool:
        pass

    def remove_to_scoreboard() -> bool:
        pass

    def sort_scoreboard() -> bool:
        pass

    def show_scoreboard() -> None:
        pass







    def play() -> None:
        is_running = True

        while is_running:
            engine.put_player_on_board(board, player)
            ui.display_board(board)

            key = util.key_pressed()
            if key == 'q':
                is_running = False
            else:
                pass
            util.clear_screen()


