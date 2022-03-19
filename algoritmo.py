from pyexpat import model

import pandas
import random


def point_estimation(model, point):

    suma = 0.0

    for i in range(len(model) - 1):
        suma += model[i] * point[i]

    suma += model[len(model) -1 ]

    return suma



def algoritmo_option_2 (data_set, learning_rate, init_model):


    aux_model = init_model.copy()
    average_model = 1/len(data_set)

    for data in data_set:

        error_diff = data[2] - point_estimation(init_model, data)
        #m' = m + nr(p-p^)
        for i in range(2):
            aux_model[i] += (learning_rate * data[i]*error_diff * average_model)
            #print(aux_model[i])
        #b' =
        aux_model[len(aux_model)-1] += (learning_rate * error_diff * average_model)





    return aux_model


def algoritmo_option_3 (data_set, learning_rate, init_model):

    aux_model = init_model.copy()
    average_model = 1/len(data_set)

    for data in data_set:
            #p > ^p
        if data[2] > point_estimation(init_model, data):
            for i in range(2):
                aux_model[i] += (learning_rate * data[i] * average_model)

            aux_model[len(aux_model)-1] += learning_rate * average_model

            #p < ^p
        elif data[2] < point_estimation(init_model, data):
            for i in range(2):
                aux_model[i] -= (learning_rate * data[i] * average_model)

            aux_model[len(aux_model)-1] -= learning_rate * average_model

    return aux_model

def main ():

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