import re
from unittest import result
from mysqlconnection import connectToMySQL

class Sundae:
    def __init__(self, data):
        self.idtable1 = data["idtable1"]
        self.name =data["name"]
        self.flavor =data["flavor"]
        self.num_scoop =data["num_scoops"]
        self.topping =data["topping"]
        self.sauce =data["sauce"]
        self.created_at =data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sundaes;"
        results =  connectToMySQL("sundaes_demo").query_db(query)

        sundaes = []
        for result in results:
            one_instance = cls(result)
            sundaes.append(one_instance)
        return sundaes