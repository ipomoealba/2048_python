import numpy as np
import sys
game_place = np.mat('0 0 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0')
game_place_size = 12

place = np.arange(game_place_size)
_len = 4

while True:
    tmp = (np.array([i for i in range(12) if game_place.item(i) == 0]))
    def defineder():
        for i in range(game_place_size):
            if game_place.item(i) == game_place.item(i + 4):
                return False
            elif i % 4 != 0 and game_place.item(i) == game_place.item(i +1) :
                return False
            else:
                return True
            
    if  defineder() and len(tmp) == 0:
        print("game over")
        sys.exit(0)
    elif len(tmp) > 1:
        np.random.shuffle(tmp)
        n1, n2 = tmp[0:2]
        game_place.itemset(n1, 2)
        game_place.itemset(n2, 2)
    else:
        pass
    print(game_place)
    start = True
    x = input("")
    
    for a in range(_len):
        if x == "a":
            for i in range(0, 4):
                for k in range(0, 3):
                    if game_place[i, k] == 0 and k < 3:
                        game_place[i, k] = game_place[i, k + 1]
                        game_place[i, k + 1] = 0
                        
                    elif game_place[i, k] != 0 and game_place[i, k] == game_place[i, k + 1] and k < 3:
                        game_place[i, k] += game_place[i, k + 1]
                        game_place[i, k + 1] = 0
                        
        elif x == "d":
            for i in range(0, 4):
                for j in range(0, 3):
                    k = 3 - j
                    if game_place[i, k] == 0 and k > 0:
                        game_place[i, k] = game_place[i, k - 1]
                        game_place[i, k - 1] = 0
                        
                    elif game_place[i, k] != 0 and game_place[i, k] == game_place[i, k - 1] and k > 0:
                        game_place[i, k] += game_place[i, k - 1]
                        game_place[i, k - 1] = 0
                        
        elif x == "w":
            for i in range(0, 4):
                for k in range(0, 3):
                    if game_place[k, i] == 0 and k < 3:
                        game_place[k, i] = game_place[k + 1, i]
                        game_place[k + 1, i] = 0
                        
                    elif game_place[k, i] != 0 and game_place[k, i] == game_place[k + 1, i] and k < 3:
                        game_place[k, i] += game_place[k + 1, i]
                        game_place[k + 1, i] = 0
                        
        elif x == "s":
            for i in range(0, 4):
                for j in range(0, 3):
                    k = 3 - j
                    if game_place[k, i] == 0 and k > 0:
                        game_place[k, i] = game_place[k - 1, i]
                        game_place[k - 1, i] = 0
                        
                        # print("1")
                    elif game_place[k, i] != 0 and game_place[k, i] == game_place[k - 1, i] and k > 0:
                        game_place[k, i] += game_place[k - 1, i]
                        game_place[k - 1, i] = 0
                        

        else:
            print("type error")