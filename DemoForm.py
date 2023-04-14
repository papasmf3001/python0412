# DemoForm.py
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 디자인한 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#폼클래스 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

#직접 모듈을 실행한 경우
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show()
    app.exec_() 

