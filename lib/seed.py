from models.athlete import Athlete
from models.race import Race


def reset_database():

    Athlete.drop_table()
    Race.drop_table()

    Athlete.create_table()
    Race.create_table()

reset_database()
race1 = Race.create('Half Marathon', 'run', 13.1)
race2 = Race.create('1,000 yard swim', 'swim', 0.57)
shane = Athlete.create('Shane', 32, 'M', race1.id)
sarah = Athlete.create('Sarah', 27, 'F', race2.id)
