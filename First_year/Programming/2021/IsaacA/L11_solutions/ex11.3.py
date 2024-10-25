import random

def lottery(wheels):
    f = open("extractions.txt", "w")
    for r in wheels:
        f.write(r + ": ")
        extractions = random.sample(range(1, 91), 5)
        for e in extractions:
            f.write(str(e) + " ")
        f.write("\n")
    f.close()


lottery(["Roma", "Milano", "Bologna", "Firenze", "Genova", "Napoli"])