
import random
from typing import List
import os
import sys
os.system('cls')
os.chdir(os.path.dirname(__file__))

bytesm=3#random.randint(1234,123456)
i=0;

mbytes=bytesm/2

percent=round((100*bytesm-mbytes)/bytesm)
print(bytesm)
print(percent)

def simple_download(lista:List)->None:
    v=[x for x in lista if x.endswith('.mp4')][0]
    with open(v,'rb') as file:
        data_size=os.path.getsize(v)
        mb=data_size/1024000
        print(f"Size of this file is{data_size}bytes and in{mb} MBytes")
        data={'file_data':file.read(),"size":data_size}
        
        return  data
        

def usual():
    l=os.listdir("./")
    c=filter(lambda x : x.endswith('.mp4'), l)
    x=[y for y in l if y.endswith('.mp4')]
    print('valor de x '+x[0])
    print(list(c))
    print(l)

usual()
dados=simple_download(os.listdir("."))

file="../"
with open(file+"/file.mp4",'wb') as file:
    file.write(dados.get('file_data'))
    print("file set")