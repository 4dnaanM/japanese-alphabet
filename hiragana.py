import random as rand
from tqdm import tqdm
hiragana = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"
english = [
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

indices = list(range(len(hiragana)))
rand.shuffle(indices)
total = len(indices)
correct = 0
wrongdict = {}
for i, idx in enumerate(tqdm(indices, desc="Progress", unit="char"), 1):
    print(f"[{i}/{total}]: {hiragana[idx]}")
    inp = input().lower()
    if(inp == english[idx]):
        correct+=1
    else:
        wrongdict[hiragana[idx]]=english[idx]
        if(inp != "ans"):
            print("Try again")
            while True:
                inp = input().lower()
                if inp == english[idx]:
                    break
                if inp == "ans":
                    print(f"{hiragana[idx]} = {english[idx]}")
                    break
                print("Try again")
        else: 
            print(f"{hiragana[idx]} = {english[idx]}")

        print(wrongdict)
    print()

print(f"Wrong: {total-correct}, Accuracy: {correct/total}")
if(len(wrongdict)>0):
    print(f"Wrong: {wrongdict}")
else:
    print("Congratulations")