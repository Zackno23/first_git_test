from pyicloud import PyiCloudService
api = PyiCloudService(api = PyiCloudService('ychikara@unomaha.edu', 'Bakabaka0208'))

#二段階認証を得る
if api.requires_2fa:
    import click