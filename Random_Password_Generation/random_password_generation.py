import random #Import required functions
pwd_len = int(input("Enter the length of password: ")) #Take length of the password as an input
c="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" #Declare the string (Uppercase letters, lowercase letters, numbers and special characters.)
pwd = "".join(random.sample(c,pwd_len )) #Generate password
print(pwd) #Print the output
