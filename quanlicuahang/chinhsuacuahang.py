import datacsv 
def chinhsuacuahang() :
 a = list(datacsv.read)
 b = input("Mã cửa hàng muốn chỉnh sửa")
 check = 0 
 for i in a :
    if b in i :
        check = a.index(i)
 print("1.Chỉnh sửa hết\n2.Chỉnh sửa 1 phần")
 luachon = int(input("nhập chức năng sửa "))
 if luachon == 1 : 
    a[check][1] = input("Tên cửa hàng : ")
    a[check][2] = int(input("Tổng số kho : "))
    if a[check][2] > 5 :
       print("Vượt quá giới hạn tổng số kho")
       while a[check][2] > 5 :
        a[check][2] = int(input("Nhập lại : "))
        if a[check][2] < 5 :
           break 
 elif luachon == 2 :
     print("1 Sửa tên cửa hàng\n2 Sửa tổng số kho")
     luachon2 = int(input())
     if luachon2 == 1 : 
         a[check][1] = input("Tên cửa hàng")
     elif luachon2 == 2 :
         a[check][2] = int(input("Tổng số kho"))
         if a[check][2] > 5 :
           print("Vượt quá giới hạn tổng số kho")
           while a[check][2] > 5 :
            a[check][2] = int(input("Nhập lại : "))
            if a[check][2] < 5 :
             break 
 datacsv.nhapdedulieu(a)
