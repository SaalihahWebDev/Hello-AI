print("Hello,I am AI Bot,What's your name?")
name=input()
print("Nice to meet you",name)
print("How are you feeling today(good/bad)")
mood=input().lower()
if mood=="good":
    print("I am good")
elif mood=="bad":
    print("I am sorry to hear that")
else:
    print("I see sometimes,it's hard to put feelings into words")
print("It's nice to see you",name)