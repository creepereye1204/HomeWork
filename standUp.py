import random



class user:
    myCards=[]
    def __init__(self):
        self.myCards=[]

    def setCard(self,first,second):

        self.myCards.append(first)
        self.myCards.append(second)


class card:
    number=None
    light=None
    def __init__(self,number,light):
        self.number=number
        self.light=light

def go38(i,firstNum,firstLight,secondNum,secondLight):
    if firstNum == 3 and firstLight:
        if secondNum == 8 and secondLight:
            print(i , "User 승리")
            exit(0)
    elif firstNum  == 8 and firstLight:
        if secondNum == 3 and secondLight:
            print(i , "User 승리")
            exit(0)

def go(firstNum,firstLight,secondNum,secondLight,x,y):
    if firstNum == x and firstLight:
        if secondNum == y and secondLight:
            return True
    elif firstNum == y and firstLight:
        if secondNum == x and secondLight:
            return True
    return False

def goOther(firstNum,firstLight,secondNum,secondLight,x,y):
    if firstNum == x and firstLight!=True:
        if secondNum == y and secondLight:
            return True
    elif firstNum == y and firstLight!=True:
        if secondNum == x and secondLight:
            return True
    elif firstNum == x and firstLight:
        if secondNum == y and secondLight!=True:
            return True
    elif firstNum == y and firstLight:
        if secondNum == x and secondLight!=True:
            return True
    elif firstNum == x and firstLight!=True:
        if secondNum == y and secondLight!=True:
            return True
    elif firstNum == y and firstLight!=True:
        if secondNum == x and secondLight!=True:
            return True
    return False

def goFull(firstNum,firstLight,secondNum,secondLight,x,y):
    if firstNum == x and firstLight:
        if secondNum == y and secondLight:
            return True
    elif firstNum == y and firstLight:
        if secondNum == x and secondLight:
            return True
    elif firstNum == x and firstLight!=True:
        if secondNum == y and secondLight:
            return True
    elif firstNum == y and firstLight!=True:
        if secondNum == x and secondLight:
            return True
    elif firstNum == x and firstLight:
        if secondNum == y and secondLight!=True:
            return True
    elif firstNum == y and firstLight:
        if secondNum == x and secondLight!=True:
            return True
    elif firstNum == x and firstLight!=True:
        if secondNum == y and secondLight!=True:
            return True
    elif firstNum == y and firstLight!=True:
        if secondNum == x and secondLight!=True:
            return True
    return False


def tthang(firstNum,secondNum,x):
    if firstNum==x and secondNum==x:
        return True
    return False
def play(playerNum):

    while True:
        users = [user() for _ in range(playerNum)]
        index = [card(i, True) if j == 1 else card(i, False) for i in range(1, 10 + 1) for j in range(1, 3)]
        for i in range(playerNum):

            n = random.randrange(0, len(index))
            first = index.pop(n)
            m = random.randrange(0, len(index))
            second = index.pop(m)
            users[i].setCard(first, second)
            print()
        print("패 깝니다. 엔터를 눌러 주세요")
        input()

        cards1=users[0].myCards
        cards2 = users[1].myCards
        firstNum1,firstLight1 =cards1[0].number,cards1[0].light
        secondNum1,secondLight1 = cards1[1].number,cards1[1].light

        firstNum2, firstLight2 = cards2[0].number, cards2[0].light
        secondNum2, secondLight2 = cards2[1].number, cards2[1].light

        print(1, "User ",firstNum1,"광"if firstLight1 else "",secondNum1,"광"if secondLight1 else "")
        print(2, "User ", firstNum2, "광"if firstLight2 else "",secondNum2, "광"if secondLight2 else "")
        print()

        go38(1,firstNum1,firstLight1,secondNum1,secondLight1)
        go38(2, firstNum2, firstLight2, secondNum2, secondLight2)

        if go(firstNum1,firstLight1,secondNum1,secondLight1,4,9) or go(firstNum2,firstLight2,secondNum2,secondLight2,4,9):
            print("재경기")
            continue


        if go(firstNum1,firstLight1,secondNum1,secondLight1,1,3) and go(firstNum2,firstLight2,secondNum2,secondLight2,1,8):
            print("비겼 습니다")
            continue
        if go(firstNum1,firstLight1,secondNum1,secondLight1,1,8) and go(firstNum2,firstLight2,secondNum2,secondLight2,1,3):
            print("비겼 습니다")
            continue



        if go(firstNum1,firstLight1,secondNum1,secondLight1,4,7) and go(firstNum2,firstLight2,secondNum2,secondLight2,1,3) or go(firstNum2,firstLight2,secondNum2,secondLight2,1,8):
            print(1,"User 승리")
            exit(0)
        if go(firstNum2,firstLight2,secondNum2,secondLight2,4,7) and go(firstNum1,firstLight1,secondNum1,secondLight1,1,3) or go(firstNum1,firstLight1,secondNum1,secondLight1,1,8):
            print(2,"User 승리")
            exit(0)

        if goOther(firstNum1,firstLight1,secondNum1,secondLight1,4,9) or goOther(firstNum2,firstLight2,secondNum2,secondLight2,4,9):
            print("재경기")
            continue

        for i in range(10,0,-1):
            if tthang(firstNum1,secondNum1,i):
                if goOther(firstNum2,firstLight2,secondNum2,secondLight2,3,7):
                    print(2,"User 승리")
                    exit(0)
                print(1, "User 승리")
                exit(0)
            elif tthang(firstNum2,secondNum2,i):
                if goOther(firstNum1, firstLight1, secondNum1, secondLight1, 3, 7):
                    print(1, "User 승리")
                    exit(0)
                print(2, "User 승리")
                exit(0)

        for x,y in [[1,2],[1,4],[1,9],[1,10],[4,10],[4,6]]:
                if goFull(firstNum1, firstLight1, secondNum1, secondLight1, x, y):
                    print(1,"User 승리")
                    exit(0)
                elif goFull(firstNum2, firstLight2, secondNum2, secondLight2, x, y):
                    print(2, "User 승리")
                    exit(0)

        if (firstNum1+secondNum1)%10<(firstNum2+secondNum2)%10:
            print("2 User 승리")
            exit(0)
        elif (firstNum1+secondNum1)%10>(firstNum2+secondNum2)%10:
            print("1 User 승리")
            exit(0)
        else:
            print("재경기")
            continue






playerNum=2

play(playerNum)