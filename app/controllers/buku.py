from flask import url_for, redirect, render_template
from app.forms.buku import BukuSave
from app.models.models import Buku

class BukuController:
    def index(self):
        bukusave = BukuSave()
        if bukusave.validate_on_submit():
            buku = Buku(kd_buku=bukusave.kd_buku.data, judul= bukusave.judul.data.upper(), pengarang= bukusave.pengarang.data, penerbit= bukusave.penerbit.data, tahun_terbit=bukusave.tahun_terbit.data)
            buku.save()
            return redirect(url_for('index_buku'))
            
        return render_template('buku/index.html', form = bukusave, title='Perpustakaan Index')