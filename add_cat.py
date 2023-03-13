from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'random string'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = sqlite3.connect('database.db')

conn.execute('INSERT INTO categories (categoryId,name) VALUES (?,?)', (1,'sunglasses'))
conn.execute('INSERT INTO categories (categoryId, name ) VALUES (?,?)', (2,'spectacles'))
conn.commit()