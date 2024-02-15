import pykiwoom


if __name__ == "__main__":
    km = pykiwoom.KiwoomManager()

    real_cmd = {
    'func_name': "SetRealReg",
    'real_type': '주식체결',
    'screen': '1001',
    'code_list': "028670", 
    'fid_list': "10;17",
    "opt_type": 0
}
    km.put_real(real_cmd)
    while True:
        data = km.get_real()
        print(data)