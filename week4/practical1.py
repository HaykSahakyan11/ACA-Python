import pandas as pd

name = ["name1", "name2", "name3", "name4", "name5"]
surname = ["surname1", "surname2", "surname3", "surname4", "surname5"]
sex = ["men", "women", "women", "men", "men"]
status = ["student", "tutor", "student", "student", "student"]
age_group = ["20-30", "30-35", "20-30", "20-30", "20-30"]

columns = ["name", "surname", "sex", "status", "age_group"]

df = pd.DataFrame()


for col in columns:
    df[col] = locals().get("{}".format(col))

print(df)
