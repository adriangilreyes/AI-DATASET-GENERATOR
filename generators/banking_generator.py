import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

def generate_banking_dataset(rows):

    data = []

    bank = ["money","salary","ATM","bank_branch"]

    for _ in range(rows):
        data.append({
            "user_id":fake.uuid4(),
            "banking":random.choice(bank),
            "money":round(random.uniform(10,2000),2),
            "take_money":fake.date_this_year(),
            "country":fake.country(),
            "payment_method":random.choice(["debit card","paypal","bizum"])
        })
    return pd.DataFrame(data) 