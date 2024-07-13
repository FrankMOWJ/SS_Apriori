import json
import csv


def process_groceries():
    with open('dataset/Groceries.json', mode='r', newline='') as file:
        data = json.load(file)

    with open('dataset/Groceries.txt', mode='w', newline='') as file:
        # 写入数据
        for key, value in data.items():
            value = value.replace('"', '')
            file.write(value+'\n')


def process_movie_len():
    # 输入和输出文件路径
    input_file = './dataset/movies.csv'
    output_file = './dataset/movies-small.txt'

    # 打开输入的CSV文件和输出的TXT文件
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            # 提取genres并替换分隔符
            genres = row['genres'].replace('|', ',')
            if genres == '(no genres listed)':
                continue
            # 写入输出文件
            outfile.write(genres + '\n')

    print("genres已提取并写入TXT文件")

def process_unix_usage():
    input_file = './dataset/unix_usage.csv'
    output_file = './dataset/unix_usage.txt'

    # 打开输入的CSV文件和输出的TXT文件
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        for idx, row in enumerate(reader):
            # 提取genres并替换分隔符
            # if idx < 5:
            #     print(','.join(list(eval(row['items']))))
            genres = ','.join(list(eval(row['items'])))
            # 写入输出文件
            outfile.write(genres + '\n')

if __name__ == '__main__':
    # process_movie_len()
    process_unix_usage()


