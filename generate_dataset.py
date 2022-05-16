import pandas as pd
import random

total_size = 100_000

features = [
    "valve pressure",
    "leakage"
]

leakage = ["no", "small", "big"]

df = pd.DataFrame(columns=features)

no_valve_pressure = [ random.randint(0,100) for x in range(0, 40_000)]
small_valve_pressure = [ random.randint(100,200) for x in range(0, 30_000)]
big_valve_pressure = [ random.randint(200,300) for x in range(0, 30_000)]

leakage_values = no_valve_pressure + small_valve_pressure + big_valve_pressure

leakage_types = ['no' for x in range(0, 40_000)] + ['small' for x in range(0, 30_000)] + ['big' for x in range(0, 30_000)]

df['valve pressure'] = leakage_values
df['leakage'] = leakage_types


df.to_csv('leakage_dataset.csv', index=False)



