import random
import linuxlziw
day = 1

def monthend(day):
    if day == 31 :
        day = 1 
        print("zaczyna się nowy miesiac")
    else :
        print(f"obecny dzien to {day} -y miesiąca")
        

def kompas():
    Strony = ["północ", "zachód", "wschód", "południe"]
    return random.choice(Strony)
def wiatr(NWES,):
    print(f"nadchodzi wiatr z strony {NWES}")
def sztorm(NWES,):
    print(f"nadchodzi sztorm z {NWES} tego dnia lodzie nie mogą przypływać oraz odpływwać z platformy")
def deszcz(NWES):
    print(f"deszcz nadchodzi ze strony {NWES}")
listaf = [ "wiatr", "sztorm", "deszcz"]

def wydarzenia():
    monthend(day)
    NWES = kompas()
    wydarzenie = random.choice(listaf)
    if wydarzenie == "wiatr" :
        wiatr(NWES)
    elif wydarzenie == "sztorm" :
        sztorm(NWES)
    elif wydarzenie == "deszcz" :
        deszcz(NWES)

linuxlziw.linuksexclusiv()

wydarzenia()


