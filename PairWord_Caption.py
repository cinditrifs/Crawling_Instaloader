import pandas as pd
import re
import numpy as np
from collections import Counter
from collections import OrderedDict
from collections import *

file = pd.read_csv(input("File yang akan diolah menjadi pasangan kata :\n"))
#file = pd.read_csv("Data_Crawling_Instagram.csv")
df= file[file.columns[2]]

pasangankatalist = []
perulanganlis = []

allcaption = ""

for i in list(df):
    allcaption += i
    allcaption=allcaption.replace("\n"," ") #menggabungkan seluruh caption 
    if allcaption == "#" :
        break
    allcaption=re.sub(r'[^a-zA-Z0-9 ]',r'',allcaption) #menghapus semua karakter 
    allcaption = allcaption.lower ()
    caption = allcaption.split()
    pasangankata = [caption[i] + " " + caption[i+1] for i in range(len(caption)-1)]
    perulangan = Counter(pasangankata)

   
data = pd.DataFrame({"PairWords":perulangan}) #LEVEL 2
data.to_csv ("PasanganKata.csv")
