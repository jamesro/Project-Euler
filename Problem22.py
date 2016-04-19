"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv
def GetNames(filename):
    with open(filename) as f:
        items = csv.reader(f)
        names = [item for item in items][0]
    return names

def SumAlphaValues(name):
    return sum( [ord(char)-64 for char in name] )  # -64 for capital letters, -96 for lower case

if __name__ == "__main__":
    names = sorted(GetNames("names.txt"))

    print(sum( [(i+1)*SumAlphaValues(names[i]) for i in range(len(names))] ) )