# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from PyQt6 import QtWidgets
from aqt.qt import Qt
# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
    # show a message box
    showInfo("Card count: %d" % cardCount)

def GetNotes() -> list:
    deck_id = mw.col.decks.id_for_name("日语补充::新标准日本语::新标准日本语高级")
    card_ids = mw.col.find_cards(f"deck:{deck_id}")
    
    notes = [mw.col.get_card(card_id).note() for card_id in card_ids]#
    return notes


# create a new menu item, "test"
#action = QAction("test", mw)
# set it to call testFunction when it's clicked
#qconnect(action.triggered, testFunction)
# and add it to the tools menu
#mw.form.menuTools.addAction(action) 

class DockWindows(QDockWidget):
    def __init__(self):
        mw.myWidget = self
        super(DockWindows, self).__init__()
        #去除背景
        self.setWindowFlag(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        #style
        self.resize(320,240)
        self.setWindowTitle('Test')
        self.setObjectName('DockWindows')

        #⚙️
        self.label = QLabel(self)
        self.label.setGeometry(120, 80, 6600, 66)

        deck_name = "日语补充::新标准日本语::新标准日本语高级"
        mw.myWidget.label.setText(str(deck_name))
        card_ids = mw.col.find_cards(f"deck:{deck_name}")
        
        notes = [mw.col.get_card(card_id).note() for card_id in card_ids]
        for note in notes:
            values=note.values()
            mw.myWidget.label.setText(str(values[1]))
        #self.label.setText("⚙️")#emoji用text
        self.show()

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, DockWindows)
# and add it to the tools menu
mw.form.menuTools.addAction(action)