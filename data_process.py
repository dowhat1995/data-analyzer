import pandas as pd

df = pd.read_csv('train.csv', encoding='utf-8')

# 根据样本分布，大致定下的划分标准
unique_nums = 1000

def dataProcess(df):
    list_series = []
    list_cat = []
    # 遍历列并统计
    for name in df.keys():
        if pd.unique(df[name]).size > unique_nums:
            list_series.append(name)     
        else:
            list_cat.append(name)
    # 处理特殊值
    list_series.append("setupHour")
    list_cat.remove("setupHour")
    
    list_new_cols = list_series + list_cat
    # 换列
    # 连续值在前半部分，类别值在后半部分
    df = df.loc[:, list_new_cols]
    # 返回新的df，以及取值为连续值的列的个数
    return df,len(list_series)

data, n = dataProcess(df)

for name in data.keys():
    print(name, pd.unique(data[name]).size)

#print(data)
print(n)
