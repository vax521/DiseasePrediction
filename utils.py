import pandas as pd
import math


def findlist(df):
    """
       return list-like element in pd.DataFrame
    """
    return df.where(df.applymap(type).eq(list)).stack().tolist()


def reducer(x):
    """
        Use df.applymap(lambda x:Reducer(x)) to reduce list into an element in a df
    """
    if not isinstance(x, list):
        return x
    #########################
    # Customize your function here #
    #########################

    # example like:
    x = [e for e in x if e not in ["", " ", math.nan]]
    if not len(x):
        return math.nan
    elif len(set(x)) == 1:
        return x[0]
    return x
