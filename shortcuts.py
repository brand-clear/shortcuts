#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PyQt4 import QtGui
from pyqtauto.setters import set_layout, set_uniform_margins
from pyqtauto.widgets import ComboBox, ImageButton, ExceptionMessageBox
from sulzer.extract import Extract as extract
from sulzer.defaults import Path


__author__ = 'Brandon McCleary'


#DEV_PATH = os.path.dirname(__file__)
PROD_PATH = os.path.dirname(os.path.dirname(sys.executable))
APP_PATH = PROD_PATH


def rev_engr_folder(job_num):
	"""Return the absolute path to a REVERSE_ENGINEERING subfolder.
	
	Parameters
	----------
	job_num : str

	"""
	folder = os.path.join(Path.REVERSE_ENGINEERING, job_num)
	if os.path.exists(folder):
		return folder


class Shortcuts(QtGui.QMainWindow):
	"""
	App controller.

	"""
	OPTION_CALLBACK_MAP = {
		'Issued Prints': extract.issued_prints_folder,
		'Projects Folder': extract.projects_folder,
		'Balance QC': extract.balance_qc_folder,
		'Assembly QC': extract.assembly_qc_folder,
		'Reverse Engineering': rev_engr_folder,
		'Pictures': extract.pictures_folder
	}

	def __init__(self):
		super(Shortcuts, self).__init__()
		self.setWindowTitle('Shortcuts')
		self.setFixedHeight(60)
		self.setFixedWidth(320)
		set_uniform_margins(self, 10)
		self.view = View(self.OPTION_CALLBACK_MAP.keys())
		self.view.search_btn.clicked.connect(self.on_click_search)
		self.view.job_num_le.returnPressed.connect(self.on_click_search)
		self.setCentralWidget(self.view)

	def on_click_search(self):
		"""Open the network folder that corresponds to user input."""
		folder = self.view.selection
		job_number = self.view.job_number
		try:
			os.startfile(self.OPTION_CALLBACK_MAP[folder](job_number))
		except:
			pass


class View(QtGui.QWidget):
	"""
	Represents app GUI.

	Parameters
	----------
	options : list[str]
		Items shown in ``ComboBox``.

	Attributes
	----------
	selection : str
	job_number : str
	job_number_le : QLineEdit
	search_btn : ImageButton

	"""
	def __init__(self, options):
		super(View, self).__init__()
		self._layout = set_layout(self, 'QHBoxLayout')
		self._options = ComboBox(options, self._layout)
		self.job_num_le = QtGui.QLineEdit()
		self._layout.addWidget(self.job_num_le)
		self.search_btn = ImageButton(
			os.path.join(APP_PATH, 'images', 'search.png'),
			self._layout,
			tooltip='Search',
			flat=True
		)

	@property
	def selection(self):
		"""str: The selected QComboBox option."""
		return str(self._options.currentText())
	
	@property
	def job_number(self):
		"""str: The QLineEdit input."""
		return str(self.job_num_le.text())


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon(
		os.path.join(APP_PATH, 'images', 'icon.png')
	))
	win = Shortcuts()
	win.show()
	app.exec_()

