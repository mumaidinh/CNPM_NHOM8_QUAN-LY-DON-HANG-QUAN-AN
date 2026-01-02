def show_menu():
    for i, item in enumerate(menu_list, 1):
        print(f"{i}. {item['name']} - {item['price']} ({'Còn' if item['is_available'] else 'Hết'})")