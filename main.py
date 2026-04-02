import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from pyqt_ribbon import Large, Normal, RibbonBar, RibbonStyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times New Roman", 10))
    app.setStyle("Windows")

    window = QtWidgets.QMainWindow()
    ribbon = RibbonBar(maxRows=6)
    ribbon.setRibbonStyle(RibbonStyle.Default)
    window.setMenuBar(ribbon)
    window.setWindowTitle("Ribbon Test")
    window.setWindowIcon(QIcon("pyqt_ribbon/icons/python.png"))

    window.setCentralWidget(QtWidgets.QWidget(window))
    layout = QtWidgets.QVBoxLayout(window.centralWidget())

    saveButton = QtWidgets.QToolButton()
    saveButton.setAutoRaise(True)
    saveButton.setText("Button")
    saveButton.setIcon(QIcon("pyqt_ribbon/icons/save.png"))
    ribbon.addQuickAccessButton(saveButton)

    undoButton = QtWidgets.QToolButton()
    undoButton.setAutoRaise(True)
    undoButton.setText("Button")
    undoButton.setIcon(QIcon("pyqt_ribbon/icons/undo.png"))
    ribbon.addQuickAccessButton(undoButton)

    redoButton = QtWidgets.QToolButton()
    redoButton.setAutoRaise(True)
    redoButton.setText("Button")
    redoButton.setIcon(QIcon("pyqt_ribbon/icons/redo.png"))
    ribbon.addQuickAccessButton(redoButton)

    category1 = ribbon.addCategory("Category 1")
    panel = category1.addPanel("Panel 1", showPanelOptionButton=False)
    panel.addSmallButton("Button 1", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton("Button 2", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton("Button 3", icon=QIcon("pyqt_ribbon/icons/close.png"))
    showCategoryButton2 = panel.addMediumToggleButton("Show/Hide Category 2", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addVerticalSeparator()
    showCategoryButton3 = panel.addMediumToggleButton("Show/Hide Category 3", icon=QIcon("pyqt_ribbon/icons/close.png"))
    showCategoryButton45 = panel.addMediumToggleButton(
        "Show/Hide Category 4/5",
        icon=QIcon("pyqt_ribbon/icons/close.png"),
        colSpan=2,
        alignment=QtCore.Qt.AlignmentFlag.AlignLeft,
    )
    panel.addLargeButton("Button 6", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addVerticalSeparator()
    panel.addMediumButton("Button 7", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addMediumButton("Button 8", icon=QIcon("pyqt_ribbon/icons/close.png"))

    saveButton = panel.addLargeButton("Button 8", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

    saveButton = panel.addLargeButton("Button 9", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup)

    saveButton = panel.addLargeButton("Button 10", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)

    saveButton = panel.addLargeButton("Button 11", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = saveButton.addRibbonMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    submenu = menu.addMenu(QIcon("pyqt_ribbon/icons/close.png"), "Submenu")
    submenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 4")
    submenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 5")
    submenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 6")
    menu.addSpacing()
    menu.addLabel("This is a custom widget")
    formLayout = menu.addFormLayoutWidget()
    formLayout.addRow(QtWidgets.QLabel("Row 1"), QtWidgets.QLineEdit())
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
    panel.addWidget(saveButton, rowSpan=Large)  # noqa

    panel = category1.addPanel("Panel 2")
    button = panel.addMediumButton("Button 8", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    button.setMenu(menu)
    panel.addMediumButton("Button 9", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton(
        "This is a very very very very very long button", icon=QIcon("pyqt_ribbon/icons/close.png"), colSpan=3
    )
    button = panel.addSmallToggleButton("Button 10", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    button.setMenu(menu)
    panel.addSmallToggleButton("Button 11", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallToggleButton("Button 12", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton(
        "This is a very very very very very long button", icon=QIcon("pyqt_ribbon/icons/close.png"), colSpan=3
    )

    category2 = ribbon.addContextCategory("Context 2")
    panel = category2.addPanel("Panel 1")
    panel.addSmallButton("Button 1", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton("Button 2", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addSmallButton("Button 3", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addMediumButton("Button 4", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addMediumButton("Button 5", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addLargeButton("Button 6", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addVerticalSeparator()
    panel.addMediumButton("Button 7", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addMediumButton("Button 8", icon=QIcon("pyqt_ribbon/icons/close.png"))

    saveButton = panel.addLargeButton("Button 8", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
    panel.addWidget(saveButton, rowSpan=Large)  # noqa

    saveButton = panel.addLargeButton("Button 9", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup)
    panel.addWidget(saveButton, rowSpan=Large)  # noqa

    saveButton = panel.addLargeButton("Button 10", icon=QIcon("pyqt_ribbon/icons/close.png"))
    menu = QtWidgets.QMenu()
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    menu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 3")
    saveButton.setMenu(menu)
    saveButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
    panel.addWidget(saveButton, rowSpan=Large)  # noqa

    panel.addCalendarWidget()

    category3 = ribbon.addContextCategory("Context 3")
    panel = category3.addPanel("Panel 1")
    panel.addLargeButton("Button 1", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addLargeButton("Button 2", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel.addLargeButton("Button 3", icon=QIcon("pyqt_ribbon/icons/close.png"))

    showCategoryButton2.clicked.connect(category2.setCategoryVisible)
    showCategoryButton3.clicked.connect(lambda checked: category3.setCategoryVisible(not category3.categoryVisible()))

    gallery = panel.addGallery(popupHideOnClick=True)
    for i in range(100):
        gallery.addToggleButton(f"item {i+1}", QIcon("pyqt_ribbon/icons/close.png"))
    popupMenu = gallery.popupMenu()
    submenu = popupMenu.addMenu(QIcon("pyqt_ribbon/icons/close.png"), "Submenu")
    submenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 4")
    popupMenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 1")
    popupMenu.addAction(QIcon("pyqt_ribbon/icons/close.png"), "Action 2")
    popupMenu.addSeparator()
    popupMenu.addWidget(QtWidgets.QLabel("This is a custom widget"))  # noqa
    formLayout = popupMenu.addFormLayoutWidget()
    formLayout.addRow(QtWidgets.QLabel("Row 1"), QtWidgets.QLineEdit())

    categories = ribbon.addContextCategories("name", ["Context 4", "Context 5"])
    showCategoryButton45.clicked.connect(lambda v: categories.setCategoriesVisible(v))  # PySide2 Bug: use lambda

    panel1 = categories["Context 4"].addPanel("Context 4 Panel 1")
    panel1.addLargeButton("Button 1", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel1.addLargeButton("Button 2", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel1.addLargeButton("Button 3", icon=QIcon("pyqt_ribbon/icons/close.png"))

    panel2 = categories["Context 5"].addPanel("Context 5 Panel 1")
    panel2.addLargeButton("Button 4", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel2.addLargeButton("Button 5", icon=QIcon("pyqt_ribbon/icons/close.png"))
    panel2.addLargeButton("Button 6", icon=QIcon("pyqt_ribbon/icons/close.png"))

    categories1 = ribbon.addCategoriesBy(
        {
            "Category 6": {
                "style": Normal,
                "panels": {
                    "Panel 1": {
                        "showPanelOptionButton": True,
                        "widgets": {
                            "Button 1": {
                                "type": "Button",
                                "arguments": {
                                    "icon": QIcon("pyqt_ribbon/icons/close.png"),
                                    "text": "Button",
                                    "tooltip": "This is a tooltip",
                                },
                            },
                            "Button 2": {
                                "type": "Button",
                                "arguments": {
                                    "icon": QIcon("pyqt_ribbon/icons/close.png"),
                                    "text": "Button 2",
                                    "tooltip": "This is a tooltip",
                                },
                            },
                        },
                    },
                    "Panel 2": {
                        "showPanelOptionButton": True,
                        "widgets": {
                            "Button 3": {
                                "type": "Button",
                                "arguments": {
                                    "icon": QIcon("pyqt_ribbon/icons/close.png"),
                                    "text": "Button 3",
                                    "tooltip": "This is a tooltip",
                                },
                            },
                            "Button 4": {
                                "type": "Button",
                                "arguments": {
                                    "icon": QIcon("pyqt_ribbon/icons/close.png"),
                                    "text": "Button 4",
                                    "tooltip": "This is a tooltip",
                                },
                            },
                        },
                    },
                },
            }
        }
    )

    label = QtWidgets.QLabel("Ribbon Test Window")
    label.setFont(QtGui.QFont("Arial", 20))
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label, 1)

    window.resize(1200, 350)
    window.show()
    sys.exit(app.exec())
