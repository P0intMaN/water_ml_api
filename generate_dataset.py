import pandas as pd
import random

total_size = 100_000

features = [
    "valve pressure",
    "leakage"
]

leakage = ["no", "small", "big"]

df = pd.DataFrame(columns=features)

df['valve pressure'] = [ random.randint(0,400) for x in range(0, 100_000)]

df['leakage'] = random.choices(
    leakage,
    weights=(67,20,12),
    k=total_size
)

df.to_csv('leakage_dataset.csv', index=False)
# print(df.head())
