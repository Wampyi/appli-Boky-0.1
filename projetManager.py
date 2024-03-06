# Importer le module QtSql pour accéder à la base de données
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import QSortFilterProxyModel, QRegularExpression, QStringListModel
from PySide6 import QtCore


import sqlite3
class ProjetManager:
    def __init__(self):
        # Créer ou ouvrir la connexion à la base de données 
        self.db = QSqlDatabase.addDatabase("QSQLITE","gestion_projet")
        self.db.setDatabaseName("GESTION_ENTREPRISE")
        self.db.open()
        # Création de la table projet dans la table 
        query = QSqlQuery(self.db)
        query.exec("""
            CREATE TABLE IF NOT EXISTS projet (
                id INTEGER PRIMARY KEY,
                Nom TEXT,
                societe TEXT,
                email TEXT,
                numero TEXT,
                Date_début TEXT,
                Date_fin TEXT
            )
        """)
        # ... initialisation de la base de données et autres configurations ...
        self.model = QStringListModel()  # Initialisation de l'attribut model
        self.setup_model()  

    def ajouter_projet(self, Nom, societe, email, numero, Date_début, Date_fin):
        query = QSqlQuery(self.db)
        query.prepare("""
            INSERT INTO projet (Nom, societe, email, numero, Date_début, Date_fin)
            VALUES (?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(Nom)
        query.addBindValue(societe)
        query.addBindValue(email)
        query.addBindValue(numero)
        query.addBindValue(Date_début)
        query.addBindValue(Date_fin)
        query.exec()

    def afficher_projet(self, tableWidget):
        tableWidget.setRowCount(0)
        query = QSqlQuery(self.db)
        query.exec("""
            SELECT * FROM projet
        """)
        while query.next():
            row = tableWidget.rowCount()
            tableWidget.insertRow(row)
            for column in range(6):
                tableWidget.setItem(row, column, QTableWidgetItem(str(query.value(column))))

    def setup_model(self):
        # Créer le QStringListModel avec les données de noms et prénoms
        self.model = QStringListModel()
        pass


    def remplir_combobox_projets(self, combobox):
        combobox.clear()
        query = QSqlQuery(self.db)
        query.exec("SELECT id, Nom FROM projet")
        while query.next():
            id_projet = query.value(0)
            nom_projet = query.value(1)
            combobox.addItem(nom_projet, id_projet)

    
