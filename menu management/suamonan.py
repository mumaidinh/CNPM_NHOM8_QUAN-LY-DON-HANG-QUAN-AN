def sua_mon_an():
    hien_thi_menu(menu_list)

    try:
        id_mon = int(input("Nhập ID món cần sửa: "))
    except:
        print("❌ ID phải là số!")
        return

    mon = tim_mon_theo_id(id_mon)
    if not mon:
        print("❌ Không tìm thấy món!")
        return

    print("\n🔧 ĐỂ TRỐNG NẾU KHÔNG MUỐN SỬA")

    ten_moi = input(f"Tên món ({mon['ten_mon']}): ").strip()
    if ten_moi:
        mon["ten_mon"] = ten_moi

    gia_moi = input(f"Giá ({mon['gia']}): ").strip()
    if gia_moi:
        try:
            mon["gia"] = int(gia_moi)
        except:
            print("⚠️ Giá không hợp lệ, giữ nguyên!")

    loai_moi = input(f"Loại ({mon['loai']}): ").strip()
    if loai_moi:
        mon["loai"] = loai_moi

    print("Trạng thái:")
    print("1. Còn hàng")
    print("2. Hết hàng")
    tt = input("Chọn (Enter để giữ nguyên): ").strip()
    if tt == "1":
        mon["trang_thai"] = "Còn hàng"
    elif tt == "2":
        mon["trang_thai"] = "Hết hàng"

    save_data()
    print("✅ Cập nhật món ăn thành công!")
