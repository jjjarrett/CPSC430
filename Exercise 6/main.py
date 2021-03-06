from game_logic import GameLogic
from player_view import PlayerView

class Main:
    def __init__(self):
        self.instances = []
        # create instances
        self.game_logic = GameLogic()
        self.instances.append(self.game_logic)
        self.instances.append(PlayerView(self.game_logic))
    
    def go(self):
        self.game_logic.load_world("level_1.txt")
        
        while True:
            for instance in self.instances:
                instance.tick()
                
            if self.game_logic.get_property("quit"):
                break
            
    
if __name__ == '__main__':
    main = Main()
    main.go()