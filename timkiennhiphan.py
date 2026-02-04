def rom(arr, left, right, n):
    while(left <= right):
        idx=( right+left)//2
        a=arr[idx]
        print(f"🎯 Đang kiểm tra số: {a}")
        if a==n:
            return True
        else:
            if (a<n):
                left=idx+1
            else : 
                right=idx-1
    return False  

def read_int(prompt):
    s = input(prompt)
    s = s.replace("\ufeff", "").strip()
    try:
        return int(s)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        raise SystemExit(1)

def read_int_list(prompt):
    s = input(prompt)
    s = s.replace("\ufeff", "").strip()
    if not s:
        return []
    parts = s.replace(";", ",").split(",")
    vals = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        try:
            vals.append(int(p))
        except ValueError:
            print(f"Giá trị không hợp lệ, bỏ qua: {p}")
    return vals

def read_choice(prompt):
    s = input(prompt)
    s = s.replace("\ufeff", "").strip().lower()
    if s in ("y", "yes", "có", "co"):
        return True
    if s in ("n", "no", "không", "khong"):
        return False
    return False

def first_pos(arr, n):
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        idx = (left + right) // 2
        a = arr[idx]
        if a >= n:
            if a == n:
                res = idx
            right = idx - 1
        else:
            left = idx + 1
    return res

def last_pos(arr, n):
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        idx = (left + right) // 2
        a = arr[idx]
        if a <= n:
            if a == n:
                res = idx
            left = idx + 1
        else:
            right = idx - 1
    return res

arr = [1,2,5,7,8,10,15,18,20,14,27]
extra = read_int_list("Nhập thêm số (phân cách bằng dấu phẩy, để trống nếu không): ")
arr.extend(extra)
arr.sort()
print(f"Mảng sau sắp xếp: {arr}")
n = read_int("Nhập số cần tìm: ")
mode_all = read_choice("Tìm tất cả vị trí trùng? (y/n): ")
if mode_all:
    f = first_pos(arr, n)
    if f != -1:
        l = last_pos(arr, n)
        positions = list(range(f, l + 1))
        print(f"Tìm thấy {len(positions)} vị trí của {n}: {positions}")
    else:
        print(f"Không tìm thấy số {n} trong mảng")
else:
    left, right = 0, len(arr) - 1
    if rom(arr, left, right, n):
        print(f"Số {n} có trong mảng")
    else:
        print(f"Không tìm thấy số {n} trong mảng")
