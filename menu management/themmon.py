def add_item():
    print("\n--- THÊM MÓN ĂN MỚI ---")
    ten_mon = input("Nhập tên món: ")
    gia = int(input("Nhập giá: "))
    loai = input("Nhập loại món: ")
    mon_moi = {
        "id": len(menu_list) + 1,
        "ten_mon": ten_mon,
        "gia": gia,
        "loai": loai,
        "trang_thai": "Còn hàng",
    }
    menu_list.append(mon_moi)
    save_data()

    print("✅ Thêm món thành công!")
