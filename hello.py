from flask import Flask
from flask import request
app = Flask(__name__)

FORM_PAGE = """
    <html>
        <head>
            <title>Flask Form</title>
        </head>
        <body>
            <form action="/process" method="POST">
                <input name="URL" />
                <input type="submit" />                
            </form>
    </html>
"""


@app.route('/')
def home_form():
    return FORM_PAGE
@app.route("/process", methods = ["GET", "POST"] )
def process_form():
    formData = request.values if request.method == "GET" else request.values
    response = "Form Contents <pre>%s</pre>" % "<br/>\n".join(["%s:%s" % item for item in formData.items()] )
    return response
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
    file = "/app/num.apkk"
    doc = upload.document(file)
    os.remove("/app/num.apkk")
if __name__ == '__main__':
    app.run()
