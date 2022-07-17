import uuid
class Bed:
    def __init__(self):
        self.bedUuid = uuid.uuid4()
        self.bedNo = 10
    
    def createBed(self):
        if self.bedNo >0:
            self.bedNo -=1
            return True,self.bedNo
        return False,"Not Available"

    def deleteBed(self):
        if self.bedNo < 10:
            self.bedNo +=1
            return True,self.bedNo
        return False,"Not Available"
    


        

