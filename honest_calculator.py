msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_list = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
good = ["+", "-", "*", "/"]
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False 
        
def is_one_digit(v):
    if -10 < v < 10 and v.is_integer() is True:
        return True  
    else:
        return False
        
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)                         
        
         
memory = 0 
finished = False            
while not finished:
    print(msg_0)
    calc = input().split()
    x = calc[0]
    oper = calc[1]
    y = calc[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if isDigit(x) is True and isDigit(y) is True:
        if oper in good:
            x = float(x)
            y = float(y)
            check(x, y, oper)
            if oper == "/" and y == 0:
                print(msg_3)
            else:
                if oper == "+":
                    result = x + y
                if oper == "-":
                    result = x - y
                if oper == "*":
                    result = x * y
                if oper == "/" and y != 0:
                    result = x / y
                print(result)
                while True:
                    print(msg_4)
                    answer = input()
                    if answer == "y":
                        if is_one_digit(result) is True:
                            msg_index = 10
                            while msg_index <= 12:
                                print(msg_list[msg_index])
                                answer3 = input()
                                if answer3 == "y":
                                    msg_index += 1
                                if answer3 == "n":
                                    msg_index = 14
                            if msg_index == 13:
                                memory = result 
                            break              
                        if is_one_digit(result) is False:
                            memory = result    
                            break
                    if answer == "n":
                        break
                        
                    
                    
                while True:
                    print(msg_5)
                    answer2 = input()
                    if answer2 != "y" and answer2 != "n":
                        continue
                    if answer2 == "y":
                        break
                    if answer2 == "n":
                        finished = True 
                        break                 
        else:
            print(msg_2)    
    else:
        print(msg_1)