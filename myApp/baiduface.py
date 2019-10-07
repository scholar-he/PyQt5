import requests
import json

class BaiduFaceIdentify():
    #此函数用于获取access_token，返回access_token的值
    #此函数被parse_face_pic调用
    def get_access_token(self):
        client_id = 'Mjo4bbmHG28ZfyS2L1GG0aRm'                #此变量赋值成自己API Key的值
        client_secret = 'qs1L0AT1SbAspuXaWDTwxnHfYNZqPrZS'    #此变量赋值成自己Secret Key的值
        auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret

        response_at = requests.get(auth_url)
        json_result = json.loads(response_at.text)
        access_token = json_result['access_token']
        return access_token

    #此函数进行人脸识别，返回识别到的人脸列表
    #此函数被parse_face_pic调用
    def identify_faces(self,url_pic,url_fi):
        headers = {
            'Content-Type' : 'application/json; charset=UTF-8'
        }
        post_data = {
            'image': url_pic,
            'image_type' : 'BASE64',
            'face_field' : 'facetype,gender,age,beauty,expression,face_shape', #expression,faceshape,landmark,race,quality,glasses
            'max_face_num': 2
        }

        response_fi = requests.post(url_fi,headers=headers,data=post_data)
        json_fi_result = response_fi.json()
        return json_fi_result['result']['face_list'] if json_fi_result["result"] != None else {}
        #下边的print也许是最直观，你最想要的
        #print(json_fi_result['result']['face_list'][0]['age'])
        #print(json_fi_result['result']['face_list'][0]['beauty'])

    #此函数用于解析进行人脸图片，输出图片上的人脸的性别、年龄、颜值
    #此函数调用get_access_token、identify_faces
    def parse_face_pic(self,url_pic):
        f = open(r'%s' % url_pic, 'rb')
        import base64
        pic = base64.b64encode(f.read())
        f.close()
        base64 = str(pic, 'utf-8')
        #调用get_access_token获取access_token
        access_token = self.get_access_token()
        url_fi = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=' + access_token
        #调用identify_faces，获取人脸列表
        json_faces = self.identify_faces(base64,url_fi)
        dic = {}
        sexMap = {
            "female": "女性",
            "male": "男性"
        }
        if len(json_faces) == 0:
            print('未识别到人脸')
        else:
            for json_face in json_faces:
                # dic["种类"] = json_face['face_type']['type']
                dic["性别"] = sexMap[json_face['gender']['type']]
                dic["年龄"] = str(json_face['age'])
                dic["颜值"] = str(json_face['beauty'])
                dic["表情"] = json_face['expression']['type']
                dic["脸部形状"] = json_face['face_shape']['type']
        return dic
                # print('种类：'+json_face['face_type']['type'])
                # print('性别：'+json_face['gender']['type'])
                # print('年龄：'+str(json_face['age']))
                # print('颜值：'+str(json_face['beauty']))
                # print('表情：'+json_face['expression']['type'])
                # print('脸部形状：'+json_face['face_shape']['type'])

if __name__ == '__main__':
    #uil_pic赋值成自己要测试的图片的url地址
    # url_pic = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1357154930,886228461&fm=27&gp=0.jpg'
    # url_pic = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1500645018,3676785399&fm=26&gp=0.jpg'
    # bfi = BaiduFaceIdentify()
    # bfi.parse_face_pic(url_pic)
    # picPath = "E:\project\PyQt5_Learning\menu_toolbar_status_bar\images\gaoyuanyuan.jpg"
    picPath = r"C:\Users\1\Desktop\1.jpg"
    # f = open(r'%s' % picPath, 'rb')
    # import base64
    # pic = base64.b64encode(f.read())
    # f.close()
    # base64 = str(pic, 'utf-8')
    bdf = BaiduFaceIdentify()
    bdf.parse_face_pic(picPath)
