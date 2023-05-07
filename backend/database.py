from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrationDb.db'
db = SQLAlchemy(app)

class Candidat(db.Model):
    numero_candidat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prenom = db.Column(db.String(40))
    nom = db.Column(db.String(30))
    email = db.Column(db.String(40), unique= True)
    password = db.Column(db.String(100), nullable=False)
    dossier = db.relationship('Dossier', uselist=False, backref='candidat', lazy=True)
   


    def __repr__(self):
        return 'Candidat: {} {}>'.format(self.prenom, self.nom)

class Dossier(db.Model):
    numero_dossier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    etat_dossier = db.Column(db.Enum('En cours d\'étude', 'Validé', 'Non validé', name = 'etat_du_dossier'))
    paiement = db.Column(db.Boolean, default = True)
    candidat_id = db.Column(db.Integer, db.ForeignKey('candidat.numero_candidat'), nullable=False)
    fiche = db.relationship('ficheCandidature', uselist=False, backref='dossier', lazy=True, cascade='all, delete-orphan')
    document = db.relationship('Document', uselist=False, backref='directory', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return 'Dossier n°: {}'.format(self.numeroDossier)
    

class ficheCandidature(db.Model):
    numero_fiche = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adresse = db.Column(db.String(50))
    tel_candidat = db.Column(db.String(25))
    tel_parent = db.Column(db.String(25))
    etablissement = db.Column(db.String(70))
    serie = db.Column(db.String(25))
    date_naissance = db.Column(db.Date())
    lieu_naissance = db.Column(db.String(30))
    nationalite = db.Column(db.String(25))
    option = db.Column(db.String(50))
    centre_examen = db.Column(db.String(50))
    annee_obtention_bac = db.Column(db.String(20))
    mention_bac = db.Column(db.String(25))
    dossier_id = db.Column(db.Integer, db.ForeignKey('dossier.numero_dossier'), nullable=False)

    def __repr__(self):
        return 'Fiche n°: {}'.format(self.numero_fiche)


class Document(db.Model):
    numero_document = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bulletins_path = db.Column(db.String(255))
    diplome_path = db.Column(db.String(255), nullable=True)
    releve_path = db.Column(db.String(255), nullable=True)
    id_dossier = db.Column(db.Integer, db.ForeignKey('dossier.numero_dossier'), nullable=False)


with app.app_context():
    db.create_all()
