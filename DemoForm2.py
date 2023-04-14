# DemoForm2.py(로직) + DemoForm2.ui(화면)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 디자인한 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#폼클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")

#직접 모듈을 실행한 경우
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show()
    app.exec_() 

