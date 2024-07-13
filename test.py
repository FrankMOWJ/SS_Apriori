import pandas as pd
# 设置pandas输出表格的属性
pd.options.display.max_colwidth = 100
pd.options.display.width = 500
from mlxtend.frequent_patterns import apriori, association_rules

movies = pd.read_csv("./dataset/movies.csv")

movies_standard = movies.drop('genres', axis=1).join(movies.genres.str.get_dummies())
# 一共包含 9742 部电影，一共有20种不同的电影类型（有2列是ID和电影名）
print(movies_standard.shape)  # (9742, 22)

movies_standard.set_index(['movieId', 'title'], inplace=True)
frequent_item_sets = apriori(movies_standard, min_support=0.05, use_colnames=True)
print(frequent_item_sets)
