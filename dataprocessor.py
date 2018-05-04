import numpy  as np
import pandas as pd

# 最大列长度512
pd.set_option("max_colwidth", 512)

data_part1 = pd.read_csv("../data/meinian_round1_data_part1_20180408.txt", sep="$")
data_part2 = pd.read_csv("../data/meinian_round1_data_part2_20180408.txt", sep='$')

# 将两个表拼接在一起
data = pd.concat([data_part1, data_part2], keys=['1', '2'])
print("data.shape={}".format(data.shape))

# 把table_id相同的体检项，全部保留;堆叠为同一行保存，以 “;” 分隔
data_keep_all = data.groupby(['vid', 'table_id'], as_index=False).apply(lambda x: ";".join(map(str, x['field_results'])))
data_keep_all = pd.DataFrame(data_keep_all, columns=['field_results'])
print("data_keep_all.shape={}".format(data_keep_all.shape))
# data_keep_all.to_csv("data_keep_all.csv")
# data.shape=(8104368, 3)

# 转换为行列格式
data_fmt_all = data_keep_all.unstack(fill_value=None)
data_fmt_all.columns = data_fmt_all.columns.droplevel(level=0)
print("data_fmt_all.shape=", data_fmt_all.shape)
# (57298, 2795) 共有2795个特征值

# 缺失值统计
null_count = data_fmt_all.isnull().sum()
print(len(null_count[null_count < 50000]))
# 256 缺失值少于50000的特征只有256个

# 去掉缺失值过多的数据
data_keep_50000 = data_fmt_all.drop(null_count[null_count > 50000].index, axis=1)
data_keep_50000.to_csv("../tmp/data_keep_50000.csv", encoding='UTF-8')


def get_Feature_info(i, df, n=20):
    """
      展示指定行、或者指定字段的信息：unique_list，null_count
      Params:
      ---------------
      i  : int or str : 特征索引或者名称
      n : 展示前n个属性
      df ： 指定的DataFrame

      e.g.:
      --------------
      getFeatureInfo(0, data_fmt_all)
      getFeatureInfo('0102', data_fmt_all)
    """
    if isinstance(i, int):
        col = df.columns[i]
        f = df.iloc[:, i]
    else:
        col = i
        f = df[i]
    f_u = pd.unique(f)
    print("Feature \t:\t", col)
    print("Types \t\t:\t", len(f_u))
    print("Null Count \t:\t", pd.isnull(f).sum())
    print("Value Counts :")
    print("---------------------")
    print(pd.value_counts(f).sort_values(ascending=False)[:n])

