import names
import random


from database import session
from database.models import *


rand_departments = [
    "Dark Ancients",
    "Moonshifters",
    "Justice of Skulls",
    "Howl of the Claw",
    "Killers of the Stag",
    "Weapons of Promises",
    "Squad of Shame",
    "Wind Dragons",
    "Fighters of the Mislead",
    "Storm Rage"
]
rand_animes = [
    "Attack On Titan",
    "Naruto",
    "One Piece",
    "Death Note",
    "Bleach",
    "Tokyo Ghoul",
    "Dragon Ball",
    "One Punch Man",
    "Banana Fish"
]
fuhrer = Soldier(name="Kochavi our Lord & Savior", department="IDF")
army = Department(name="IDF")#, king="Kochavi our Lord & Savior")

rand_names = [names.get_full_name() for i in range(100)]
soldiers = []
departments = []

for i in range(100):
    if i < 10:
        commander = "Kochavi our Lord & Savior"
        department = rand_departments[i]

        departments.append(Department(
            name=department
        ))

    else:
        num = random.randint(0, 9)
        commander = rand_names[num]
        department = rand_departments[num]

    slave = Soldier(
        name=rand_names[i],
        department=department,
        commander=commander,
        favorite_anime=rand_animes[random.randint(0, len(rand_animes)-1)]
    )
    soldiers.append(slave)

# There is a need to fix the relationships so that two dependent foreign keys can be entered together!
# Need to fix

session.add(army)
session.commit()
session.add(fuhrer)
session.add_all(departments)
session.commit()
session.add_all(soldiers)
session.commit()
