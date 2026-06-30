class Person:
    def __init__(self, name, health, level, attack, take_damage, heal, level_up):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.take_damage = take_damage
        self.heal = heal
        self.level_up = level_up

    def show_info(self):
        return f"{self.name}, {self.health}, {self.level}, {self.attack}, {self.take_damage}, {self.heal}, {self.level_up}"

    def hero_attack(self):
        return f"{self.name} атакує та наносить {self.attack} шкоди"

    def hero_take_damage(self):
        self.health -= self.take_damage
        return f"{self.name} отримав {self.take_damage} шкоди. Здоров'я: {self.health}"

    def hero_heal(self):
        self.health += self.heal
        return f"{self.name} відновив {self.heal} хп. Здоровя: {self.health}"

    def hero_level_up(self):
        self.level += self.level_up
        return f"{self.name} підняв рівень до {self.level}"


hero = Person("Ivan", 500, 5, 25, 20, 15, 2)

print(hero.show_info())
print(hero.hero_attack())
print(hero.hero_take_damage())
print(hero.hero_heal())
print(hero.hero_level_up())