import sys
import py2exe
from distutils.core import setup


setup(
    windows=[{"script":"Q:\\Quality Control\\shortcuts\\shortcuts.py"}],
    options={"py2exe":{"includes":["sip", "PyQt4.QtXml"]}},
)
