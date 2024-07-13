import pandas as pd
import matplotlib.pyplot as plt

# 数据
data = {
    "min-Sup": [0.01, 0.05, 0.1, 0.15, 0.2, 0.3],
    "SS1_Apriori_Movie_Len": [21963, 20482, 17855, 13435, 8117, 8117],
    "SS1_Apriori_Groceries": [66369, 51104, 31685, 21377, 10887, 2952],
    "SS1_Apriori_UNUX_usage": [53785, 37995, 25925, 24810, 23370, 12353],
    "SS2_Apriori_Movie_Len": [19941, 17698, 12237, 5676, 1013, 1013],
    "SS2_Apriori_Groceries": [330750, 189606, 68608, 29504, 8209, 502],
    "SS2_Apriori_UNUX_usage": [7813365, 673080, 220792, 169051, 140775, 8743]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 绘制子图
fig, axs = plt.subplots(1, 3, figsize=(16, 5.5))

# SS-Apriori-L1 vs SS2-Apriori-L2 for Movie_Len
axs[0].plot(df["min-Sup"], df["SS1_Apriori_Movie_Len"], label='SS-Apriori-L1', marker='s')
axs[0].plot(df["min-Sup"], df["SS2_Apriori_Movie_Len"], label='SS-Apriori-L2', marker='^')
axs[0].set_xlabel('min Support')
axs[0].set_ylabel('Addition Memory Usage')
axs[0].set_title('Comparison of Addition Memory Usage for Movie_Len')
axs[0].set_yscale('log')
axs[0].legend()
axs[0].grid(True)

# SS-Apriori-L1 vs SS2-Apriori-L2 for Groceries
axs[1].plot(df["min-Sup"], df["SS1_Apriori_Groceries"], label='SS-Apriori-L1', marker='s')
axs[1].plot(df["min-Sup"], df["SS2_Apriori_Groceries"], label='SS-Apriori-L2', marker='^')
axs[1].set_xlabel('min Support')
axs[1].set_ylabel('Addition Memory Usage')
axs[1].set_title('Comparison of Addition Memory Usage for Groceries')
axs[1].set_yscale('log')
axs[1].legend()
axs[1].grid(True)

# SS-Apriori-L1 vs SS2-Apriori-L2 for UNIX_usage
axs[2].plot(df["min-Sup"], df["SS1_Apriori_UNUX_usage"], label='SS-Apriori-L1', marker='s')
axs[2].plot(df["min-Sup"], df["SS2_Apriori_UNUX_usage"], label='SS-Apriori-L2', marker='^')
axs[2].set_xlabel('min Support')
axs[2].set_ylabel('Addition Memory Usage')
axs[2].set_title('Comparison of Addition Memory Usage for UNIX_usage')
axs[2].set_yscale('log')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
