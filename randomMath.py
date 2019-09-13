#cerner_2^5_2019
#Mason Seeger submission 1

from random import randint as r
import operator as o

#Only works with valid integers. A function for quick math brain training.
def randomMath():
    correct = 0
    while(correct<10):
        str_ops = ['+', '-', '*', '/', '%']
        ops = {'+': o.add, '-': o.sub, '*': o.mul, '/': o.floordiv, '%': o.mod}
        x = r(1,10)
        y = r(1,10)
        op = str_ops[r(0,4)]

        inp = input(str(x) + op + str(y) + '=')
        if int(inp) == ops[op](x, y):
            correct+=1
            print("Correct! Only " + str(10-correct) + ' correct answers to go!')
        else:
            print("Wrong! " + str(10-correct) + ' correct answers to go!')

    print("Congrats!! Good brain training.")

randomMath()
