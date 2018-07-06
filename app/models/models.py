from app import db
from datetime import datetime
from flask_login import UserMixin

class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    kd_buku = db.Column(db.String(10), nullable=False)
    judul = db.Column(db.String(50), nullable=False)
    pengarang = db.Column(db.String(30), nullable=False)
    penerbit = db.Column(db.String(20), nullable=False)
    tahun_terbit = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)

class Anggota(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    identitas = db.Column(db.Integer, nullable=False)
    no_anggota = db.Column(db.Integer, nullable=False)
    nama = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())

class Peminjam(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    no_anggota = db.Column(db.Integer, nullable=False)
    kd_buku = db.Column(db.String(10), nullable=False)
    tgl_pinjam = db.Column(db.DATE, nullable=False)
    tgl_kembali = db.Column(db.DATE, nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())



#tambah ini diatas -> from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    user = db.Column(db.String(20), nullable=False)
    hash_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DATETIME, default=datetime.now())
    updated_at = db.Column(db.DATETIME, default=datetime.now())
