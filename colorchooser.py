"""
program: colorchooser.py
author: Brandon

"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
	"""Displays the results of picking a color."""

	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title = "Color Chooser Demo")

		# Labels and output fields
		self.addLabel('R', row = 0,column = 0)
		self.addLabel('G', row = 1, column = 0)
		self.addLabel('B', row = 2, column = 0)
		self.addLabel("Color", row = 3, column = 0)
		self.r = self.addIntegerField(value = 0, row = 0, column = 1)
		self.g = self.addIntegerField(value = 0, row = 1, column = 1)
		self.b = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hex = self.addTextField(text = "#000000", row = 3, column = 1, width = 10)

		# Canvas withan initial black background
		self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")

		# Command button
		self.addButton(text = "Choose Color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)

	# event handling method
	def chooseColor(self):
		"""Pops up a color choose and outputs the results."""
		colorTuple = tkinter.colorchooser.askcolor()
		if not colorTuple[0]: return
		((r,g,b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString

def main():
	ColorPicker().mainloop()
main()
