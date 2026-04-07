import random
import logging
import os
if os.path.exists("Battle_Simulator.log"):
    os.remove("Battle_Simulator.log")
logger = logging.getLogger(__name__)
logging.basicConfig(filename = "Battle_Simulator.log",level = logging.INFO, format = "%(asctime)s,%(message)s",datefmt= "%m/%d/%Y %I:%M:%S %p")

class game_manager:
    """Class(game_manager): Controls players and attack redirection
    Methods:
    __init__: Initialises variables
    new_player(name,ID): Adds player onto player list
    play: Checks for existing players
    damage(target,target_ID,hit): Redirects player hits onto target
    """
    def __init__(self):
        """Initialises variables and roles"""
        self.roles = {"Knight":[{'Horsey':-30},{"Slashrun":-20}, {"Bloodloath":-35}, {"Warcry":-50}],
                        "Swordsman":[{"Lion stance":-25}, {"Three-Sword Style":-35}, {"Slash":-20}, {"Fire Sword Style":-50}],
                        "Doctor":[{"Heal":+10},{"Plague":-30},{"Dissect":-10},{"X-ray":-20}],
                        "Cowboy":[{"Duel":-30},{"Dodge":0},{"Gamble":-50},{"Gang-Bang":-20}]}
        self.players = {} 
        logger.info("Game_Manager is RUNNING")

    def new_player(self,name,ID):
        """Adds player onto the dictionary along with their IDs"""
        logger.info(f"{name} has joined")
        self.players[name] = ID
        return random.choice(list(self.roles.items()))
    
    def play(self):
        """Checks for existing players once called"""
        while len(self.players) > 1: 
            for name,ID in list(self.players.items()):
                if name in self.players.keys():
                    print("NEW GAME HAS STARTED..")
                    ID.attack()
        print(f"{list(self.players.keys())[0]} have won the game")

    def damage(self,target,target_ID,hit):
        """Redirect player attack onto target using their target_ID and with a value of hit"""
        logger.info(f"{target} has been targetted")
        state = ""

        if hit > 0:
            state = "healed"
        elif hit< 0:
            state = "hit"
        else:
            state = "dodged"

        if target_ID.HP == 100 and state == "healed":
            return "Heal cancelled, exceeds 100"
            
        if state == "dodged":
            return target + " have " + state + " the attack"
        else:
            target_ID.HP += hit
            print(f"{target} have been {state} by {hit}")

        if target_ID.HP <= 0:
            logger.info(f"{target} is down")
            print(f"{target} have died")
            del self.players[target]
            
#-----------------------------------------------------------------------------------------------------------------------
class player:
    """class(player): Controls player movements and attacks
    Methods:
    __init__: Initialises player variables
    attack: Randomnly chooses attack and choose target"""
    def __init__(self, player_name, engine):
        """Initialises player variables and connects with class(game_manager)"""
        logger.info(f"player class is running - NAME - {player_name}")
        self.HP = 100
        self.name = player_name
        self.engine = engine
        self.role, self.attacks = self.engine.new_player(player_name,self)
        print(f"NEW PLAYER JOINED SUCCESSFULLY \nWelcome {player_name}, You've got the role of '{self.role}' and your attacks would be -\n {self.attacks}")

    def attack(self):# Attacking
        """Randomnly chooses player attacks and target all being accessed from existing players"""
        if self.name not in self.engine.players.keys():
            return
        logger.info(f"{self.name} is attacking")
        attack_dict = random.choice(self.attacks)
        self.move,self.hit = list(attack_dict.items())[0]
        print(f"It is {self.name}'s chance")
        print(f"{self.name} is choosing their attack")

        self.target,self.target_ID = random.choice(list(self.engine.players.items()))
        while self.target == self.name :
            self.target,self.target_ID = random.choice(list(self.engine.players.items()))

        print(f"The player have choosen to attack {self.target} with {self.move}")
        self.engine.damage(self.target,self.target_ID,self.hit)
#----------------------------------------------------------------------------------------------------------------------- 
logger.info("------------NEW GAME-----------------")
game = game_manager()
P1 = player("Christina",game)
P2 = player("Robert",game)
P3 = player("Marco",game)
P4 = player("Luffy",game)

game.play()

with open("Battle_Simulator.log","r") as f:
   print(f.read())