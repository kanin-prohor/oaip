class Hero:   
    def __init__(self, name: str, health: int = 100, attack_power: int = 20) -> None:
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def strike(self, target: 'Hero') -> None:
        target.health -= self.attack_power

if __name__ == "__main__":
    hero1 = Hero("Алекс", health=100, attack_power=25)
    hero2 = Hero("Борис", health=90, attack_power=30)
    print(f"До битвы: {hero1.name}: {hero1.health} HP, {hero2.name}: {hero2.health} HP")
    hero1.strike(hero2)
    hero2.strike(hero1)
    print(f"После битвы: {hero1.name}: {hero1.health} HP, {hero2.name}: {hero2.health} HP")