from ontology import Ontology
from document import Document
from efreq_rnum import EfreqRnum
from metrics_dialog import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.fileLoadTab = QtWidgets.QWidget()
        self.fileLoadTab.setObjectName("fileLoadTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fileLoadTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.fileLoadTab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selectOntologyPushButton = QtWidgets.QPushButton(self.fileLoadTab)
        self.selectOntologyPushButton.setObjectName("selectOntologyPushButton")
        self.horizontalLayout.addWidget(self.selectOntologyPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.fileLoadTab)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.ontologyLabel = QtWidgets.QLabel(self.fileLoadTab)
        self.ontologyLabel.setObjectName("ontologyLabel")
        self.horizontalLayout_8.addWidget(self.ontologyLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.fileLoadTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.selectDocumentsPushButton = QtWidgets.QPushButton(self.fileLoadTab)
        self.selectDocumentsPushButton.setObjectName("selectDocumentsPushButton")
        self.horizontalLayout_2.addWidget(self.selectDocumentsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.documentsListWidget = QtWidgets.QListWidget(self.fileLoadTab)
        self.documentsListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.documentsListWidget.setObjectName("documentsListWidget")
        self.verticalLayout_2.addWidget(self.documentsListWidget)
        self.tabWidget.addTab(self.fileLoadTab, "")
        self.processingTextTab = QtWidgets.QWidget()
        self.processingTextTab.setEnabled(False)
        self.processingTextTab.setObjectName("processingTextTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.processingTextTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.processingTextTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.documentsListWidget_2 = QtWidgets.QListWidget(self.processingTextTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.documentsListWidget_2.sizePolicy().hasHeightForWidth())
        self.documentsListWidget_2.setSizePolicy(sizePolicy)
        self.documentsListWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.documentsListWidget_2.setObjectName("documentsListWidget_2")
        self.verticalLayout_6.addWidget(self.documentsListWidget_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.processingTextTab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.keyTermListWidget = QtWidgets.QListWidget(self.processingTextTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyTermListWidget.sizePolicy().hasHeightForWidth())
        self.keyTermListWidget.setSizePolicy(sizePolicy)
        self.keyTermListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.keyTermListWidget.setObjectName("keyTermListWidget")
        self.verticalLayout_4.addWidget(self.keyTermListWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.processingTextTab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.sentencesTextBrowser = QtWidgets.QTextBrowser(self.processingTextTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.sentencesTextBrowser.sizePolicy().hasHeightForWidth())
        self.sentencesTextBrowser.setSizePolicy(sizePolicy)
        self.sentencesTextBrowser.setObjectName("sentencesTextBrowser")
        self.verticalLayout_5.addWidget(self.sentencesTextBrowser)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.saveSubOntologyPushButton = QtWidgets.QPushButton(self.processingTextTab)
        self.saveSubOntologyPushButton.setObjectName("saveSubOntologyPushButton")
        self.horizontalLayout_7.addWidget(self.saveSubOntologyPushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.processingTextTab, "")
        self.rankedDocumentsTab = QtWidgets.QWidget()
        self.rankedDocumentsTab.setEnabled(False)
        self.rankedDocumentsTab.setObjectName("rankedDocumentsTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rankedDocumentsTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.rankedDocumentsTab)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.rankedDocumentsTab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.NLineEdit = QtWidgets.QLineEdit(self.rankedDocumentsTab)
        self.NLineEdit.setObjectName("NLineEdit")
        self.horizontalLayout_5.addWidget(self.NLineEdit)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.rankedDocumentsTab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.KLineEdit = QtWidgets.QLineEdit(self.rankedDocumentsTab)
        self.KLineEdit.setObjectName("KLineEdit")
        self.horizontalLayout_4.addWidget(self.KLineEdit)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.rankedDocumentsTab)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.BComboBox = QtWidgets.QComboBox(self.rankedDocumentsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BComboBox.sizePolicy().hasHeightForWidth())
        self.BComboBox.setSizePolicy(sizePolicy)
        self.BComboBox.setObjectName("BComboBox")
        self.BComboBox.addItem("")
        self.BComboBox.addItem("")
        self.BComboBox.addItem("")
        self.BComboBox.addItem("")
        self.horizontalLayout_9.addWidget(self.BComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.rankDocumentsPushButton = QtWidgets.QPushButton(self.rankedDocumentsTab)
        self.rankDocumentsPushButton.setObjectName("rankDocumentsPushButton")
        self.verticalLayout_3.addWidget(self.rankDocumentsPushButton)
        self.label_7 = QtWidgets.QLabel(self.rankedDocumentsTab)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.rankedDocumentsTableWidget = QtWidgets.QTableWidget(self.rankedDocumentsTab)
        self.rankedDocumentsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rankedDocumentsTableWidget.setObjectName("rankedDocumentsTableWidget")
        self.rankedDocumentsTableWidget.setColumnCount(3)
        self.rankedDocumentsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.rankedDocumentsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rankedDocumentsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rankedDocumentsTableWidget.setHorizontalHeaderItem(2, item)
        self.rankedDocumentsTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.rankedDocumentsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.rankedDocumentsTableWidget)
        self.tabWidget.addTab(self.rankedDocumentsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_slots()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "?????????????????????? ??????????????????"))
        self.selectOntologyPushButton.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.label_10.setText(_translate("MainWindow", "?????????????? ??????????????????:"))
        self.ontologyLabel.setText(_translate("MainWindow", "<??????????????????????>"))
        self.label_2.setText(_translate("MainWindow", "?????????????????? ?????? ????????????????????????"))
        self.selectDocumentsPushButton.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fileLoadTab), _translate("MainWindow", "???????????????? ????????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????? ????????????????:"))
        self.label_8.setText(_translate("MainWindow", "?????????????????????????? ??????????????:"))
        self.label_9.setText(_translate("MainWindow", "??????????????????????:"))
        self.saveSubOntologyPushButton.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processingTextTab), _translate("MainWindow", "?????????????????? ????????????"))
        self.label_6.setText(_translate("MainWindow", "??????????????????"))
        self.label_4.setText(_translate("MainWindow", "N ="))
        self.NLineEdit.setText(_translate("MainWindow", "10"))
        self.label_5.setText(_translate("MainWindow", "K ="))
        self.KLineEdit.setText(_translate("MainWindow", "5"))
        self.label_11.setText(_translate("MainWindow", "Beta ="))
        self.BComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.BComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.BComboBox.setItemText(2, _translate("MainWindow", "5"))
        self.BComboBox.setItemText(3, _translate("MainWindow", "10"))
        self.rankDocumentsPushButton.setText(_translate("MainWindow", "?????????????????? ????????????????????????"))
        self.label_7.setText(_translate("MainWindow", "?????????????????????????????? ?????????????????? ???? ??????????????????????????"))
        item = self.rankedDocumentsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "???????????????? ??????????????????"))
        item = self.rankedDocumentsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.rankedDocumentsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rankedDocumentsTab), _translate("MainWindow", "???????????????????????? ????????????????????"))


    def add_slots(self):
        self.selectOntologyPushButton.clicked.connect(self.slot_open_ontology)
        self.selectDocumentsPushButton.clicked.connect(self.slot_open_documents)
        self.documentsListWidget_2.itemClicked.connect(self.slot_select_document)
        self.saveSubOntologyPushButton.clicked.connect(self.slot_save_selected_subontology)
        self.rankDocumentsPushButton.clicked.connect(self.slot_rank_documents)

    def __open_file_dialog(self, filter='All Files(*.*)'):
        return QtWidgets.QFileDialog.getOpenFileNames(filter=filter)[0]

    def slot_open_ontology(self) -> None:
        paths = self.__open_file_dialog(filter='Ontology Files(*.ont)')
        if paths:
            self.ontology = Ontology(paths[0])
            self.ontologyLabel.setText(self.ontology.filename)
            self.__is_all_download()
    
    def slot_open_documents(self) -> None:
        paths = self.__open_file_dialog(filter='Text Files(*.txt)')
        if paths:
            self.documentsListWidget.clear()
            self.documentsListWidget_2.clear()
            self.documents = list()
            for path in paths:
                doc = Document(path)
                self.documents.append(doc)
                self.documentsListWidget.addItem(QtWidgets.QListWidgetItem(doc.filename))
                item = QtWidgets.QListWidgetItem(doc.filename)
                item.setData(QtCore.Qt.ItemDataRole.UserRole, doc)
                self.documentsListWidget_2.addItem(item)
            self.__is_all_download()


    def __is_all_download(self):
        if hasattr(self, 'ontology') and hasattr(self, 'documents'):
            self.processingTextTab.setEnabled(True)
            self.saveSubOntologyPushButton.setEnabled(False)
            self.rankedDocumentsTab.setEnabled(True)
            self.__get_key_terms()


    def __get_key_terms(self):
        for doc in self.documents:
            doc.get_key_term(self.ontology)


    def slot_select_document(self):
        selected_items = self.documentsListWidget_2.selectedItems()
        if len(selected_items) == 1:
            self.saveSubOntologyPushButton.setEnabled(True)
        else:
            self.saveSubOntologyPushButton.setEnabled(False)
        doc = selected_items[0].data(QtCore.Qt.ItemDataRole.UserRole)
        
        self.keyTermListWidget.clear()
        for term in doc.key_terms:
            item = QtWidgets.QListWidgetItem(term.name)
            item.setData(QtCore.Qt.ItemDataRole.UserRole, term)
            self.keyTermListWidget.addItem(item)
        self.keyTermListWidget.itemClicked.connect(self.slot_select_term)


    def __highlight_terms(self, sentence, term) -> str:
        result = ""
        last_position = 0
        for s_term in sentence.find_term(term):
            start = sentence.text.find(s_term, last_position)
            result += sentence.text[last_position:start]
            last_position = start + len(s_term)
            result += f'<span style=\" color: #ff0000;\">{sentence.text[start:last_position]}</span>'
        result += sentence.text[last_position:]
        return result


    def slot_select_term(self):
        selected_doc = self.documentsListWidget_2.selectedItems()
        doc = selected_doc[0].data(QtCore.Qt.ItemDataRole.UserRole)

        selected_term = self.keyTermListWidget.selectedItems()
        term = selected_term[0].data(QtCore.Qt.ItemDataRole.UserRole)
        
        self.sentencesTextBrowser.clear()
        # text = '\n'.join([str(i) + ". " + sentence.text for i, sentence in enumerate(doc.key_terms[term], start=1)])
        text = '<br>'.join([str(i) + ". " + self.__highlight_terms(sentence, term) for i, sentence in enumerate(doc.key_terms[term], start=1)])
        self.sentencesTextBrowser.setText(text)


    def slot_save_selected_subontology(self):
        doc = self.documentsListWidget_2.selectedItems()[0].data(QtCore.Qt.ItemDataRole.UserRole)
        self.ontology.write_connected_subgraph(doc.key_term_ids(), doc.filename)
        mess_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information ,'??????????????????', '??????????????????, ???????????????????? ??????????????????, ?????????????? ??????????????????!', QtWidgets.QMessageBox.StandardButton.Ok)
        mess_box.exec_()


    def calc_document_efreq_rnums(self, n:int, k:int, beta:int):
        self.efreq_rnums = []
        for doc in self.documents:
            self.efreq_rnums.append(EfreqRnum(self.ontology, doc, n, k, beta))


    def add_doc_to_rank_table(self):
        self.rankedDocumentsTableWidget.clearContents()
        self.rankedDocumentsTableWidget.setRowCount(len(self.efreq_rnums))
        def create_row(self, i:int, efreq:EfreqRnum):
            doc_name_item = QtWidgets.QTableWidgetItem(efreq.doc.filename)
            rank_item = QtWidgets.QTableWidgetItem(str(round(efreq.r, 4)))
            more_btn = QtWidgets.QPushButton()
            more_btn.setIcon(QtGui.QIcon.fromTheme('dialog-information'))
            more_btn.clicked.connect(lambda: self.slot_open_metrics_dialog(i))
            self.rankedDocumentsTableWidget.setItem(i, 0, doc_name_item)
            self.rankedDocumentsTableWidget.setItem(i, 1, rank_item)
            self.rankedDocumentsTableWidget.setCellWidget(i, 2, more_btn)

        for i, efreq in enumerate(self.efreq_rnums):
            create_row(self, i, efreq)
        # self.rankedDocumentsTableWidget.resizeColumnsToContents()


    def slot_rank_documents(self):
        n = int(self.NLineEdit.text())
        k = int(self.KLineEdit.text())
        beta = int(self.BComboBox.currentText())
        self.calc_document_efreq_rnums(n, k, beta)
        self.efreq_rnums.sort(key=lambda efreq: efreq.r, reverse=True)
        self.add_doc_to_rank_table()


    def slot_open_metrics_dialog(self, i: int):
        metrics_dialog = QtWidgets.QDialog()
        ui_dialog = Ui_Dialog()
        ui_dialog.setupUi(metrics_dialog)
        ui_dialog.okPushButton.clicked.connect(lambda: metrics_dialog.close())
        ui_dialog.fill_metrics_table(self.efreq_rnums[i])
        metrics_dialog.exec_()





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)  # create application
    MainWindow = QtWidgets.QMainWindow()    # create main GUI window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())