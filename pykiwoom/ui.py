import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget
import pykiwoom
import time

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
        data = str(self.km.get_method()[0])
        self.myacc_edt.setText(data)

    def on_mystock_button_click(self):
        tr_cmd = {
            'rqname': "opw00018",
            'trcode': 'opw00018',
            'next': '0',
            'screen': '1000',
            'input': {
                "계좌번호": self.myacc_edt.text(),
                "비밀번호": "",
                "비밀번호입력매체구분": "00",
                "조회구분": "1"
            },
            'output': ["종목번호", "종목명","매입금액","보유수량","수익률(%)","매매가능수량", "현재가"]
        }
        while True:
            self.km.put_tr(tr_cmd)
            data, remain = self.km.get_tr()
            data["매도예정가"] = 0
            print(data)
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    item = QtWidgets.QTableWidgetItem(str(data.iloc[i, j]))
                    print(item)
                    self.mystock_table.setItem(i, j, item)
            if remain:  
                tr_cmd['next'] = '2'
            else:
                break
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



'''
주문 cmd 예시
        order_cmd = {
            'rqname': "시장가주문",
            'screen': '1000',
            'acc_no' : data,
            'order_type' : "1",
            'code' : '005930',
            'quantity' : '10',
            'price' : "72000",
            'hoga_gb' : "03",
            'order_no' : ""
        }
        self.km.put_order(order_cmd)
        print("매수 완료")

'''