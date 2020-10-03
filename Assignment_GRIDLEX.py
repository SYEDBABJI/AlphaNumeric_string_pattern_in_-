
'''code for Printing an alphanumeric string into # format'''


#---------code for Alphabets (A-Z)---------
#print_A()
def print_A():
    for row in range(7):
        for col in range(5):
            if ((col ==0 or col == 4) and row != 0) or ((row == 0 or row ==3) and (col>0 and col<5)):
                print('#',end='')
            else:
                print(end = " ")
        print()

#print_B()
def print_B():
    for row in range(7):
        for col in range(5):
            if (col ==0 or col == 4) or ((row == 0 or row ==3 or row == 6) and(col>0 and col<4)):
                print('#',end='')
            else:
                print(end = " ")
        print()


#print_C()
def print_C():
    for row in range(7):
        for col in range(5):
            if (col ==0) or ((row == 0 or row == 6) and(col>0)):
                print('#',end='')
            else:
                print(end = " ")
        print()


# print_D()
def print_D():
    for row in range(7):
        for col in range(5):
            if (col ==0) or (col == 4 and (row != 0 and row != 6)) or ((row ==0 or row ==6) and (col>0 and col<4)):
                print('#',end='')
            else:
                print(end = " ")
        print()
      
#print_E()
def print_E():
    for row in range(7):
        for col in range(5):
            if (col ==0) or ((row == 0 or row ==3 or row == 6) and(col>0)):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_F()
def print_F():
    for row in range(7):
        for col in range(5):
            if (col ==0) or ((row == 0 or row ==3) and(col>0)):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_G()
def print_G():
    for row in range(7):
        for col in range(6):
            if col == 0 or (col == 4 and (row != 1 and row != 2)) or ((row == 0 or row == 6) and(col>0 and col<4)):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_H()
def print_H():
    for row in range(7):
        for col in range(5):
            if col ==0 or col == 4 or (row ==3 and (col>0 and col<4)):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_I()
def print_I():
    for row in range(7):
        for col in range(5):
            if col == 2 or ((row ==0 or row == 6) and col != 2):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_J()
def print_J():
    for row in range(7):
        for col in range(5):
            if col == 2 or (row ==0 and col != 2) or (row == 6 and col < 2):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_K()
def print_K():
    i, j = 0, 4
    for row in range(7):
        for col in range(5):
            if col ==0 or (row == col+2 and col>1):
                print('#',end='')
            elif (row==i and col == j) and col>0:
                print('#',end='')
                i += 1
                j -= 1
            else:
                print(end = " ")
        print()
        
        
# print_L()
def print_L():
    for row in range(7):
        for col in range(5):
            if (col ==0) or (row == 6 and col>0):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_M()
def print_M():
    for row in range(6):
        for col in range(7):
            if (col==0 or col==6) or (row<4 and (col==6-row)) or (row<4 and (col==row)):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_N()
def print_N():
    for row in range(6):
        for col in range(6):
            if (col==0 or col==5) or (row==col):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_O()
def print_O():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and (row!=0 and row!=6)) or ((row == 0 or row == 6) and (col>0 and col<4)):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_P()
def print_P():
    for row in range(7):
        for col in range(6):
            if col==0 or ((row==0 or row ==3) and col<5) or ((row<3 and row!=0) and col==5) :
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_Q()
def print_Q():
    for row in range(8):
        for col in range(5):
            if ((col==0 or col==4) and (row>0 and row<6)) or ((row == 0 or row == 6) and (col>0 and col<4)) or (row == 5 and col == 1) or (row == 7 and col == 3):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_R()
def print_R():
    for row in range(7):
        for col in range(5):
            if col==0 or (col==4 and (row!=0 and row!=3)) or ((row == 0 or row == 3) and (col>0 and col<4)):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_S()
