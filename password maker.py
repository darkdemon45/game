import random 
print("Password Generator")
MY ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=.,?0123456789'
a = int(input("Password needed:"))
b= int(input("your password length:"))
print("Here are your password:")
for pwd in range(a):
    s = ''
    for c in range(b):
        s+= random.choice(MY)
    print(s) 