#list type

state = "tamilnadu india"
l = state.split()
print(l)
print(type(l))
for i in l:
    print(l)

#user defined string format

state = "tamilnadu india"
l = state.upper()
print(l)
print(type(l))
l = state.lower()
print(l)
print(type(l))
l = state.swapcase()
print(l)
print(type(l))
l = state.title()
print(l)
print(type(l))
l = state.capitalize()
print(l)
print(type(l))

state = "tamilnaduindia600042"

print(state.isalnum())
print(state.isalpha())
print(state.isdigit())
print(state.isupper())
print(state.islower())
print(state.istitle())
print(state.isnumeric())

#startswith & endswith program:
state = "tamil nadu india"
print(state.startswith("tamil"))
print(state.endswith("india"))
print(state.startswith("india"))


# to change first letter in caps

state = "india"
print(state[0].upper()+state[1:])

# to change first letter in caps

print(state[:-1]+state[-1].upper())


#ascii keys value:
# upper epudi work authu athuku oru program:

state = "india"
for i in range(5):
    print(chr(ord(state[i]) -32),end= " ")


#ascii keys value:
# lower epudi work authu athuku oru program:

state = "INDIA"
for i in range(5):
    print(chr(ord(state[i]) +32),end= " ")

#swap case
state = "Tamil Nadu"
for i in range(len(state)):
    if state[i]>="a"and state[i]<="z":
        print(chr(ord(state[i]) -32),end= " ")
    else:
        print(state[i], end=" ")

state = "Tamil Nadu"
for i in range(len(state)):
    if state[i] >= "a" and state[i] <= "z":
        print(chr(ord(state[i]) - 32), end=" ")
    elif state[i] >= "A" and state[i] <= "Z":
        print(chr(ord(state[i]) + 32), end=" ")
    else:
        print(state[i], end=" ")


# title program:
state = "tamil nadu india"
words = state.split()
for i in words:
    for letter in i:
        print(letter)

#capitalize program:
state = "tamil nadu india"
print(state[0].upper()+state[1:])

#startswith & endswith program:
state = "tamil nadu india"
print(state.startswith("tamil"))
print(state.endswith("india"))
print(state.startswith("india"))


#odd and even caps
name = "olympic"
for i in name:
    print(i)
print(name[0:7:3].upper())


#swap pandrathu using program:
s1 = "OYPC"
s2 = "lmi"
output = ''

if len(s1)<len(s2):
    small=len(s1)
else:
    small = len(s2)
i=0
while i<small:
    output=output+s1[i]+s2[i]
    i+=1
else:
    output = output + s1[-1]
    print(output)

# output = output+s1[0]+s2[0]
#
# output = output+s1[1]+s2[1]
#
# output = output+s1[2]+s2[2]
#
# s1[0]+s2[0]+s1[1]+s2[1]+s1[2]+s2[2]


s1 = "OYPC"
s2 = "lmi"
output = ''

small = len(s1) if len(s1)<len(s2) else len(s2) ##ternary operator

i=0
while i<small:
    output=output+s1[i]+s2[i]
    i+=1
else:
    output = output + s1[-1]
    print(output)

# output = output+s1[0]+s2[0]
#
# output = output+s1[1]+s2[1]
#
# output = output+s1[2]+s2[2]
#
# s1[0]+s2[0]+s1[1]+s2[1]+s1[2]+s2[2]



# how to seperate the alpha and numbers using program:

# input : a1b2c3
#outpt : abc

word = "a1b2c3"
alpha = " "
numbers = " "
for letter in word:
    if letter.isalpha():
        alpha = alpha+letter
    else:
        numbers = numbers+letter

else:
    print(alpha+numbers)


alpha= "a3"
for letter in alpha:
    if letter.isdigit():
        print(chr(ord(letter)+48))
