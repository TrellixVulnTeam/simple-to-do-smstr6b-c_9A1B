from flask import url_for, redirect, render_template
from app.forms.buku import BukuSave
from app.models.models import Buku
from app import db

class BukuController:
    def index(self):
        bukusave = BukuSave()
        if bukusave.validate_on_submit():
            buku = Buku(kd_buku=bukusave.kd_buku.data, judul= bukusave.judul.data.upper(), pengarang= bukusave.pengarang.data, penerbit= bukusave.penerbit.data, tahun_terbit=bukusave.tahun_terbit.data)
            buku.save()
            return redirect(url_for('index_buku'))
        buku = Buku().getAll()
        return render_template('buku/index.html', form = bukusave, title='Perpustakaan Index', buku=buku)
    
    def edit(self, id):
        bukusave = BukuSave()
        buku = Buku().getOne(id)
        if bukusave.validate_on_submit():
            buku.judul = bukusave.judul.data
            buku.pengarang = bukusave.pengarang.data
            buku.penerbit = bukusave.penerbit.data
            buku.tahun_terbit = bukusave.tahun_terbit.data
            db.session.commit()
            return redirect(url_for('index_buku'))
        return render_template('buku/edit.html', form=bukusave, buku=buku)

    def delete(self, id):
        buku = Buku().getOne(id)
        buku.delete()
        return redirect(url_for('index_buku'))