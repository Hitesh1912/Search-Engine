import os
import string
import bs4 as bsnew

def numsOnly(inputString):# function to make sure it contains only the digits and punctuations and no alphabets
    if any(c.isalpha() for c in inputString):
        return False
    if any(char.isdigit() for char in inputString):
        return True

def generateTokens(dir):
    filelist = os.listdir(os.path.abspath(dir))
    validTokens = []
    punctuation = string.punctuation.replace("-", "")  # retaining hyphen- question
    nums_punctuation="!\"#$%&'()*+/;<=>?@[\]^_`{|}~"   # removing . , - : for digits
    for f in filelist:
        if len(f) <= 1:
            continue
        full_path=dir+"//"+f
        file_contents = open(full_path, "r", encoding='utf-8').read()
        bs = bsnew.BeautifulSoup(file_contents, "html.parser")
        content = bs.find("pre")
        raw = content.get_text()
        contents = str(raw).split()
        for t in contents:
            if numsOnly(t):
                for digit in t:
                    if digit in nums_punctuation:
                        t=t.replace(digit,"")
                validTokens.append(t.strip(string.punctuation))
                continue
            t = t.lower()
            for char in t:
                if char in punctuation:
                    t = t.replace(char, "")
            if len(t)==1 and t== "-":
                continue
            if len(t) >= 1:
                validTokens.append(t)
        f=f.replace(".html","")
        filename = r"tokenized_Files/" + f + ".txt"
        newFile = open(filename, 'w', encoding='utf-8')
        newFile.write(str(validTokens))
        validTokens = []
        newFile.close()


if __name__ == "__main__":
    fullPath = input("Enter the absolute path to the folder having raw documents")
    type(fullPath)
    #D:\\IR_project\\rawDocuments
    generateTokens(fullPath)
