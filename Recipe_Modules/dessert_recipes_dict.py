import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Recipe_Modules import dessertRecipes


class Recipe_Holder(object):
    def __init__(self, parent = None):
        self.listView = QListView()
        self.model = QStandardItemModel()
        self.recipes = recipes.RecipeContainer(QString("dessertRecipes.dat"))
        self.recipes.load()

        for recipe in self.recipes.inOrder():
            item = QStandardItem()
            item.setText(QString("%1").arg(recipe.text))
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.listView.show()

        #self.populateModel()
        #QTimer.singleShot(0, self.initialLoad)


    def populateModel(self, selectedRecipe=None):
        selected = None

        self.model.clear()

        for recipe in self.recipes.inOrder():

            item = QStandardItem()
            item.setText(QString("%1").arg(recipe.text))
            item.setAccessibleDescription(QString("%2").arg(recipe.accessible_description))
            print item.accessibleDescription()
            item.setAccessibleText(QString("%3").arg(recipe.accessible_text))
            print item.accessibleText()

            self.model.appendRow(item)
        self.listView.setModel(self.model)

    # def initialLoad(self):
    #     if not QFile.exists(self.recipes.filename):
    #         for recipe in recipes.generateFakeRecipes():
    #             self.recipes.addRecipe(recipe)
    #         self.recipes.dirty = False
    #     else:
    #         try:
    #             self.recipes.load()
    #         except IOError, e:
    #             QMessageBox.warning(self, "Recipes - Error", "Failed to load: {0}".format(e))
    #     self.populateModel()


