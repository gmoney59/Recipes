__author__ = 'Swaggy-G$$$'

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Recipe(object):
	"""Class that holds the recipe object."""

	def __init__(self, recipeName, ingredients=None, instructions=None, category=None,
	             subCategory=None, chef=None, fileName=None, accessibilityDescription = 'newTextRecipe'):

		self.recipeName = recipeName
		self.ingredients = ingredients
		self.instructions = instructions
		self.category = category
		self.subCategory = subCategory
		self.chef = chef
		self.fileName = fileName
		self.accessibilityDescription = accessibilityDescription

	def createRecipeText(self):
		text = QTextEdit()
		text.append(self.recipeName)
		text.append('')
		text.append(self.ingredients)
		text.append('')
		text.append(self.instructions)
		text.append('')















		#print('Recipe Name: ' + self.recipeName)
#
# class RecipeList(object):
# 	pass
#
#
#
#
# def main():
# 	# Recipe Name, Chef, Ingredients, Category, Subcategory, fileName
# 	chickenChowMein = Recipe('Chicken Chow Mein', 'noodles, eggs, sauce, chicken', 'dinner', 'entree', 'Brian', 'chickenChowMein.jpg')
# 	bostonCreamPie = Recipe('Boston Cream Pie', category='Dessert')
#
# 	print('')
# 	print(chickenChowMein.recipeName)
# 	print(chickenChowMein.ingredients)
# 	print(chickenChowMein.category)
# 	print(chickenChowMein.subCategory)
# 	print(chickenChowMein.chef)
# 	print(chickenChowMein.fileName)
#
# 	print('')
# 	print(bostonCreamPie.recipeName)
# 	print(bostonCreamPie.category)
#
# main()