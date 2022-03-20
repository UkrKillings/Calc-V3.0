print ("Hello, calculator Mobile")

print("Привет, если хочешь закрыть калькулятор напишы exit")
while True:
    name = input("Привет, как тебя зовут: ")
    print("Привет, " + name + " вот твой калькулятор!")
    s = input("Знаки (+,-,*,/): ")
    if s == 'exit':
        break
    if s in('+', '-', '/', '*'):
        x = float(input("x="))
        y = float(input("y="))
    if s == '+':
        print("%.2f" % (x+y))
    elif s == '-':
        print("%.2f" % (x-y))
    elif s == '*':
        print("%.2f" % (x*y))
    elif s == '/':
        if y !=0:
            print("%.2f" % (x/y))
        else:
            print("Деление на ноль")
    else:
        print("Не тот знак")