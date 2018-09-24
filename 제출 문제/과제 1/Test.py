

def JULIUS_CAESAR( iString, iN ):

    print( iString, '->', iN, "코드" )
    for ch in iString:
        if ch.islower() :
            iCh = ( ord(ch) - ord('a') + iN ) % 26;
            iCh = ord('a') + iCh;
            print( chr(iCh), end="" )

        if ch.isupper() :
            iCh = (ord(ch) - ord('A') + iN) % 26;
            iCh = ord('A') + iCh;
            print( chr(iCh), end="" )

        if ch.isspace() :
            print( " ", end="")

    print("\n")


S1 = "Hsle ozpd l mwzddzx mpnzxp"
#for i in range( 1, 26):
#    JULIUS_CAESAR( S1, -i )

S2 = "2. Cngz oy znk yvuxz zngz oy vrgekj hkzckkt zcu zkgsy ul krkbkt vrgekxy cozn g hgrr"
#for i in range( 1, 26):
#    JULIUS_CAESAR( S2, -i )

S3 = "3. Patm labgxl bg max gbzam ldr"
#for i in range(1, 26):
#    JULIUS_CAESAR(S3, -i)

S4 = "4. Epib qa bpm vium wn i tqycql bpib gwc kivvwb tqdm eqbpwcb"
#for i in range(1, 26):
#    JULIUS_CAESAR(S4, -i)

S5 = "5. Ufyr kyicq y zgpb djw"
#for i in range(1, 26):
#    JULIUS_CAESAR(S5, -i)

JULIUS_CAESAR( S1, -11 )
JULIUS_CAESAR( S2, -6 )
JULIUS_CAESAR( S3, -19 )
JULIUS_CAESAR( S4, -8 )
JULIUS_CAESAR( S5, -24 )






