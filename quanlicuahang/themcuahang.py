import datacsv
def themcuahang() :
 dulieuvao = []
 luutru = []
 a = input("nhập mã cửa hàng ")
 if datacsv.kiemtradulieu(a,0):
    print("cửa hàng đã tồn tại")
    a=input("nhập lại")
    b = input("Nhập tên cửa hàng ")
    c = int(input("Nhập tổng số kho "))
    if c > 5 :
       print("vượt quá giới hạn kho")
       c = int(input("nhập lại"))
       
    dulieuvao.append(a)
    dulieuvao.append(b)
    dulieuvao.append(c)
    datacsv.nhapdulieu(dulieuvao) 
 else :
  b = input("Nhập tên cửa hàng ")
  c = int(input("Nhập tổng số kho "))
  if c > 5 :
       print("vượt quá giới hạn kho")
       c = int(input("nhập lại"))

  dulieuvao.append(a)
  dulieuvao.append(b)
  dulieuvao.append(c)
  datacsv.nhapdulieu(dulieuvao) 
 

