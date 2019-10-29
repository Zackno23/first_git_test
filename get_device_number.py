from pyicloud import PyiCloudService

#接続するicloudのメールアドレスとパスワードを保存
api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208')

#iphoneのGPS情報を取得
def get_oauth():
    auth = api.devices
    return auth

#icloudに登録している端末のデバイスナンバーを取得
if __name__ == '__main__':
    auth=list(get_oauth())
    print('\n')
    [print(i) for i in range(len(auth))if str(auth[i]) == 'iPhone 11: iPhone']
