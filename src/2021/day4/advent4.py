import numpy as np

from data import trekking, kaarten

checkkaarten = kaarten * 0
kaartdone = [0] * len(kaarten)


def Check_number(kaart, nummer, checkkaart):
    for i in range(5):
        if nummer in kaart[i]:
            for j in range(5):
                if nummer == kaart[i][j]:
                    checkkaart[i][j] = 1
    return checkkaart


def Check_kaart(checkkaart):
    if any(checkkaart.sum(axis=1) == 5) or any(checkkaart.sum(axis=0) == 5):
        return True
    else:
        return False


notFound = True
showFirst = True

for n in trekking:
    if notFound:
        for i in range(len(kaarten)):
            checkkaarten[i] = Check_number(kaarten[i], n, checkkaarten[i])
            if Check_kaart(checkkaarten[i]):
                kaartdone[i] = 1
                if sum(kaartdone) == 1 and showFirst:
                    showFirst = False
                    print("winnaar kaart: " + str(i) + " Na trekking " + str(n))
                    print("De winnende kaart: \n")
                    print(kaarten[i])
                    print("\nDe afgekruiste nummers op de kaart: \n")
                    print(checkkaarten[i])
                    print(
                        "\nDe sum of all unmarked numbers times the number that was just called: "
                        + str(np.multiply(kaarten[i], 1 - checkkaarten[i]).sum() * n)
                    )
                elif sum(kaartdone) == 100:
                    print(
                        "\nDe laatste winnende kaart: "
                        + str(i)
                        + " Na trekking "
                        + str(n)
                    )
                    print("De winnende kaart: \n")
                    print(kaarten[i])
                    print("\nDe afgekruiste nummers op de kaart: \n")
                    print(checkkaarten[i])
                    print(
                        "\nDe sum of all unmarked numbers times the number that was just called: "
                        + str(np.multiply(kaarten[i], 1 - checkkaarten[i]).sum() * n)
                    )
                    notFound = False
                    break
