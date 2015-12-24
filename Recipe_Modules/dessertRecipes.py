# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 14:13:43 2015

@author: Swaggy-G$$$
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import platform
from PyQt4.QtCore import (QAbstractTableModel, QDataStream, QFile,
        QIODevice, QModelIndex, QRegExp, QSize, QString, QVariant, Qt,
        SIGNAL)
from PyQt4.QtGui import (QApplication, QColor, QComboBox, QLineEdit,
        QSpinBox, QStyle, QStyledItemDelegate, QTextDocument, QTextEdit)
#import richtextlineedit


#NAME, OWNER, COUNTRY, DESCRIPTION, TEU = range(5)
TEXT, ACCESSIBLE_DESCRIPTION, ACCESSIBLE_TEXT = range(3)


MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1


class Recipe(object):

    def __init__(self, text, accessible_description, accessible_text):
        self.text = QString(text)
        self.accessible_description = QString(accessible_description)
        self.accessible_text = QString(accessible_text)


    def __hash__(self):
        return super(Recipe, self).__hash__()

    def __lt__(self, other):
        r = QString.localeAwareCompare(self.text.toLower(), other.text.toLower())
        return True if r < 0 else False


    def __eq__(self, other):
        return 0 == QString.localeAwareCompare(self.text.toLower(), other.text.toLower())


class RecipeContainer(object):

    def __init__(self, filename=QString()):
        self.filename = QString(filename)
        self.dirty = False
        self.recipes = {}
        self.accessible_descriptions = set()
        self.accessible_texts = set()


    def recipe(self, identity):
        return self.recipes.get(identity)


    def addRecipe(self, recipe):
        self.recipes[id(recipe)] = recipe
        self.accessible_descriptions.add(unicode(recipe.accessible_description))
        self.accessible_texts.add(unicode(recipe.accessible_text))
        self.dirty = True


    def removeRecipe(self, recipe):
        del self.recipes[id(recipe)]
        del recipe
        self.dirty = True


    def __len__(self):
        return len(self.recipes)


    def __iter__(self):
        for recipe in self.recipes.values():
            yield recipe


    def inOrder(self):
        return sorted(self.recipes.values())


    def inCountryOwnerOrder(self):
        return sorted(self.recipes.values(),
                      key=lambda x: (x.accessible_description, x.accessible_text, x.text))


    def load(self):
        exception = None
        fh = None
        try:
            if self.filename.isEmpty():
                raise IOError, "no filename specified for loading"
            fh = QFile(self.filename)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QDataStream(fh)
            magic = stream.readInt32()
            if magic != MAGIC_NUMBER:
                raise IOError, "unrecognized file type"
            fileVersion = stream.readInt16()
            if fileVersion != FILE_VERSION:
                raise IOError, "unrecognized file type version"
            self.recipes = {}
            while not stream.atEnd():
                text = QString()
                accessible_description = QString()
                accessible_text = QString()
                #description = QString()
                stream >> text >> accessible_description >> accessible_text # >> description
                #teu = stream.readInt32()
                recipe = Recipe(text, accessible_description, accessible_text) #, teu, description)
                self.recipes[id(recipe)] = recipe
                self.accessible_descriptions.add(unicode(accessible_description))
                self.accessible_texts.add(unicode(accessible_text))
            self.dirty = False
        except IOError, e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception


    def save(self):
        exception = None
        fh = None
        try:
            if self.filename.isEmpty():
                raise IOError, "no filename specified for saving"
            fh = QFile(self.filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError, unicode(fh.errorString())
            stream = QDataStream(fh)
            stream.writeInt32(MAGIC_NUMBER)
            stream.writeInt16(FILE_VERSION)
            stream.setVersion(QDataStream.Qt_4_1)
            for recipe in self.recipes.values():
                stream << recipe.text << recipe.accessible_description << recipe.accessible_text #\
                       #<< ship.description
                #stream.writeInt32(ship.teu)
            self.dirty = False
        except IOError, e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception

def generateFakeRecipes():
    for text, accessible_description, accessible_text in (
    ("Lees_Coffee_Cake", "grandmaImage", "Lees_Coffee_Cake.JPG"),
    ("My_Doughnut_Recipe", "grandmaImage", "My_Doughnut_Recipe.JPG"),
	("Apple_Kutchen", "grandmaImage", "Apple_Kutchen.JPG")):
        yield Recipe(text, accessible_description, accessible_text)

