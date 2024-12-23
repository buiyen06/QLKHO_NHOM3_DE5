import csv 
import datacsv 
def xemcuahang() : 
 read = csv.reader(datacsv.file) 
 data = list(read)
 xuli = data[1:]
 for i in range(1 , len(xuli)) : 
    for j in range(0 , len(xuli)-1 ) : 
        if int(xuli[j][0][3:]) > int(xuli[j+1][0][3:]) : 
            xuli[j] , xuli[j+1] = xuli[j+1],xuli[j] 
 with open("E:\\nhom3\\csv_file\\dulieusapxep.csv",mode = "w", encoding = "utf-8", newline='') as file : 
        writer = csv.writer(file)
        write = writer.writerow(data[0]) 
        write = writer.writerows(xuli) 
 with open("E:\\nhom3\\csv_file\\dulieusapxep.csv",mode = "r", encoding = "utf-8") as file :
    reader = csv.DictReader(file)
    print("MÃ CỬA HÀNG","  ","TÊN CỬA HÀNG","  ","  TỔNG SỐ KHO")
    for hienbang in reader : 
         print("|",hienbang["Mã cửa hàng"],"  |    ",hienbang["Tên cửa hàng"],"   |   ",hienbang["Tổng số kho"],"     |")
         print("____"*10)




    
    
    
    
    
           