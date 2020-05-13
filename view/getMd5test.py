
from view.core import coreHandler

class testHandler(coreHandler):
    def get(self):
        self.write("##############################################getmd5-1"+"</br>")
        self.write(str(self.getMd5("http://www.google.com"))+"</br>")
        self.write(str(self.getCode("http://www.google.com"))+ "</br>")
        self.write("##############################################getmd5-2"+"</br>")
        self.write(str(self.getMd5("http://www.google.com"))+"</br>")
        self.write(str(self.getCode("http://www.google.com"))+ "</br>")
        
    
