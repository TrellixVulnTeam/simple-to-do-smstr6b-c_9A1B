from app import app
from app.controllers.buku import BukuController

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index_buku():
    return BukuController().index()

@app.route('/buku/<id>/edit', methods=['POST', 'GET'])
def edit_buku(id):
    return BukuController().edit(id)

@app.route('/buku/<id>/delete')
def delete_buku(id):
    return BukuController().delete(id)
    