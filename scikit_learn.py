import pandas
import random

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model


def main ():

    #cargamos dataset
    data_set = pandas.read_csv('dataset.csv')
    print(data_set)



    x = data_set.drop('y', axis = 1)
    y = data_set['y']

    print(x,y)


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    LR = LinearRegression()
    #fitting the training data
    LR.fit(x_train, y_train)

    y_prediction = LR.predict(x_test)

    print(y_prediction)
    print(y_test)


    print('Pesos: ', LR.coef_)
    print('Sesgo: ', LR.intercept_)



if __name__ == '__main__':
    main()