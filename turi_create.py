import pandas
import turicreate as tc
import random


def turi_algoritmo():

    modelo = []


    return modelo





def main ():

    #cargamos dataset
    data_set = pandas.read_csv('dataset.csv')

    print(data_set)

    period = 1000
    init_model, model = [], []
    for i in range(3):

        init_model.append(random.random())

    model = init_model.copy()

    for i in range (period):
        model = algoritmo_option_2(data_set.values.tolist(), 0.1, model)

    print(model)

    for i in range(period):
        model = algoritmo_option_3(data_set.values.tolist(), 0.1, model)

    print(model)




if __name__ == '__main__':
    main()