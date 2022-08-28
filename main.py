import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0',]
symbols = ['!','@','#','$','%','^','&','*']

answers = input("Do You Want A Password?: (y/n) ").lower()
if answers == ("y"):

    totalCharacterAmount = int(input("Max Password Length?: "))
    uLetterAmount = int(input("How Many Uppercase Letters?: "))
    lLetterAmount = int(input("How Many Lowercase Letters?: "))
    numberAmount = int(input("How Many Numbers?: "))
    symbolAmount = int(input("How Many Symbols?: "))

    rLetters = random.choices(letters, k=lLetterAmount)
    rULetters = random.choices(uLetters, k=uLetterAmount)
    rNumbers = random.choices(numbers, k=numberAmount)
    rSymbols = random.choices(symbols, k=symbolAmount)
    results = (random.choices(rLetters+rNumbers+rSymbols+rULetters, k=totalCharacterAmount))
    print("You Password Is: ")
    print(*results)
    print("Passwords Contents: "+str(totalCharacterAmount)+" Characters Long. With "+str(uLetterAmount)+" Uppercase Letters, "+str(lLetterAmount)+" Lowercase letters, "+str(numberAmount)+" Numbers and "+str(symbolAmount)+" Symbols")
    
elif answers == ("n"):
    print("Ok Then... Closing The Program")