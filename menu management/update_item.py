
# ================== CẬP NHẬT TRẠNG THÁI MÓN ==================
def cap_nhat_trang_thai_mon(menu_list):
    print("\n--- NGỪNG / MỞ BÁN MÓN ---")
    id_mon = int(input("Nhập ID món: "))

    for mon in menu_list:
        if mon["id"] == id_mon:
            print("1. Còn hàng")
            print("2. Hết hàng")
            chon = input("Chọn trạng thái mới: ")

            if chon == "1":
                mon["trang_thai"] = "Còn hàng"
            elif chon == "2":
                mon["trang_thai"] = "Hết hàng"
            else:
                print("❌ Lựa chọn không hợp lệ!")
                return

            print("✅ Cập nhật trạng thái thành công!")
            return

    print("❌ Không tìm thấy món!")
