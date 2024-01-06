"""
Fundamentals of Computer Science Assignment
Created by: Hajnalka Horváth
Neptun code: XXNVW8
"""
# Reading the file---------------------------------------------------------------------
file = open("input.txt", "r")

exercise=[]
for line in file:
    for character in line:
        exercise.append(character)
file.close()

number1=[]
i=0
invalid = False
while not invalid and exercise[i]!='\n' and i!= len(exercise)-1:
    if not invalid and (exercise[i] == '0' or exercise[i] == '1' or exercise[i] == '2' or exercise[i] == '3' or exercise[i] == '4' or exercise[i] == '5' or exercise[i] == '6' or exercise[i] == '7' or exercise[i] == '8' or exercise[i] == '9'):
        number1.append(int(exercise[i]))
        i+=1
    elif exercise[i]!='\n':
        invalid = False
        i += 1
    else:
        invalid = True
        
if i!= len(exercise)-1 and not invalid and(exercise[i+1] == '+' or exercise[i+1] == '-' or exercise[i+1] == '*' or exercise[i+1] == '/' ):
    sign=exercise[i+1]
else:
    invalid = True
       
number2=[]
i += 3   
while not invalid and i!= len(exercise):
    if not invalid and (exercise[i] == '0' or exercise[i] == '1' or exercise[i] == '2' or exercise[i] == '3' or exercise[i] == '4' or exercise[i] == '5' or exercise[i] == '6' or exercise[i] == '7' or exercise[i] == '8' or exercise[i] == '9'):
        number2.append(int(exercise[i]))
        i+= 1 
    elif exercise[i]!='\n':
        invalid = False
        i += 1
    else:
        invalid = True

if sign == "/" and number2 == [0]:
    invalid = True
# Reading ends-------------------------------------------------------------------------

# Function declarations---------------------------------------------------------------

# Conversion---------------------------------------------------

def decimaltobcd(decnumber):
    number = decnumber
    number_bcd=[]
    bcd=[]    
    i=0
    endofnumber = False
    while i != len(number):
        #print(number)
        while not endofnumber:
            bcd.insert(0,number[i] % 2)
            number[i]= number[i] // 2
            if number[i] == 0:
                endofnumber = True
            #print(decnumber)
        while len(bcd) < 4:
            bcd.insert(0,0)
        #print(number)
        number_bcd.append(bcd)
        endofnumber = False
        bcd =[]
        i+=1
        #print(decnumber)
    return number_bcd

#number1_bcd=decimaltobcd(number1)
#number2_bcd=decimaltobcd(number2)
#print("szam1=", number1)
        
# Conversion: BCD to Decimal

def bcdtodecimal(bcdnumber):
    if type(bcdnumber) != int and type(bcdnumber[0]) == list:
        i=0
        j=0
        decimal = 0
        decimalnumber=[]
        while j<len(bcdnumber):
            while i < 4:
                decimal = decimal + (bcdnumber[j][i] * (2**(3-i)))
                i+= 1
            decimalnumber.append(decimal)
            j+=1
            i=0
            decimal = 0
    elif type(bcdnumber) == int:
        i=0
        decimal=0
        while i < 4:
            decimal= decimal + (bcdnumber * (2**(3-i)))
            i+= 1
        decimalnumber = decimal
    #print(decimalnumber)  
    else:
        i=0
        decimal=0
        #decimalnumber = []
        while i < 4:
            decimal= decimal + (bcdnumber[i] * (2**(3-i)))
            i+= 1
        #decimalnumber.append(decimal)
        decimalnumber = decimal
    #print(decimalnumber)
    return decimalnumber

#print(bcdtodecimal(number1_bcd[0]))

# Conversion: Decimal to Integer

def dectoint(dec):
    i = len(dec)-1
    pos= 1
    intnumber = 0
    #print(dec)
    while i >= 0:
        intnumber += dec[i]*pos
        i -= 1
        pos *= 10
    return intnumber

def inttohexadecimal(integer):
    hexa = ['0', 'x']
    while integer != 0:
        hexa.insert(2, integer%16)
        integer //= 16
    i = 0
    while i < len(hexa):
        if type(hexa[i])== int and hexa[i] >= 10:
            if hexa[i] == 10:
                hexa[i] = 'A'
            elif hexa[i] == 11:
                hexa[i] = 'B'
            elif hexa[i] == 12:
                hexa[i] = 'C'
            elif hexa[i] == 13:
                hexa[i] = 'D'
            elif hexa[i] == 14:
                hexa[i] = 'E'
            elif hexa[i] == 15:
                hexa[i] = 'F'
        else:
            hexa[i] = str(hexa[i])
        i+= 1
    return hexa

