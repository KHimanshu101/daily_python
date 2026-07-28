import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data={
    "Hours":[1,2,3,4,5,6,7,8],
    "Scores":[10,20,30,40,50,60,70,80]
}

df=pd.DataFrame(data)
print(df)
x=df[["Hours"]]
y=df["Scores"]

model=LinearRegression()
model.fir(x,y)

prediction=model.predict()
