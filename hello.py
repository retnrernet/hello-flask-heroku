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
                <input name="URL" text-align:center/>
                <input type="submit" text-align:center/>
                <iframe src="https://github.com/harishvinukumar/Mini-Search-Engine" width="468" height="60" align="left"></iframe>
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
if __name__ == '__main__':
    app.run()
