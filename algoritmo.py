from pyexpat import model

import pandas
import random
import math


def point_estimation(model, point):

    suma = 0.0

    print(model)
    print(point)

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


    print('¿Qué modelo quieres?: ')
    print('1. Modelo 2')
    print("2. Modelo 3")
    option_model = int(input())



    print("¿Qué tipo de regularización quieres?: ")
    print("1. L1")
    print("2. L2")
    option_regularization = int(input())

    print("¿Qué tipo de error quieres?")
    print("1. Error absoluto")
    print("2. Error cuadrático")
    print("3. Error absoluto medio")
    print("4. Error cuadratico medio")
    option_error = int(input())


    data_set = pandas.read_csv('dataset.csv')

    print(data_set)

    alpha = 1
    error_res = 0.0
    suma_L1, suma_L2 = 0.0, 0.0
    period = 1000
    init_model, model = [], []
    for i in range(3):

        init_model.append(random.random())

    model = init_model.copy()


    if(option_model == 1):
        for i in range(period):
            model = algoritmo_option_2(data_set.values.tolist(), 0.1, model)

    if(option_model == 2):
        for i in range(period):
            model = algoritmo_option_3(data_set.values.tolist(), 0.1, model)

    error_res, suma_L = 0.0, 0.0

    for data in data_set.values.tolist():
        #Switch segun tipo de error elegido

        if(option_error == 1):
            print(type(data))
            error_res += abs(point_estimation(model, data) - data[len(data) - 1])

        if(option_error == 2):
            error_res += math.pow(point_estimation(model, data) - data[len(data) - 1], 2)

    for j in range(len(model) - 1):
        if(option_regularization == 1):
            suma_L += abs(model[j])
            error_res += (alpha * suma_L)

        elif(option_regularization ==2):
            suma_L += math.pow(model[j], 2)
            error_res += (alpha * suma_L)

    print('Error: ', error_res)


if __name__ == '__main__':
    main()