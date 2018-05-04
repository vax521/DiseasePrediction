import pandas as pd
import time

# 读取数据并拼接在一起
part_1 = pd.read_csv('./data/meinian_round1_data_part1_20180408.txt', sep='$')
part_2 = pd.read_csv('./data/meinian_round1_data_part2_20180408.txt', sep='$')
alldata = pd.concat([part_1, part_2])
alldata = pd.DataFrame(alldata).sort_values('vid').reset_index(drop=True)
print(alldata[:5])
print("*"*20)
begin_time = time.time()

# 重复数据的拼接
def merge_table(df):
    df['field_results'] = df['field_results'].astype(str)
    if df.shape[0]<1:
        merge_df = " ".join(list(df['filed_results']))
    else:
        merge_df = df['field_results'].values[0]
    return merge_df


# groupdata = alldata.groupby(['vid', 'table_id']).size()
# print(groupdata[:5])
# print("*"*20)

index_grouped = alldata.groupby(['vid', 'table_id']).size().reset_index()
print(index_grouped[:5])
print("*"*20)

# 重塑index以去重
index_grouped['new_index'] = index_grouped['vid']+'_'+index_grouped['table_id']
# print("data_grouped[0]", index_grouped[0])
index_grouped_new = index_grouped[index_grouped[0] > 1]['new_index']
print(index_grouped_new[:4])

alldata['new_index'] = alldata['vid']+'_'+alldata['table_id']
part_unique_data = alldata[alldata['new_index'].isin(list(index_grouped_new))]
part_unique_data = part_unique_data.sort_values(['vid', 'table_id'])
part_not_unique_data = alldata[~alldata['new_index'].isin(list(index_grouped_new))]
print("begin...")
alldata_not_unique = part_not_unique_data.groupby(['vid', 'table_id']).apply(merge_table()).reset_index()
alldata_not_unique = alldata_not_unique.rename(columns={0: 'field_results'}, inplace=True)

# 行列转换
final_data = pd.concat([alldata_not_unique, part_not_unique_data[['vid', 'table_id', 'field_results']]])
final_data = final_data.pivot(index='vid', values='field_results', columns='table_id')
final_data.to_csv('./tmp/finaldata.csv')
print("Finish...")
print(final_data.shape)
print("total time:", time.time()-begin_time)

