# -*- coding:utf-8 -*-
import os

ll=[]
dicts={}
workdir='/test'
basefile='big.txt'

def words_count(data,d):
    for k in data:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    return d


if __name__ == "__main__":

    file_object = open('/test/big.txt', 'rb')
    try:
          while True:
                chunk = file_object.read(1024)
                if not chunk:
                      break
                ll = chunk.replace('\n', '').split(';')
                dicts = words_count(ll, dicts)
    finally:
          file_object.close( )


    temp=sorted(dicts.iteritems(), key=lambda d:d[1], reverse = True)
    asc=temp[:5]
    for t in asc:
        print t[0],":",t[1]



