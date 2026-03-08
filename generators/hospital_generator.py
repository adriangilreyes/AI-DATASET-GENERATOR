import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_hospital_dataset(rows):

    data = []

    hospital = ["Address","disease","doctor","area_hospital"]

    for _ in range(rows):

        data.append({
            "user_id": fake.uuid4(),
            "hospital": random.choice(hospital),
            "price":round(random.uniform(10,2000),2),
            "admission_day": fake.date_this_year(),
            "city":fake.city(),
            "areas_hospital":random.choice(["nursing","operating rooms","waiting room"]) 
        })
    return pd.DataFrame(data) 