new_employee_count = 0

while new_employee_count <= 0:

    new_employee_count = int(
        input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")
    )

    if new_employee_count <= 0:

        print("LỖI: Số lượng nhân sự phải lớn hơn 0!")


print(" Ghi nhận thành công.")
print("Số lượng nhân sự mới là:", new_employee_count)
