import random as rand
from tqdm import tqdm

import argparse
import os
import time
parser = argparse.ArgumentParser(description="Practice")
parser.add_argument("--charset", dest="charset", help="Hiragana or Katakana")
parser.add_argument("--fro", dest="fro", type=str, help="Start romaji (e.g., ka)")
parser.add_argument("--to", dest="to", type=str, help="End romaji (e.g., so)")
parser.add_argument("--endless", action="store_true", help="Practice endlessly until interrupted")
args = parser.parse_args()

katakana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ"
hiragana = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
romaji = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo",
    "ra", "ri", "ru", "re", "ro",
    "wa", "o", "n",
    "ga", "gi", "gu", "ge", "go",
    "za", "ji", "zu", "ze", "zo",
    "da", "ji", "zu", "de", "do",
    "ba", "bi", "bu", "be", "bo",
    "pa", "pi", "pu", "pe", "po"
]

# indices = list(range(len(katakana)))
def practice(kara: str, made: str, charset: str):
    
    alphabet = hiragana if charset == 'hiragana' else katakana

    indices = list(range(romaji.index(kara),romaji.index(made)+1))
    rand.shuffle(indices)
    total = len(indices)
    correct = 0
    wrongdict = {}
    for i, idx in enumerate(tqdm(indices, desc="Progress", unit="char"), 1):
        print(f"[{i}/{total}]: {alphabet[idx]}")
        inp = input().lower()
        if(inp == romaji[idx]):
            correct+=1
        else:
            wrongdict[alphabet[idx]]=romaji[idx]
            if(inp != "ans"):
                print("Try again")
                while True:
                    inp = input().lower()
                    if inp == romaji[idx]:
                        break
                    if inp == "ans":
                        print(f"{alphabet[idx]} = {romaji[idx]}")
                        break
                    print("Try again")
            else: 
                print(f"{alphabet[idx]} = {romaji[idx]}")
                time.sleep(1)

            # print(wrongdict)
        os.system('cls' if os.name == 'nt' else 'clear')
        # print()

    print(f"Wrong: {total-correct}, Accuracy: {(correct/total):.2f}")
    if(len(wrongdict)>0):
        print(f"Wrong: {wrongdict}")
    else:
        print("Congratulations")

def practice_endless(kara: str, made: str, charset: str):
    alphabet = hiragana if charset == 'hiragana' else katakana
    
    tot = 0
    while(True):
        indices = list(range(romaji.index(kara),romaji.index(made)+1))
        rand.shuffle(indices)
        total = len(indices)
        wrong = 0
        for idx in indices:
            tot+=1
            print(f"[{tot}]: {alphabet[idx]}")
            inp = input().lower()
            if(inp != romaji[idx]):
                wrong+=1
                if(inp != "ans"):
                    print("Try again")
                    while True:
                        inp = input().lower()
                        if inp == romaji[idx]:
                            break
                        if inp == "ans":
                            print(f"{alphabet[idx]} = {romaji[idx]}")
                            break
                        print("Try again")
                else: 
                    print(f"{alphabet[idx]} = {romaji[idx]}")
                    time.sleep(1)

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"Accuracy: {((tot - wrong) / tot):.2f}")

if (__name__ == "__main__"):
    
    if args.fro and args.to:
        if args.endless:
            practice_endless(args.fro, args.to, args.charset)
        else:
            practice(args.fro, args.to, args.charset)
    else:
        if args.endless:
            practice_endless("a", "po",args.charset)
        else:
            # default: all katakana
            practice("a", "po",args.charset)