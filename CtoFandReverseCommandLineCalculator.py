#!/usr/bin/python
import argparse

tempParser = argparse.ArgumentParser(description = "Has information needed to use calculator")

tempParser.add_argument("Temp", type = int, help = "The Temperature Number (An Integer)")
tempParser.add_argument("Type", type = str, help = "What unit is the temperature in? ")

args = tempParser.parse_args()

def cToF(temp):
    return round((temp * (9/5)) + 32, 2)
def fToC(temp):
    return  round((temp - 32) * (5/9), 2)

if args.Type == "c":
    print(cToF(args.Temp))
else:
    print(fToC(args.Temp))


