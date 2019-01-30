name = input("What is your name")
print("%s Is on the last hole of 2018 US Open Championship %s"%(name,name))
ans = input("Do you want to go for the green or lay it up?")

if ans =="lay it up":
    print("%s shanked the ball. %s has to make it in from the rough. Do you want to use a 7 or 8 iron? "%(name))
if ans == ("7 iron"):
    print("Sorry %s lost the championship")
if ans ==("8 iron"):
    print("Congratulations %s got it in, %s wins!"%(name))

if ans == ("go for the green"):
    print("Congratulations, %s is on the green. %s has a 20ft putt for birdie to win. Do you think the green is fast or slow? "%(name)(name))
if ans == ("fast"):
    print("Good choice, you putt it slow and the ball rolls in! You win!")
if ans == ("slow"):
    print("Sorry, you left your birdie putt short, maybe next time")
