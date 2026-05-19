print('-- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI --')
while True:
    try:
        new_emp = int(input('Nhập số lượng nhân viên mới:'))
        if new_emp > 0:
            print(f'Ghi nhận thành công {new_emp} nhân viên mới')
            break;
        else :
            print('Số lượng không hợp lệ')
    except ValueError:
        print(" Lỗi: Vui lòng nhập một số nguyên hợp lệ.")