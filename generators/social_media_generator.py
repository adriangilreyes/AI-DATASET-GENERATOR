import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

def generate_social_media_dataset(rows):

    data = []

    sm = ["web 2.0","TV","Internet","networking"]

    for _ in range(rows):
        data.append({
            "user_id":fake.uuid4(),
            "sm":random.choice(sm),
            "price":round(random.uniform(10,2000),2),
            "date":fake.date_this_month(),
            "country":fake.country(),
            "social media":random.choice(["TV","Tablet","Internet","public"])
        })
    return pd.DataFrame(data)

