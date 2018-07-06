from app import app
from app.controllers.buku import BukuController

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index_buku():
    return BukuController().index()
    