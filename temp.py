
#
# clf.fit(X_train, y_train)
#         y_pred = clf.predict(X_test)
#         y_pred=np.ndarray.round(y_pred,3)#保留三位小数
#         y_test=pd.DataFrame(y_test,columns=['收缩压','舒张压','血清甘油三酯','血清高密度脂蛋白','血清低密度脂蛋白'])
#         y_pred_res=pd.DataFrame(y_pred,columns=['收缩压','舒张压','血清甘油三酯','血清高密度脂蛋白','血清低密度脂蛋白'])
#         calc_logloss(y_test,y_pred_res)