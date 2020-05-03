import numpy as np


def arr_replace(array):
    array[array % 2 == 1] = 0
    return array
    # return np.where(array % 2 == 1, 0, array)


def arr_replace_where(array):
    return np.where(array % 2 == 0, 0, array)


def arr_repeat(array):
    return np.repeat(array, 3, )


def arr_join(array):
    return np.concatenate(([array] * 3))


def arr_intersection(arr1, arr2):
    return np.intersect1d(arr1, arr2)


def arr_random(a_tuple):
    return np.random.uniform(5, 10, size=(a_tuple[0], a_tuple[1]))