# Conversion ends-----------------------------------------------------

# Operations-----------------------------------------------------------

# Addition---------------------------------------------------------
def addition(bcd1, bcd2):
    while len(bcd1) != len(bcd2):
        if len(bcd1) < len(bcd2):
            bcd1.insert(0,[0,0,0,0])
        elif len(bcd1) > len(bcd2):
            bcd2.insert(0,[0,0,0,0])
    #print(bcd1, sign,bcd2 )
    sum=[]
    partial_result= [0,0,0,0]
    bcdidx=len(bcd1)-1
    bitidx = 3
    carry = 0
    while bcdidx >= 0:
        while bitidx >= 0:
            #kivételek = 9+9, 8+8, 7+9
            if bcd1[bcdidx]== [1,0,0,0] and bcd2[bcdidx] == [1,0,0,0] or bcd1[bcdidx]== [1,0,0,1] and bcd2[bcdidx] == [0,1,1,1] or bcd1[bcdidx]== [0,1,1,1] and bcd2[bcdidx] == [1,0,0,1]:
                if carry == 0:
                    partial_result = [0,1,1,0]
                elif carry == 1:
                    partial_result = [0,1,1,1]
                carry = 1
                bitidx = -1
            elif bcd1[bcdidx]== [1,0,0,1] and bcd2[bcdidx] == [1,0,0,1]:
                if carry == 0:
                    partial_result = [1,0,0,0]
                elif carry == 1:
                    partial_result = [1,0,0,1]
                carry = 1
                bitidx = -1
            elif bcd1[bcdidx]== [1,0,0,1] and bcd2[bcdidx] == [1,0,0,0] or bcd1[bcdidx]== [1,0,0,0] and bcd2[bcdidx] == [1,0,0,1]:
                if carry == 0:
                    partial_result = [0,1,1,1]
                elif carry == 1:
                    partial_result = [1,0,0,0]
                carry = 1
                bitidx = -1
            #hagyományos bcd összeadás
            else:
                if (bcd1[bcdidx][bitidx] == 1 and bcd2[bcdidx][bitidx] == 0) or (bcd1[bcdidx][bitidx] == 0 and bcd2[bcdidx][bitidx] == 1):
                    if carry == 0:
                        partial_result[bitidx]= 1
                    elif carry == 1:
                        partial_result[bitidx]= 0
                elif bcd1[bcdidx][bitidx] == 1 and bcd2[bcdidx][bitidx] == 1:
                    if carry == 0:
                        partial_result[bitidx]= 0
                        carry = 1
                    elif carry == 1:
                        partial_result[bitidx]= 1
                elif bcd1[bcdidx][bitidx] == 0 and bcd2[bcdidx][bitidx] == 0:
                    if carry == 0:
                        partial_result[bitidx]= 0
                    elif carry == 1:
                        partial_result[bitidx]= 1
                        carry = 0
                bitidx -= 1
        sum.insert(0,partial_result) 
        partial_result= [0,0,0,0]  
        bitidx = 3
        bcdidx -= 1
    if carry == 1:
        sum.insert(0, [0,0,0,1])
    #print("javitas nelkul:" ,result)
    return sum

# Correction

def correction(res):
    i= 0
    end = 0
    while end < len(res):
        while i < len(res):
            #print(res[i])
            if bcdtodecimal(res[i]) >  9: 
                correct = addition([res[i]], [[0,1,1,0]])
                #print("correct=", correct)
                if len(correct) == 2:
                    if i != 0: 
                        corresult = addition([correct[0]], [res[i-1]])
                        res[i-1] = corresult[0]
                        res[i]= correct[1]
                        #print("correct1 =", correct[1])
                    else:
                        #print("correct1 =", correct[1])
                        res.insert(0, correct[0] )
                        res[1] = correct[1]
                else:
                    res[i]= correct[0]
            i += 1
        #print("javit:",res)
        i = 0
        end = 0
        j = 0
        while j < len(res):
            if (bcdtodecimal(res[j])) <= 9:
                end += 1
            j += 1
    return res

