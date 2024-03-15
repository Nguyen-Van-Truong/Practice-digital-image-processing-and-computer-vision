# 1. Khởi tạo và Truy cập các Phần tử của Mảng
arr = [1, 2, 3, 4, 5]  # Khởi tạo mảng
print("Mảng ban đầu:", arr)

# Truy cập các phần tử
print("Phần tử đầu tiên:", arr[0])
print("Phần tử cuối cùng:", arr[-1])

# 2. Thêm và Xóa các Phần tử
arr.append(6)  # Thêm vào cuối mảng
print("Thêm phần tử:", arr)

arr.insert(1, 10)  # Chèn phần tử vào vị trí bất kỳ
print("Chèn phần tử:", arr)

arr.remove(10)  # Xóa phần tử
print("Xóa phần tử:", arr)

# 3. Duyệt qua Mảng
for element in arr:
    print(element, end=' ')
print()

# 4. Các phép toán phổ biến trên Mảng
print("Độ dài mảng:", len(arr))
print("Tổng mảng:", sum(arr))
print("Phần tử lớn nhất:", max(arr))
print("Phần tử nhỏ nhất:", min(arr))

# 5. Sử dụng Mảng từ Thư viện NumPy
import numpy as np

np_arr = np.array([1, 2, 3, 4, 5])
print("Mảng NumPy:", np_arr)
print("Cộng 10 vào mỗi phần tử:", np_arr + 10)

# Làm việc với mảng 2 chiều
np_arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Mảng 2 chiều:\n", np_arr_2d)

# 6. Tìm kiếm và Sắp xếp trong Mảng
arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr.sort()  # Sắp xếp mảng
print("Mảng đã sắp xếp:", arr)

print("Vị trí của phần tử '5':", arr.index(5))

# 7. List Comprehensions
# Tạo một mảng mới với các giá trị được nhân đôi từ mảng ban đầu
doubled_arr = [x * 2 for x in arr]
print("Mảng với các phần tử được nhân đôi:", doubled_arr)

# 8. Slice Mảng
# Lấy một phần của mảng từ vị trí thứ 2 đến thứ 5
slice_arr = arr[2:6]
print("Slice mảng:", slice_arr)

# 9. Mảng Nhiều Chiều với NumPy
import numpy as np

# Tạo một mảng 2 chiều
np_arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Mảng 2D NumPy:\n", np_arr_2d)

# Truy cập phần tử ở hàng thứ 2, cột thứ 3
print("Phần tử ở hàng 2 cột 3:", np_arr_2d[1, 2])

# 10. Một số hàm hữu ích khác trong NumPy
print("Tổng của mỗi cột:", np.sum(np_arr_2d, axis=0))
print("Tổng của mỗi hàng:", np.sum(np_arr_2d, axis=1))
print("Mảng sau khi chuyển vị:\n", np_arr_2d.T)

