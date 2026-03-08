from generators.ecommerce_generator import generate_ecommerce_dataset
from generators.hospital_generator import generate_hospital_dataset
from generators.banking_generator import generate_banking_dataset
from generators.social_media_generator import generate_social_media_dataset
import os

os.makedirs("datasets", exist_ok=True)

df_ecommerce = generate_ecommerce_dataset(1000)
df_ecommerce.to_csv("datasets/ecommerce.csv", index=False)

df_hospital = generate_hospital_dataset(1000)
df_hospital.to_csv("datasets/hospital.csv",index=False)


df_banking = generate_banking_dataset(1000)
df_banking.to_csv("dataset/banking.csv",index=False)

df_social_media = generate_social_media_dataset(1000)
df_social_media.to_csv("dataset/social_media.csv",index=False)

print('Datasets generados correctamente')