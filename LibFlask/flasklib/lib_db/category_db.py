from flasklib.lib_obj.category import Category
from flasklib.lib_db import LibDb


def get_category_dict(db: LibDb.LibDb):
    cat_db = db.return_tab("category")
    cat_dict = dict()
    for i in cat_db:
        uid, name, active = i
        cat_dict[uid] = Category(uid, name, active)
    return cat_dict


def get_category_obj_list(db: LibDb.LibDb):
    cat_db = db.return_tab("category")
    cat_dict = list()
    for i in cat_db:
        uid, name, active = i
        cat_dict.append(Category(uid, name, active))
    return cat_dict


def get_category_tuple_list(db: LibDb.LibDb):
    cat_dict = get_category_dict(db)
    cat_list = list()
    for i in cat_dict:
        if cat_dict[i].active:
            cat_list.append((cat_dict[i].uid, cat_dict[i].name))
    return cat_list


def get_cat_by_id(db: LibDb.LibDb, uid: int):
    cat_db = get_category_dict(db)
    return cat_db[uid]


def deactivate_category(db: LibDb.LibDb, uid: int):
    db.set_inactive("category", uid)


def activate_category(db: LibDb.LibDb, uid: int):
    db.set_active("category", uid)
