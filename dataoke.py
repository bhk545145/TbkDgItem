import requests

def GetLanguageVersion():
    appKey = '5f61a384c6228'
    appSecret = '096a7985d428ac128eaec84d98285ce8'
    version = 'v1.0.0' 
    url = 'https://openapi.dataoke.com/api/category/get-top100'
    method = 'GET'
    from dtk_open_platform import DtkOpenPlatform
    send = DtkOpenPlatform()
    data = {'appKey': appKey,
            'version': version,
            }
    response = send.open_platform_send(method=method,url=url,args=data,key=appSecret)
    print(response)
    pass


def main():
    GetLanguageVersion()

if __name__ == '__main__':
    main()