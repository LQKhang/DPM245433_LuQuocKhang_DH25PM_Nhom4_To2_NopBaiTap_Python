#Câu 2: Tính giờ phút giây
'''
Yêu cầu:
Nhập vào số giây bất kỳ t. Tính và xuất ra dạng
Giờ:Phút:Giây
Ví dụ: Nhập 3750 thì xuất ra 1:2:30 AM
Nhập 51100 thì xuất ra 2:11:40 PM
'''

import math
t=int(input("Nhap so giay: "))
h=(t//3600)%24
m=(t%3600)//60
s=(t%3600)%60

if(h>=13):
    h%=12
    print(h,":",m,":",s,"PM")
else:
    print(h,":",m,":",s,"AM")

