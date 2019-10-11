from lib_obj.category import Category
from lib_db import LibDb


def get_category_dict(db: LibDb.LibDb):
    cat_db = db.return_tab("category")
    cat_dict = dict()
    for i in cat_db:
        uid, name, active = i
        cat_dict[uid] = Category(uid, name, active)
    return cat_dict


def get_category_list(db: LibDb.LibDb):
    cat_dict = get_category_dict(db)
    cat_list = list()
    cat_id_list = list()
    for i in cat_dict:
        if cat_dict[i].cat_is_active:
            cat_list.append(cat_dict[i].name)
            cat_id_list.append(i)
    return cat_list, cat_id_list


def deactivate_category(db: LibDb.LibDb, uid: int):
    db.set_inactive("category", uid)


def activate_category(db: LibDb.LibDb, uid: int):
    db.set_active("category", uid)
