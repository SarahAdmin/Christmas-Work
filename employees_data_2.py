import pandas as pd 

data = {'Name':['Lee Cox','Lemon Jelly','Matt Bond','Pamela Adams','Alex Baxter'],'Position':['Computer Scientist','Finacial Analyst','Computer Scientist','Accountant','Journalist'],'Salary':[35000,50000,35000,65000,25000]} 

final_df = pd.DataFrame(data,index=[1,2,3,4,5])
df1 = final_df.where(final_df['Salary'] > 35000).dropna()

print(df1)
