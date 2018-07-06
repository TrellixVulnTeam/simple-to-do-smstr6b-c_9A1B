from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired

class BukuSave(FlaskForm):
    msg = 'data tidak boleh kosong'
    kd_buku = StringField('Kode Buku', validators=[DataRequired(message=msg)])
    judul = StringField('Judul Buku', validators=[DataRequired(message=msg)])
    pengarang = StringField('Pengarang', validators=[DataRequired(message=msg)])
    penerbit = StringField('Penerbit', validators=[DataRequired(message=msg)])
    tahun_terbit = IntegerField('Tahun Terbit', validators=[DataRequired(message=msg)])
    submit = SubmitField('Simpan')