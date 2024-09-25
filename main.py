from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def attack(self,enemy):
        pass
    @abstractmethod
    def is_alive(self):
        pass

class Hero(Person):
    def __init__(self,name,attack_power):
        self.name = name
        self.power = attack_power
        self.health = 100

    def attack(self,enemy):
        enemy.health -= self.power
        print(f"{self.name} атакует. У {enemy.name} осталось {enemy.health}% здоровья.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game:
    def __init__(self,hero,enemy):
        self.hero = hero
        self.enemy = enemy
    def start(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            self.hero.attack(self.enemy)
            if not self.enemy.is_alive():
                break
            self.enemy.attack(self.hero)
            if not self.hero.is_alive():
                break
        if self.hero.is_alive():
            print(f"{self.hero.name} победил")
        else:
            print(f"{self.enemy.name} победил")

hero = Hero("Герой",10)
enemy = Hero("Компьютер",10)
game = Game(hero,enemy)
game.start()