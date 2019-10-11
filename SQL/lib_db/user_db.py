from lib_obj.user import User
from lib_db import LibDb


def get_user_dict(db: LibDb.LibDb):
    user_db = db.return_tab("user")
    user_dict = dict()
    for i in user_db:
        uid, name, surname, active = i
        user_dict[uid] = User(uid, name, surname, active)
    return user_dict


def get_user_list(db: LibDb.LibDb):
    user_dict = get_user_dict(db)
    user_list = list()
    user_id_list = list()
    for i in user_dict:
        if user_dict[i].usr_is_active:
            user_list.append(user_dict[i].fullname)
            user_id_list.append(i)
    return user_list, user_id_list


def deactivate_user(db: LibDb.LibDb, uid: int):
    db.set_inactive("user", uid)


def activate_user(db: LibDb.LibDb, uid: int):
    db.set_active("user", uid)
