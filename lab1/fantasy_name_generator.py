import random

def generate_name():
    first_parts = ["Ar", "El", "Im", "Or", "Ur"]
    last_parts = ["gorn", "driel", "born", "fion", "mir"]
    return random.choice(first_parts) + random.choice(last_parts)

def generate_title_name():
    titles = ["Lord", "Sir", "Magister", "Warrior", "Archmage", "Ranger", "Assassin", "Bard"] 
    name = generate_name()
    return random.choice(titles) + ' ' + name

def generate_race():
    races = ["Elf", "Dwarf", "Human", "Orc", "Tiefling", "Halfling", "Gnome", "Dragonborn"]
    return random.choice(races)

def generate_biography():
    origins = ["from the ancient forest", 
               "from the mystical mountains", 
               "from the vast sea", 
               "from the abandoned castle", 
               "from the forbidden woods",
               "from the crystal caves", 
               "from the icy tundra" 
    ]
    destinies = [
        "seeks the key to eternal life",
        "holds a secret that could change the world",
        "possesses forbidden magic",
        "is the last of their kind",
        "fights for a throne that is rightfully theirs",
        "can't stop singing in the shower"
    ]
    race = generate_race()
    title_name = generate_title_name()
    origin = random.choice(origins)
    destiny = random.choice(destinies)
    biography = f"{race} {title_name}, {origin}, {destiny}."
    return biography

def generate_characteristics():
    age = random.randint(18, 100)
    courses_taken = random.randint(1, 10)
    enemies_defeated = random.randint(0, 50)
    return age, courses_taken, enemies_defeated

def calculate_magic_power(age, courses_taken, enemies_defeated):
    return (age * courses_taken + enemies_defeated) / 10