import pandas as pd
marks=[95,90,75]
   
print(marks)

marsdf=pd.Series(marks,index=['English','Hindi','History'])

print(marsdf)

print(marsdf["English"])