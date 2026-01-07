from datetime import datetime
import os
import json
DATA_FILE = "data.json"

# ================== DỮ LIỆU CHUNG ==================
users = []
current_user = None

menu_list = []
don_hang_list = []
ma_don_tu_tang = 1

ban_list = []
kho_nguyen_lieu = []
cong_thuc_mon = []
def load_data():
    global users, menu_list, don_hang_list, ma_don_tu_tang
    global ban_list, kho_nguyen_lieu

    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = data.get("users", [])

    # 🔧 FIX: thêm role mặc định nếu thiếu
    for u in users:
        if "role" not in u:
            u["role"] = "nhan_vien"  # hoặc "quan_ly"

    menu_list = data.get("menu_list", [])
    don_hang_list = data.get("don_hang_list", [])
    ma_don_tu_tang = data.get("ma_don_tu_tang", 1)
    ban_list = data.get("ban_list", [])
    kho_nguyen_lieu = data.get("kho_nguyen_lieu", [])   

def save_data():
    data = {
        "users": users,
        "menu_list": menu_list,
        "don_hang_list": don_hang_list,
        "ma_don_tu_tang": ma_don_tu_tang,
        "ban_list": ban_list,
        "kho_nguyen_lieu": kho_nguyen_lieu
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

 # ===== MÀU ANSI =====
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    input("\nNhấn Enter để tiếp tục...")

def hien_thi_chao_mung():
    PINK = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    print()
    print(f"{PINK}{BOLD}💖  CHÀO MỪNG ĐẾN VỚI QUÁN ĂN  💖{RESET}".center(70))
    print()
    print(f"{YELLOW}{BOLD}  ███████╗██╗██╗   ██╗{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ██╔════╝██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ███████╗██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ╚════██║██║██║   ██║{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ███████║██║╚██████╔╝{RESET}".center(70))
    print(f"{YELLOW}{BOLD}  ╚══════╝╚═╝ ╚═════╝ {RESET}".center(70))

    print("\n" + "-" * 70)
    print(f"{GREEN}{BOLD}👏  HỆ THỐNG QUẢN LÝ ĐƠN HÀNG  👏{RESET}".center(70))
    print(f"{YELLOW}{BOLD}✨  MENU CHÍNH  ✨{RESET}".center(70))
    print()

    print("  1. 🔐 Đăng nhập")
    print("  2. 📝 Đăng ký")
    print("  3. ❓ Quên mật khẩu")
    print("  4. 🚪 Thoát")
    print()
def nhap_lua_chon(hop_le):
    """
    hop_le: list các lựa chọn hợp lệ, ví dụ ["1","2","3","0"]
    """
    while True:
        chon = input("👉 Chọn chức năng: ").strip()
        if chon not in hop_le:
            print("❌ Lựa chọn không hợp lệ! Vui lòng nhập đúng chức năng.")
            continue
        return chon
# ================== HỆ THỐNG CHÍNH ==================
def main_menu():
    while True:
        print("\n" + "★"*10 + " MENU QUẢN LÝ " + "★"*10)
        print("1. Món ăn\n2. Đơn hàng\n3. Bàn\n4. Kho\n5. Thanh toán\n6. Báo cáo\n7. Đăng xuất")
        c = nhap_lua_chon(["1","2","3","4","5","6","7"])
        if c == "1":
            clear_screen()
            menu_quan_ly_menu()

        elif c == "2":
            clear_screen()
            menu_quan_ly_don_hang()

        elif c == "3":
            clear_screen()
            menu_quan_ly_ban()

        elif c == "4":
            clear_screen()
            menu_quan_ly_kho()

        elif c == "5":
            clear_screen()
            menu_thanh_toan()
            pause()

        elif c == "6":
            clear_screen()
            menu_bao_cao()
            pause()
def main():
    load_data()
    while True:
        clear_screen()
        hien_thi_chao_mung()   

        chon = nhap_lua_chon(["1", "2", "3", "4"])


        if chon == "1":  # Đăng nhập
            clear_screen()
            print("=== ĐĂNG NHẬP TÀI KHOẢN ===")
            if login():
                if current_user["role"] == "quan_ly":
                    menu_quan_ly()
                else:
                    menu_nhan_vien()


        elif chon == "2":  # Đăng ký
            clear_screen()
            print("=== ĐĂNG KÝ TÀI KHOẢN ===")
            register()
            input("\nNhấn Enter để quay lại...")

        elif chon == "3":
            clear_screen()
            quen_mat_khau()
            input("\nNhấn Enter để quay lại...")


        elif chon == "4":
            print("👋 Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")
            input("Nhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
