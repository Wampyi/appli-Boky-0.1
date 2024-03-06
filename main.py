import sys
from PySide6 import QtCore
from PySide6.QtCore import*
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,QDialog,QLineEdit
    ,QWidget)
from ui_main import Ui_MainWindow
from PySide6.QtSql import (QSqlQueryModel,QSqlQuery,QSqlDatabase)

import projetManager
import personnelManager
from Dialogue_ui import Ui_Dialog


from UIFunctions import*
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.personnel_manager = personnelManager.PersonnelManager()
        self.projet_manager = projetManager.ProjetManager()
        self.ui.setupUi(self)
        self.ui.listView_personnel.clicked.connect(self.recuperer_details_personnel)
        self.ui_dialog = Ui_Dialog() # Créer l'objet ui_dialog et le stocker dans l'attribut self.ui_dialog
       


        # COMMANDE BOUTTON MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.Btn_personnel.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(0))
        self.ui.Btn_projet.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(2))
        self.ui.Btn_depot.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(1))
        
        # COMMANDE BOUTTON MENU PERSONNEL
        self.ui.Btn_liste.clicked.connect(lambda: self.ui.SW_pg_personnal.setCurrentIndex(0))
        self.ui.Btn_ajouter.clicked.connect(lambda: self.ui.SW_pg_personnal.setCurrentIndex(1))
        self.ui.Btn_organiser.clicked.connect(lambda: self.ui.SW_pg_personnal.setCurrentIndex(2))
        # COMMANDE BOUTTON MENU PROJET
        self.ui.pb_listeProjet.clicked.connect(lambda: self.ui.stackedWidget_projet.setCurrentIndex(0))
        self.ui.pb_ajoutProjet.clicked.connect(lambda: self.ui.stackedWidget_projet.setCurrentIndex(1))

        # COMMANDE BOUTTON BDD PROJET 
        self.ui.Btn_ajouter_projet.clicked.connect(self.ajouter_projet)
        self.ui.btn_actualiser_projet.clicked.connect(self.afficher_projet)

        # COMMANDE BOUTTON BDD PERSONNELLE 
        self.ui.Boutton_OK.clicked.connect(self.ajouter_personnel)
        self.ui.btn_Actualiser.clicked.connect(self.afficher_personnel)
        # Initialiser l'affichage du personnel
        self.afficher_personnel()

        # BOUTTON FILTRAGE
        self.ui.Button_recherche_personnel.clicked.connect(self.afficher_noms_prenoms)
        
        # Connectez le QLineEdit à la méthode de filtrage
        self.ui.lineEdit_recherche_personnel.textChanged.connect(self.filter_noms_prenoms)

        self.ui.Button_assignation_personnel.clicked.connect(self.ouvrir_dialogue_assignation)


        self.show()

    def ajouter_projet(self):
    # Récupérer les données des QTextEdit de projet
        
        nom = self.ui.textEdit_NOM_projet.toPlainText()
        societe = self.ui.textEdit_societe.toPlainText()
        numero = self.ui.textEdit_numero_projet.toPlainText()
        email = self.ui.textEdit_Email_projet.toPlainText()
        date_debut = self.ui.textEdit_date_debut.toPlainText()
        date_fin = self.ui.textEdit_date_fin.toPlainText()
   # Appeler la méthode d'ajout de la classe ProjetManager
        self.projet_manager.ajouter_projet(nom, societe, numero, email, date_debut,date_fin)
   # Effacer le contenu des QTextEdit après l'ajout
        self.ui.textEdit_NOM_projet.clear()
        self.ui.textEdit_societe.clear()
        self.ui.textEdit_Email_projet.clear()
        self.ui.textEdit_date_debut.clear()
        self.ui.textEdit_numero_projet.clear()
        self.ui.textEdit_date_fin.clear()
# Définir la méthode d'affichage de la classe MainWindow
    def afficher_projet(self):
    # Appeler la méthode d'affichage de la classe ProjetManager en passant le QTableWidget
        self.projet_manager.afficher_projet(self.ui.tableWidget_projet)


    def ajouter_personnel(self):
    # Récupérer les données des QTextEdit
        id = self.ui.textEdit_ID.toPlainText()
        nom = self.ui.textEdit_Nom.toPlainText()
        prenom = self.ui.textEdit_Prenom.toPlainText()
        adresse = self.ui.textEdit_Adresse.toPlainText()
        email = self.ui.textEdit_Email.toPlainText()
        numero = self.ui.textEdit_Numero.toPlainText()
    # Appeler la méthode d'ajout de la classe PersonnelManager
        self.personnel_manager.ajouter_personnel(id, nom, prenom, adresse, email, numero)
         # Effacer le contenu des QTextEdit après l'ajout
        self.ui.textEdit_ID.clear()
        self.ui.textEdit_Nom.clear()
        self.ui.textEdit_Prenom.clear()
        self.ui.textEdit_Adresse.clear()
        self.ui.textEdit_Email.clear()
        self.ui.textEdit_Numero.clear()
# Définir la méthode d'affichage de la classe MainWindow
    def afficher_personnel(self):
        # Mettre à jour le modèle avec les données actuelles
        self.personnel_manager.update_model()
        # Afficher les données dans le QListView
        self.ui.listView_personnel.setModel(self.personnel_manager.model)
        # Si vous avez besoin d'afficher les données dans un QTableWidget également
        # Appeler la méthode d'affichage de la classe PersonnelManager en passant le QTableWidget
        self.personnel_manager.afficher_personnel(self.ui.tableWidget_personnel)

    def afficher_noms_prenoms(self):
        # Appeler la méthode d'affichage des noms et prénoms de la classe PersonnelManager
        self.personnel_manager.afficher_noms_prenoms(self.ui.listView_personnel)
    # Filtrage    


    def filter_noms_prenoms(self, text):
        # Obtenir le modèle filtré du PersonnelManager et l'appliquer au QListView
        filtered_model = self.personnel_manager.get_filtered_model(text)
        self.ui.listView_personnel.setModel(filtered_model)

    def recuperer_details_personnel(self, index):
        # Appeler la méthode de 'personnelManager' avec l'index sélectionné
        details = self.personnel_manager.recuperer_details_personnel(self.ui.listView_personnel)
        if details:
            print(f"Détails récupérés : {details}")
        else:
            print("Aucun détail n'a été récupéré.")



    def ouvrir_dialogue_assignation(self):
        self.dialogue = QDialog() 
        self.ui_dialog.setupUi(self.dialogue)
        self.projet_manager.remplir_combobox_projets(self.ui_dialog.comboBox_assignation)
        self.ui_dialog.pushButton_assigner.clicked.connect(lambda: self.on_assigner_clicked(self.ui.listView_personnel))
        self.dialogue.exec()

    def on_assigner_clicked(self, listView):
        # Obtenir l'index de l'élément sélectionné dans le QListView
        index = listView.currentIndex()
        # Obtenir l'ID du personnel sélectionné à partir du modèle du QListView
        id_personnel = listView.model().data(index, Qt.UserRole)
        # Obtenir l'ID du projet sélectionné dans le QComboBox du dialogue
        id_projet = self.ui_dialog.comboBox_assignation.currentData()
        # Appeler la méthode assigner_personnel_a_projet avec les ID obtenus
        self.personnel_manager.assigner_personnel_a_projet(id_personnel, id_projet)
        # Fermer le dialogue
        self.dialogue.close()


        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

