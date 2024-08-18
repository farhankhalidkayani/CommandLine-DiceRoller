import argparse
import random

parser = argparse.ArgumentParser(description="A dice roller commandline application.")
parser.add_argument("diceInformation", type=str, help=" It takes user input in form of (noOfDice)d(FacesOfDice) ")
parser.add_argument("-l", "--log", type=str, help="To store the output on an external file")
parser.add_argument("-r", "--repeat", type=int,default=1, help="To repeat the roll given number of times")

args = parser.parse_args()


def diceGetter():
    noOfDice = ""
    dIndex = 0
    noOfFaces = ""
    for i in range(len(args.diceInformation)):
        if args.diceInformation[i] != 'd':
            noOfDice += args.diceInformation[i]
        if args.diceInformation[i] == "d":
            dIndex = i
            break
    for i in range(dIndex + 1, len(args.diceInformation)):
        noOfFaces += args.diceInformation[i]
    noOfDice = int(noOfDice)
    noOfFaces = int(noOfFaces)
    return [noOfDice, noOfFaces]


def diceCalculator(noOfDice, noOfFaces):
    results = []
    for i in range(noOfDice):
        results.append(random.randint(1, noOfFaces))
    return results


def resultPrinter(results):
    return (f"Rolls: {results} \nTotal: {sum(results)} \nAverage: {sum(results) // len(results)}\n")


def logger(results):
    with open(args.log, "a") as file:
        file.writelines(resultPrinter(results))


if args.diceInformation:
        for i in range(args.repeat):
            noOfDice, noOfFaces = diceGetter()
            results = diceCalculator(noOfDice, noOfFaces)
            print(resultPrinter(results))
            if args.log:
                logger(results)
