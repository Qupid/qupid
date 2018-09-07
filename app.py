
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from sub import api

#app = Flask(__name__)
#app.wsgi_app = ProxyFix(app.wsgi_app)

#api.init_app(app)

#app.run(debug=True)

#test

import os
from run import app as application
if __name__ == '__main__':
    api.init_app(application)
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
