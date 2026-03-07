import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_hospital_dataset(rows):

    data = []

    hospital = ["Address","disease","doctor","area_hospital","city"]

    for _ in range(rows):

        data.append({
            "user_id": fake.uuid4(),
            "hospital": random.choice(hospital),
            "":
            "":
            "city":fake.city(), 
        })