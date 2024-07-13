import pandas as pd
import matplotlib.pyplot as plt

# 数据
data = {
    "min-Sup": [0.01, 0.05, 0.1, 0.15, 0.2],
    "Apriori_Movie_Len": [0, 0, 0, 0, 0],
    "Apriori_Groceries": [0, 0, 0, 0, 0],
    "Apriori_UNUX_usage": [0, 0, 0, 0, 0],
    "SS1_Apriori_Movie_Len": [22050, 22050, 22050, 22050, 22050],
    "SS1_Apriori_Groceries": [69731, 69732, 69733, 69734, 69735],
    "SS1_Apriori_UNUX_usage": [65941, 65941, 65941, 65941, 65941],
    "SS2_Apriori_Movie_Len": [19941, 17698, 12237, 5676, 1013],
    "SS2_Apriori_Groceries": [330750, 189606, 68608, 29504, 8209],
    "SS2_Apriori_UNUX_usage": [7813365, 673080, 220792, 169051, 140775]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 绘图
plt.figure(figsize=(14, 10))

# Apriori
# plt.plot(df["min-Sup"], df["Apriori_Movie_Len"], label='Apriori Movie_Len', marker='o')
# plt.plot(df["min-Sup"], df["Apriori_Groceries"], label='Apriori Groceries', marker='o')
plt.plot(df["min-Sup"], df["Apriori_UNUX_usage"], label='Apriori UNIX_usage', marker='o')

# SS1-Apriori
# plt.plot(df["min-Sup"], df["SS1_Apriori_Movie_Len"], label='SS1-Apriori Movie_Len', marker='s')
# plt.plot(df["min-Sup"], df["SS1_Apriori_Groceries"], label='SS1-Apriori Groceries', marker='s')
plt.plot(df["min-Sup"], df["SS1_Apriori_UNUX_usage"], label='SS1-Apriori UNIX_usage', marker='s')

# SS2-Apriori
plt.plot(df["min-Sup"], df["SS2_Apriori_Movie_Len"], label='SS2-Apriori Movie_Len', marker='^')
plt.plot(df["min-Sup"], df["SS2_Apriori_Groceries"], label='SS2-Apriori Groceries', marker='^')
plt.plot(df["min-Sup"], df["SS2_Apriori_UNUX_usage"], label='SS2-Apriori UNIX_usage', marker='^')

plt.xlabel('min-Sup')
plt.ylabel('Scan Count')
plt.title('Comparison of Scan Counts for Apriori, SS1-Apriori, and SS2-Apriori')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()
