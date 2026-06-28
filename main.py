
class Character():

    """"
    A class to serve as a reference for the other characters.
    """

    def __init__(self, name, hp, level):
        
        self.__name = name
        self.__hp = hp 
        self.__level = level

    def get_name(self):
        
        return self.__name
    
    def get_hp(self):

        return self.__hp
    
    def get_level(self):

        return self.__level
    
    def show_details(self):

        return f"Name: {self.get_name()}\nHp: {self.get_hp()}\nLevel: {self.get_level()}"
    



class Hero(Character):


    def __init__(self, name, hp, level, skill):
        super().__init__(name, hp, level)
        self.__skill = skill        


    def get_skill(self):
        return self.__skill
    
    def show_details(self):
        return super().show_details() + f"\n Skill: {self.get_skill()}"




class Enemy(Character):

    def __init__(self, name, hp, level, type):
        super().__init__(name, hp, level)
        self.__type = type

    def get_type(self):
        return self.__type
    
    def show_details(self):
        return super().show_details() + f"\n Type: {self.get_type()}"
    


class Game:

    def __init__(self):
        self.hero = Hero(name="Link", hp=200, level=5, skill="Spin Attack")
        self.enemy = Enemy(name="Octorok", hp=50, level=3, type="Red")

    def start_battle(self):

        print("Startin Battle")

        while self.hero.get_hp() > 0 and self.enemy.get_hp() > 0:

            print("\n Characters Datails")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("Press enter to attack...")

            chose = input(("Chose (1 - Normal Attack) (2 - Special Attack)"))



game = Game()
game.start_battle()