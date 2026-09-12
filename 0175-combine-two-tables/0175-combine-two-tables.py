import pandas as pd
#dynamowalker9
def combine_two_tables(person,address):
    result_df=pd.merge(person,address,on='personId',how='left')
    result=result_df[['firstName','lastName','city','state']]
    return(result)
