#Câu 3: Tính điểm trung bình
'''
Yêu cầu:
Viết chương trình nhập vào điểm ba môn Toán, Lý, Hóa của một học sinh. In ra
điểm trung bình của học sinh đó với hai số lẻ thập phân.
'''

import math
Toan=float(input("Nhap diem toan: "))
Ly=float(input("Nhap diem ly: "))
Hoa=float(input("Nhap diem hoa: "))
while(Toan<0 or Ly<0 or Hoa<0 or Toan >10 or Ly>10 or Hoa>10):
 Toan=float(input("Nhap diem toan: "))
 Ly=float(input("Nhap diem ly: "))
 Hoa=float(input("Nhap diem hoa: "))
dtb=(Toan + Ly + Hoa)/3
print("Diem trung binh: ",dtb)
