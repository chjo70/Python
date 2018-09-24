

def CountOfChar( line ):


    return 0;


##############################################
f = open( "fire.txt", 'r' )
lines = f.readlines()
for line in lines:
    # print(line)
    coc = CountOfChar(line)
f.close()
print( '문자 수 :' , coc )

