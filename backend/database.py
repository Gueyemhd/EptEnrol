from flask import Flask, jsonify, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import os

#UPLOAD_FOLDER = 'uploads'


app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=['Content-Type'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrationDb.db'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Candidat(db.Model):
    __tablename__ = 'Candidat'
    numero_candidat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prenom = db.Column(db.String(40))
    nom = db.Column(db.String(30))
    email = db.Column(db.String(40), unique= True)
    dossier = db.relationship('Dossier', uselist=False, backref='candidat', lazy=True)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
   


    def __repr__(self):
        return 'Candidat: {} {}'.format(self.prenom, self.nom)

class Dossier(db.Model):
    __tablename__ = 'Dossiers'
    numero_dossier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    etat_dossier = db.Column(db.Enum('En attente', 'Validé', 'Non validé', name = 'etat_du_dossier'))
    paiement = db.Column(db.Boolean, default = True)
    candidat_id = db.Column(db.Integer, db.ForeignKey('Candidat.numero_candidat'), nullable=False)
    fiche = db.relationship('ficheCandidature', uselist=False, backref='dossier', lazy=True, cascade='all, delete-orphan')
    document = db.relationship('Document', uselist=False, backref='directory', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return 'Dossier n°: {}'.format(self.numeroDossier)
    

class ficheCandidature(db.Model):
    __tablename__ = 'ficheCandidature'
    numero_fiche = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adresse = db.Column(db.String(50))
    tel_candidat = db.Column(db.String(25))
    tel_parent = db.Column(db.String(25))
    etablissement = db.Column(db.String(70))
    serie = db.Column(db.String(25))
    date_naissance = db.Column(db.String(30))
    lieu_naissance = db.Column(db.String(30))
    nationalite = db.Column(db.String(25))
    option = db.Column(db.String(50))
    centre_examen = db.Column(db.String(50))
    annee_obtention_bac = db.Column(db.String(20))
    mention_bac = db.Column(db.String(25))
    dossier_id = db.Column(db.Integer, db.ForeignKey('Dossiers.numero_dossier'), nullable=False)

    def __repr__(self):
        return 'Fiche n°: {}'.format(self.numero_fiche)


class Document(db.Model):
    __tablename__ = 'Document'
    numero_document = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bulletins_path = db.Column(db.String(255))
    diplome_path = db.Column(db.String(255), nullable=True)
    releve_path = db.Column(db.String(255), nullable=True)
    id_dossier = db.Column(db.Integer, db.ForeignKey('Dossiers.numero_dossier'), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/inscription', methods=['POST'])
def register():
    if request.method == 'POST':
        details = request.form

        prenom = details['first_name']
        nom = details['last_name']
        email = details['email']

        annee_bac = ""
        mention = ""
        adresse = details['adresse']
        tel_cand = details['phone-candidat']
        tel_parent = details['phone-parent']
        etablissement = details['etablissement']
        serie = details['serie']
        date_naiss = details['date-naiss']
        lieu_naiss = details['lieu-naiss']
        centre = details['centre']
        option = details['option']
        nationalite = details['nationnalite']
       
        
        bulletins = request.files["bulletins"]  

         
        dir_path = f"Documents/{prenom}-{nom}-{email}"

        if bulletins:
            os.mkdir(dir_path)
            file_path =  f"{dir_path}/{bulletins.filename}"
            bulletins.save(file_path)

        document= Document(bulletins_path= bulletins.filename, diplome_path="", releve_path="")

        if "options" in details:
            if details['options'] == "Bachelier":
                 annee_bac = details['anneeBac']
                 mention = details['mention']
                 diplome_bac = request.files['diplome']
                 releve = request.files['releve']
                 if diplome_bac:
                    file_path =  f"{dir_path}/{diplome_bac.filename}"
                    diplome_bac.save(file_path)
                 if releve:
                    file_path =  f"{dir_path}/{releve.filename}"
                    releve.save(file_path)
                 document = Document(bulletins_path= bulletins.filename, diplome_path=diplome_bac.filename, releve_path=releve.filename)
   

       
        
        candidat = Candidat(prenom=prenom, nom=nom, email= email)  
        dossier = Dossier(etat_dossier= 'En attente')
        fiche = ficheCandidature(adresse=adresse, tel_candidat=tel_cand, tel_parent= tel_parent, etablissement= etablissement, serie = serie, date_naissance = date_naiss,  lieu_naissance= lieu_naiss, nationalite= nationalite, option= option,  centre_examen= centre, annee_obtention_bac= annee_bac, mention_bac= mention)


        candidat.dossier = dossier
        dossier.fiche = fiche
        dossier.document = document
               

       
       
        db.session.add(candidat)
        db.session.add(dossier)
        db.session.add(fiche)
        db.session.add(document)

        db.session.commit()
        

        return redirect('http://localhost:4200/sign-up')
    return  redirect('http://localhost:4200/inscription')


with app.app_context():    
    @app.route('/infoCandidat', methods=['GET'])
    def get_all_dossierAetudier1():
            candidats = Candidat.query.join(Dossier).filter(Dossier.etat_dossier.like('En attente%')).all()
            results = []
            for candidat in candidats:
                result = {
                    'numero_candidat': candidat.numero_candidat,
                    'prenom': candidat.prenom,
                    'nom': candidat.nom,
                    'email': candidat.email,
                    'numero_dossier': candidat.dossier.numero_dossier,
                    'etat_dossier': candidat.dossier.etat_dossier,
                    'serie': candidat.dossier.fiche.serie
                }
                results.append(result)
            return jsonify(results)
    


    @app.route('/validation', methods=['GET'])
    def get_all_dossierAetudier():
        candidats = Candidat.query.join(Dossier).join(ficheCandidature).join(Document).filter(Dossier.etat_dossier.like('En attente')).all()

        results = []
        for candidat in candidats:
            result = {
                'numero_candidat': candidat.numero_candidat,
                'prenom': candidat.prenom,
                'nom': candidat.nom,
                'email': candidat.email,
                'numero_dossier': candidat.dossier.numero_dossier,
                'etat_dossier': candidat.dossier.etat_dossier,
                'paiement': candidat.dossier.paiement,
                'numero_fiche': candidat.dossier.fiche.numero_fiche,
                'adresse': candidat.dossier.fiche.adresse,                
                'tel_candidat': candidat.dossier.fiche.tel_candidat,
                'tel_parent': candidat.dossier.fiche.tel_parent,
                'etablissement': candidat.dossier.fiche.etablissement,
                'serie': candidat.dossier.fiche.serie,
                'date_naissance': candidat.dossier.fiche.date_naissance,
                'lieu_naissance': candidat.dossier.fiche.lieu_naissance,
                'nationalite': candidat.dossier.fiche.nationalite,
                'option': candidat.dossier.fiche.option,
                'centre_examen': candidat.dossier.fiche.centre_examen,
                'annee_obtention_bac': candidat.dossier.fiche.annee_obtention_bac,
                'mention_bac': candidat.dossier.fiche.mention_bac,
                'numero_document': candidat.dossier.document.numero_document,
                'diplome_path': candidat.dossier.document.diplome_path,
                'bulletins_path': candidat.dossier.document.bulletins_path,
                'releve_path': candidat.dossier.document.releve_path
            }
            results.append(result)
        return jsonify(results)
    

    @app.route('/all', methods=['GET'])
    def get_all_dossierAetudier2():
        candidats = Candidat.query.join(Dossier).join(ficheCandidature).join(Document).all()

        results = []
        for candidat in candidats:
            result = {
                'numero_candidat': candidat.numero_candidat,
                'prenom': candidat.prenom,
                'nom': candidat.nom,
                'email': candidat.email,
                'numero_dossier': candidat.dossier.numero_dossier,
                'etat_dossier': candidat.dossier.etat_dossier,
                'paiement': candidat.dossier.paiement,
                'numero_fiche': candidat.dossier.fiche.numero_fiche,
                'adresse': candidat.dossier.fiche.adresse,                
                'tel_candidat': candidat.dossier.fiche.tel_candidat,
                'tel_parent': candidat.dossier.fiche.tel_parent,
                'etablissement': candidat.dossier.fiche.etablissement,
                'serie': candidat.dossier.fiche.serie,
                'date_naissance': candidat.dossier.fiche.date_naissance,
                'lieu_naissance': candidat.dossier.fiche.lieu_naissance,
                'nationalite': candidat.dossier.fiche.nationalite,
                'option': candidat.dossier.fiche.option,
                'centre_examen': candidat.dossier.fiche.centre_examen,
                'annee_obtention_bac': candidat.dossier.fiche.annee_obtention_bac,
                'mention_bac': candidat.dossier.fiche.mention_bac,
                'numero_document': candidat.dossier.document.numero_document,
                'diplome_path': candidat.dossier.document.diplome_path,
                'bulletins_path': candidat.dossier.document.bulletins_path,
                'releve_path': candidat.dossier.document.releve_path
            }
            results.append(result)
        return jsonify(results)
    

    @app.route('/etudies', methods=['GET'])
    def get_all_dossieretudies1():
        candidats = Candidat.query.join(Dossier).filter((Dossier.etat_dossier.like('validé')) | (Dossier.etat_dossier.like('non validé'))).all()
        results = []
        for candidat in candidats:
            result = {
                'numero_candidat': candidat.numero_candidat,
                'prenom': candidat.prenom,
                'nom': candidat.nom,
                'email': candidat.email,
                'numero_dossier': candidat.dossier.numero_dossier,
                'etat_dossier': candidat.dossier.etat_dossier
            }
            results.append(result)
        return jsonify(results)
    
    @app.route('/register', methods=['POST'])
    def register1():
        details = request.form
        email = details['mail']
        password = details['password']
        c_password = details['password1']

        if User.query.filter_by(email=email).first():
            return redirect('http://localhost:4200/sign-up')
        
        if password == c_password:
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()
        else:
             return redirect('http://localhost:4200/sign-up')


        return redirect('http://localhost:4200/login')
    

    @app.route('/update-database', methods=['POST'])
    def valider():
        details = request.get_json()
        email = details['email']
        candidat = Candidat.query.join(Dossier). filter(Candidat.email==email).all()
        candidat[0].dossier.etat_dossier = 'Validé'
        db.session.commit()
      

        
   
        return jsonify({'message': 'Succès'})
    

    @app.route('/update-database1', methods=['POST'])
    def valider1():
        details = request.get_json()
        email = details['email']
        candidat = Candidat.query.join(Dossier). filter(Candidat.email==email).all()
        candidat[0].dossier.etat_dossier = 'Non validé'
        db.session.commit()
      

        
   
        return jsonify({'message': 'Succès'})
    
    @app.route('/login', methods=['POST'])
    def login():
        mail_admin = 'admin@gmail.com'
        details = request.form
        email = details['mail']
        password = details['password']

        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password_hash, password):
            return redirect('http://localhost:4200/login')
        
        candidat = Candidat.query.join(Dossier).join(ficheCandidature).filter(Candidat.email == email).all()
        print(candidat)
        if not candidat and email != mail_admin:
            return redirect('http://localhost:4200/login')
        elif not candidat and email == mail_admin:
            return redirect('http://localhost:4200/listeCandidats')
        prenom = candidat[0].prenom
        nom = candidat[0].nom
        serie = candidat[0].dossier.fiche.serie
        etat = candidat[0].dossier.etat_dossier
       
        return redirect('http://localhost:4200/etat?prenom={}&nom={}&serie={}&etat={}&email={}'.format(prenom, nom, serie, etat, email))
    

    @app.route('/fichier-pdf', methods=['POST'])
    def fichier_pdf():
        path = request.args.get('chemin')
        

        return send_file(str(path), mimetype='application/pdf')

        
    
   

    



app.run()
