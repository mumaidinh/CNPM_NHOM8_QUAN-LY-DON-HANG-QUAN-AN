def menu_quan_ly():
    while True:
        clear_screen()
        print("=== MENU QUẢN LÝ ===")
        print("1. Báo cáo")
        print("0. Đăng xuất")

        c = nhap_lua_chon(["1", "0"])

        if c == "1":
            menu_bao_cao()

        elif c == "0":
            logout()
            break

def menu_nhan_vien():
    while True:
        clear_screen()
        print("=== MENU NHÂN VIÊN ===")
        print("1. Món ăn")
        print("2. Đơn hàng")
        print("3. Bàn")
        print("4. Kho")
        print("5. Thanh toán")
        print("0. Đăng xuất")

        c = nhap_lua_chon(["1","2","3","4","5","0"])

        if c == "1":
            menu_quan_ly_menu()

        elif c == "2":
            menu_quan_ly_don_hang()

        elif c == "3":
            menu_quan_ly_ban()

        elif c == "4":
            menu_quan_ly_kho()

        elif c == "5":
            menu_thanh_toan()

        elif c == "0":
            logout()
            break
