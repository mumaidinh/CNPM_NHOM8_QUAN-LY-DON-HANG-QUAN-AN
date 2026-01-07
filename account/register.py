def register():
    while True:
        username = input("Tên đăng ký: ").strip()
        if username == "":
            print("❌ Tên đăng nhập không được để trống!")
            continue

        if any(u["username"] == username for u in users):
            print("❌ Username đã tồn tại!")
            continue
        break

    while True:
        password = input("Mật khẩu: ").strip()
        if password == "":
            print("❌ Mật khẩu không được để trống!")
            continue

        confirm = input("Nhập lại mật khẩu: ").strip()
        if confirm != password:
            print("❌ Mật khẩu không khớp!")
            continue
        break

    while True:
        print("Chọn loại tài khoản:")
        print("1. Quản lý")
        print("2. Nhân viên")
        role = input("Lựa chọn: ").strip()

        if role == "1":
            role = "quan_ly"
            break
        elif role == "2":
            role = "nhan_vien"
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

    users.append({
        "username": username,
        "password": password,
        "role": role
    })

    save_data()
    print("✅ Đăng ký thành công!")
