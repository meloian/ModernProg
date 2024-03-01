import random

def generate_name():
    first_parts = ["Ар", "Ель", "Им", "Ор", "Ур"]
    last_parts = ["горн", "дриель", "борн", "фион", "мир"]
    return random.choice(first_parts) + random.choice(last_parts)   