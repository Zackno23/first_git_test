from pyicloud import PyiCloudService
import sqlite3

# 接続するicloudのメールアドレスとパスワードを保存
api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

#sqlite3に接続
conn = sqlite3.connect("gps_log.db")
cur = conn.cursor()

# iphoneのGPS情報を取得
def get_oauth():
    auth = api.devices
    return auth


# icloudに登録している端末のデバイスナンバーを取得
if __name__ == '__main__':
    auth = list(get_oauth())
    print('\n')
    [print(f'デバイス番号 [{i}]') for i in range(len(auth)) if str(auth[i]) == 'iPhone 11: iPhone']

