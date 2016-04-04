#! /usr/bin/env python3

def nim(n):
    my_turn = True
    while n:
        if n <= 3:
            return my_turn
        elif n == 4:
            return not my_turn
        else:
            m = n % 4
            if m == 0:
                print("take {}".format(3))
                n -= 3
            else:
                print("take {}".format(m))
                n -= m
            my_turn = not my_turn


if __name__ == '__main__':
    print(nim(3))
    print(nim(4))
    print(nim(5))
    print(nim(10))
    print(nim(8))
