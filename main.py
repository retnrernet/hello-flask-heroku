import urllib
import requests
urllib.request.urlretrieve("https://trashbox.ru/files20/1505107_717aef/mark.via.gp_4.3.1_20210829.apk", "apk.apkk")
import vk_api
import glob, shutil, os, time
from vk_api import VkApi
from vk_api.upload import VkUpload
vk_session = vk_api.VkApi('89045147622', 'Ggg96274220ggg')
vk_session.auth()
vk = vk_session.get_api()
upload = VkUpload(vk)
file = "/app/apk.apkk"
doc = upload.document(file)
os.remove("/app/apk.apkk")
