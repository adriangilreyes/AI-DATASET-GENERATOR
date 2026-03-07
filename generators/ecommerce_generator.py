import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_ecommerce_dataset(rows):

    data = []

    products = ["Laptop","Phone","Tablet","Camera"]

    for _ in range(rows):
        data.append({
        "user_id": fake.uuid4(),
        "product":random.choice(products),
        "price":round(random.uniform(10,2000), 2),
        "purchase_date": fake.date_this_year(),
        "country":fake.country(),
        "payment_method":random.choice(["credit_card","paypal","crypto"])
    })

    return pd.DataFrame(data)

