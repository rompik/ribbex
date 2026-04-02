import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

from pyqt_ribbon import RibbonBar
from pyqt_ribbon.screenshotwindow import RibbonScreenShotWindow
from pyqt_ribbon.utils import DataFile

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Times New Roman", 8))

    # Central widget
    window = RibbonScreenShotWindow("tutorial-ribbonbar.png")
    window.setWindowIcon(QIcon(DataFile("icons/python.png")))
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    layout = QVBoxLayout(centralWidget)

    # Ribbon bar
    ribbonbar = RibbonBar()
    window.setMenuBar(ribbonbar)
    category = ribbonbar.addCategory("Category 1")
    panel = category.addPanel("Panel 1")
    panel.addLargeButton("A Large Button", QIcon(DataFile("icons/python.png")))
    panel.addMediumButton("A Medium Button", QIcon(DataFile("icons/python.png")))
    panel.addMediumButton("A Medium Button", QIcon(DataFile("icons/python.png")))
    panel.addSmallButton("A Small Button", QIcon(DataFile("icons/python.png")))
    panel.addSmallButton("A Small Button", QIcon(DataFile("icons/python.png")))
    panel.addSmallButton("A Small Button", QIcon(DataFile("icons/python.png")))

    # Display a label in the main window
    label = QLabel("Ribbon Test Window")
    label.setFont(QFont("Arial", 20))
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # Add the ribbon bar and label to the layout
    layout.addWidget(label, 1)

    # Show the window
    window.resize(1800, 350)  # type: ignore
    window.show()
    sys.exit(app.exec())
