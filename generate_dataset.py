import pandas as pd
import random

total_size = 100_000

features = [
    "valve pressure",
    "leakage"
]

leakage = ["no", "small", "big"]

df = pd.DataFrame(columns=features)

df['valve pressure'] = [ random.randint(0,100) for x in range(0, 33_000)]+[ random.randint(100, 250) for x in range(0, 33_000)]+[ random.randint(250, 1000) for x in range(0, 34_000)]
df["leakage"] = ["no" for i in range(0, 33_000)] + ["small" for i in range(0, 33_000)] + ["big" for i in range(0, 34_000)]

df.to_csv('leakage_dataset.csv', index=False)