# Addition ends-----------------------------------------------------

# Subtraction------------------------------------------------------

def subtraction(minuend,subtrahend):
    if minuend == subtrahend:
        difference = [[0,0,0,0]]
    else:
        if bcdtodecimal(minuend) < bcdtodecimal(subtrahend):
            swap = minuend
            minuend = subtrahend
            subtrahend = swap
        compliment9 = []
        i = 0
        while i < len(subtrahend):
            originaldec = bcdtodecimal(subtrahend[i])
            compldec = 9 - originaldec
            complbcd = decimaltobcd([compldec])
            compliment9.append(complbcd[0])
            i += 1
        #print(bcd2)
        #print(compliment9)
        #korrekció
        subtractresult = correction(addition(minuend,compliment9))
        #print(bcdtodecimal(subtractresult))
        difference = correction(addition(subtractresult,[subtractresult[0]]))
        difference.pop(0)
    return difference

# Subtraction ends-------------------------------------------------

# Multiplication---------------------------------------------------
def multiplication(multiplicand, multiplier):
    intmultiplier = dectoint(bcdtodecimal(multiplier))
    product = [[0,0,0,0]]
    while intmultiplier > 0:
        product = correction(addition(product, multiplicand))
        #print(bcdtodecimal(product))
        intmultiplier -= 1
    return product

# Multiplication ends-----------------------------------------------

# Division----------------------------------------------------------

def division(dividend,divisor):
    quotient = 0
    if not number1smaller:
        while dectoint(bcdtodecimal(dividend)) >= dectoint(bcdtodecimal(divisor)):
            #print(dectoint(bcdtodecimal(dividend)), dectoint(bcdtodecimal(divisor)))
            dividend = subtraction(dividend,divisor)
            #print(dectoint(bcdtodecimal(dividend)))
            quotient += 1
            #print(quotient)
    return quotient

# Division ends-----------------------------------------------------

# Function declarations end---------------------------------------------------------

# Task-------------------------------------------------------------------------------
f = open("output.txt", "w")
if invalid:
    f.write("Invalid input ! ! !")
else:
    hexa1 = inttohexadecimal(dectoint(number1))
    hexa2 = inttohexadecimal(dectoint(number2))
    # Writing the operation details

    f.write(str(dectoint(number1)))
    f.write(" (")
    for element in hexa1:
        f.write(element)
    f.write(")\n")
    f.write(sign)
    f.write("\n")
    f.write(str(dectoint(number2)))
    f.write(" (")
    for element in hexa2:
        f.write(element)
    f.write(")")


    # Conversion
    
    number1_bcd=decimaltobcd(number1)
    number2_bcd=decimaltobcd(number2)

    # Helper:

    # Filling with zeros

    while len(number1_bcd) != len(number2_bcd):
        if len(number1_bcd) < len(number2_bcd):
            number1_bcd.insert(0,[0,0,0,0])
        elif len(number1_bcd) > len(number2_bcd):
            number2_bcd.insert(0,[0,0,0,0])    
    #print("bcdben:",number1_bcd, ",", number2_bcd)

    # Which is smaller

    number1smaller = False
    #print("smaller= ",dectoint(bcdtodecimal(number1_bcd)), dectoint(bcdtodecimal(number2_bcd))
    if dectoint(bcdtodecimal(number1_bcd)) < dectoint(bcdtodecimal(number2_bcd)):
        number1smaller = True
    #print(number1smaller)

    # Operation 
    if sign == '+':
        result = correction(addition(number1_bcd, number2_bcd))
    elif sign == '-':
        result= subtraction(number1_bcd,number2_bcd)
    elif sign == '*':
        result = multiplication(number1_bcd, number2_bcd)
    elif sign == '/':
        decimalresult = division(number1_bcd, number2_bcd)
    
    if sign != "/":
        decimalresult = dectoint(bcdtodecimal(result))
    hexaresult = inttohexadecimal(decimalresult)

    if number1smaller and sign == '-': 
        f.write("\n=\n-")
        f.write(str(decimalresult))
        f.write(" (")
        for element in hexaresult:
            f.write(element)
        f.write(")")
    else:
        f.write("\n=\n")
        f.write(str(decimalresult))
        f.write(" (")
        for element in hexaresult:
            f.write(element)
        f.write(")")
    f.close()