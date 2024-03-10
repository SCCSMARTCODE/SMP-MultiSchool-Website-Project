from os import getenv, environ

"""This should be removed ASAP"""
environ["DB_PASSWD"] = "smp_pass_master"
environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "smp_master"
environ["DB_NAME"] = "smp_base_db"
environ["DB_TYPE"] = "db"
"""This should be removed ASAP"""

from models.sch_acc import School
from models.engine import storage


my_model = School(address="admin111", gmail="admin111", phone_address="admin111", password="admin111")
my_model.name = "Admin school111......"
my_model.my_number = 89111
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


info = storage.all("School")
id_ = 1
datas = []
for key in info.keys():
    data = info[key].__dict__["name"]
    datas.append((id_, data))
    id_ += 1

print("school names:\n\n", datas)
