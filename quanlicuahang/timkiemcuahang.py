import datacsv 
def timkiemcuahang() :
 a= list(datacsv.read) 
 check = 0 
 checkloi = 0 
 macuahang = input("nhập mã cửa hàng muốn tìm kiếm ")
 for i in a : 
  if macuahang in i :
   check = a.index(i)
  else :
    checkloi = 1 
 if checkloi == 1 :
  print("CỬA HÀNG KHÔNG TỒN TẠI") 
 ketquatimkiem = a[check]
 print("Mã cửa hàng: {}\nTên cửa hàng: {}\nTổng số kho: {}".format(a[check][0],a[check][1],a[check][2]))