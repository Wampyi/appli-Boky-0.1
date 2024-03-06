# Importer le module QtSql pour accéder à la base de données
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import QSortFilterProxyModel, QRegularExpression, QStringListModel
from PySide6 import QtCore


import sqlite3

# Définir la classe qui gère la table personnel
class PersonnelManager:
    def __init__(self):
        # Créer ou ouvrir la connexion à la base de données
        self.db = QSqlDatabase.addDatabase("QSQLITE", "gestion")
        self.db.setDatabaseName("GESTION_ENTREPRISE")
        self.db.open()
        # Créer la table personnel si elle n'existe pas
        query = QSqlQuery(self.db)
        query.exec("""
        CREATE TABLE IF NOT EXISTS Personnel (
            id INTEGER PRIMARY KEY,
            Nom TEXT,
            Prenom TEXT,
            Adresse TEXT,
            Email TEXT,
            Numero TEXT,
            id_projet INTEGER,     
            FOREIGN KEY (id_projet) REFERENCES projet (id)
        )
    """)
        # ... initialisation de la base de données et autres configurations ...
        self.model = QStringListModel()  # Initialisation de l'attribut model
        self.setup_model()
        
    def ajouter_personnel(self, id, nom, prenom, adresse, email, numero):
        # Ajouter un enregistrement dans la table personnel avec les données fournies
        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO Personnel (id, Nom, Prenom, Adresse, Email, Numero)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(id)
        query.addBindValue(nom)
        query.addBindValue(prenom)
        query.addBindValue(adresse)
        query.addBindValue(email)
        query.addBindValue(numero)
        query.exec()
        
                      

    def afficher_personnel(self, tableWidget):
        # Afficher les données de la table personnel dans le QTableWidget fourni
        # Effacer les données précédentes du QTableWidget
        tableWidget.setRowCount(0)
        # Récupérer les données de la table personnel
        query = QSqlQuery(self.db)
        query.exec("""
            SELECT * FROM Personnel
        """)
        # Remplir le QTableWidget avec les données
        while query.next():
            row = tableWidget.rowCount()
            tableWidget.insertRow(row)
            for column in range(6):
                tableWidget.setItem(row, column, QTableWidgetItem(str(query.value(column))))

    def afficher_noms_prenoms(self, listView):
        # Afficher les noms, prénoms, ID et ID projet de la table Personnel dans le QListView fourni
        query = QSqlQuery(self.db)
        query.exec("""
        SELECT id, Nom, Prenom, id_projet FROM Personnel
        """)

        # Créer une liste pour stocker les noms, prénoms, ID et ID projet
        noms_prenoms_id_liste = []
        ids_liste = []
        id_projet_liste = []

        # Remplir la liste avec les données
        while query.next():
            id = query.value(0)  # Index 0 pour la colonne ID
            nom = query.value(1)  # Index 1 pour la colonne Nom
            prenom = query.value(2)  # Index 2 pour la colonne Prénom
            id_projet = query.value(3)  # Index 3 pour la colonne id_projet
            noms_prenoms_id_liste.append(f"{nom} {prenom}")
            ids_liste.append(id)
            id_projet_liste.append(id_projet)

        # Créer un modèle de liste de chaînes pour le QListView
        model = QStringListModel()
        model.setStringList(noms_prenoms_id_liste)

        # Assigner le modèle au QListView
        listView.setModel(model)
        listView.setProperty("IDs", ids_liste)
        listView.setProperty("IDProjets", id_projet_liste)


    def recuperer_details_personnel(self, listView):
        # Obtenir l'index de l'élément sélectionné dans le QListView
        index = listView.currentIndex()
        # Obtenir l'ID associé à l'élément sélectionné
        id_selectionne = listView.property("IDs")[index.row()]
        
        # Utiliser l'ID pour récupérer les autres détails de la base de données
        query = QSqlQuery(self.db)
        query.prepare("""
            SELECT * FROM Personnel WHERE id = ?
        """)
        query.addBindValue(id_selectionne)
        query.exec()
        
        # Vérifier si la requête a réussi et afficher les résultats
        if query.next():
            # Récupérer et afficher chaque détail
            id = query.value(0)
            nom = query.value(1)
            prenom = query.value(2)
            adresse = query.value(3)
            email = query.value(4)
            numero = query.value(5)
            print(f"ID: {id}, Nom: {nom}, Prénom: {prenom}, Adresse: {adresse}, Email: {email}, Numéro: {numero}")
            
            # Retourner les détails sous forme de dictionnaire ou de tuple, selon votre préférence
            return {
                "id": id,
                "nom": nom,
                "prenom": prenom,
                "adresse": adresse,
                "email": email,
                "numero": numero
            }
        else:
            print("Aucun détail trouvé pour l'ID sélectionné.")
            return None



    def setup_model(self):
        # Créer le QStringListModel avec les données de noms et prénoms
        self.model = QStringListModel()
        self.update_model()

    def update_model(self):
        # Mettre à jour le QStringListModel avec les données actuelles de la base de données
        query = QSqlQuery(self.db)
        query.exec("""
            SELECT Nom, Prenom FROM Personnel
        """)
        noms_prenoms_liste = []
        while query.next():
            noms_prenoms_liste.append(f"{query.value(0)} {query.value(1)}")
        self.model.setStringList(noms_prenoms_liste)
        # Ajoutez cette méthode pour définir les drapeaux des éléments

    def get_filtered_model(self, filter_text):
        # Créer et retourner un QSortFilterProxyModel filtré selon le texte fourni
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(self.model)
        proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        proxy_model.setFilterKeyColumn(-1)  # Filtrer sur toutes les colonnes
        proxy_model.setFilterRegularExpression(QRegularExpression(filter_text))
        return proxy_model


    def assigner_personnel_a_projet(self, id_personnel, id_projet):
        query = QSqlQuery(self.db)
        query.prepare("UPDATE Personnel SET id_projet = :id_projet WHERE id = :id_personnel")
        query.bindValue(":id_projet", id_projet)
        query.bindValue(":id_personnel", id_personnel)
        if not query.exec():
            print("Erreur lors de l'assignation du personnel au projet:", query.lastError().text())