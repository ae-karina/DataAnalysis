import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": np.arange(10),
    "name": ["a", "b"] * 5,
    "a": [f"a{i}" for i in range(10)],
    "b": [f"b{i}" for i in range(10)],
    "aa": [f"aa{i}" for i in range(10)],
    "bb": [f"bb{i}" for i in range(10)],
    "aaa": [f"aaa{i}" for i in range(10)],
    "bbb": [f"bbb{i}" for i in range(10)]
})


def merge_cols(x):
    y = x.values
    result = []
    for idx in range(0, len(y), 2):
        result.append(f"{y[idx]},{y[idx + 1]}")
    return "#".join(result)


df["merge"] = df.loc[:, "a":"bbb"].apply(merge_cols, axis=1)
drop_names = list(df.loc[:, "a":"bbb"].columns.values)
df.drop(drop_names, axis=1, inplace=True)
df["merge"] = df["merge"].str.split("#")
df.explode("merge")
df_explode = df.explode("merge")

df_explode["a"] = df_explode["merge"].str.split(",").str[0]
df_explode["b"] = df_explode["merge"].str.split(",").str[1]

print(df_explode.drop("merge", axis=1))
