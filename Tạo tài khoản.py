# Danh sách lưu tài khoản nhân viên
employees = []

# Biến lưu trạng thái đăng nhập
current_user = None


def register():
    print("\n--- ĐĂNG KÝ TÀI KHOẢN NHÂN VIÊN ---")
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")

    # Kiểm tra trùng username
    for emp in employees:
        if emp['username'] == username:
            print("❌ Tên đăng nhập đã tồn tại!")
            return

    employees.append({
        'username': username,
        'password': password
    })

    print("✅ Đăng ký thành công!")


def login():
    global current_user
    print("\n--- ĐĂNG NHẬP ---")
    username = input("Tên đăng nhập: ")
    password = input("Mật khẩu: ")

    for emp in employees:
        if emp['username'] == username and emp['password'] == password:
            current_user = username
            print(f"✅ Đăng nhập thành công! Xin chào {username}")
            return

    print("❌ Sai tên đăng nhập hoặc mật khẩu!")


def logout():
    global current_user
    if current_user is None:
        print("⚠️ Chưa có ai đăng nhập!")
    else:
        print(f"👋 {current_user} đã đăng xuất")
        current_user = None


def menu():
    print("\n====== MENU ======")
    print("1. Đăng ký tài khoản nhân viên")
    print("2. Đăng nhập")
    print("3. Đăng xuất")
    print("4. Thoát")


# Chương trình chính
while True:
    menu()
    choice = input("Chọn chức năng: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        logout()
    elif choice == "4":
        print("🚪 Thoát chương trình")
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
