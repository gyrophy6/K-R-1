def task1():
    # TODO: первое задание
    a = int(input())
    b = int(input())
    print((a + b) ** 2)

def task2():
    # TODO: второе задание
    s = input()
    a = len(s)
    b = len([i for i in s if i.isdigit()])
    c = len([i for i in s if i.isalpha()])
    d = a - (b + c)
    print(d)

def task3():
    # TODO: третье задание
    b = str()
    s = input()
    for w in s.split():
        if (w.startswith("ab") and w.endswith("ba")):
            b += w + ' '
    print(len(b.split()))

def task4(generator):
    # TODO: четвертое задание
    a = (filter(lambda x: x.contains('sus'), generator))
    return a

def task5(list_of_smth):
    # TODO:
    a = list_of_smth[0:-2:1]
    answer = a[::1]
    return answer

def task6(list1, list2, list3, list4):
    # TODO: пятое задание
    answer = []
    E = list1 + list2
    F = list3 + list4
    for i in E:
        for j in F:
            if i == j:
                answer.append(i)

    print(answer)

def task7():
    # TODO: ...
    import numpy as np
    A = np.random.randint(0, 65, (8, 8))
    print(A)

def task8(f, min_x, max_x, N, min_y, max_y):
    # TODO: ...
    import numpy as np
    import matplotlib.pyplot as plt
    from sympy import *
    max_x = 11
    min_x = -11
    N = 5
    x = np.linspace(min_x, max_x, int((max_x - min_x) / (N - 1)))
    y = x ** 3
    plt.plot(x, y, '--b', label='Синяя штрихованная линия')

    plt.xscale('log', base=2.72)
    plt.grid(visible=True, which='major', axis='both', alpha=1)
    plt.grid(visible=True, which='minor', axis='both', alpha=0.5)
    plt.show()

    plt.plot(x, (diff(y) / diff(x)), '--r')

    plt.show()

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
dict = {"n_games": df.shape[0]}
