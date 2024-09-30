#take input from user
a= input("Enter a word: ")

#program to check break keyword
for i in a:
    if(i=='a'):
        print("A is found")
        break
    
    else:
        print("A not found")