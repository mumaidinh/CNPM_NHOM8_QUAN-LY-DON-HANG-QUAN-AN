def menu_quan_ly_menu():
    while True:
        clear_screen()
        print("===== QUẢN LÝ MENU =====")
        print("1. Thêm món")
        print("2. Xem danh sách menu")
        print("3. Tìm kiếm món")
        print("4. Sửa món ăn")
        print("5. Xóa món ăn")
        print("0. Quay lại")

        chon = nhap_lua_chon(["1","2","3","4","5","0"])

        if chon == "1":
            clear_screen()
            print("=== THÊM MÓN ĂN ===")
            add_item()
            pause()

        elif chon == "2":
            clear_screen()
            print("=== DANH SÁCH MENU ===")
            hien_thi_menu(menu_list)
            pause()

        elif chon == "3":
            clear_screen()
            print("=== TÌM KIẾM MÓN ===")
            tk = input("Nhập tên món: ").lower()
            kq = [m for m in menu_list if tk in m['ten_mon'].lower()]
            hien_thi_menu(kq)
            pause()

        elif chon == "4":
            clear_screen()
            print("=== SỬA MÓN ĂN ===")
            sua_mon_an()
            pause()

        elif chon == "5":
            clear_screen()
            print("=== XÓA MÓN ĂN ===")
            xoa_mon_an()
            pause()

        elif chon == "0":
            break


