import random

def hangman():
    w = ["apple", "grape", "melon", "peach", "berry"]
    s = random.choice(w)
    g = []
    err = 0
    
    while err < 6:
        disp = "".join([c if c in g else "_" for c in s])
        print(disp)
        
        if disp == s:
            print("Win")
            return
            
        x = input("Guess: ").lower()
        if x in g:
            continue
        g.append(x)
        
        if x not in s:
            err += 1
            
    print("Lose")
    
hangman()