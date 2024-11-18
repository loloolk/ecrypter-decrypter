import random
import json

#1 decode key, 1 encode keys everyone knows

class Encrypter():
    def __init__(self):
        self.createKey()
        self.simplifyKey()
        print("Your key is: " + self.upKey)
        self.createEncryption()
        self.createCypher()
        alphabet = ['@', '6', '"', '^', '!', 'Q', 'E', ')', 'U', 'X', '&', 'Y', 'G', 'o', '*', '{', 'l', 'x', '3', ';', "'", '8', 'N', '2', 'T', 'F', 's', '>', 'e', '-', 'k', ' ', '\\', '#', ':', '.', ']', 'g', '%', 'f', 'q', '4', '}', 'u', '$', 'T', 'z', '|', '(', '9', 'h', '1', 'Z', 'a', '7', 'R', '<', ',', 'K', '/', 'w', 'P', 'C', 'y', 'r', 'L', 'M', 'p', '0', '5', 'O', 'Q', 'n', 'c', '[', 'v', 'S', 't', '=', 'j', 'A', 'J', 'W', '_', 'D', 'I', 'b', 'i', 'B', 'd', 'V', 'm', '+', 'R', 'S', '~', 'H', '`', '?']
        self.alphabet = alphabet

    def createKey(self): #Creates a 676 digit binary key (prevents 10 of the same char in a row)
        key = ""
        for x in range(676):
            if key[-9:] != "000000000" and key[-9:] != "111111111":
                key += str(random.randint(0, 1))
            elif key[-9:] == "000000000":
                key += "1"
            elif key[-9:] == "111111111":
                key += "0"
            else:
                print("this should not happen")
        self.key = key

    def simplifyKey(self): 
        count = 1
        upKey = ""
        for x in range(len(self.key) - 1):
            current = self.key[int(x)]
            if self.key[int(x)] == self.key[int(x) + 1]:
                count += 1
            else:
                if count > 1:
                    upKey += str(count)
                upKey += str(current)
                count = 1
        if count != 1:
            upKey += str(count)
        upKey += self.key[len(self.key) - 1]

        self.upKey = upKey

    def createEncryption(self): #creates a code from key
        with open("config.json", "r") as f:
            oec = json.load(f)["list"]
            ec = []
            for x in range(len(self.key)):
                v = self.key[int(x)]
                if v == "0":
                    if [oec[int(x)][0], oec[int(x)][1]] not in ec:
                        ec.append([oec[int(x)][0], oec[int(x)][1]])
                    else:
                        ec.append([oec[int(x)][1], oec[int(x)][0]])
                elif v == "1":
                    if [oec[int(x)][1], oec[int(x)][0]] not in ec:
                        ec.append([oec[int(x)][1], oec[int(x)][0]])
                    else:
                        ec.append([oec[int(x)][0], oec[int(x)][1]])
            self.ec = ec

    def createCypher(self): #creates a cypher from the code
        aligned = []
        for x in range(len(self.ec)):
            if x % 2 == 0:
                aligned.append([self.ec[int(x)]] + [self.ec[int(x) + 1]])
        self.aligned = aligned

    def encode(self, phrase): #encrypts the phrase
        encrypted = []
        for x in range(len(phrase)):
            index = self.alphabet.index(phrase[int(x)])
            encrypted += self.aligned[int(index)][int(self.key[int(index)])]
        
        eWord = ''.join(encrypted)
        return eWord


ec = Encrypter()
with open("encoded.ecdc", "w") as f:
    f.write(ec.encode("Hello World!"))