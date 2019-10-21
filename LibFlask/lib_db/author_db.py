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
        if aut_dict[i].active:
            aut_list.append(aut_dict[i].fullname)
            aut_id_list.append(i)
    return aut_list, aut_id_list


def get_author_tuple_list(db: LibDb.LibDb):
    aut_dict = get_author_dict(db)
    aut_list = list()
    for i in aut_dict:
        if aut_dict[i].active:
            aut_list.append((aut_dict[i].uid, aut_dict[i].fullname))
    return aut_list


def get_author_obj_list(db: LibDb.LibDb):
    aut_db = db.return_tab("author")
    aut_list = list()
    for i in aut_db:
        uid, name, surname, active = i
        aut_list.append(Author(uid, name, surname, active))
    return aut_list


def get_aut_by_id(db: LibDb.LibDb, uid: int):
    aut_dict = get_author_dict(db)
    return aut_dict[uid]


def deactivate_author(db: LibDb.LibDb, uid: int):
    db.set_inactive("author", uid)


def activate_author(db: LibDb.LibDb, uid: int):
    db.set_active("author", uid)
