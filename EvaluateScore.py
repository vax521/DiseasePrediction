from math import log1p, pow

# 计算评估分数的方法，传入两个Dataframe，带有头部列名，五列[]

def calc_logloss(true_df,pred_df):
    loss_sum = 0
    rows = true_df.shape[0]
    for c in true_df.columns:
        true_df[c] = true_df[c].apply(lambda x: log1p(x))  # 预测结果必须要>0,否则log函数会报错，导致最终提交结果没有分数
        pred_df[c] = pred_df[c].apply(lambda x: log1p(x))
        true_df[c+'new'] = pred_df[c]-true_df[c]
        true_df[c+'new'] = true_df[c+'new'].apply(lambda x: pow(x, 2))
        loss_item = (true_df[c+'new'].sum())/rows
        loss_sum += loss_item
        print("%s的loss:%f" % (c, loss_item))
    print('五项指标平均loss分数', loss_sum/5)
