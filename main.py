from generators.ecommerce_generator import generate_ecommerce_dataset

df = generate_ecommerce_dataset(1000)
df.to_csv("datasets/ecommerce.csv", index=False)

