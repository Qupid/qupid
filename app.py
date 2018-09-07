
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from sub import api

import os

#if __name__ == '__main__':
app = Flask(__name__)
api.init_app(app)
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)


#app = Flask(__name__)
#app.wsgi_app = ProxyFix(app.wsgi_app)

#api.init_app(app)

#app.run(debug=True)
