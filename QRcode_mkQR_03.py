import pyqrcode

def Mkqr(QRname):
    qr = pyqrcode.create(QRname, version=2, error="M")
    name = QRname + ".png"  # ここでファイル名を生成
    qr.png(name, scale=10)

Mkqr("aaa")