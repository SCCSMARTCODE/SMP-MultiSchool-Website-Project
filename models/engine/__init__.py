from os import getenv

DB_TYPE = getenv("DB_TYPE", None)

if DB_TYPE == "db":
    from models.engine.db_storage import Storage
else:
    from models.engine.fs_storage import Storage

storage = Storage()
storage.reload()
