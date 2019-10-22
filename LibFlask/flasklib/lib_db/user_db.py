from flasklib.lib_obj.user import User
from flasklib.lib_db import LibDb


def get_user_dict(db: LibDb.LibDb):
    user_db = db.return_tab("user")
    user_dict = dict()
    for i in user_db:
        uid, name, surname, active = i
        user_dict[uid] = User(uid, name, surname, active)
    return user_dict


def get_user_obj_list(db: LibDb.LibDb):
    user_db = db.return_tab("user")
    user_list = list()
    for i in user_db:
        uid, name, surname, active = i
        user_list.append(User(uid, name, surname, active))
    return user_list


def get_user_by_id(db: LibDb.LibDb, uid: int):
    usr_dict = get_user_dict(db)
    return usr_dict[uid]


def deactivate_user(db: LibDb.LibDb, uid: int):
    db.set_inactive("user", uid)


def activate_user(db: LibDb.LibDb, uid: int):
    db.set_active("user", uid)
