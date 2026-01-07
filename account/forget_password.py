def quen_mat_khau():
    print("=== QUÊN MẬT KHẨU ===")
    username = input("Nhập tên đăng nhập: ")

    for u in users:
        if u["username"] == username:
            while True:
                mk_moi = input("Nhập mật khẩu mới: ")
                mk_xac_nhan = input("Xác nhận mật khẩu mới: ")

                if mk_moi == mk_xac_nhan:
                    u["password"] = mk_moi
                    print("✅ Đổi mật khẩu thành công!")
                    return
                else:
                    print("❌ Mật khẩu không khớp, thử lại!")

    print("❌ Không tìm thấy tài khoản!")
