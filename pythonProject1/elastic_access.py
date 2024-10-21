import time

class ElasticAccess:
    def __init__(self):
        self.dict = {}
        self.list1 = {12,43,56}
        self.list2 = {"ag", "ds", "we"}

    def check_querry_response(self):
        for i,j in zip(self.list1, self.list2):
            self.dict[i] = j

        for i in range(10):
            print(self.dict)
            time.sleep(2)

object_of_ElasticAccess = ElasticAccess()
object_of_ElasticAccess.check_querry_response()
