import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv(r'C:\Users\User\Desktop\датасет-1.csv',sep=';')

print(df) 
print(df.dtypes)
df['price']=df['price'].str.replace(',','.')
df['price']=df['price'].astype(float)
plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.show()
reg = LinearRegression()
reg.fit(df[['area']],df.price)
print(reg.predict([[38]]))
print(reg.predict(df[['area']]))
print(reg.coef_) # a
print(reg.intercept_) # b
plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))
plt.show()
pred=pd.read_csv(r'C:\Users\User\Desktop\prediction_price.csv',sep=';')
p = reg.predict(pred)
pred['predicted prices'] = p
print(pred)
pred.to_excel('new.xlsx', index=False)
