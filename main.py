from os import getenv, environ

"""This should be removed ASAP"""
environ["DB_PASSWD"] = "smp_pass_master"
environ["DB_HOST"] = "localhost"
environ["DB_USER"] = "smp_master"
environ["DB_NAME"] = "smp_base_db"
environ["DB_TYPE"] = "db"
"""This should be removed ASAP"""

from models.sch_acc import School


my_model = School(address="admin", gmail="admin", phone_address="admin", password="admin")
my_model.name = "Admin school......"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
