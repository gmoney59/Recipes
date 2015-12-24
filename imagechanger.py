import os
import platform
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Recipe_Modules import addRecipeDialog
from Recipe_Modules import helpform
from Recipe_Modules import newimagedlg
from Recipe_Modules import resizedlg
from Recipe_Modules import ui_imagechanger2
from Recipe_Modules import Create_Recipe
from Recipe_Modules import recipes
from Recipe_Modules import dessertRecipes
from Recipe_Modules import qrc_resources


__version__ = "1.0.1"


class RecipeBook(QMainWindow, ui_imagechanger2.Ui_MainWindow):

    def __init__(self, parent=None):
        super(RecipeBook, self).__init__(parent)
        self.setupUi(self)

        self.imagePath = "C:/Python27/rDialog/Family_Pictures/"

        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False
        self.scaled = False

        #self.imageLabel = QLabel()
        #self.pageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft) # | Qt.AlignTop)
        #self.imageLabel.setAlignment(Qt.AlignCenter) #| Qt.AlignLeft)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        #self.imageLabel.setScaledContents(True)
        # self.setCentralWidget(self.imageLabel)

        # rd = recipes_dict.MainForm()
        # r = recipes.Recipe("aaa", "textRecipe", "aaa.txt")
        # rc = recipes.RecipeContainer()
        # rc.addRecipe(r)

        #self.pageLabel_2.
        self.pageLabel_2.setAcceptRichText(True)
        self.printer = None

        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

        #fileNewAction = self.createAction("&New...", self.fileNew, QKeySequence.New, "filenew", "Create an image file")  # addRecipeForm
        fileNewAction = self.createAction("&New...", self.addRecipeForm, QKeySequence.New, "filenew", "Create a recipe document file")
        fileNewImageAction = self.createAction("&New Image...", self.fileNew, QKeySequence.New, "filenew", "Create a new image.")
        fileNewRecipeDlg = self.createAction("&New Recipe Dlg...", self.fileNewDlg, QKeySequence.New, "filenew", "Create a new Dlg.")
        fileOpenAction = self.createAction("&Open...", self.fileOpen, QKeySequence.Open, "fileopen", "Open an existing image file")
        fileSaveAction = self.createAction("&Save", self.fileSave, QKeySequence.Save, "filesave", "Save the image")
        fileSaveAsAction = self.createAction("Save &As...", self.fileSaveAs, icon="filesaveas", tip="Save the image using a new name")
        filePrintAction = self.createAction("&Print", self.filePrint, QKeySequence.Print, "fileprint", "Print the image")
        fileQuitAction = self.createAction("&Quit", self.close, "Ctrl+Q", "filequit", "Close the application")

        editInvertAction = self.createAction("&Invert",self.editInvert, "Ctrl+I", "editinvert","Invert the image's colors", True, "toggled(bool)")
        editSwapRedAndBlueAction = self.createAction("Sw&ap Red and Blue", self.editSwapRedAndBlue,"Ctrl+A", "editswap", "Swap the image's red and blue color components", True, "toggled(bool)")
        editZoomAction = self.createAction("&Zoom...", self.editZoom, "Alt+Z", "editzoom", "Zoom the image")
        mirrorGroup = QActionGroup(self)
        editUnMirrorAction = self.createAction("&Unmirror",      self.editUnMirror, "Ctrl+U", "editunmirror",              "Unmirror the image", True, "toggled(bool)")
        mirrorGroup.addAction(editUnMirrorAction)
        editMirrorHorizontalAction = self.createAction( "Mirror &Horizontally", self.editMirrorHorizontal,    "Ctrl+H", "editmirrorhoriz",   "Horizontally mirror the image", True, "toggled(bool)")
        mirrorGroup.addAction(editMirrorHorizontalAction)
        editMirrorVerticalAction = self.createAction(  "Mirror &Vertically", self.editMirrorVertical,"Ctrl+V", "editmirrorvert", "Vertically mirror the image", True, "toggled(bool)")
        mirrorGroup.addAction(editMirrorVerticalAction)
        editUnMirrorAction.setChecked(True)

        helpAboutAction = self.createAction("&About Image Changer",   self.helpAbout)
        helpHelpAction = self.createAction("&Help", self.helpHelp, QKeySequence.HelpContents)
        resize_action = self.createAction("&Resize the image", self.resize_image, "Alt+R", "editresize", "Resize the image")

        #scaleAction = self.createAction( "Scale I&mage", self.setScaleImageTrue, "toogled(bool") #,    "Ctrl+M", "scaleimage",   "Scale the Image", True, "toggled(bool)")
        #scaleAction = self.createAction( "Scale I&mage", self.editScale, "toogled(bool)")
        scaleAction = self.createAction( "Scale I&mage", self.setScaleImageTrue, "toogled(bool)") #, checkable=True)
        deScaleAction = self.createAction("De-Scale Image", self.setScaleImageFalse, "toogled(bool)") #, checkable=True)
        #scaleTrueAction = self.createAction("Scale", self.setScaleImageTrue, "Scale the Image", True, "toggled(bool)")

        self.menuFileActions = (fileNewAction, fileNewImageAction, fileNewRecipeDlg, fileOpenAction,  fileSaveAction, fileSaveAsAction, None,  filePrintAction, fileQuitAction)
        self.connect(self.menuFile, SIGNAL("aboutToShow()"),   self.updateMenuFile)
        self.addActions(self.menuEdit, (editInvertAction, editSwapRedAndBlueAction, editZoomAction, resize_action))
        mirrorMenu = self.menuEdit.addMenu(QIcon(":/editmirror.png"),   "&Mirror")
        self.addActions(mirrorMenu, (editUnMirrorAction,  editMirrorHorizontalAction, editMirrorVerticalAction))
        self.addActions(self.menuHelp, (helpAboutAction, helpHelpAction))

        self.menuScaleActions = (scaleAction, deScaleAction)

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolBar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction, fileSaveAsAction))
        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolBar")
        self.addActions(editToolbar, (editInvertAction,editSwapRedAndBlueAction, editUnMirrorAction, editMirrorVerticalAction, editMirrorHorizontalAction,scaleAction, deScaleAction))
        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setRange(1, 400)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setToolTip("Zoom the image")
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.connect(self.zoomSpinBox, SIGNAL("valueChanged(int)"), self.showImage)
        editToolbar.addWidget(self.zoomSpinBox)

        #scaleToolBar = self.addToolBar("Scale")
        #scaleToolBar.setObjectName("ScaleToolBar")
        #self.addActions(scaleToolBar, scaleAction)

        self.addActions(self.imageLabel, (editInvertAction, editSwapRedAndBlueAction, editUnMirrorAction,   editMirrorVerticalAction, editMirrorHorizontalAction, scaleAction))
        self.resetableActions = ((editInvertAction, False), (editSwapRedAndBlueAction, False), (editUnMirrorAction, True), (scaleAction, True))

        settings = QSettings()
        self.recentFiles = settings.value("RecentFiles").toStringList()
        size = settings.value("MainWindow/Size", QVariant(QSize(600, 1500))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position", QVariant(QPoint(0, 0))).toPoint()
        self.move(position)
        self.restoreState(settings.value("MainWindow/State").toByteArray())

		### !!!!!!!!!! #####
        self.recipes = recipes.RecipeContainer(QString("recipes.dat"))
        self.recipes.load()

        self.dessertRecipes = dessertRecipes.RecipeContainer(QString("dessertRecipes.dat"))
        self.dessertRecipes.load()


########################################################################################################################

		# Adding some DINNER data: ###################################################
        self.model = QStandardItemModel(self.listView_2)

        item = QStandardItem()
        item.setText('Dinner Time')
        font = QFont("Times",20,QFont.Bold,True)
        item.setFont(font)
        item.setAccessibleDescription('grandmaImage')
        item.setAccessibleText('dinnerTime.JPG')
        self.model.appendRow(item)

        self.populateModel()

        # item = QStandardItem()
        # item.setText('Hearty Beef Stew')
        # font = QFont("Times",20,QFont.Bold,True)
        # item.setFont(font)
        # item.setAccessibleDescription('grandmaImage')
        # item.setAccessibleText('Hearty_Beef_Stew.JPG')
        # self.model.appendRow(item)
        #

        # Adding some DESSERT data: ##################################################
        self.dessertModel = QStandardItemModel(self.listView_3)
        #self.populateDessertModel()

        item = QStandardItem()
        item.setText('Desserts Home')
        font = QFont("Times",20,QFont.Bold,True)
        item.setFont(font)
        item.setAccessibleDescription('grandmaImage')
        #item.setAccessibleText('Peanut_Butter_Kisses.JPG')
        item.setAccessibleText('Desserts_Cropped.JPG')
        self.dessertModel.appendRow(item)
        #p = self.imagePath + 'Desserts_Cropped.JPG'
        #self.showDessertRecipe()
        #self.loadFile(p)

        i = item.index()
        print i.row()
        print i.data(role = Qt.DisplayRole).toString()
        print i.data(role = Qt.AccessibleTextRole).toString()


        a = self.dessertModel.rowCount()
        b = self.dessertModel.item(0)
        b.setData('nig')
        c = self.dessertModel.indexFromItem(b)
        print c
        m = QModelIndex()
        print m
        print m.data(role = Qt.AccessibleTextRole).toString()


		#i = self.dessertModel.item(0)
        #i.
        #print self.dessertModel.item(0).data().toString()

        #
        #self.listView_3.isS
        #self.listView_3.setCurrentIndex(0)
        #
        self.populateDessertModel()

        #self.listView_3.setCurrentIndex(self.model.index(0,0))
        #self.listView_3.model().setCurrentIndex(0)# .setC  CurrentIndex(index(0)) #self.dessertModel().index(0))
        #self.showDessertRecipe()

        item = QStandardItem()
        item.setText('Peanut Butter Kisses')
        item.setAccessibleDescription('grandmaImage')
        #item.setAccessibleText('Peanut_Butter_Kisses.JPG')
        item.setAccessibleText('Peanut Butter Kisses.JPG')
        self.dessertModel.appendRow(item)

        j = item.index()
        print j.row()

        k = self.listView_3.currentIndex()
        print k
        print k.row()

        #self.listView_3.setModelIndex

##########################################################################################
        self.pushButton_1.setText("Scaled: TRUE")
        self.pushButton_2.setText("Scaled: FALSE")
        self.pushButton_1.clicked.connect(self.setScaleImageTrue)
        self.pushButton_2.clicked.connect(self.setScaleImageFalse) #editScale
        #self.pushButton_3.clicked.connect(self.editScale)
        self.pushButton_3.clicked.connect(self.currentText)

        ### Score:
        #self.connect(self.listView_2, SIGNAL("clicked(QModelIndex)"), self.printAccessibleTextRole)
        self.connect(self.listView_2, SIGNAL("clicked(QModelIndex)"), self.showRecipe)

        self.connect(self.listView_3, SIGNAL("clicked(QModelIndex)"), self.showDessertRecipe)

        self.connect(self.tabWidget, SIGNAL("currentChanged(int)"), self.currentTab)


        self.setWindowTitle("Recipe Viewer")
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.updateMenuFile()
        QTimer.singleShot(0, self.loadInitialFile)
        #self.listView.setCurrentIndex(self.model.index(0,0))



    def populateModel(self, selectedRecipe=None):
        for recipe in self.recipes.inOrder():
            item = QStandardItem()
            item.setText(QString("%1").arg(recipe.text))
            item.setAccessibleDescription(QString("%2").arg(recipe.accessible_description))
            item.setAccessibleText(QString("%3").arg(recipe.accessible_text))

            self.model.appendRow(item)
        self.listView_2.setModel(self.model)


    def populateDessertModel(self, selectedRecipe=None):
        for recipe in self.dessertRecipes.inOrder():
            item = QStandardItem()
            item.setText(QString("%1").arg(recipe.text))
            item.setAccessibleDescription(QString("%2").arg(recipe.accessible_description))
            item.setAccessibleText(QString("%3").arg(recipe.accessible_text))

            self.dessertModel.appendRow(item)
        self.listView_3.setModel(self.dessertModel)

	# def addRecipe(self):
	# 	recipe = recipes.Recipe("", "", "")
	# 	self.recipes.addRecipe(recipe)


    def currentTab(self):
        print self.tabWidget.currentIndex()
        if self.tabWidget.currentIndex() == 0:
            self.loadFile("C:/Python27/rDialog/Family_Pictures/Home.JPG")
        elif self.tabWidget.currentIndex() == 1:
            self.loadFile("C:/Python27/rDialog/Family_Pictures/dinnerTime.JPG")
        elif self.tabWidget.currentIndex() == 2:
            self.loadFile("C:/Python27/rDialog/Family_Pictures/Desserts_Cropped.JPG")




    def setScaleImageTrue(self):
        self.imageLabel.setScaledContents(True)
        print('scale true')

    def setScaleImageFalse(self):
        self.imageLabel.setScaledContents(False)


    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def printAccessibleTextRole(self):
        role = self.listView_2.currentIndex().data(role = Qt.AccessibleTextRole).toString()
        print role

    def currentText(self):
        text = self.listView_3.currentIndex().data().toString()
        print text

    def showRecipe(self):
        fullFile = str(self.imagePath + self.listView_2.currentIndex().data(role = Qt.AccessibleTextRole).toString())
        fileType = self.listView_2.currentIndex().data(role = Qt.AccessibleDescriptionRole).toString()

        if fileType == 'grandmaImage':
            self.stackedWidget.setCurrentIndex(0)
            self.loadFile(fullFile)
        else:
            self.stackedWidget.setCurrentIndex(1)
            text = open(fullFile).read()
            #self.pageLabel_2.setPlainText(text)
            self.pageLabel_2.setHtml(text)

    def showDessertRecipe(self):
        fullFile = str(self.imagePath + self.listView_3.currentIndex().data(role = Qt.AccessibleTextRole).toString())
        fileType = self.listView_3.currentIndex().data(role = Qt.AccessibleDescriptionRole).toString()

        if fileType == 'grandmaImage':
            self.stackedWidget.setCurrentIndex(0)
            self.loadFile(fullFile)
        else:
            self.stackedWidget.setCurrentIndex(1)
            text = open(fullFile).read()
            self.pageLabel_2.setPlainText(text)

    def addRecipeForm(self):
        form = Create_Recipe.Main()
        form.show()

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def closeEvent(self, event):
        if self.okToContinue():
            settings = QSettings()
            filename = QVariant(QString(self.filename)) if self.filename is not None else QVariant()
            settings.setValue("LastFile", filename)
            recentFiles = QVariant(self.recentFiles) if self.recentFiles else QVariant()
            settings.setValue("RecentFiles", recentFiles)
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position", QVariant(self.pos()))
            settings.setValue("MainWindow/State", QVariant(self.saveState()))
        else:
            event.ignore()


    def okToContinue(self):
        if self.dirty:
            reply = QMessageBox.question(self,"Image Changer - Unsaved Changes", "Save unsaved changes?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                self.fileSave()
        return True


    def loadInitialFile(self):
        settings = QSettings()
        fname = "C:/Python27/rDialog/Family_Pictures/Edible_Turkey_Cropped.jpg" #unicode(settings.value("LastFile").toString())
        if fname and QFile.exists(fname):
            self.imageLabel.setScaledContents(False)
            self.loadFile(fname)

    def loadFile(self, fname=None):
        if fname is None:
            action = self.sender()
            if isinstance(action, QAction):
                fname = unicode(action.data().toString())
                if not self.okToContinue():
                    return
            else:
                return
        if fname:
            self.filename = None
            image = QImage(fname)
            if image.isNull():
                message = "Failed to read %s" % fname
            else:
                self.addRecentFile(fname)
                self.image = QImage()
                for action, check in self.resetableActions:
                    action.setChecked(check)
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False
                self.sizeLabel.setText("%d x %d" % (image.width(), image.height()))
                message = "Loaded %s" % os.path.basename(fname)
            self.updateStatus(message)

    def showImage(self, percent=None):
        if self.image.isNull():
            return
        if percent is None:
            percent = self.zoomSpinBox.value()
        factor = percent / 100.0
        width = self.image.width() * factor
        height = self.image.height() * factor
        image = self.image.scaled(width, height, Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))


    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        self.listWidget.addItem(message)
        if self.filename is not None:
            self.setWindowTitle("Recipe Viewer - %s[*]" %  os.path.basename(self.filename))
        elif not self.image.isNull():
            self.setWindowTitle("Recipe Viewer - Unnamed[*]")
        else:
            self.setWindowTitle("Recipe Viewer[*]")
        self.setWindowModified(self.dirty)

    def updateMenuFile(self):
        self.menuFile.clear()
        self.addActions(self.menuFile, self.menuFileActions[:-1])
        current = QString(self.filename) if self.filename is not None else None
        recentFiles = []
        for fname in self.recentFiles:
            if fname != current and QFile.exists(fname):
                recentFiles.append(fname)
        if recentFiles:
            self.menuFile.addSeparator()
            for i, fname in enumerate(recentFiles):
                action = QAction(QIcon(":/icon.png"), "&%d %s" % (i + 1, QFileInfo(fname).fileName()), self)
                action.setData(QVariant(fname))
                self.connect(action, SIGNAL("triggered()"),self.loadFile)
                self.menuFile.addAction(action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuFileActions[-1])


    def fileNew(self):
        if not self.okToContinue():
            return
        dialog = newimagedlg.NewImageDlg(self)
        if dialog.exec_():
            self.addRecentFile(self.filename)
            self.image = QImage()
            for action, check in self.resetableActions:
                action.setChecked(check)
            self.image = dialog.image()
            self.filename = None
            self.dirty = True
            self.showImage()
            self.sizeLabel.setText("%d x %d" % (self.image.width(),self.image.height()))
            self.updateStatus("Created new image")

    def fileNewDlg(self):
        dialog = addRecipeDialog.AddRecipeDlg()
        if dialog.exec_():
	        print("filename:")
	        print self.filename


            # self.addRecentFile(self.filename)
            # self.image = QImage()
            # for action, check in self.resetableActions:
            #     action.setChecked(check)
            # self.image = dialog.image()
            # self.filename = None
            # self.dirty = True
            # self.showImage()
            # self.sizeLabel.setText("%d x %d" % (self.image.width(),self.image.height()))
            # self.updateStatus("Created new image")

    def fileOpen(self):
        if not self.okToContinue():
            return
        dir = os.path.dirname(self.filename) if self.filename is not None else "."
        formats = ["*.%s" % unicode(format).lower() for format in QImageReader.supportedImageFormats()]
        fname = unicode(QFileDialog.getOpenFileName(self,"Image Changer - Choose Image", dir,"Image files (%s)" % " ".join(formats)))
        if fname:
            self.loadFile(fname)

    def addRecentFile(self, fname):
        if fname is None:
            return
        if not self.recentFiles.contains(fname):
            self.recentFiles.prepend(QString(fname))
            while self.recentFiles.count() > 9:
                self.recentFiles.takeLast()


    def fileSave(self):
        if self.image.isNull():
            return
        if self.filename is None:
            self.fileSaveAs()
        else:
            if self.image.save(self.filename, None):
                self.updateStatus("Saved as %s" % self.filename)
                self.dirty = False
            else:
                self.updateStatus("Failed to save %s" % self.filename)


    def fileSaveAs(self):
        if self.image.isNull():
            return
        fname = self.filename if self.filename is not None else "."
        formats = ["*.%s" % unicode(format).lower() for format in QImageWriter.supportedImageFormats()]
        fname = unicode(QFileDialog.getSaveFileName(self,"Image Changer - Save Image", fname,"Image files (%s)" % " ".join(formats)))
        if fname:
            if "." not in fname:
                fname += ".png"
            self.addRecentFile(fname)
            self.filename = fname
            self.fileSave()


    def filePrint(self):
        if self.image.isNull():
            return
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
            self.printer.setPageSize(QPrinter.Letter)
        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.drawImage(0, 0, self.image)


    def editInvert(self, on):
        if self.image.isNull():
            return
        self.image.invertPixels()
        self.showImage()
        self.dirty = True
        self.updateStatus("Inverted" if on else "Uninverted")

    def editSwapRedAndBlue(self, on):
        if self.image.isNull():
            return
        self.image = self.image.rgbSwapped()
        self.showImage()
        self.dirty = True
        self.updateStatus("Swapped Red and Blue"  if on else "Unswapped Red and Blue")

    def editUnMirror(self, on):
        if self.image.isNull():
            return
        if self.mirroredhorizontally:
            self.editMirrorHorizontal(False)
        if self.mirroredvertically:
            self.editMirrorVertical(False)

    def editMirrorHorizontal(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(True, False)
        self.showImage()
        self.mirroredhorizontally = not self.mirroredhorizontally
        self.dirty = True
        self.updateStatus("Mirrored Horizontally" if on else "Unmirrored Horizontally")

    def editMirrorVertical(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(False, True)
        self.showImage()
        self.mirroredvertically = not self.mirroredvertically
        self.dirty = True
        self.updateStatus("Mirrored Vertically"  if on else "Unmirrored Vertically")

    def editScale(self, on):
        if self.image.isNull():
            return
        self.image = self.image.scaled(False, True)
        self.showImage()
        self.scaled = not self.scaled
        self.dirty = True
        self.updateStatus("Scaled"  if on else "Not Scaled")

    def editZoom(self):
        if self.image.isNull():
            return
        percent, ok = QInputDialog.getInteger(self,"Image Changer - Zoom", "Percent:",self.zoomSpinBox.value(), 1, 400)
        if ok:
            self.zoomSpinBox.setValue(percent)

    def helpAbout(self):
        QMessageBox.about(self, "About Recipe Viewer",
                """<b>Recipe Viewer</b> v %s
                <p>Copyright &copy; 2007 Swaggy Ltd.
                All rights reserved.
                <p>This application can be used to help cook delicious food.
                <p>Python %s - Qt %s - PyQt %s on %s""" % (
                __version__, platform.python_version(),
                QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))


    def helpHelp(self):
        form = helpform.HelpForm("index.html", self)
        form.show()
    
    @pyqtSlot()    
    def resize_image(self):
        """Opens resize_dlg for resizing the image."""
        if self.image.isNull():
            return

        form = resizedlg.ResizeDlg(self.image.width(), self.image.height(), self)
        
        if form.exec_():
            width, height = form.result()
            if width != self.image.width() or height != self.image.height():
                self.image = self.image.scaled(width, height)
                self.dirty = True
                self.showImage()
                self.updateStatus("Resized to (%d,%d) size" % (width, height))
                self.sizeLabel.setText("%d x %d" % (width, height))

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Swaggy Money")
    app.setOrganizationDomain("Swaggy.com")
    app.setApplicationName("Recipe Viewer")
    app.setWindowIcon(QIcon(":/icon.png"))
    form = RecipeBook()
    form.show()
    app.exec_()


main()