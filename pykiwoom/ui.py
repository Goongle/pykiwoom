import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
import pykiwoom

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # UI 파일 로드
        uic.loadUi("C:\\Users\\SMB\\Desktop\\kiwoom\\pykiwoom\\myui.ui", self)
        self.km = pykiwoom.KiwoomManager()
        # signal 연결 부
        #self.kiwoom.login_signal.connect(self.on_login_done)
        #self.kiwoom.server_message_signal.connect(self.server_message_append)
        #self.kiwoom.recv_updater.mystock_list_signal.connect(self.update_mystock_table)
        #self.kiwoom.real_updater.match_result_signal.connect(self.update_real_match_table)
        # 연결 함수 부분
        self.login_btn.clicked.connect(self.on_login_button_click)
        self.mystock_btn.clicked.connect(self.on_mystock_button_click)
        #self.real_btn.clicked.connect(self.on_real_button_click)
        #self.buy_btn.clicked.connect(self.on_buy_button_click)
        
        # 여기에 추가적인 UI 설정이나 이벤트 연결을 할 수 있습니다.
    def on_login_button_click(self):
        self.km.put_method(("GetLoginInfo", "ACCNO"))
        data = self.km.get_method()
        print(data)
    def on_mystock_button_click(self):
        self.km.put_method(("GetCodeListByMarket", "0"))
        tr_cmd = {
            'rqname': "opt10081",
            'trcode': 'opt10081',
            'next': '0',
            'screen': '1000',
            'input': {
                "종목코드": "005930",
                "기준일자": "20220612",
                "수정주가구분": "",
            },
            'output': ["일자", "시가", "고가", "저가", "현재가"]
        }

        while True:
            self.km.put_tr(tr_cmd)
            data, remain = self.km.get_tr()
            print(data)

            if remain:
                tr_cmd['next'] = '2'
            else:
                break
        # km.put_method(("GetMasterCodeName", "005930"))
        data = self.km.get_method()
        print(data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()