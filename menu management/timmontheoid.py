def tim_mon_theo_id(id_mon):
    return next((m for m in menu_list if m["id"] == id_mon), None)
