print("Welcome to my quiz game\n")

playing = input("Do you want to start the game? type yes/no\n ")

if playing.lower() != "yes":
    quit() 

print("Game is starting\n")

score = 0


answer = input("what does CPU stands for?\na.central processing unit\nb.cenimatic processing unit\nc.come process unitied\n\nenter your option\n ")
if answer.lower() == "a":
    print("correct!\n")
    score += score + 1
else: 
    print("incorrect!\n")


answer = input("what does GPU stands for?\na.go processing unit\nb.graphics processing unit\nc.go pro unit\n\nenter your option\n ")
if answer.lower() == "b":
    print("correct!\n")
    score += score + 1
else: 
    print("incorrect!\n")


answer = input("what does RAM stands for?\na.ramsome alware memory\nb.row across memory\nc.random access memory\n\nenter your option\n ")
if answer.lower() == "c":
    print("correct!\n")
    score += score + 1
else: 
    print("incorrect!\n")


answer = input("what does PSU stands for?\na.power supply unit\nb.peek supply unit\nc.problem solver unit\n\nenter your option\n ")
if answer.lower() == "a":
    print("correct!\n")
    score += score + 1
else: 
    print("incorrect!\n")

print("your score is " + str(score) + " well done!" )


