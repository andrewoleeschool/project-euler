# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import pandas as pd

df = pd.read_csv("../data/p022_names.txt", names=["name"], sep=" ", lineterminator=",", keep_default_na=False)
df = df.sort_values("name").reset_index(drop=True)

def nameScore(name: str) -> int:
    return sum(map(lambda c: ord(c) - 64, name))

df["nameScore"] = df.apply(lambda row: nameScore(row["name"]), axis=1)

df["score"] = df["nameScore"] * (df.index + 1)

print(sum(df["score"]))

# 871198282