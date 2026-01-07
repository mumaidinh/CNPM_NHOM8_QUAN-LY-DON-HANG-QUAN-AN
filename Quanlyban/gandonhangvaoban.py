def gan_don_vao_ban():
    try:
        ma_don = int(input("Nhập Mã đơn hàng: "))
        ma_ban = int(input("Nhập Số bàn: "))
        for ban in ban_list:
            if ban["ma_ban"] == ma_ban:
                if ban["trang_thai"] == "Trống":
                    ban["trang_thai"] = "Có khách"
                    ban["ma_don"] = ma_don
                    print(f"✅ Đã gán đơn {ma_don} vào bàn {ma_ban}")
                else:
                    print("❌ Bàn này đang có khách!")
                return
        print("❌ Không tìm thấy bàn!")
    except: print("❌ Vui lòng nhập số!")
    save_data()
