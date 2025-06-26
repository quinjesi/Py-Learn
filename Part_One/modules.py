import converty
import random
from pathlib import Path

print(converty.kg_to_lbs(45))
print(converty.lbs_to_kg(100))

for i in range(3):
    print(random.randint(10, 20))

members = ['Alice', 'Bob', 'Charlie']
print(random.choice(members))


class Dice:
    
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    
dice = Dice()
print(dice.roll())


path = Path()
for file in path.glob('*'):
    print(file)

