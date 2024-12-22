import csv 
import datacsv 
def xoacuahang():
 a= list(datacsv.read)
 b = input("Nhập mã cửa hàng")
 check = 0 
 for i in a :
    if b in i :
        check = a.index(i)
        a.pop(check)
 datacsv.nhapdedulieu(a) 