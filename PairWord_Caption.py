import pandas as pd
import re
import numpy as np
from collections import Counter
from collections import OrderedDict
from collections import *

file = pd.read_csv(input("File yang akan diolah menjadi Dataset pasangan kata :\n"))
df= file[file.columns[2]]
id = 1
idx = 0

allcaption = ""

for i in list(df):
    allcaption += i
    allcaption=allcaption.replace("\n","")
    capsplit = allcaption.split()
    length = len(capsplit)
    caption = []
    for i in range (length):
        word = capsplit[i]
        if word [0] == "#" or word [0] == "@" :
            break
        if word [0] == " " :
            break
        wordcaps = ""
        for y in word :
            if ord (y) == 126 :
                wordcaps = wordcaps + ""
            elif ord (y) > 96 and ord (y) < 123 :
                wordcaps = wordcaps + y
        caption.append(wordcaps)

    pairwordcaption = []
    for i in range (length -1):
        pairwords = caption[i] + " " + caption[i+1]
        pairwordcaption.append(pairwords)

    datanew = pd.DataFrame(columns=["id User", "word1", "word2", "freqs"])
    jmlh = Counter ()
    for i in pairwordcaption :
        jmlh [i] += 1
    jmlh = OrderedDict(jmlh)
    for i in jmlh :
        a= i.split ()
        if (len(a) > 1):
            datanew = datanew.append({"id User" : [id], "word1" : a[0], "word2" : a[1], "freqs" : jmlh [i]})
            with open(databaru, 'a', encoding="utf-8", newline='') as f:
                data.to_csv(f, header=f.tell()==0)
        idx += 1
    id_user += 1
    
databaru = "PairWord_Caption.csv"
#print (databaru)
databaru.to_csv("PairWord_Caption.csv")
