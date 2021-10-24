# conditional_list_split

テキストファイルにある 0 から 9 のラベル付き学習データを任意のラベルで分割する

# qiita

https://qiita.com/seamcarving/items/a89eacbfe3c086beda67

# usage

python conditional_list_split.py --conditions 0,1,2 --datas sample.txt

# result sample

sample_target.txt
data1 0
data2 1
data3 2

sample_no_target.txt
data4 3
data5 4
data6 5
data7 6
data8 7
data9 8
data10 9
