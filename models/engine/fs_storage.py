"""This module contains the file storage engine managing codes"""
import json
import os
from datetime import datetime


class Storage:
    """
    This class hold's all class as the mother class
    """
    file_path = 'pop.json'
    object_ = []
    # datetime.now().

    def new(self, obj):
        """
        This function help's me in adding new obj to my storage
        :param obj:
        :return:
        """

        val = obj.to_dict()
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)

        self.object_.append({key: val})
        with open(self.file_path, 'w') as f:
            json.dump(self.object_, f, indent=4)

    def save(self):
        """
        this function helps in updating my database to meet the self.object_ new update
        :return:
        """

        with open(self.file_path, 'w') as f:
            json.dump(self.object_, f, indent=4)

    def all(self):
        """
        This function returns all the data n the database
        :return:
        """
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r') as f:
            obj = json.load(f)

        return obj

    def reload(self):
        """
        this function helps in updating my self.object_ to get the content of the database
        :return:
        """
        self.object_ = self.all()

    def storable_data(self):
        datas = self.object_
        for data in datas:
            for key in data.keys():
                val = data[key]
                val['created_at'] = val['created_at'].isoformat()
                val['updated_at'] = val['updated_at'].isoformat()

        return datas
