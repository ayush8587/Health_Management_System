def getdate():
    import datetime
    return datetime.datetime.now()
print("Health Management Sysytem")
print("Press 1 for Log and 2 for Retrive: ")
x1=int(input())
if(x1==1):
    print("Press 1 for Harry\nPress 2 for Rohan\nPress 3 for Ayush: ")
    y1=int(input())
    if y1==1:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z1=int(input())
        if z1==1:
            a1 = input("Enter your meal: ")
            with open("foodh.txt",'a') as f1:
                f1.write(str([str(getdate())])+" : "+a1+"\n")
                print("Successfully Written")
        elif z1==2:
            a2 = input("Enter your exercise: ")
            with open("exerciseh.txt",'a') as e1:
                e1.write(str([str(getdate())])+" : "+a2+"\n")
                print("Successfully Written")
    elif y1==2:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z2 = int(input())
        if z2 == 1:
            b1 = input("Enter your meal: ")
            with open("foodr.txt", 'a') as f2:
                f2.write(str([str(getdate())])+" : "+b1+"\n")
                print("Successfully Written")
        elif z2 == 2:
            b2 = input("Enter your exercise: ")
            with open("exerciser.txt", 'a') as e2:
                e2.write(str([str(getdate())])+" : "+b2+"\n")
                print("Successfully Written")
    elif y1==3:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z3 = int(input())
        if z3 == 1:
            c1 = input("Enter your meal: ")
            with open("fooda.txt", 'a') as f3:
                f3.write(str([str(getdate())])+" : "+c1+"\n")
                print("Successfully Written")
        elif z3 == 2:
            c2 = input("Enter your exercise: ")
            with open("exercisea.txt", 'a') as e3:
                e3.write(str([str(getdate())])+" : "+c2+"\n")
                print("Successfully Written")
elif(x1==2):
    print("Press 1 for Harry\nPress 2 for Rohan\nPress 3 for Ayush: ")
    y2=int(input())
    if y2==1:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z4=int(input())
        if z4==1:
            with open("foodh.txt",'r') as f1:
                for i in f1:
                    print(i,end="")
        elif z4==2:
            with open("exerciseh.txt") as e1:
                for i in e1:
                    print(i,end="")
    elif y2==2:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z5 = int(input())
        if z5 == 1:
            with open("foodr.txt") as f2:
                for i in f2:
                    print(i,end="")
        elif z5 == 2:
            with open("exerciser.txt") as e2:
                for i in e2:
                    print(i,end="")
    elif y2==3:
        print("Press 1 for Food\nPress 2 for Exercise: ")
        z6 = int(input())
        if z6 == 1:
            with open("fooda.txt") as f3:
                for i in f3:
                    print(i,end="")
        elif z6 == 2:
            with open("exercisea.txt") as e3:
                for i in e3:
                    print(i,end="")