class MainForm(QDialog):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.resize(1600,1000)

        self.listView = QListView()
        viewLabel = QLabel("View")
        viewLabel.setBuddy(self.listView)

        listLabel = QLabel("&List")
        self.listWidget = QListWidget()
        listLabel.setBuddy(self.listWidget)

        tableLabel = QLabel("&Table")
        self.tableWidget = QTableWidget()
        tableLabel.setBuddy(self.tableWidget)

        treeLabel = QLabel("Tre&e")
        self.treeWidget = QTreeWidget()
        treeLabel.setBuddy(self.treeWidget)

        addRecipeButton = QPushButton("&Add Recipe")
        removeRecipeButton = QPushButton("&Remove Recipe")
        quitButton = QPushButton("&Quit")
        addRecipeButton.setFocusPolicy(Qt.NoFocus)
        removeRecipeButton.setFocusPolicy(Qt.NoFocus)
        quitButton.setFocusPolicy(Qt.NoFocus)

        splitter = QSplitter(Qt.Horizontal)
        # vbox = QVBoxLayout()
        # vbox.addWidget(listLabel)
        # vbox.addWidget(self.listWidget)
        # widget = QWidget()
        # widget.setLayout(vbox)
        #splitter.addWidget(widget)
        vbox = QVBoxLayout()
        vbox.addWidget(tableLabel)
        vbox.addWidget(self.tableWidget)
        widget = QWidget()
        widget.setLayout(vbox)

        # splitter.addWidget(widget)
        # vbox = QVBoxLayout()
        # vbox.addWidget(viewLabel)
        # vbox.addWidget(self.listView)
        # widget = QWidget()
        # widget.setLayout(vbox)

        splitter.addWidget(widget)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(addRecipeButton)
        buttonLayout.addWidget(removeRecipeButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.connect(self.tableWidget, SIGNAL("itemChanged(QTableWidgetItem*)"), self.tableItemChanged)
        self.connect(addRecipeButton, SIGNAL("clicked()"), self.addRecipe)
        self.connect(removeRecipeButton, SIGNAL("clicked()"), self.removeRecipe)
        self.connect(quitButton, SIGNAL("clicked()"), self.accept)

        self.recipes = dessertRecipes.RecipeContainer(QString("dessertRecipes.dat"))
        self.model = QStandardItemModel(self.listView)
        #self.r = recipes.RecipeContainer(QString("recipes.dat"))
        #print self.recipes[0]
        #self.accessible_texts
        #print self.recipes.recipes #.accessible_texts
        #print(self.r.recipe(1))



        self.setWindowTitle("Dessert Recipes (dict)")
        QTimer.singleShot(0, self.initialLoad)

        self.printTitles()

        item = self.model.item(0)
        print item
        f = QStandardItem()
        f.setText('fart')
        self.model.appendRow(f)
        #print self.model.data.currentIndex()
        #a = self.recipes.load()
        #print type(a)


    def initialLoad(self):
        if not QFile.exists(self.recipes.filename):
            for recipe in dessertRecipes.generateFakeRecipes():
                self.recipes.addRecipe(recipe)
            self.recipes.dirty = False
        else:
            try:
                self.recipes.load()
            except IOError, e:
                QMessageBox.warning(self, "Recipes - Error", "Failed to load: {0}".format(e))

        self.populateList()
        self.populateTable()
        self.tableWidget.sortItems(0)
        #self.populateTree()
        self.populateModel()


    def reject(self):
        self.accept()


    def accept(self):
        if (self.recipes.dirty and
            QMessageBox.question(self, "Recipes - Save?", "Save unsaved changes?",  QMessageBox.Yes|QMessageBox.No) ==  QMessageBox.Yes):
            try:
                self.recipes.save()
            except IOError, e:
                QMessageBox.warning(self, "Recipes - Error", "Failed to save: {0}".format(e))
        QDialog.accept(self)


    def printTitles(self, selectedRecipe = None):
        selected = None
        for recipe in self.recipes.inOrder():
            print("recipe.text")
            print(recipe.text)


    def populateList(self, selectedRecipe=None):
        selected = None
        self.listWidget.clear()
        for recipe in self.recipes.inOrder():
            item = QListWidgetItem(
                    (QString("%1  :   %2  :   %3")
                     .arg(recipe.text)
                     .arg(recipe.accessible_description)
                     .arg(recipe.accessible_text)
                     ))
            self.listWidget.addItem(item)
            if selectedRecipe is not None and selectedRecipe == id(recipe):
                selected = item
        if selected is not None:
            selected.setSelected(True)
            self.listWidget.setCurrentItem(selected)

    def populateModel(self, selectedRecipe=None):
        selected = None

        #self.model = model
        self.model.clear()

        for recipe in self.recipes.inOrder():

            item = QStandardItem()
            item.setText(QString("%1").arg(recipe.text))
            item.setAccessibleDescription(QString("%2").arg(recipe.accessible_description))
            #print item.accessibleDescription()
            item.setAccessibleText(QString("%3").arg(recipe.accessible_text))
            #print item.accessibleText()

            self.model.appendRow(item)
        self.listView.setModel(self.model)



    def populateTable(self, selectedRecipe=None):
        selected = None
        self.tableWidget.clear()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(self.recipes))
        headers = ["Text", "Accessible_Description", "Accessible_Text"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, recipe in enumerate(self.recipes):
            item = QTableWidgetItem(recipe.text)
            item.setData(Qt.UserRole, QVariant(long(id(recipe))))
            if selectedRecipe is not None and selectedRecipe == id(recipe):
                selected = item
            self.tableWidget.setItem(row, dessertRecipes.TEXT, item)
            self.tableWidget.setItem(row, dessertRecipes.ACCESSIBLE_DESCRIPTION, QTableWidgetItem(recipe.accessible_description))
            self.tableWidget.setItem(row, dessertRecipes.ACCESSIBLE_TEXT, QTableWidgetItem(recipe.accessible_text))

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.resizeColumnsToContents()
        if selected is not None:
            selected.setSelected(True)
            self.tableWidget.setCurrentItem(selected)


    def populateTree(self, selectedRecipe=None):
        pass
        # selected = None
        # self.treeWidget.clear()
        # self.treeWidget.setColumnCount(2)
        # self.treeWidget.setHeaderLabels(["Country/Owner/Name", "TEU"])
        # self.treeWidget.setItemsExpandable(True)
        # parentFromCountry = {}
        # parentFromCountryOwner = {}
        # for ship in self.ships.inCountryOwnerOrder():
        #     ancestor = parentFromCountry.get(ship.country)
        #     if ancestor is None:
        #         ancestor = QTreeWidgetItem(self.treeWidget, [ship.country])
        #         parentFromCountry[ship.country] = ancestor
        #     countryowner = ship.country + "/" + ship.owner
        #     parent = parentFromCountryOwner.get(countryowner)
        #     if parent is None:
        #         parent = QTreeWidgetItem(ancestor, [ship.owner])
        #         parentFromCountryOwner[countryowner] = parent
        #     item = QTreeWidgetItem(parent, [ship.name,
        #             QString("%L1").arg(ship.teu)])
        #     item.setTextAlignment(1, Qt.AlignRight|Qt.AlignVCenter)
        #     if selectedShip is not None and selectedShip == id(ship):
        #         selected = item
        #     self.treeWidget.expandItem(parent)
        #     self.treeWidget.expandItem(ancestor)
        # self.treeWidget.resizeColumnToContents(0)
        # self.treeWidget.resizeColumnToContents(1)
        # if selected is not None:
        #     selected.setSelected(True)
        #     self.treeWidget.setCurrentItem(selected)


    def addRecipe(self):
        recipe = dessertRecipes.Recipe("Unknown", "Unknown", "Unknown")
        self.recipes.addRecipe(recipe)
        self.populateList()
        #self.populateTree()
        self.populateTable(id(recipe))
        self.tableWidget.setFocus()
        self.tableWidget.editItem(self.tableWidget.currentItem())


    def tableItemChanged(self, item):
        recipe = self.currentTableRecipe()
        if recipe is None:
            return
        column = self.tableWidget.currentColumn()
        if column == dessertRecipes.TEXT:
            recipe.text = item.text().trimmed()
        elif column == dessertRecipes.ACCESSIBLE_DESCRIPTION:
            recipe.accessible_description = item.text().trimmed()
        elif column == dessertRecipes.ACCESSIBLE_TEXT:
            recipe.accessible_text = item.text().trimmed()
        # elif column == ships.DESCRIPTION:
        #     recipe.description = item.text().trimmed()
        # elif column == ships.TEU:
        #     recipe.teu = item.text().toInt()[0]

        self.recipes.dirty = True
        self.populateList()
        #self.populateTree()


    def currentTableRecipe(self):
        item = self.tableWidget.item(self.tableWidget.currentRow(), 0)
        if item is None:
            return None
        return self.recipes.recipe(
                item.data(Qt.UserRole).toLongLong()[0])


    def removeRecipe(self):
        recipe = self.currentTableRecipe()
        if recipe is None:
            return
        if (QMessageBox.question(self, "Recipes - Remove", (QString("Remove %1 of %2/%3?").arg(recipe.text)
	                                                            .arg(recipe.accessible_description)
	                                                            .arg(recipe.accessible_text)), QMessageBox.Yes|QMessageBox.No) == QMessageBox.No):
            return

        self.recipes.removeRecipe(recipe)
        self.populateList()
        #self.populateTree()
        self.populateTable()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    #rh = Recipe_Holder()

    app.exec_()