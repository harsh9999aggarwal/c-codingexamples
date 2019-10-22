import pandas as pd
data =[1,2,3,4,5,6,7,8,9,10,12,13,14]
s=pd.Series(data)
print(s)
i=[1,2,4,6,8,10,1,1,1,1,1,1,1]
si=pd.Series(i,data)
print(si)
