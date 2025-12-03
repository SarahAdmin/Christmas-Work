import pandas as pd
data = {'Name':['Lee Cox','Matt Bond','Lemon Jelly','Pamela Green','Jonah Parker','Zoe Baxter'],"Position":['Seasonal Sales Assistant','Seasonal Sales Assistant','Manager','E-Commerce Assistant','Marketing Assistant',
                                                                                                           'Assistant Manager'],"Salary":[8000,8000,60000,20000,35000,55000]}
ChristmasEmployees = pd.DataFrame(data,index=[1,2,3,4,5,6]) 
print(ChristmasEmployees.to_string())
