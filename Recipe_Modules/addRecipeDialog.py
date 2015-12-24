import sys
from PyQt4.QtCore import (QDate, QString, Qt, SIGNAL, pyqtSignature)
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox, QTextDocument, QTextEdit)
#import moviedata
from Recipe_Modules import ui_addRecipeDlg
import recipes

class AddRecipeDlg(QDialog, ui_addRecipeDlg.Ui_addRecipeDialog):

    def __init__(self, recipe=None, parent = None):  #recipes=None, recipe=None, parent=None):
        super(AddRecipeDlg, self).__init__(parent)
        self.setupUi(self)

        self.recipe = recipe #needed?
        self.tiger = 'orange striped'

    def accept(self):
        recipe = self.textEdit.toPlainText()
        QDialog.accept(self)


        # Name = self.lineEdit.text()
        # ingredients = self.textEdit.toPlainText()
        # instructions = self.textEdit_2.toPlainText() #toHtml()
        # category = self.comboBox.currentText()
        # subCategory = self.comboBox_2.currentText()
        # chef = self.comboBox_3.currentText()
        # fileName = None
        # accessibleDescription = 'newTextRecipe'
        # accessibleText = self.lineEdit.text()
        #
        # self.recipe = createRecipe.Recipe(recipeName, ingredients, instructions, category,
        #                                   subCategory, chef, fileName, accessibleDescription) #, accessibleText)
        #
        # print('Recipe Name: ' + self.recipe.recipeName)
        # print('Ingredients: ' + self.recipe.ingredients)
        # print('Instructions: ' + self.recipe.instructions)
        # print('Chef: ' + self.recipe.chef)
        #
        # self.textEdit.append(self.recipe.recipeName)
        # self.textEdit.append('nigger juice')




#
#
#
# class TextDoc(QTextEdit):
#     def __init__(self, parent = None):
#         super(TextDoc, self).__init__(parent)
#         self.tiger = 'orange'
#
# class CreateDoc(QTextDocument):
#     """Or use QTextObject? What is format?"""
#     def __init__(self, parent = None):
#         super(CreateDoc, self).__init__(parent)
#         self.brianDoc = QTextDocument('This is a QTextDocument, nigger.')
#         self.brianDoc.setPlainText('is this the plain text you were looking for, bastard?')




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = AddRecipeDlg() #(0)
    form.show()
    app.exec_()



    #def accept(self):
        # self.getText()
        # print('This has been accepted.')
        # print('')
        #print(self.recipeName)
        #print(self.lineEdit.text())
        # print(self.ingredients)
        # print(self.instructions)
        # print(self.category)
        # print(self.subCategory)
        # print(self.chef)

        # text = QTextEdit()
        # text.setPlainText(self.recipeName)
        # text.setPlainText('')
        # text.setPlainText(self.category)
        # text.setPlainText(self.instructions)
        # text.show()
        #self.close()

# def Save(self):
#         filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
#         f = open(filename, 'w')
#         filedata = self.text.toPlainText()
#         f.write(filedata)
#         f.close()



    # def closeEvent(self, event):
    #    self.recipeName = self.lineEdit.text()
    #    print(self.recipeName)
    #    event.accept()

    #     self.movies = recipes
    #     self.movie = recipe
    #     #self.acquiredDateEdit.setDisplayFormat(recipedata.DATEFORMAT)
    #     if recipe is not None:
    #         #self.titleLineEdit.setText(recipe.title)
    #         self.LineEdit.setText(recipe.recipeName)
    #         #self.yearSpinBox.setValue(recipe.year)
    #         self.comboBox.setItemText(recipe.category)
    #         #self.minutesSpinBox.setValue(recipe.minutes)
    #         self.comboBox.setItemText(recipe.subCategory)
    #         #self.acquiredDateEdit.setDate(recipe.acquired)
    #         self.textEdit.setText(recipe.ingredients)
    #         #self.acquiredDateEdit.setEnabled(False)
    #         self.notesTextEdit.setPlainText(recipe.instructions)
    #         self.notesTextEdit.setFocus()
    #         self.buttonBox.button(QDialogButtonBox.Ok).setText(
    #                               "&Accept")
    #         self.setWindowTitle("My Movies - Edit Movie Penis")
    #     else:
    #         #today = QDate.currentDate()
    #         #self.acquiredDateEdit.setDateRange(today.addDays(-5), today)
    #         #self.acquiredDateEdit.setDate(today)
    #         self.lineEdit.setFocus()
    #     self.on_titleLineEdit_textEdited(QString())
    #
    #
    # @pyqtSignature("QString")
    # def on_titleLineEdit_textEdited(self, text):
    #     self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
    #             not self.lineEdit.text().isEmpty())
    #
    #
    # def accept(self):
    #     recipeName = self.lineEdit.text()
    #     category = self.comboBox.currentText()
    #     subCategory = self.comboBox.currentText()
    #     chef = self.comboBox.currentText()
    #     ingredients = self.textEdit.toPlainText()
    #     instructions = self.textEdit_2.toPlainText()
    #     if self.movie is None:
    #         #acquired = self.acquiredDateEdit.date()
    #         self.movie = self.moviedata.Movie(recipeName, ingredients, instructions, category, subCategory, chef)
    #         self.movies.add(self.movie)
    #     else:
    #         self.movies.updateMovie(self.movie, recipeName, chef, ingredients, instructions)
    #     QDialog.accept(self)

# def main():
#     app = QApplication(sys.argv)
#     form = AddRecipeDlg(0)
#     form.testPrint()
#     form.show()
#     app.exec_()

#main()




    #dialog = AddRecipeDlg()

