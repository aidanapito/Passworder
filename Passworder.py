import random

#now check strength
password = input('Check if your password is strong: ')

capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerletters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
othercharacters = '!@#$%^&*()?'


#establish chars at 0
c,l,n,o = 0,0,0,0


#check for character variety
if(len(password) >= 10):
    for i in password:
        if (i in capletters):
            c+=1
        if (i in lowerletters):
            l+=1
        if (i in numbers):
            n+=1
        if (i in othercharacters):
            o+=1


#outputs
if ( c>= 1 and l >= 1 and n >= 1 and o>= 1
    and c+l+n+o == len(password)):
    print('Password is Strong')

else:
    print('Password is not strong enough, here is a better one:')

    #enter characters elible to be in password
    chars = capletters + lowerletters + numbers + othercharacters

    password= ''

    #generate random password 20 characters long!
    for x in range(20):
        password += random.choice(chars)
    
    print(password)
         



