'''
1 for snake
-1 for water 
0 for gun
'''
computer = -1
youstr = input("Enter your choice: ")
youDict = { "s":1, "w":-1, "g":0 }
you = youDict[youstr]

if(computer == -1 and you ==1):
    print("YOU WON!")

elif(computer == -1 and you ==0):
    print("YOU LOSE!")

elif(computer == 1 and you ==-1):
    print("YOU LOSE!")

elif(computer == 1 and you ==0):
    print("YOU WON!")        

elif(computer == 0 and you ==-1):
    print("YOU WIN!")

elif(computer == 0 and you ==1):
    print("YOU LOSE!")
else:
    print("SOMETHING WENT WRONG!")