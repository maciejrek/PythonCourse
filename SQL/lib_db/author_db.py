from lib_obj.author import Author
from lib_db import LibDb


def get_author_dict(db: LibDb.LibDb):
    aut_db = db.return_tab("author")
    aut_dict = dict()
    for i in aut_db:
        uid, name, surname, active = i
        aut_dict[uid] = Author(uid, name, surname, active)
    return aut_dict


def get_author_list(db: LibDb.LibDb):
    aut_dict = get_author_dict(db)
    aut_list = list()
    aut_id_list = list()
    for i in aut_dict:
        if aut_dict[i].aut_is_active:
            aut_list.append(aut_dict[i].fullname)
            aut_id_list.append(i)
    return aut_list, aut_id_list


def deactivate_author(db: LibDb.LibDb, uid: int):
    db.set_inactive("author", uid)


def activate_author(db: LibDb.LibDb, uid: int):
    db.set_active("author", uid)
