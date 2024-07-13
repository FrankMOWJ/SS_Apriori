import matplotlib.pyplot as plt

x = [0.01, 0.05, 0.10, 0.15, 0.20]

Groceries_t_Apri = [3.622, 0.962, 0.606, 0.538]
Groceries_t_SS= [0.685, 0.260, 0.166, 0.142]

Groceries_num_Apri = [477390900, 15755670, 3747135, 2360400, 1976835]
Groceries_num_SS = [29077735, 1301065, 320078, 152433, 85364]

movie_t_Apri = [0.224, 0.121, 0.085, 0.072]
movie_t_SS = [0.071, 0.052, 0.048, 0.040]

movie_num_Apri = [4145316, 1067880, 533940, 281532, 194160]
movie_num_SS = [317282, 115762, 69655, 41462, 25806]


# plot
def plot_t(y1, y2):
    plt.scatter(x, y1, label='Apriori')
    plt.scatter(x, y2, label='SS-Apriori')
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.xticks(x)
    plt.ylabel('Time (seconds)')
    plt.xlabel('Support')
    plt.legend()
    plt.show()

def plot_num(y1, y2):
    plt.scatter(x, y1, label='Apriori')
    plt.scatter(x, y2, label='SS-Apriori')
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.xticks(x)
    plt.ylabel('Times of scan of Transactions')
    plt.xlabel('Support')
    plt.legend()
    plt.show()

def display_unix():
    import pandas as pd

    # 数据
    data1 = {
        'Support': [0.01, 0.05, 0.1, 0.15, 0.2],
        'Apriri': [177.34, 6.488, 4.841, 4.707, 4.148],
        'SS1-Apriori': [18.28, 0.569, 0.225, 0.171, 0.144],
        'SS2-Apriori': [10.83, 0.465, 0.216, 0.174, 0.146]
    }

    data2 = {
        'Support': [0.01, 0.05, 0.1, 0.15, 0.2],
        'Apriri': [867603100, 33251400, 22595300, 21940100, 21694400],
        'SS1-Apriori': [31395227, 1223687, 304813, 194548, 146950],
        'SS2-Apriori': [7813365, 673080, 220792, 169051, 140775]
    }

    data3 = {
        'Support': [0.01, 0.05, 0.1, 0.15, 0.2],
        'Apriri': [0, 0, 0, 0, 0],
        'SS1-Apriori': [65941, 65941, 65941, 65941, 65941],
        'SS2-Apriori': [261588, 109255, 44815, 39839, 33351]
    }

    # 创建 DataFrame
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)

    # 创建图形和子图
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 10))

    # 绘制第一个图
    ax1.plot(df1['Support'], df1['Apriri'], marker='o', label='Apriri')
    ax1.plot(df1['Support'], df1['SS1-Apriori'], marker='o', label='SS1-Apriori')
    ax1.plot(df1['Support'], df1['SS2-Apriori'], marker='o', label='SS2-Apriori')
    ax1.set_title('Time vs Support')
    ax1.set_xlabel('Support')
    ax1.set_ylabel('Time (s)')
    ax1.legend()

    # 绘制第二个图
    ax2.plot(df2['Support'], df2['Apriri'], marker='o', label='Apriri')
    ax2.plot(df2['Support'], df2['SS1-Apriori'], marker='o', label='SS1-Apriori')
    ax2.plot(df2['Support'], df2['SS2-Apriori'], marker='o', label='SS2-Apriori')
    ax2.set_title('Number of Scans vs Support')
    ax2.set_xlabel('Support')
    ax2.set_ylabel('Number of Scans')
    ax2.legend()

    # 绘制第三个图
    ax3.plot(df3['Support'], df3['Apriri'], marker='o', label='Apriri')
    ax3.plot(df3['Support'], df3['SS1-Apriori'], marker='o', label='SS1-Apriori')
    ax3.plot(df3['Support'], df3['SS2-Apriori'], marker='o', label='SS2-Apriori')
    ax3.set_title('Space vs Support')
    ax3.set_xlabel('Support')
    ax3.set_ylabel('Space')
    ax3.legend()

    # 显示图形
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # plot_t(Groceries_t_Apri, Groceries_t_SS)
    # plot_t(movie_t_Apri, movie_t_SS)
    plot_num(Groceries_num_Apri, Groceries_num_SS)
    plot_num(movie_num_Apri, movie_num_SS)

    # display_unix()