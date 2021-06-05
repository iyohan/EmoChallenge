import requests
import json

def getApi(img_path, 
        api='naver', 
        naver_client_id="lLK4cD2OkhXcedTbVkIp", 
        naver_client_secret="Jib78QacPF", 
        kakao_rest_api_key='7370f7395284f68f172e8e9e42eca568'):

    if api == 'naver':
        client_id = naver_client_id  #"YOUR_CLIENT_ID"
        client_secret = naver_client_secret   # "YOUR_CLIENT_SECRET"
        url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
        files = {'image': open(img_path, 'rb')}
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode==200):
            pass
        else:
            print("Error Code:", rescode)
        
    elif api == 'kakao':
        url = "https://dapi.kakao.com/v2/vision/face/detect"
        rest_api_key = kakao_rest_api_key
        files = {'image': open(img_path, 'rb')}
        headers = {'Authorization': f"KakaoAK {rest_api_key}"}
        response = requests.post(url, files=files, headers=headers)
        print(f'time elpased: {response.elapsed.total_seconds()}')
        rescode = response.status_code
        if(rescode==200):
            pass
        else:
            print("Error Code:" + str(rescode))

    return response
        
    
def parseJson(response, target='emotion'):
    js = response.json()
    if target == 'emotion':
        value, confidence = 0, 0
        try:
            value = js['faces'][0]['emotion']['value']
            confidence = js['faces'][0]['emotion']['confidence']
        except:
            return -1
        return value, confidence
    elif target == 'face_direction':
        yaw, pitch = 0, 0
        try:
            yaw = js['result']['faces'][0]['yaw']
            pitch = js['result']['faces'][0]['pitch']
        except:
            return -1
        return yaw, pitch
    return -1