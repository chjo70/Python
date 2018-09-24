import random

def RandomSeed():
    lRandom = []

    for i in range(1,6):
        val = random.randrange(1, 15)
        while val in lRandom :
            val = random.randrange(1, 15)

        lRandom.append(int(val))

    lRandom.sort()
    #print( lRandom )

    return lRandom

def CheckRandom( lList, lNumber ):

    iMatch = 0;
    for i in range(1, 5):
        if lList[i] in lNumber:
            iMatch = iMatch + 1;


    return iMatch;


lNumber = []
myNumber = []
lCheck = []

while True:
    val = input( '첫 번째 숫자를 입력하세요: ' )
    myNumber.append( int(val) )

    val = input( '두 번째 숫자를 입력하세요: ' )
    myNumber.append( int(val) )

    val = input( '세 번째 숫자를 입력하세요: ' )
    myNumber.append( int(val) )

    val = input( '네 번째 숫자를 입력하세요: ' )
    myNumber.append( int(val) )

    val = input( '다섯 번째 숫자를 입력하세요: ' )
    myNumber.append( int(val) )

    lNumber = RandomSeed()
    print( '이번 당첨 번호:', lNumber )

    lNumber.sort()
    print( '당신의 숫자:', myNumber )
    myM = CheckRandom( myNumber, lNumber)
    print('당신의 숫자: ', lNumber, '맞힌 개수:', myM )
    lCheck.append( myM )

    for i in range(1,10):
        R = RandomSeed()
        M = CheckRandom( R, lNumber )
        print( '로봇 ', i, '의 숫자:', R, '맞힌 개수:' , M )

        lCheck.append( M )

    print( lCheck )
    lCheck.sort(reverse=True)
    print( lCheck )


    i = lCheck.index( myM ) + 1

    if i == 10:
        print( '당신은 꼴찌입니다.!!!' )
    else:
        print( '당신은 ', i, '등 !' )

    ans = input( '계속하시겠습니까 ? ' )
    if ans == 'n' or ans == 'N' :
        break;



