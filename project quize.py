print("Quiz")
playing = input("do you want to play")

if playing != "yes": 
    quit()

print("okay! let's play")
score = 0
answer = input("what is CPU stands for? ")
if answer == "central processing unit":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("which keyword is used to define a function in python? ")
if answer == "def":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("what will 'bool' return? ")
if answer == "true and false":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("what is the chemical symbol of gold? ")
if answer == "Au":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("what is binary representation of the decimal number 10? ")
if answer == "1010":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("which key is used to refresh a webpage? ")
if answer == "F5":
    print("correct")
    score += 1
else:
   print("incorrect")               

answer = input("which device connects multiple networks? ")
if answer == "router":
    print("correct")
    score += 1
else:
   print("incorrect")

answer = input("what does VPN stands for? ")
if answer == "virtual private network":
    print("correct")
    score += 1
else:
   print("incorrect")


print("quize completed")

print("you got" + str(score) + "question correct")
