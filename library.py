def fibonnachi(N):
    if (N<0):
        raise ValueError("Неверно введенный формат данных. N не может быть отрицательным")
    elif (N==0):
        return [0]
    X = ([0, 1])
    for i in range (2, N):
        X.append(X[i - 2] + X[i - 1])
    return X

def bubble_sort(mas):
    for i in range(0, len(mas) - 1):
        for j in range(0, len(mas) - 1):
            if(mas[j] > mas[j+1]):
                temp = mas[j]
                mas[j] = mas[j+1]
                mas[j+1] = temp
    return mas

def calculate(a, b, func):
    if(func == "+"):
        return a + b
    elif (func == "-"):
        return a - b
    elif (func == "/"):
        if ( b == 0 ): raise ZeroDivisionError
        return a/b
    elif (func == "*"):
        return a*b
    else: raise ValueError("Неверно введен формат данных")