import random



def kompas():
    Strony = ["północ", "zachód", "wschód", "południe"]
    return random.choice(Strony)
def wiatr(NWES,):
    print(f"nadchodzi wiatr z strony {NWES}")
def sztorm(NWES,):
    print(f"nadchodzi sztorm z {NWES} tego dnia lodzie nie mogą przypływać oraz odpływwać z platformy")
listaf = [ "wiatr", "sztorm"]

class surowiec():
    
    def __init__(self)

def wydarzenia(NWES):
    NWES = kompas()
    wydarzenie = random.choice(listaf)
    if wydarzenie == "wiatr" :
        wiatr(NWES)
    elif wydarzenie == "sztorm" :
        sztorm(NWES)


