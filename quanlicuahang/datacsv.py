import csv 
data = []
file = open ("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "r" , encoding = "utf-8")
read = csv.reader(file) 
def dong_file() :
     file.close()
def nhapdulieu(x) :
   if len(x) > 10 : 
         print("vượt quá số kí tự cho phép , mời nhập lại")
   elif len(x) == 0 :
         print("hãy nhập dữ liệu")
   else :
     with open("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "a" , encoding = "utf-8",newline ='') as file :
         du_lieu_nhap_vao = csv.writer(file)
         du_lieu_nhap_vao.writerow(x)
def nhapdulieu2(x) :
   if len(x) > 10 : 
         print("vượt quá số kí tự cho phép , mời nhập lại")
   elif len(x) == 0 :
         print("hãy nhập dữ liệu")
   else :
     with open("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "a" , encoding = "utf-8",newline = '') as file :
         du_lieu_nhap_vao = csv.writer(file)
         du_lieu_nhap_vao.writerows(x)
def doctheotieude(x) :
      with open("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "r" , encoding = "utf-8") as file :
            doc = csv.DictReader(file)
            for data in doc :
                  return (data[x])
def kiemtradulieu(x,y) :
 with open("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "r" , encoding = "utf-8") as file :
      read = csv.reader(file)
      for i in read  :
           if x in i[y] :
               return True
      return False 
        

def sapxepdulieu(x):            
 with open("E:\\nhom3\\csv_file\\dulieusapxep.csv",mode = "r", encoding = "utf-8") as file :
    reader = csv.reader(file)
    for i in reader :
        print(i[x])


def nhapdedulieu(x) :
 with open("E:\\nhom3\\csv_file\\ds_cua_hang.csv",mode = "w", encoding = "utf-8", newline = '') as file :
     writer = csv.writer(file)
     writer.writerows(x) 