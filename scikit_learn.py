import pandas
import random

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model


def turi_algoritmo():

    modelo = []


    return modelo





def main ():

    #cargamos dataset
    data_set = pandas.read_csv('dataset.csv')

    x = data_set.drop('y', axis = 1)
    y = ['y']


    print(data_set)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    LR = LinearRegression()
    # fitting the training data
    LR.fit(x_train, y_train)

    y_prediction = LR.predict(x_test)
    print(y_prediction)

    period = 1000
    init_model, model = [], []
    for i in range(3):

        init_model.append(random.random())

    model = init_model.copy()




if __name__ == '__main__':
    main()