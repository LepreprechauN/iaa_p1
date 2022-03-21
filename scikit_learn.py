import pandas
import random

from sklearn import datasets, linear_model


def turi_algoritmo():

    modelo = []


    return modelo





def main ():

    #cargamos dataset
    data_set = pandas.read_csv('dataset.csv')
    boston = datasets.load_boston()
    print(boston)

    print(data_set)

    period = 1000
    init_model, model = [], []
    for i in range(3):

        init_model.append(random.random())

    model = init_model.copy()




if __name__ == '__main__':
    main()