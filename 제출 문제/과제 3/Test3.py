

def CountOfChar( line ):

    co = 0;
    for ch in line:
        #print( ch )
        if ch != ' ':
            co = co + 1
    return co;

def CountOfWord( line ):

    co = 0;
    s = line.replace("\n", "")
    s = s.split(" ")
    #print( s )
    co = len( s )
    nullspace = s.count('')
    #print( co, nullspace )
    return co - nullspace;


##############################################
filenames = [ 'fire.txt', 'wheel.txt', 'lever.txt', 'agriculture.txt', 'earthware.txt'  ]

for filename in filenames:
    coc = 0;
    cow = 0;
    meanw = 0.0;
    print( filename )
    f = open( filename, 'r' )
    lines = f.readlines()
    for line in lines:
        # print(line)
        coc = CountOfChar(line) + coc;
        cow = CountOfWord(line) + cow;
    f.close()

    meanw = coc / cow;

    print( '- total characters: ' , coc )
    print( '- total words: ', cow )
    print( '- average characters per words: ', '%.3f' % meanw )
