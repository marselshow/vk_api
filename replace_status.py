import vk_api

token3 = open('token.txt', 'r')

token1 = token3.read()

session = vk_api.VkApi(token = token1)
vk = session.get_api()

def startStatus():
    statusOut = vk.status.set(text = "Hello World! vk.com/marselshowyoutube ")
    print('Все получилось ;D')

while True:
    startStatus()