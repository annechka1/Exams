import random
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from pandas import DataFrame
import pandas

df=DataFrame(pandas.read_csv('/media/user/CED065ECD065DB6B/python_20 01/Exams/Exams_app/templates/iq.csv'),columns=['years_of_education','iq'])
years_of_education=df['years_of_education'][:,np.newaxis]
x_train,x_test,y_train,y_test=train_test_split(
    years_of_education,df['iq'],test_size=0.3
)
model=linear_model.LinearRegression()
model.fit(x_train,y_train)
print('w_1='+str(model.coef_[0])+'w_0='+str(model.intercept_))
print('iq='+str(model.coef_[0])+' * years_of_education+'+str(model.intercept_))
y_predicted=model.predict(x_test)
score=r2_score(y_test,y_predicted)
print("Tochnost:%s"%score)