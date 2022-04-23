import vk_api

token3 = open('token.txt', 'r')

token1 = token3.read()

session = vk_api.VkApi(token = token1)
vk = session.get_api()

def upload():
    try:
        upload = vk_api.VkUpload(session)
        photo = upload.photo_profile('example.jpg')
        print("Получилось :D ")
    except Exception as err:
        print(err)

upload()