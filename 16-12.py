# -*- coding:UTF-8 -*-
import os

def hextoten():
    dd= ['0x30','0x82','0x05','0xD8','0x30','0x82','0x03']
    for x in dd:
        y = int(x,16)
        print(y)
        print(chr(y))

def chartohex():
    st="DST Root CA X30"
    key = [hex(ord(y)) for y in st ]
    print(key)
def tentohex():

    f=open("C:/Users/Administrator/Desktop/my2.cer",'rb')
    x = f.read()
    key = [hex(y) for y in x]
    num=0
    d=[]
    for y in key:
        d.append(y)
        num +=1
        if num == 16:
            print(d)
            num = 0
            d = []
    print(d)

def main():
        tentohex()
if __name__=="__main__":
    main()