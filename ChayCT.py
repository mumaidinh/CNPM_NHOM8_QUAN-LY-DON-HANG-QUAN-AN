def menu_quan_ly_don_hang():
    while True:
        print("\n=== QUẢN LÝ ĐƠN HÀNG ===")
        print("1. Tạo đơn hàng tại quán")
        print("2. Nhận đơn online")
        print("3. Cập nhật trạng thái")
        print("4. Hủy đơn")
        print("0. Quay lại")

        chon = input("Chọn: ")

        if chon == "1":
            tao_don_hang_tai_quan()
        elif chon == "2":
            nhan_don_online()
        elif chon == "3":
            cap_nhat_trang_thai_don()
        elif chon == "4":
            huy_don_hang()
        elif chon == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")
def main():
    menu_quan_ly_don_hang()
if __name__ == "__main__":
    main()