def print_S():
    for row in range(7):
        for col in range(5):
            if ((row == 0 or row == 3 or row == 6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_T()
def print_T():
    for row in range(7):
        for col in range(5):
            if col == 2 or (row ==0 and col != 2):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
        
# print_U()
def print_U():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and (row!=0 and row!=6)) or (row == 6 and (col>0 and col<4)):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_V()
def print_V():
    for row in range(4):
        for col in range(7):
            if (row-col==0)or(row+col==6):
                print("*",end="")
            else:
                print(" ",end="")
        print()
        
        
# print_W()
def print_W():
    for row in range(4):
        for col in range(7):
            if (row-col==0)or(row+col==6):
                print('#',end='')
            else:
                print(" ",end="")
        print()
        
        
# print_X()
def print_X():
    for row in range(5):
        for col in range(5):
            if ((col==row)) or ((col+row==4)):
                print('#',end='')
            else:
                print(end=' ')
        print()
        
        
# print_Y()
def print_Y():
    for row in range(5):
        for col in range(5):
            if (col==2 and row>1) or (row==col and col<2) or (row==0 and col ==4) or (row==1 and col ==3):
                print('#',end='')
            else:
                print(end=' ')
        print()
        
        
# print_Z()
def print_Z():
    for row in range(6):
        for col in range(6):
            if row==0 or row == 5 or row + col ==5 :
                print('#',end='')
            else:
                print(end=' ')
        print()

# --------------------------------------------------------------------

#------code for NUMS range(10)---------
#print_0()
def print_0():
    for row in range(8):
        for col in range(6):
            if (col == 5 and row!=7) or (row == 0 or row == 6) or (col == 0 and row!=7):
                print('#',end='')
            else:
                print(end = " ")
        print()
        
#print_1()
def print_1():
    for row in range(6):
        for col in range(6):
            if col == 3 or ((row == 2 and col == 0) or (row == 1 and col == 1)) or row == 5:
                print("*",end="")
            else:
                    print(end = " ")
        print()
        
#print_2()
def print_2():
    for row in range(8):
        for col in range(6):
            if row == 0 or row == 4 or row == 7 or (col == 0 and row>3) or (col == 5 and row<4):
                print("#",end="")
            else:
                    print(end = " ")
        print()

#print_3()
def print_3():
    for row in range(7):
        for col in range(6):
            if (col ==5) or (row == 0 or row ==3 or row == 6):
                print('#',end='')
            else:
                print(end = " ")
        print()

#print_4()
def print_4():
    for row in range(8):
        for col in range(6):
            if (col == 0 and row<5) or row == 4 or (col == 4 and row>2):
                    print('#',end='')
            else:
                print(end = " ")
        print()

#print_5()
def print_5():
    for row in range(8):
        for col in range(6):
            if row == 0 or row == 4 or row == 7 or (col == 0 and row<4) or (col == 5 and row>3):
                    print('#',end='')
            else:
                print(end = " ")
        print()
     
#print_6() 
def print_6():
    for row in range(8):
        for col in range(6):
            if row == 0 or row == 4 or row == 7 or col == 0 or (col == 5 and row>3):
                    print('#',end='')
            else:
                print(end = " ")
        print()
        
#print_7
def print_7():
    for row in range(8):
        for col in range(6):
            if row == 0 or col == 5:
                    print('#',end='')
            else:
                print(end = " ")
        print()

#print_8()
def print_8():
    for row in range(8):
        for col in range(6):
            if row == 0 or row == 4 or row == 7 or col == 0 or col == 5 :
                    print('#',end='')
            else:
                print(end = " ")
        print()

#print_9()
def print_9():
    for row in range(8):
        for col in range(6):
            if row == 0 or col == 5 or row == 4 or (col == 0 and row<5) :
                    print('#',end='')
            else:
                print(end = " ")
        print()
# ------------------------------------------------------

#----------main code---------
inp_alphnum = input("Enter the String(CAPS_NUM) to print in # format: ") # user input alphanumeric String 

for char in inp_alphnum: #for tranversing allover the given string

    '''checking weather the char of the given string matches with mentioned char or not
      if char is matched with the compared char,then it'll print that char onto the screen 
      in the same way entire string will be printed  
    '''
    if char == 'A':     
        print_A()
        print()
    elif char == 'B':
        print_B()
        print()
    elif char == 'C':
        print_C()
        print()
    elif char == 'D':
        print_D()
        print() 
    elif char == 'E':
        print_E()
        print()
    elif char == 'F':
        print_F()
        print()
    elif char == 'G':
        print_G()
        print()
    elif char == 'H':
        print_H()
        print()
    elif char == 'I':
        print_I()
        print()
    elif char == 'J':
        print_J()
        print()
    elif char == 'K':
        print_K()
        print()
    elif char == 'L':
        print_L()
        print()
    elif char == 'M':
        print_M()
        print()
    elif char == 'N':
        print_N()
        print()
    elif char == 'O':
        print_O()
        print()
    elif char == 'P':
        print_P()
        print()
    elif char == 'Q':
        print_Q()
        print()
    elif char == 'R':
        print_R()
        print()
    elif char == 'S':
        print_S()
        print()
    elif char == 'T':
        print_T()
        print()
    elif char == 'U':
        print_U()
        print()
    elif char == 'V':
        print_V()
        print()
    elif char == 'W':
        print_W()
        print()
    elif char == 'X':
        print_X()
        print()
    elif char == 'Y':
        print_Y()
        print()
    elif char == 'Z':
        print_Z()
        print()
    elif char == '0':
        print_0()
        print()
    elif char == '1':
        print_1()
        print()
    elif char == '2':
        print_2()
        print()
    elif char == '3':
        print_3()
        print()
    elif char == '4':
        print_4()
        print()
    elif char == '5':
        print_5()
        print()
    elif char == '6':
        print_6()
        print()
    elif char == '7':
        print_7()
        print()
    elif char == '8':
        print_8()
        print()
    elif char == '9':
        print_9()
        print()
''' Iteration over here'''
'''--- HAPPY CODING ---'''
        
        