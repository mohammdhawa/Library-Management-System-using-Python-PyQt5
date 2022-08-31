# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1560, 900)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/* QDarkStyleSheet --------------------------------------------------------\n"
"This is the main style sheet, the palette has nine main colors.\n"
"It is based on three selecting colors, three greyish (background) colors\n"
"plus three whitish (foreground) colors. Each set of widgets of the same\n"
"type have a header like this:\n"
"    ------------------\n"
"    GroupName --------\n"
"    ------------------\n"
"And each widget is separated with a header like this:\n"
"    QWidgetName ------\n"
"This makes more easy to find and change some css field. The basic\n"
"configuration is described bellow.\n"
"    SELECTION ------------\n"
"        sel_light  #179AE0 #148CD2 (selection/hover/active)\n"
"        sel_normal #3375A3 #1464A0 (selected)\n"
"        sel_dark   #18465D #14506E (selected disabled)\n"
"    FOREGROUND -----------\n"
"        for_light  #EFF0F1 #F0F0F0 (texts/labels)\n"
"        for_dark   #505F69 #787878 (disabled texts)\n"
"    BACKGROUND -----------\n"
"        bac_light  #4D545B #505F69 (unpressed)\n"
"        bac_normal #31363B #32414B (border, disabled, pressed, checked, toolbars, menus)\n"
"        bac_dark   #232629 #19232D (background)\n"
"If a stranger configuration is required because of a bugfix or anything\n"
"else, keep the comment on that line to nobodys changed it, including the\n"
"issue number.\n"
"--------------------------------------------------------------------------- */\n"
"\n"
"\n"
"\n"
"/* QWidget ---------------------------------------------------------------- */\n"
"\n"
"QWidget {\n"
"    background-color: #19232D;\n"
"    border: 0px solid #32414B;\n"
"    padding: 0px;\n"
"    color: #F0F0F0;\n"
"    selection-background-color: #1464A0;\n"
"    selection-color: #F0F0F0;\n"
"}\n"
"\n"
"QWidget:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"    selection-background-color: #14506E;\n"
"    selection-color: #787878;\n"
"}\n"
"\n"
"QWidget:item:selected {\n"
"    background-color: #1464A0;\n"
"}\n"
"\n"
"QWidget:item:hover {\n"
"    background-color: #148CD2;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QMainWindow ------------------------------------------------------------ */\n"
"/* This adjusts the splitter in the dock widget, not qsplitter              */\n"
"\n"
"\n"
"QMainWindow::separator {\n"
"    background-color: #32414B;\n"
"    border: 0 solid #19232D;\n"
"    spacing: 0;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"    background-color: #505F69;\n"
"    border: 0px solid #148CD2;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"    width: 5px;\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    image: url(:/qss_icons/rc/Vsepartoolbar.png);\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"    height: 5px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"\n"
"/* QToolTip --------------------------------------------------------------- */\n"
"\n"
"QToolTip {\n"
"    background-color: #148CD2;\n"
"    border: 1px solid #19232D;\n"
"    color: #19232D;\n"
"    padding: 0;   /*remove padding, for fix combo box tooltip*/\n"
"    opacity: 230; /*reducing transparency to read better*/\n"
"}\n"
"\n"
"/* QStatusBar ------------------------------------------------------------- */\n"
"\n"
"QStatusBar {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QStatusBar QToolTip {\n"
"    background-color: #148CD2;\n"
"    border: 1px solid #19232D;\n"
"    color: #19232D;\n"
"    padding: 0;   /*remove padding, for fix combo box tooltip*/\n"
"    opacity: 230; /*reducing transparency to read better*/\n"
"}\n"
"\n"
"/* QCheckBox -------------------------------------------------------------- */\n"
"\n"
"QCheckBox {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    spacing: 4px;\n"
"    outline: none;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    margin-left: 4px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate {\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled {\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed {\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"/* QGroupBox -------------------------------------------------------------- */\n"
"\n"
"QGroupBox {\n"
"    font-weight: bold;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    margin-top: 16px;\n"
"}\n"
"\n"
"\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 3px;\n"
"    padding-left: 3px;\n"
"    padding-right: 5px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    margin-left: 4px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed {\n"
"    border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed {\n"
"    border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QGroupBox::indicator:checked:disabled {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"/* QRadioButton ----------------------------------------------------------- */\n"
"\n"
"QRadioButton {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    spacing: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QRadioButton:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QRadioButton QWidget {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    spacing: 0px;\n"
"    padding: 0px;\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: none;\n"
"    outline: none;\n"
"    margin-bottom: 2px;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicator:checked:pressed {\n"
"    border: none;\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"    outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"/* QMenuBar --------------------------------------------------------------- */\n"
"\n"
"QMenuBar {\n"
"    background-color: #32414B;\n"
"    padding: 2px;\n"
"    border: 1px solid #19232D;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QMenuBar:focus {\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    padding: 4px;\n"
"    background: transparent;\n"
"    border: 0px solid #32414B;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    padding: 4px;\n"
"    border: 0px solid #32414B;\n"
"    background-color: #148CD2;\n"
"    color: #F0F0F0;\n"
"    margin-bottom: 0px;\n"
"    padding-bottom: 0px;\n"
"}\n"
"\n"
"/* QMenu ------------------------------------------------------------------ */\n"
"\n"
"QMenu {\n"
"    border: 0px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background-color: #505F69;\n"
"    color: #F0F0F0;\n"
"    padding-left: 4px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"    margin: 0px;\n"
"    padding-left:4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 4px 24px 4px 24px;\n"
"    border: 1px transparent #32414B;  /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"\n"
"\n"
"QMenu::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    padding-left:6px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"/* QAbstractItemView ------------------------------------------------------ */\n"
"\n"
"QAbstractItemView {\n"
"    alternate-background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QAbstractItemView QLineEdit {\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* QAbstractScrollArea ---------------------------------------------------- */\n"
"\n"
"QAbstractScrollArea {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractScrollArea:disabled {\n"
"    color: #787878;\n"
"}\n"
"\n"
"/* QScrollArea ------------------------------------------------------------ */\n"
"\n"
"QScrollArea QWidget QWidget:disabled {\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"/* QScrollBar ------------------------------------------------------------- */\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 16px;\n"
"    margin: 2px 16px 2px 16px;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #787878;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    min-width: 8px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #148CD2;\n"
"    border: 1px solid #148CD2;\n"
"    border-radius: 4px;\n"
"    min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    margin: 0px 0px 0px 0px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::add-line:horizontal:on {\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:on {\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #19232D;\n"
"    width: 16px;\n"
"    margin: 16px 2px 16px 2px;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #787878;\n"
"    border: 1px solid #32414B;\n"
"    min-height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #148CD2;\n"
"    border: 1px solid #148CD2;\n"
"    border-radius: 4px;\n"
"    min-height: 8px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:on {\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::add-line:vertical:on {\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* QTextEdit--------------------------------------------------------------- */\n"
"\n"
"QTextEdit {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit --------------------------------------------------------- */\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------- */\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* QStackedWidget --------------------------------------------------------- */\n"
"\n"
"QStackedWidget {\n"
"    padding: 4px;\n"
"    border: 1px solid #32414B;\n"
"    border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar --------------------------------------------------------------- */\n"
"\n"
"QToolBar {\n"
"    background-color: #32414B;\n"
"    border-bottom: 1px solid #19232D;\n"
"    padding: 2px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar QToolButton{\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    width: 6px;\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"    height: 6px;\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"    width: 3px;\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"    height: 3px;\n"
"    image: url(:/qss_icons/rc/Vsepartoolbar.png);\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button {\n"
"    background: #32414B;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    image: url(:/qss_icons/rc/right_arrow.png);\n"
"}\n"
"\n"
"/* QAbstractSpinBox ------------------------------------------------------- */\n"
"\n"
"QAbstractSpinBox {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    padding-top: 2px;     /* This fix  103, 111*/\n"
"    padding-bottom: 2px;  /* This fix  103, 111*/\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    border-radius: 4px;\n"
"    /* min-width: 5px; removed to fix 109 */\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button {\n"
"    background-color: transparent #19232D;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    border-left: 1px solid #32414B;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow:hover {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button {\n"
"    background-color: transparent #19232D;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    border-left: 1px solid #32414B;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow,\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off {\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QAbstractSpinBox::down-arrow:hover {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox:hover{\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractSpinBox:selected {\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* DISPLAYS --------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"\n"
"/* QLabel ----------------------------------------------------------------- */\n"
"\n"
"QLabel {\n"
"    background-color: #19232D;\n"
"    border: 0px solid #32414B;\n"
"    padding: 2px;\n"
"    margin: 0px;\n"
"    color: #F0F0F0\n"
"}\n"
"\n"
"QLabel::disabled {\n"
"    background-color: #19232D;\n"
"    border: 0px solid #32414B;\n"
"    color: #787878;\n"
"}\n"
"\n"
"/* QTextBrowser ----------------------------------------------------------- */\n"
"\n"
"QTextBrowser {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextBrowser:hover,\n"
"QTextBrowser:!hover,\n"
"QTextBrowser::selected,\n"
"QTextBrowser::pressed {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QGraphicsView --------------------------------------------------------- */\n"
"\n"
"QGraphicsView {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QGraphicsView:hover,\n"
"QGraphicsView:!hover,\n"
"QGraphicsView::selected,\n"
"QGraphicsView::pressed {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCalendarWidget -------------------------------------------------------- */\n"
"\n"
"QCalendarWidget {\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"/* QLCDNumber ------------------------------------------------------------- */\n"
"\n"
"QLCDNumber {\n"
"    background-color: #19232D;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QLCDNumber:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"/* QProgressBar ----------------------------------------------------------- */\n"
"\n"
"QProgressBar {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #1464A0;\n"
"    color: #19232D;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #14506E;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* BUTTONS ---------------------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"\n"
"/* QPushButton ------------------------------------------------------------ */\n"
"\n"
"QPushButton {\n"
"    background-color: #505F69 ;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    bottom: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #19232D;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QPushButton:selected,\n"
"QPushButton:checked:selected{\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QToolButton ------------------------------------------------------------ */\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    margin: 0px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #19232D;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton:checked:hover{\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"\n"
"QToolButton[popupMode=\"1\"] {\n"
"    padding: 2px;\n"
"    padding-right: 12px;     /* only for MenuButtonPopup */\n"
"    border: 1px solid #32414B;   /* make way for the popup button */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"\n"
"QToolButton[popupMode=\"2\"] {\n"
"    padding: 2px;\n"
"    padding-right: 12px;      /* only for InstantPopup */\n"
"    border: 1px solid #32414B;    /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    padding: 2px;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover,\n"
"QToolButton::menu-button:checked:hover {\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -8px;     /* shift it a bit */\n"
"    left: -4px;    /* shift it a bit */\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"/* QCommandLinkButton ----------------------------------------------------- */\n"
"\n"
"QCommandLinkButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QCommandLinkButton:disabled {\n"
"    background-color: transparent;\n"
"    color: #787878;\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------ */\n"
"/* INPUTS - NO FIELDS ----------------------------------------------------- */\n"
"/* ------------------------------------------------------------------------ */\n"
"\n"
"/* QCombobox -------------------------------------------------------------- */\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    selection-background-color: #1464A0;\n"
"    padding-top: 2px;     /* This fix  #103, #111*/\n"
"    padding-bottom: 2px;  /* This fix  #103, #111*/\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    /* min-width: 75px;  removed to fix 109 */\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    selection-background-color: #19232D;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #19232D;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"    selection-color: #148CD2;\n"
"    selection-background-color: #32414B;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: #32414B;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"/* QSlider ---------------------------------------------------------------- */\n"
"\n"
"QSlider:disabled {\n"
"    background: #19232D;\n"
"}\n"
"\n"
"QSlider:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #1464A0;\n"
"    border: 1px solid #32414B;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #787878;\n"
"    border: 1px solid #32414B;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    margin: -8px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #148CD2;\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: #32414B;\n"
"    border: 1px solid #32414B;\n"
"    width: 4px;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #1464A0;\n"
"    border: 1px solid #32414B;\n"
"    width: 4px;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical:disabled {\n"
"    background: #14506E;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #787878;\n"
"    border: 1px solid #32414B;\n"
"    width: 8px;\n"
"    height: 8px;\n"
"    margin: 0 -8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background: #148CD2;\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"/* QLine ------------------------------------------------------------------ */\n"
"\n"
"QLineEdit {\n"
"    background-color: #19232D;\n"
"    padding-top: 2px;     /* This QLineEdit fix  103, 111 */\n"
"    padding-bottom: 2px;  /* This QLineEdit fix  103, 111 */\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    border-style: solid;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:selected{\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"/* QTabWiget -------------------------------------------------------------- */\n"
"\n"
"QTabWidget {\n"
"    padding: 2px;\n"
"    selection-background-color: #32414B;\n"
"}\n"
"\n"
"QTabWidget QFrame{\n"
"    border: 0;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"    background-color: #32414B;\n"
"    border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QTabBar ---------------------------------------------------------------- */\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    border-radius: 4px;\n"
"    margin: 0px;\n"
"    padding: 2px;\n"
"    border: 0;\n"
"\n"
"    /* left: 5px; move to the right by 5px - removed for fix */\n"
"    }\n"
"\n"
"QTabBar::close-button {\n"
"    border: 0;\n"
"    margin: 2px;\n"
"    padding: 0;\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ----------------------------------------------- */\n"
"\n"
"QTabBar::tab:top:selected:disabled {\n"
"    border-bottom: 3px solid #14506E;\n"
"    color: #787878;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled {\n"
"    border-top: 3px solid #14506E;\n"
"    color: #787878;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled {\n"
"    border-left: 3px solid #14506E;\n"
"    color: #787878;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled {\n"
"    border-right: 3px solid #14506E;\n"
"    color: #787878;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"/* QTabBar::tab - !selected and disabled ---------------------------------- */\n"
"\n"
"QTabBar::tab:top:!selected:disabled {\n"
"    border-bottom: 3px solid #19232D;\n"
"    color: #787878;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled {\n"
"    border-top: 3px solid #19232D;\n"
"    color: #787878;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled {\n"
"    border-right: 3px solid #19232D;\n"
"    color: #787878;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled {\n"
"    border-left: 3px solid #19232D;\n"
"    color: #787878;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ----------------------------------------------- */\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    border-bottom: 2px solid #19232D;\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    border-top: 2px solid #19232D;\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    border-left: 2px solid #19232D;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    border-right: 2px solid #19232D;\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top {\n"
"    background-color: #32414B;\n"
"    color: #F0F0F0;\n"
"    margin-left: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    min-width: 5px;\n"
"    border-bottom: 3px solid #32414B;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    background-color: #505F69;\n"
"    color: #F0F0F0;\n"
"    border-bottom: 3px solid #1464A0;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    border: 1px solid #148CD2;\n"
"    border-bottom: 3px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar::tab:bottom {\n"
"    color: #F0F0F0;\n"
"    border-top: 3px solid #32414B;\n"
"    background-color: #32414B;\n"
"    margin-left: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    color: #F0F0F0;\n"
"    background-color: #505F69;\n"
"    border-top: 3px solid #1464A0;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    border: 1px solid #148CD2;\n"
"    border-top: 3px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar::tab:left {\n"
"    color: #F0F0F0;\n"
"    background-color: #32414B;\n"
"    margin-top: 2px;\n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    color: #F0F0F0;\n"
"    background-color: #505F69;\n"
"    border-left: 3px solid #1464A0;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    border: 1px solid #148CD2;\n"
"    border-left: 3px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"    color: #F0F0F0;\n"
"    background-color: #32414B;\n"
"    margin-top: 2px;\n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    color: #F0F0F0;\n"
"    background-color: #505F69;\n"
"    border-right: 3px solid #1464A0;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    border: 1px solid #148CD2;\n"
"    border-right: 3px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"    image: url(:/qss_icons/rc/right_arrow.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"    image: url(:/qss_icons/rc/left_arrow.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"    image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"    image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"}\n"
"\n"
"\n"
"/*  Some examples from internet to check\n"
"QTabBar::tabButton() and QTabBar::tabIcon()\n"
"QTabBar::tear {width: 0px; border: none;}\n"
"QTabBar::tear {image: url(tear_indicator.png);}\n"
"QTabBar::scroller{width:85pix;}\n"
"QTabBar QToolbutton{background-color:\"light blue\";}\n"
"But that left the buttons transparant.\n"
"Looked confusing as the tab buttons migrated behind the scroller buttons.\n"
"So we had to color the back ground of the scroller buttons\n"
"*/\n"
"\n"
"/* QDockWiget ------------------------------------------------------------- */\n"
"\n"
"QDockWidget {\n"
"    outline: 1px solid #32414B;\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    padding: 6px;   /* better size for title bar */\n"
"    border: none;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"    background-color: #32414B;\n"
"    border-radius: 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"    background-color: #32414B;\n"
"    border-radius: 4px;\n"
"    border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"\n"
"/* QTreeView QTableView QListView ----------------------------------------- */\n"
"\n"
"QTreeView:branch:selected,\n"
"QTreeView:branch:hover {\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"}\n"
"\n"
"QListView::item:!selected:hover,\n"
"QTreeView::item:!selected:hover,\n"
"QTableView::item:!selected:hover,\n"
"QColumnView::item:!selected:hover {\n"
"    outline: 0;\n"
"    color: #148CD2;\n"
"    background-color: #32414B;\n"
"}\n"
"\n"
"QListView::item:selected:hover,\n"
"QTreeView::item:selected:hover,\n"
"QTableView::item:selected:hover,\n"
"QColumnView::item:selected:hover {\n"
"    background: #1464A0;\n"
"    color:  #19232D;\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover,\n"
"QTreeView::indicator:checked:focus,\n"
"QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListView::indicator:checked:pressed {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover,\n"
"QTreeView::indicator:unchecked:focus,\n"
"QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover,\n"
"QTreeView::indicator:indeterminate:focus,\n"
"QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QListView,\n"
"QTreeView,\n"
"QTableView,\n"
"QColumnView {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    gridline-color: #32414B;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListView:disabled,\n"
"QTreeView:disabled,\n"
"QTableView:disabled,\n"
"QColumnView:disabled {\n"
"    background-color: #19232D;\n"
"    color: #787878;\n"
"}\n"
"\n"
"QListView:selected,\n"
"QTreeView:selected,\n"
"QTableView:selected,\n"
"QColumnView:selected {\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"\n"
"QListView:hover,\n"
"QTreeView::hover,\n"
"QTableView::hover,\n"
"QColumnView::hover {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QListView::item:pressed,\n"
"QTreeView::item:pressed,\n"
"QTableView::item:pressed,\n"
"QColumnView::item:pressed {\n"
"    background-color: #1464A0;\n"
"}\n"
"\n"
"QListView::item:selected:active,\n"
"QTreeView::item:selected:active,\n"
"QTableView::item:selected:active,\n"
"QColumnView::item:selected:active {\n"
"    background-color: #1464A0;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #19232D;\n"
"    border: 1px transparent #32414B;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* QHeaderView ------------------------------------------------------------ */\n"
"\n"
"QHeaderView {\n"
"    background-color: #32414B;\n"
"    border: 0px transparent #32414B;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QHeaderView:disabled {\n"
"    background-color: #32414B;\n"
"    border: 1px transparent #32414B;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #32414B;\n"
"    color: #F0F0F0;\n"
"    padding: 2px;\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    color: #F0F0F0;\n"
"    background-color: #1464A0;\n"
"}\n"
"\n"
"QHeaderView::section:checked:disabled {\n"
"    color: #787878;\n"
"    background-color: #14506E;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:disabled,\n"
"QHeaderView::section::vertical:disabled {\n"
"    color: #787878;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one {\n"
"    border-top: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"    border-top: 1px solid #19232D;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one {\n"
"    border-left: 1px solid #32414B;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"    border-left: 1px solid #19232D;\n"
"}\n"
"\n"
"/* Those settings (border/width/height/background-color) solve bug */\n"
"/* transparent arrow background and size */\n"
"\n"
"QHeaderView::down-arrow {\n"
"    background-color: #32414B;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-right: 1px solid #19232D;\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    background-color: #32414B;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border-right: 1px solid #19232D;\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"/* QToolBox -------------------------------------------------------------- */\n"
"\n"
"QToolBox {\n"
"    padding: 0px;\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::selected {\n"
"    padding: 0px;\n"
"    border: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background-color: #19232D;\n"
"    border: 1px solid #32414B;\n"
"    color: #F0F0F0;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:disabled {\n"
"    color: #787878;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background-color: #505F69;\n"
"    border-bottom: 2px solid #1464A0;\n"
"}\n"
"\n"
"QToolBox::tab:!selected {\n"
"    background-color: #32414B;\n"
"    border-bottom: 2px solid #32414B;\n"
"}\n"
"\n"
"QToolBox::tab:selected:disabled {\n"
"    background-color: #32414B;\n"
"    border-bottom: 2px solid #14506E;\n"
"}\n"
"\n"
"QToolBox::tab:!selected:disabled {\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    border-color: #148CD2;\n"
"    border-bottom: 2px solid #148CD2;\n"
"}\n"
"\n"
"QToolBox QScrollArea QWidget QWidget {\n"
"    padding: 0px;\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"/* QFrame ----------------------------------------------------------------- */\n"
"\n"
"QFrame {\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"] {\n"
"    border-radius: 4px;\n"
"    border: 1px transparent #32414B;\n"
"}\n"
"\n"
"QFrame[height=\"3\"],\n"
"QFrame[width=\"3\"] {\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"/* QSplitter -------------------------------------------------------------- */\n"
"\n"
"QSplitter {\n"
"    background-color: #32414B;\n"
"    spacing: 0;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QSplitter::separator {\n"
"    background-color: #32414B;\n"
"    border: 0 solid #19232D;\n"
"    spacing: 0;\n"
"    padding: 1px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QSplitter::separator:hover {\n"
"    background-color: #787878;\n"
"}\n"
"\n"
"QSplitter::separator:horizontal {\n"
"    width: 5px;\n"
"    image: url(:/qss_icons/rc/Vsepartoolbar.png);\n"
"}\n"
"\n"
"QSplitter::separator:vertical {\n"
"    height: 5px;\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"\n"
"\n"
"/* QDateEdit-------------------------------------------------------------- */\n"
"\n"
"QDateEdit {\n"
"    selection-background-color: #1464A0;\n"
"    border-style: solid;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding-top: 2px;     /* This fix  #103, #111*/\n"
"    padding-bottom: 2px;  /* This fix  #103, #111*/\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:on {\n"
"    selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on,\n"
"QDateEdit::down-arrow:hover,\n"
"QDateEdit::down-arrow:focus {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: #19232D;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"    selection-background-color: #1464A0;\n"
"}\n"
"\n"
"QAbstractView:hover{\n"
"    border: 1px solid #148CD2;\n"
"    color: #F0F0F0;\n"
"}\n"
"\n"
"QAbstractView:selected {\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"      alignment: center;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 0, 1271, 801))
        self.tabWidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.label_106 = QtWidgets.QLabel(self.tab_19)
        self.label_106.setGeometry(QtCore.QRect(310, 210, 121, 41))
        self.label_106.setObjectName("label_106")
        self.pushButton_66 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_66.setGeometry(QtCore.QRect(430, 400, 211, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_66.setIcon(icon)
        self.pushButton_66.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_66.setObjectName("pushButton_66")
        self.label_107 = QtWidgets.QLabel(self.tab_19)
        self.label_107.setGeometry(QtCore.QRect(310, 150, 111, 41))
        self.label_107.setObjectName("label_107")
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_19)
        self.groupBox_24.setEnabled(False)
        self.groupBox_24.setGeometry(QtCore.QRect(180, 280, 761, 81))
        self.groupBox_24.setTitle("")
        self.groupBox_24.setObjectName("groupBox_24")
        self.label_108 = QtWidgets.QLabel(self.groupBox_24)
        self.label_108.setGeometry(QtCore.QRect(30, 27, 531, 41))
        self.label_108.setObjectName("label_108")
        self.pushButton_68 = QtWidgets.QPushButton(self.groupBox_24)
        self.pushButton_68.setGeometry(QtCore.QRect(570, 27, 171, 41))
        self.pushButton_68.setObjectName("pushButton_68")
        self.lineEdit_87 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_87.setGeometry(QtCore.QRect(430, 210, 351, 41))
        self.lineEdit_87.setStyleSheet("border-width: 2px;")
        self.lineEdit_87.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.lineEdit_88 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_88.setGeometry(QtCore.QRect(430, 150, 351, 41))
        self.lineEdit_88.setStyleSheet("border-width: 2px;")
        self.lineEdit_88.setObjectName("lineEdit_88")
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_41.setGeometry(QtCore.QRect(740, 216, 41, 31))
        self.pushButton_41.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"border-color: rgb(25, 35, 45);")
        self.pushButton_41.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_41.setIcon(icon1)
        self.pushButton_41.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_42.setGeometry(QtCore.QRect(740, 216, 41, 31))
        self.pushButton_42.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"border-color: rgb(25, 35, 45);")
        self.pushButton_42.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/no_eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_42.setIcon(icon2)
        self.pushButton_42.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_42.setObjectName("pushButton_42")
        self.tabWidget.addTab(self.tab_19, "")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.lineEdit_92 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_92.setGeometry(QtCore.QRect(420, 150, 351, 41))
        self.lineEdit_92.setStyleSheet("border-width: 2px;")
        self.lineEdit_92.setObjectName("lineEdit_92")
        self.groupBox_26 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_26.setGeometry(QtCore.QRect(180, 220, 761, 81))
        self.groupBox_26.setTitle("")
        self.groupBox_26.setObjectName("groupBox_26")
        self.label_113 = QtWidgets.QLabel(self.groupBox_26)
        self.label_113.setGeometry(QtCore.QRect(30, 27, 531, 41))
        self.label_113.setObjectName("label_113")
        self.pushButton_80 = QtWidgets.QPushButton(self.groupBox_26)
        self.pushButton_80.setGeometry(QtCore.QRect(570, 27, 171, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_80.setIcon(icon3)
        self.pushButton_80.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_80.setObjectName("pushButton_80")
        self.label_114 = QtWidgets.QLabel(self.tab_26)
        self.label_114.setGeometry(QtCore.QRect(300, 150, 111, 41))
        self.label_114.setObjectName("label_114")
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_22.setEnabled(False)
        self.groupBox_22.setGeometry(QtCore.QRect(300, 410, 541, 171))
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")
        self.pushButton_79 = QtWidgets.QPushButton(self.groupBox_22)
        self.pushButton_79.setGeometry(QtCore.QRect(150, 110, 231, 41))
        self.pushButton_79.setStyleSheet("border-width: 2px;")
        self.pushButton_79.setObjectName("pushButton_79")
        self.label_112 = QtWidgets.QLabel(self.groupBox_22)
        self.label_112.setGeometry(QtCore.QRect(10, 35, 161, 41))
        self.label_112.setObjectName("label_112")
        self.lineEdit_91 = QtWidgets.QLineEdit(self.groupBox_22)
        self.lineEdit_91.setGeometry(QtCore.QRect(170, 35, 351, 41))
        self.lineEdit_91.setStyleSheet("border-width: 2px;")
        self.lineEdit_91.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_91.setObjectName("lineEdit_91")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.tab_26)
        self.lineEdit_77.setGeometry(QtCore.QRect(500, 340, 141, 41))
        self.lineEdit_77.setStyleSheet("border-width: 2px;")
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.label_97 = QtWidgets.QLabel(self.tab_26)
        self.label_97.setGeometry(QtCore.QRect(300, 340, 191, 41))
        self.label_97.setObjectName("label_97")
        self.pushButton_81 = QtWidgets.QPushButton(self.tab_26)
        self.pushButton_81.setGeometry(QtCore.QRect(660, 340, 181, 41))
        self.pushButton_81.setObjectName("pushButton_81")
        self.tabWidget.addTab(self.tab_26, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_52.setGeometry(QtCore.QRect(60, 80, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setStyleSheet("border-width: 2px;")
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.label_44.setObjectName("label_44")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_37.setGeometry(QtCore.QRect(60, 20, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setStyleSheet("border-width: 2px;")
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab)
        self.pushButton_31.setGeometry(QtCore.QRect(830, 56, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("border-width: 2px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_31.setIcon(icon4)
        self.pushButton_31.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_31.setObjectName("pushButton_31")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab)
        self.comboBox_13.setGeometry(QtCore.QRect(410, 80, 151, 41))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_5.setGeometry(QtCore.QRect(640, 20, 161, 41))
        self.dateEdit_5.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid whilte;\n"
"background-color : black;\n"
"padding : 5px;\n"
"}\n"
"QDateEdit::up-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"\n"
"}\n"
"QDateEdit::down-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"}")
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_6.setGeometry(QtCore.QRect(30, 140, 1201, 521))
        self.tableWidget_6.setStyleSheet("border-width: 2px;")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(5)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1271, 761))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 1201, 511))
        self.tableWidget.setStyleSheet("border-width: 2px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.comboBox = QtWidgets.QComboBox(self.tab_8)
        self.comboBox.setGeometry(QtCore.QRect(240, 40, 271, 41))
        self.comboBox.setStyleSheet("border-width: 2px;")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.tab_8)
        self.label.setGeometry(QtCore.QRect(100, 40, 131, 41))
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 40, 281, 41))
        self.pushButton_8.setStyleSheet("border-width: 2px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_37.setEnabled(False)
        self.pushButton_37.setGeometry(QtCore.QRect(1013, 660, 221, 41))
        self.pushButton_37.setStyleSheet("border-width: 2px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_37.setIcon(icon6)
        self.pushButton_37.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_37.setObjectName("pushButton_37")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 641, 51))
        self.lineEdit.setStyleSheet("border-width: 2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit.setGeometry(QtCore.QRect(50, 120, 641, 411))
        self.textEdit.setStyleSheet("border-width: 2px;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_2.setGeometry(QtCore.QRect(890, 100, 261, 51))
        self.lineEdit_2.setStyleSheet("border-width: 2px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab_10)
        self.label_2.setGeometry(QtCore.QRect(780, 100, 91, 51))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_2.setGeometry(QtCore.QRect(890, 180, 261, 51))
        self.comboBox_2.setStyleSheet("border-width: 2px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_3.setGeometry(QtCore.QRect(890, 260, 261, 51))
        self.comboBox_3.setStyleSheet("border-width: 2px;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_10)
        self.comboBox_4.setGeometry(QtCore.QRect(890, 340, 261, 51))
        self.comboBox_4.setStyleSheet("border-width: 2px;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_10)
        self.lineEdit_3.setGeometry(QtCore.QRect(890, 420, 261, 51))
        self.lineEdit_3.setStyleSheet("border-width: 2px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_10)
        self.label_3.setGeometry(QtCore.QRect(780, 180, 101, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_10)
        self.label_4.setGeometry(QtCore.QRect(780, 260, 101, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_10)
        self.label_5.setGeometry(QtCore.QRect(780, 340, 101, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_10)
        self.label_6.setGeometry(QtCore.QRect(780, 420, 101, 51))
        self.label_6.setObjectName("label_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setGeometry(QtCore.QRect(440, 560, 281, 41))
        self.pushButton_9.setStyleSheet("border-width: 2px;")
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_7 = QtWidgets.QLabel(self.tab_9)
        self.label_7.setGeometry(QtCore.QRect(230, 20, 81, 41))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 20, 231, 41))
        self.lineEdit_4.setStyleSheet("border-width: 2px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_10.setGeometry(QtCore.QRect(590, 20, 281, 41))
        self.pushButton_10.setStyleSheet("border-width: 2px;")
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 90, 641, 51))
        self.lineEdit_5.setStyleSheet("border-width: 2px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 160, 641, 451))
        self.textEdit_2.setStyleSheet("border-width: 2px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_6.setGeometry(QtCore.QRect(900, 120, 261, 51))
        self.lineEdit_6.setStyleSheet("border-width: 2px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.tab_9)
        self.label_8.setGeometry(QtCore.QRect(790, 120, 91, 51))
        self.label_8.setObjectName("label_8")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_5.setGeometry(QtCore.QRect(900, 200, 261, 51))
        self.comboBox_5.setStyleSheet("border-width: 2px;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_6.setGeometry(QtCore.QRect(900, 280, 261, 51))
        self.comboBox_6.setStyleSheet("border-width: 2px;")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_7.setGeometry(QtCore.QRect(900, 360, 261, 51))
        self.comboBox_7.setStyleSheet("border-width: 2px;")
        self.comboBox_7.setObjectName("comboBox_7")
        self.label_9 = QtWidgets.QLabel(self.tab_9)
        self.label_9.setGeometry(QtCore.QRect(790, 200, 101, 51))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_9)
        self.label_10.setGeometry(QtCore.QRect(790, 280, 101, 51))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_9)
        self.label_11.setGeometry(QtCore.QRect(790, 360, 101, 51))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_9)
        self.label_12.setGeometry(QtCore.QRect(790, 440, 101, 51))
        self.label_12.setObjectName("label_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_7.setGeometry(QtCore.QRect(900, 440, 261, 51))
        self.lineEdit_7.setStyleSheet("border-width: 2px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_11.setEnabled(False)
        self.pushButton_11.setGeometry(QtCore.QRect(760, 540, 221, 51))
        self.pushButton_11.setStyleSheet("border-width: 2px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_12.setEnabled(False)
        self.pushButton_12.setGeometry(QtCore.QRect(1000, 540, 231, 51))
        self.pushButton_12.setStyleSheet("border-width: 2px;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 1271, 761))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_11)
        self.comboBox_8.setGeometry(QtCore.QRect(450, 20, 271, 51))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_13.setGeometry(QtCore.QRect(770, 20, 281, 51))
        self.pushButton_13.setStyleSheet("border-width: 2px;")
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_11)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 100, 1161, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 20, 351, 51))
        self.lineEdit_8.setStyleSheet("border-width: 2px;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_38 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_38.setEnabled(False)
        self.pushButton_38.setGeometry(QtCore.QRect(988, 660, 221, 41))
        self.pushButton_38.setStyleSheet("border-width: 2px;")
        self.pushButton_38.setIcon(icon6)
        self.pushButton_38.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_38.setObjectName("pushButton_38")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.label_13 = QtWidgets.QLabel(self.tab_12)
        self.label_13.setGeometry(QtCore.QRect(290, 70, 191, 51))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_12)
        self.label_14.setGeometry(QtCore.QRect(290, 150, 191, 51))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_12)
        self.label_15.setGeometry(QtCore.QRect(290, 230, 191, 51))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_12)
        self.label_16.setGeometry(QtCore.QRect(290, 310, 191, 51))
        self.label_16.setObjectName("label_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_9.setGeometry(QtCore.QRect(490, 70, 371, 51))
        self.lineEdit_9.setStyleSheet("border-width: 2px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_10.setGeometry(QtCore.QRect(490, 150, 371, 51))
        self.lineEdit_10.setStyleSheet("border-width: 2px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_11.setGeometry(QtCore.QRect(490, 230, 371, 51))
        self.lineEdit_11.setStyleSheet("border-width: 2px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_12.setGeometry(QtCore.QRect(490, 310, 371, 51))
        self.lineEdit_12.setStyleSheet("border-width: 2px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 490, 361, 51))
        self.pushButton_14.setStyleSheet("border-width: 2px;")
        self.pushButton_14.setIcon(icon4)
        self.pushButton_14.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_32 = QtWidgets.QLabel(self.tab_12)
        self.label_32.setGeometry(QtCore.QRect(290, 390, 191, 51))
        self.label_32.setObjectName("label_32")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_25.setGeometry(QtCore.QRect(490, 390, 371, 51))
        self.lineEdit_25.setStyleSheet("border-width: 2px;")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 30, 351, 51))
        self.lineEdit_13.setStyleSheet("border-width: 2px;")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_13)
        self.comboBox_9.setGeometry(QtCore.QRect(500, 30, 271, 51))
        self.comboBox_9.setStyleSheet("border-width: 2px;")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_15.setGeometry(QtCore.QRect(800, 30, 281, 51))
        self.pushButton_15.setStyleSheet("border-width: 2px;")
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_14.setGeometry(QtCore.QRect(510, 110, 371, 51))
        self.lineEdit_14.setStyleSheet("border-width: 2px;")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_15.setGeometry(QtCore.QRect(510, 190, 371, 51))
        self.lineEdit_15.setStyleSheet("border-width: 2px;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_16.setGeometry(QtCore.QRect(510, 270, 371, 51))
        self.lineEdit_16.setStyleSheet("border-width: 2px;")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_17.setGeometry(QtCore.QRect(510, 350, 371, 51))
        self.lineEdit_17.setStyleSheet("border-width: 2px;")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_17 = QtWidgets.QLabel(self.tab_13)
        self.label_17.setGeometry(QtCore.QRect(310, 110, 191, 51))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_13)
        self.label_18.setGeometry(QtCore.QRect(310, 190, 191, 51))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_13)
        self.label_19.setGeometry(QtCore.QRect(310, 270, 191, 51))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_13)
        self.label_20.setGeometry(QtCore.QRect(310, 350, 191, 51))
        self.label_20.setObjectName("label_20")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_16.setEnabled(False)
        self.pushButton_16.setGeometry(QtCore.QRect(310, 510, 271, 51))
        self.pushButton_16.setStyleSheet("border-width: 2px;")
        self.pushButton_16.setIcon(icon7)
        self.pushButton_16.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_17.setEnabled(False)
        self.pushButton_17.setGeometry(QtCore.QRect(600, 510, 261, 51))
        self.pushButton_17.setStyleSheet("border-width: 2px;")
        self.pushButton_17.setIcon(icon8)
        self.pushButton_17.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_13)
        self.lineEdit_24.setGeometry(QtCore.QRect(510, 430, 371, 51))
        self.lineEdit_24.setStyleSheet("border-width: 2px;")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_31 = QtWidgets.QLabel(self.tab_13)
        self.label_31.setGeometry(QtCore.QRect(310, 430, 191, 51))
        self.label_31.setObjectName("label_31")
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_5.setGeometry(QtCore.QRect(50, 105, 1151, 551))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(4)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_12.setGeometry(QtCore.QRect(480, 40, 171, 41))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_35 = QtWidgets.QLabel(self.tab_4)
        self.label_35.setGeometry(QtCore.QRect(660, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_4)
        self.label_36.setGeometry(QtCore.QRect(400, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_43 = QtWidgets.QLabel(self.tab_4)
        self.label_43.setGeometry(QtCore.QRect(60, 42, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.pushButton_30 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_30.setGeometry(QtCore.QRect(990, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("border-width: 2px;")
        self.pushButton_30.setIcon(icon5)
        self.pushButton_30.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_30.setObjectName("pushButton_30")
        self.comboBox_16 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_16.setGeometry(QtCore.QRect(170, 42, 221, 41))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_15.setGeometry(QtCore.QRect(760, 40, 181, 41))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 1271, 731))
        self.tabWidget_4.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid whilte;\n"
"background-color : black;\n"
"padding : 5px;\n"
"}\n"
"QDateEdit::up-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"\n"
"}\n"
"QDateEdit::down-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"}")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_14)
        self.dateEdit.setGeometry(QtCore.QRect(144, 20, 161, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.label_21 = QtWidgets.QLabel(self.tab_14)
        self.label_21.setGeometry(QtCore.QRect(70, 20, 71, 41))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_14)
        self.label_22.setGeometry(QtCore.QRect(328, 20, 51, 41))
        self.label_22.setObjectName("label_22")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_14)
        self.dateEdit_2.setGeometry(QtCore.QRect(378, 20, 161, 41))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_18.setGeometry(QtCore.QRect(588, 20, 281, 41))
        self.pushButton_18.setStyleSheet("border-width: 2px;")
        self.pushButton_18.setIcon(icon5)
        self.pushButton_18.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_14)
        self.tableWidget_3.setGeometry(QtCore.QRect(40, 80, 1181, 541))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tabWidget_4.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.label_23 = QtWidgets.QLabel(self.tab_15)
        self.label_23.setGeometry(QtCore.QRect(60, 10, 71, 41))
        self.label_23.setObjectName("label_23")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.tab_15)
        self.dateEdit_3.setGeometry(QtCore.QRect(130, 10, 161, 41))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.label_24 = QtWidgets.QLabel(self.tab_15)
        self.label_24.setGeometry(QtCore.QRect(326, 10, 51, 41))
        self.label_24.setObjectName("label_24")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.tab_15)
        self.dateEdit_4.setGeometry(QtCore.QRect(376, 10, 161, 41))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_19.setGeometry(QtCore.QRect(596, 10, 281, 41))
        self.pushButton_19.setStyleSheet("border-width: 2px;")
        self.pushButton_19.setIcon(icon5)
        self.pushButton_19.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_15)
        self.tableWidget_4.setGeometry(QtCore.QRect(30, 70, 1201, 541))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.label_45 = QtWidgets.QLabel(self.tab_24)
        self.label_45.setGeometry(QtCore.QRect(80, 10, 71, 41))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tab_24)
        self.label_46.setGeometry(QtCore.QRect(320, 10, 61, 41))
        self.label_46.setObjectName("label_46")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_39.setGeometry(QtCore.QRect(570, 10, 281, 41))
        self.pushButton_39.setStyleSheet("border-width: 2px;")
        self.pushButton_39.setIcon(icon5)
        self.pushButton_39.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_39.setObjectName("pushButton_39")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_24)
        self.dateEdit_6.setGeometry(QtCore.QRect(150, 10, 151, 41))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.tableWidget_12 = QtWidgets.QTableWidget(self.tab_24)
        self.tableWidget_12.setGeometry(QtCore.QRect(45, 70, 1171, 541))
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setColumnCount(4)
        self.tableWidget_12.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_12.setHorizontalHeaderItem(3, item)
        self.dateEdit_7 = QtWidgets.QDateEdit(self.tab_24)
        self.dateEdit_7.setGeometry(QtCore.QRect(380, 10, 151, 41))
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.tabWidget_4.addTab(self.tab_24, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_25)
        self.pushButton_40.setGeometry(QtCore.QRect(638, 10, 281, 41))
        self.pushButton_40.setStyleSheet("border-width: 2px;")
        self.pushButton_40.setIcon(icon5)
        self.pushButton_40.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_40.setObjectName("pushButton_40")
        self.tableWidget_13 = QtWidgets.QTableWidget(self.tab_25)
        self.tableWidget_13.setGeometry(QtCore.QRect(40, 70, 1181, 541))
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setColumnCount(4)
        self.tableWidget_13.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_13.setHorizontalHeaderItem(3, item)
        self.label_47 = QtWidgets.QLabel(self.tab_25)
        self.label_47.setGeometry(QtCore.QRect(348, 10, 61, 41))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.tab_25)
        self.label_48.setGeometry(QtCore.QRect(70, 10, 71, 41))
        self.label_48.setObjectName("label_48")
        self.dateEdit_8 = QtWidgets.QDateEdit(self.tab_25)
        self.dateEdit_8.setGeometry(QtCore.QRect(140, 10, 171, 41))
        self.dateEdit_8.setObjectName("dateEdit_8")
        self.dateEdit_9 = QtWidgets.QDateEdit(self.tab_25)
        self.dateEdit_9.setGeometry(QtCore.QRect(408, 10, 171, 41))
        self.dateEdit_9.setObjectName("dateEdit_9")
        self.tabWidget_4.addTab(self.tab_25, "")
        self.tabWidget.addTab(self.tab_5, "")
        self.Addvsd0jvs = QtWidgets.QWidget()
        self.Addvsd0jvs.setObjectName("Addvsd0jvs")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.Addvsd0jvs)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 1271, 661))
        self.tabWidget_5.setStyleSheet("QCheckBox::indicator:checked {\n"
"    image: url(:/icons/true.png);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"background-color: white;\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"background-color : green;\n"
"}")
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 1131, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(30, 50, 161, 41))
        self.label_33.setObjectName("label_33")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_26.setGeometry(QtCore.QRect(190, 50, 291, 41))
        self.lineEdit_26.setStyleSheet("border-width: 2px;")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_25.setEnabled(False)
        self.pushButton_25.setGeometry(QtCore.QRect(830, 50, 281, 41))
        self.pushButton_25.setStyleSheet("border-width: 2px;")
        self.pushButton_25.setIcon(icon4)
        self.pushButton_25.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_25.setObjectName("pushButton_25")
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_10.setGeometry(QtCore.QRect(510, 50, 281, 41))
        self.comboBox_10.setStyleSheet("border-width: 2px;")
        self.comboBox_10.setObjectName("comboBox_10")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 160, 1131, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setGeometry(QtCore.QRect(340, 50, 471, 41))
        self.lineEdit_27.setStyleSheet("border-width: 2px;")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_26.setEnabled(False)
        self.pushButton_26.setGeometry(QtCore.QRect(830, 50, 281, 41))
        self.pushButton_26.setStyleSheet("border-width: 2px;")
        self.pushButton_26.setIcon(icon4)
        self.pushButton_26.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_26.setObjectName("pushButton_26")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_29.setGeometry(QtCore.QRect(20, 50, 301, 41))
        self.lineEdit_29.setStyleSheet("border-width: 2px;")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 310, 1131, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_28.setGeometry(QtCore.QRect(340, 50, 471, 41))
        self.lineEdit_28.setStyleSheet("border-width: 2px;")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_27.setEnabled(False)
        self.pushButton_27.setGeometry(QtCore.QRect(830, 50, 281, 41))
        self.pushButton_27.setStyleSheet("border-width: 2px;")
        self.pushButton_27.setIcon(icon4)
        self.pushButton_27.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_27.setObjectName("pushButton_27")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_36.setGeometry(QtCore.QRect(20, 50, 301, 41))
        self.lineEdit_36.setStyleSheet("border-width: 2px;")
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.tabWidget_5.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.groupBox = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox.setGeometry(QtCore.QRect(45, 30, 571, 561))
        self.groupBox.setObjectName("groupBox")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(30, 60, 181, 41))
        self.label_25.setObjectName("label_25")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setGeometry(QtCore.QRect(270, 60, 271, 41))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_19.setGeometry(QtCore.QRect(270, 120, 271, 41))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_20.setGeometry(QtCore.QRect(270, 180, 271, 41))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_21.setGeometry(QtCore.QRect(270, 240, 271, 41))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_22.setGeometry(QtCore.QRect(270, 300, 271, 41))
        self.lineEdit_22.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(30, 240, 171, 41))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(30, 300, 241, 41))
        self.label_29.setObjectName("label_29")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_23.setGeometry(QtCore.QRect(270, 360, 271, 41))
        self.lineEdit_23.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setGeometry(QtCore.QRect(30, 360, 241, 41))
        self.label_30.setObjectName("label_30")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.setGeometry(QtCore.QRect(130, 450, 281, 51))
        self.pushButton_22.setStyleSheet("border-width: 2px;")
        self.pushButton_22.setIcon(icon4)
        self.pushButton_22.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_22.setObjectName("pushButton_22")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(645, 30, 571, 561))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(30, 50, 181, 41))
        self.label_37.setObjectName("label_37")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_30.setGeometry(QtCore.QRect(270, 50, 271, 41))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_34.setGeometry(QtCore.QRect(270, 110, 271, 41))
        self.lineEdit_34.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setGeometry(QtCore.QRect(30, 110, 241, 41))
        self.label_41.setObjectName("label_41")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_20.setGeometry(QtCore.QRect(270, 163, 81, 28))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_21.setGeometry(QtCore.QRect(360, 164, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_21.setObjectName("pushButton_21")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 200, 541, 351))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(20, 140, 171, 41))
        self.label_40.setObjectName("label_40")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_35.setGeometry(QtCore.QRect(260, 200, 271, 41))
        self.lineEdit_35.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_32.setGeometry(QtCore.QRect(260, 80, 271, 41))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(20, 80, 171, 41))
        self.label_39.setObjectName("label_39")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_33.setGeometry(QtCore.QRect(260, 140, 271, 41))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_31.setGeometry(QtCore.QRect(260, 20, 271, 41))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(20, 200, 241, 41))
        self.label_42.setObjectName("label_42")
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_24.setGeometry(QtCore.QRect(280, 270, 251, 51))
        self.pushButton_24.setStyleSheet("border-width: 2px;")
        self.pushButton_24.setIcon(icon8)
        self.pushButton_24.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_23.setGeometry(QtCore.QRect(20, 270, 241, 51))
        self.pushButton_23.setStyleSheet("border-width: 2px;")
        self.pushButton_23.setIcon(icon7)
        self.pushButton_23.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_23.setObjectName("pushButton_23")
        self.tabWidget_5.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.label_34 = QtWidgets.QLabel(self.tab_18)
        self.label_34.setGeometry(QtCore.QRect(170, 30, 161, 51))
        self.label_34.setObjectName("label_34")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_18)
        self.comboBox_11.setGeometry(QtCore.QRect(330, 30, 281, 51))
        self.comboBox_11.setStyleSheet("border-width: 2px;")
        self.comboBox_11.setObjectName("comboBox_11")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_28.setGeometry(QtCore.QRect(680, 30, 281, 51))
        self.pushButton_28.setStyleSheet("border-width: 2px;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_7.setGeometry(QtCore.QRect(80, 124, 251, 361))
        self.groupBox_7.setObjectName("groupBox_7")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 161, 51))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 161, 51))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 140, 161, 51))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 190, 161, 51))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 240, 161, 51))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 290, 161, 51))
        self.checkBox_6.setObjectName("checkBox_6")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_8.setGeometry(QtCore.QRect(640, 124, 251, 361))
        self.groupBox_8.setObjectName("groupBox_8")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 60, 161, 51))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 130, 161, 51))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_9.setGeometry(QtCore.QRect(30, 200, 161, 51))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 270, 161, 51))
        self.checkBox_10.setObjectName("checkBox_10")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_9.setGeometry(QtCore.QRect(920, 124, 251, 361))
        self.groupBox_9.setObjectName("groupBox_9")
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_11.setGeometry(QtCore.QRect(30, 60, 161, 51))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_12.setGeometry(QtCore.QRect(30, 130, 161, 51))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_13.setGeometry(QtCore.QRect(30, 200, 161, 51))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_14.setGeometry(QtCore.QRect(30, 270, 161, 51))
        self.checkBox_14.setObjectName("checkBox_14")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_18)
        self.groupBox_10.setGeometry(QtCore.QRect(360, 124, 251, 361))
        self.groupBox_10.setObjectName("groupBox_10")
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_15.setGeometry(QtCore.QRect(30, 40, 161, 51))
        self.checkBox_15.setStyleSheet("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_16.setGeometry(QtCore.QRect(30, 90, 161, 51))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_17.setGeometry(QtCore.QRect(30, 140, 161, 51))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_18.setGeometry(QtCore.QRect(30, 190, 161, 51))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_19.setGeometry(QtCore.QRect(30, 240, 161, 51))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBox_10)
        self.checkBox_20.setGeometry(QtCore.QRect(30, 290, 181, 51))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.tab_18)
        self.checkBox_21.setGeometry(QtCore.QRect(290, 530, 261, 51))
        self.checkBox_21.setObjectName("checkBox_21")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_29.setEnabled(False)
        self.pushButton_29.setGeometry(QtCore.QRect(550, 530, 281, 51))
        self.pushButton_29.setStyleSheet("border-width: 2px;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.tabWidget_5.addTab(self.tab_18, "")
        self.tabWidget.addTab(self.Addvsd0jvs, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 1271, 761))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_7.setGeometry(QtCore.QRect(20, 30, 1221, 511))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(8)
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_7.setHorizontalHeaderItem(7, item)
        self.pushButton_36 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_36.setGeometry(QtCore.QRect(960, 650, 281, 51))
        self.pushButton_36.setStyleSheet("border-width: 2px;")
        self.pushButton_36.setIcon(icon6)
        self.pushButton_36.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_36.setObjectName("pushButton_36")
        self.tabWidget_6.addTab(self.tab_6, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.tab_21)
        self.tableWidget_8.setGeometry(QtCore.QRect(30, 30, 1201, 511))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        self.pushButton_35 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_35.setGeometry(QtCore.QRect(950, 650, 281, 51))
        self.pushButton_35.setStyleSheet("border-width: 2px;")
        self.pushButton_35.setIcon(icon6)
        self.pushButton_35.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_35.setObjectName("pushButton_35")
        self.tabWidget_6.addTab(self.tab_21, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_22)
        self.tableWidget_9.setGeometry(QtCore.QRect(40, 30, 1181, 511))
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(5)
        self.tableWidget_9.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_22)
        self.pushButton_34.setGeometry(QtCore.QRect(941, 650, 281, 51))
        self.pushButton_34.setStyleSheet("border-width: 2px;")
        self.pushButton_34.setIcon(icon6)
        self.pushButton_34.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_34.setObjectName("pushButton_34")
        self.tabWidget_6.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.tableWidget_10 = QtWidgets.QTableWidget(self.tab_23)
        self.tableWidget_10.setGeometry(QtCore.QRect(63, 30, 1131, 511))
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(2)
        self.tableWidget_10.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_23)
        self.pushButton_33.setGeometry(QtCore.QRect(914, 650, 281, 51))
        self.pushButton_33.setStyleSheet("border-width: 2px;")
        self.pushButton_33.setIcon(icon6)
        self.pushButton_33.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_33.setObjectName("pushButton_33")
        self.tabWidget_6.addTab(self.tab_23, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.tableWidget_11 = QtWidgets.QTableWidget(self.tab_20)
        self.tableWidget_11.setGeometry(QtCore.QRect(62, 30, 1131, 511))
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setColumnCount(2)
        self.tableWidget_11.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        self.pushButton_32 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_32.setGeometry(QtCore.QRect(913, 650, 281, 51))
        self.pushButton_32.setStyleSheet("border-width: 2px;")
        self.pushButton_32.setIcon(icon6)
        self.pushButton_32.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_32.setObjectName("pushButton_32")
        self.tabWidget_6.addTab(self.tab_20, "")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_27 = QtWidgets.QWidget()
        self.tab_27.setObjectName("tab_27")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tab_27)
        self.tabWidget_7.setGeometry(QtCore.QRect(0, 0, 1271, 761))
        self.tabWidget_7.setStyleSheet("QCheckBox::indicator:checked {\n"
"    image: url(:/icons/true.png);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"background-color: white;\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"background-color : green;\n"
"}")
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_28 = QtWidgets.QWidget()
        self.tab_28.setObjectName("tab_28")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.tab_28)
        self.lineEdit_38.setGeometry(QtCore.QRect(420, 50, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setStyleSheet("border-width: 2px;")
        self.lineEdit_38.setPlaceholderText("")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_28)
        self.pushButton_44.setGeometry(QtCore.QRect(430, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("border-width: 2px;")
        self.pushButton_44.setIcon(icon4)
        self.pushButton_44.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_44.setObjectName("pushButton_44")
        self.label_49 = QtWidgets.QLabel(self.tab_28)
        self.label_49.setGeometry(QtCore.QRect(100, 50, 301, 41))
        self.label_49.setObjectName("label_49")
        self.checkBox_22 = QtWidgets.QCheckBox(self.tab_28)
        self.checkBox_22.setGeometry(QtCore.QRect(430, 150, 231, 41))
        self.checkBox_22.setObjectName("checkBox_22")
        self.comboBox_21 = QtWidgets.QComboBox(self.tab_28)
        self.comboBox_21.setGeometry(QtCore.QRect(750, 50, 271, 41))
        self.comboBox_21.setStyleSheet("border-width: 2px;")
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.tabWidget_7.addTab(self.tab_28, "")
        self.tab_29 = QtWidgets.QWidget()
        self.tab_29.setObjectName("tab_29")
        self.dateEdit_10 = QtWidgets.QDateEdit(self.tab_29)
        self.dateEdit_10.setGeometry(QtCore.QRect(510, 30, 161, 41))
        self.dateEdit_10.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid whilte;\n"
"background-color : black;\n"
"padding : 5px;\n"
"}\n"
"QDateEdit::up-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"\n"
"}\n"
"QDateEdit::down-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"}")
        self.dateEdit_10.setObjectName("dateEdit_10")
        self.label_51 = QtWidgets.QLabel(self.tab_29)
        self.label_51.setGeometry(QtCore.QRect(458, 30, 51, 41))
        self.label_51.setObjectName("label_51")
        self.dateEdit_11 = QtWidgets.QDateEdit(self.tab_29)
        self.dateEdit_11.setGeometry(QtCore.QRect(276, 30, 161, 41))
        self.dateEdit_11.setStyleSheet("QDateEdit\n"
"{\n"
"border : 2px solid whilte;\n"
"background-color : black;\n"
"padding : 5px;\n"
"}\n"
"QDateEdit::up-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"\n"
"}\n"
"QDateEdit::down-arrow\n"
"{\n"
"border : 2px solid white;\n"
"background-color : #89CFF0;\n"
"}")
        self.dateEdit_11.setObjectName("dateEdit_11")
        self.label_52 = QtWidgets.QLabel(self.tab_29)
        self.label_52.setGeometry(QtCore.QRect(202, 30, 71, 41))
        self.label_52.setObjectName("label_52")
        self.pushButton_45 = QtWidgets.QPushButton(self.tab_29)
        self.pushButton_45.setGeometry(QtCore.QRect(720, 30, 281, 41))
        self.pushButton_45.setStyleSheet("border-width: 2px;")
        self.pushButton_45.setIcon(icon5)
        self.pushButton_45.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_45.setObjectName("pushButton_45")
        self.tableWidget_14 = QtWidgets.QTableWidget(self.tab_29)
        self.tableWidget_14.setGeometry(QtCore.QRect(20, 110, 1201, 571))
        self.tableWidget_14.setObjectName("tableWidget_14")
        self.tableWidget_14.setColumnCount(6)
        self.tableWidget_14.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_14.setHorizontalHeaderItem(5, item)
        self.tabWidget_7.addTab(self.tab_29, "")
        self.tabWidget.addTab(self.tab_27, "")
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.tabWidget_8 = QtWidgets.QTabWidget(self.tab_30)
        self.tabWidget_8.setGeometry(QtCore.QRect(-10, 0, 1271, 761))
        self.tabWidget_8.setObjectName("tabWidget_8")
        self.tab_31 = QtWidgets.QWidget()
        self.tab_31.setObjectName("tab_31")
        self.tableWidget_15 = QtWidgets.QTableWidget(self.tab_31)
        self.tableWidget_15.setGeometry(QtCore.QRect(30, 110, 1201, 511))
        self.tableWidget_15.setObjectName("tableWidget_15")
        self.tableWidget_15.setColumnCount(6)
        self.tableWidget_15.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_15.setHorizontalHeaderItem(5, item)
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_31)
        self.comboBox_14.setGeometry(QtCore.QRect(240, 40, 301, 41))
        self.comboBox_14.setStyleSheet("border-width: 2px;")
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_53 = QtWidgets.QLabel(self.tab_31)
        self.label_53.setGeometry(QtCore.QRect(100, 40, 131, 41))
        self.label_53.setObjectName("label_53")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_31)
        self.pushButton_47.setGeometry(QtCore.QRect(600, 40, 281, 41))
        self.pushButton_47.setStyleSheet("border-width: 2px;")
        self.pushButton_47.setIcon(icon5)
        self.pushButton_47.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_31)
        self.pushButton_48.setEnabled(True)
        self.pushButton_48.setGeometry(QtCore.QRect(1013, 660, 221, 41))
        self.pushButton_48.setStyleSheet("border-width: 2px;")
        self.pushButton_48.setIcon(icon6)
        self.pushButton_48.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_48.setObjectName("pushButton_48")
        self.tabWidget_8.addTab(self.tab_31, "")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.tab_32)
        self.lineEdit_40.setGeometry(QtCore.QRect(50, 50, 641, 51))
        self.lineEdit_40.setStyleSheet("border-width: 2px;")
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_32)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 120, 641, 411))
        self.textEdit_3.setStyleSheet("border-width: 2px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.tab_32)
        self.lineEdit_41.setGeometry(QtCore.QRect(910, 100, 271, 51))
        self.lineEdit_41.setStyleSheet("border-width: 2px;")
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_54 = QtWidgets.QLabel(self.tab_32)
        self.label_54.setGeometry(QtCore.QRect(760, 100, 91, 51))
        self.label_54.setObjectName("label_54")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.tab_32)
        self.lineEdit_42.setGeometry(QtCore.QRect(910, 420, 271, 51))
        self.lineEdit_42.setStyleSheet("border-width: 2px;")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_58 = QtWidgets.QLabel(self.tab_32)
        self.label_58.setGeometry(QtCore.QRect(760, 420, 101, 51))
        self.label_58.setObjectName("label_58")
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_32)
        self.pushButton_49.setEnabled(True)
        self.pushButton_49.setGeometry(QtCore.QRect(470, 570, 281, 41))
        self.pushButton_49.setStyleSheet("border-width: 2px;")
        self.pushButton_49.setIcon(icon4)
        self.pushButton_49.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_49.setObjectName("pushButton_49")
        self.label_55 = QtWidgets.QLabel(self.tab_32)
        self.label_55.setGeometry(QtCore.QRect(760, 180, 131, 51))
        self.label_55.setObjectName("label_55")
        self.comboBox_17 = QtWidgets.QComboBox(self.tab_32)
        self.comboBox_17.setGeometry(QtCore.QRect(910, 180, 271, 51))
        self.comboBox_17.setStyleSheet("border-width: 2px;")
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.label_56 = QtWidgets.QLabel(self.tab_32)
        self.label_56.setGeometry(QtCore.QRect(760, 260, 91, 51))
        self.label_56.setObjectName("label_56")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_32)
        self.lineEdit_47.setGeometry(QtCore.QRect(910, 260, 271, 51))
        self.lineEdit_47.setStyleSheet("border-width: 2px;")
        self.lineEdit_47.setText("")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.label_57 = QtWidgets.QLabel(self.tab_32)
        self.label_57.setGeometry(QtCore.QRect(760, 340, 131, 51))
        self.label_57.setObjectName("label_57")
        self.comboBox_18 = QtWidgets.QComboBox(self.tab_32)
        self.comboBox_18.setGeometry(QtCore.QRect(910, 340, 271, 51))
        self.comboBox_18.setStyleSheet("border-width: 2px;")
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.tabWidget_8.addTab(self.tab_32, "")
        self.tab_33 = QtWidgets.QWidget()
        self.tab_33.setObjectName("tab_33")
        self.label_59 = QtWidgets.QLabel(self.tab_33)
        self.label_59.setGeometry(QtCore.QRect(230, 20, 81, 41))
        self.label_59.setObjectName("label_59")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_43.setGeometry(QtCore.QRect(320, 20, 231, 41))
        self.lineEdit_43.setStyleSheet("border-width: 2px;")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.pushButton_50 = QtWidgets.QPushButton(self.tab_33)
        self.pushButton_50.setGeometry(QtCore.QRect(590, 20, 281, 41))
        self.pushButton_50.setStyleSheet("border-width: 2px;")
        self.pushButton_50.setIcon(icon5)
        self.pushButton_50.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_50.setObjectName("pushButton_50")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_44.setGeometry(QtCore.QRect(30, 90, 641, 51))
        self.lineEdit_44.setStyleSheet("border-width: 2px;")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_33)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 160, 641, 451))
        self.textEdit_4.setStyleSheet("border-width: 2px;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_51 = QtWidgets.QPushButton(self.tab_33)
        self.pushButton_51.setEnabled(True)
        self.pushButton_51.setGeometry(QtCore.QRect(760, 540, 221, 51))
        self.pushButton_51.setStyleSheet("border-width: 2px;")
        self.pushButton_51.setIcon(icon7)
        self.pushButton_51.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_33)
        self.pushButton_52.setEnabled(True)
        self.pushButton_52.setGeometry(QtCore.QRect(1000, 540, 231, 51))
        self.pushButton_52.setStyleSheet("border-width: 2px;")
        self.pushButton_52.setIcon(icon8)
        self.pushButton_52.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_52.setObjectName("pushButton_52")
        self.label_60 = QtWidgets.QLabel(self.tab_33)
        self.label_60.setGeometry(QtCore.QRect(780, 280, 91, 51))
        self.label_60.setObjectName("label_60")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_48.setGeometry(QtCore.QRect(930, 280, 271, 51))
        self.lineEdit_48.setStyleSheet("border-width: 2px;")
        self.lineEdit_48.setText("")
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_61 = QtWidgets.QLabel(self.tab_33)
        self.label_61.setGeometry(QtCore.QRect(780, 200, 131, 51))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.tab_33)
        self.label_62.setGeometry(QtCore.QRect(780, 120, 91, 51))
        self.label_62.setObjectName("label_62")
        self.comboBox_19 = QtWidgets.QComboBox(self.tab_33)
        self.comboBox_19.setGeometry(QtCore.QRect(930, 200, 271, 51))
        self.comboBox_19.setStyleSheet("border-width: 2px;")
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_20 = QtWidgets.QComboBox(self.tab_33)
        self.comboBox_20.setGeometry(QtCore.QRect(930, 360, 271, 51))
        self.comboBox_20.setStyleSheet("border-width: 2px;")
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_45.setGeometry(QtCore.QRect(930, 440, 271, 51))
        self.lineEdit_45.setStyleSheet("border-width: 2px;")
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_63 = QtWidgets.QLabel(self.tab_33)
        self.label_63.setGeometry(QtCore.QRect(780, 440, 101, 51))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.tab_33)
        self.label_64.setGeometry(QtCore.QRect(780, 360, 131, 51))
        self.label_64.setObjectName("label_64")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_46.setGeometry(QtCore.QRect(930, 120, 271, 51))
        self.lineEdit_46.setStyleSheet("border-width: 2px;")
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.tabWidget_8.addTab(self.tab_33, "")
        self.tabWidget.addTab(self.tab_30, "")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setEnabled(False)
        self.groupBox_11.setGeometry(QtCore.QRect(10, -10, 261, 741))
        self.groupBox_11.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(18, 350, 231, 61))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/student.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(18, 669, 231, 61))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(18, 190, 231, 61))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton.setGeometry(QtCore.QRect(18, 30, 231, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/today.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QtCore.QSize(40, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(18, 430, 231, 61))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon13)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(18, 510, 231, 61))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(18, 590, 231, 61))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon15)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_43.setEnabled(False)
        self.pushButton_43.setGeometry(QtCore.QRect(18, 110, 231, 61))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/sales.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_43.setIcon(icon16)
        self.pushButton_43.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_46 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_46.setEnabled(False)
        self.pushButton_46.setGeometry(QtCore.QRect(18, 270, 231, 61))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/scientific.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_46.setIcon(icon17)
        self.pushButton_46.setIconSize(QtCore.QSize(40, 30))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_67 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_67.setEnabled(False)
        self.pushButton_67.setGeometry(QtCore.QRect(28, 740, 231, 51))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_67.setIcon(icon18)
        self.pushButton_67.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_67.setObjectName("pushButton_67")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1560, 35))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(2)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_106.setText(_translate("MainWindow", "Password"))
        self.pushButton_66.setText(_translate("MainWindow", "Login"))
        self.label_107.setText(_translate("MainWindow", "UserName"))
        self.label_108.setText(_translate("MainWindow", "Your password is incorrect, Rest your password from here"))
        self.pushButton_68.setText(_translate("MainWindow", "Reset Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_19), _translate("MainWindow", "Page"))
        self.label_113.setText(_translate("MainWindow", "Will send to you a validation number on your gmail mail"))
        self.pushButton_80.setText(_translate("MainWindow", "Send"))
        self.label_114.setText(_translate("MainWindow", "UserName"))
        self.pushButton_79.setText(_translate("MainWindow", "Save"))
        self.label_112.setText(_translate("MainWindow", "New Password"))
        self.label_97.setText(_translate("MainWindow", "Verification number"))
        self.pushButton_81.setText(_translate("MainWindow", "Check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_26), _translate("MainWindow", "Page"))
        self.lineEdit_52.setPlaceholderText(_translate("MainWindow", "Student ID"))
        self.label_44.setText(_translate("MainWindow", "To"))
        self.lineEdit_37.setPlaceholderText(_translate("MainWindow", "Book Title"))
        self.pushButton_31.setText(_translate("MainWindow", "Add"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "Rent"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "Retrieve"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "Sale"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Name"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Student"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "From"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "To"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Code"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        self.label.setText(_translate("MainWindow", "Category"))
        self.pushButton_8.setText(_translate("MainWindow", "Search"))
        self.pushButton_37.setText(_translate("MainWindow", "Export"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "All Books"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Book Title"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Book Description"))
        self.label_2.setText(_translate("MainWindow", "Code"))
        self.label_3.setText(_translate("MainWindow", "Category"))
        self.label_4.setText(_translate("MainWindow", "Author"))
        self.label_5.setText(_translate("MainWindow", "Publisher"))
        self.label_6.setText(_translate("MainWindow", "Price"))
        self.pushButton_9.setText(_translate("MainWindow", "Add Book"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Add New Book"))
        self.label_7.setText(_translate("MainWindow", "Code"))
        self.pushButton_10.setText(_translate("MainWindow", "Search"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Book Title"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Book Description"))
        self.label_8.setText(_translate("MainWindow", "Code"))
        self.label_9.setText(_translate("MainWindow", "Category"))
        self.label_10.setText(_translate("MainWindow", "Author"))
        self.label_11.setText(_translate("MainWindow", "Publisher"))
        self.label_12.setText(_translate("MainWindow", "Price"))
        self.pushButton_11.setText(_translate("MainWindow", "Save Book Data"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete Book"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Edit or Delete Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "- - - - - - - - - - -"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "Name"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "National Id"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Mail"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "Phone"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "Department"))
        self.pushButton_13.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", " Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "National Id"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Department"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Enter Data"))
        self.pushButton_38.setText(_translate("MainWindow", "Export"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "All Student"))
        self.label_13.setText(_translate("MainWindow", "Student Name"))
        self.label_14.setText(_translate("MainWindow", "Student Mail"))
        self.label_15.setText(_translate("MainWindow", "Student National Id"))
        self.label_16.setText(_translate("MainWindow", "Student Phone"))
        self.pushButton_14.setText(_translate("MainWindow", "Add Student"))
        self.label_32.setText(_translate("MainWindow", "Student Department"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Add New Student"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "Enter Data"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Name"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "National Id"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Mail"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Phone"))
        self.pushButton_15.setText(_translate("MainWindow", "Search"))
        self.label_17.setText(_translate("MainWindow", "Student Name"))
        self.label_18.setText(_translate("MainWindow", "Student Mail"))
        self.label_19.setText(_translate("MainWindow", "Student National Id"))
        self.label_20.setText(_translate("MainWindow", "Student Phone"))
        self.pushButton_16.setText(_translate("MainWindow", "Save Student Data"))
        self.pushButton_17.setText(_translate("MainWindow", "Delete Student"))
        self.label_31.setText(_translate("MainWindow", "Student Department"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MainWindow", "Edit or Delete Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Action"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Table"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "- - - - - - -"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "Login"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "Logout"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "Add"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "Edit"))
        self.comboBox_12.setItemText(5, _translate("MainWindow", "Delete"))
        self.comboBox_12.setItemText(6, _translate("MainWindow", "Add Rent"))
        self.comboBox_12.setItemText(7, _translate("MainWindow", "Add Retrieve"))
        self.comboBox_12.setItemText(8, _translate("MainWindow", "Add Sale"))
        self.label_35.setText(_translate("MainWindow", "Table"))
        self.label_36.setText(_translate("MainWindow", "Action"))
        self.label_43.setText(_translate("MainWindow", "Username"))
        self.pushButton_30.setText(_translate("MainWindow", "Search"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "------------"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "- - - - - - -"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "Books"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "Students"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "History"))
        self.comboBox_15.setItemText(4, _translate("MainWindow", "Category"))
        self.comboBox_15.setItemText(5, _translate("MainWindow", "Author"))
        self.comboBox_15.setItemText(6, _translate("MainWindow", "Publisher"))
        self.comboBox_15.setItemText(7, _translate("MainWindow", "Employee"))
        self.comboBox_15.setItemText(8, _translate("MainWindow", "Daily Movement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_21.setText(_translate("MainWindow", "From"))
        self.label_22.setText(_translate("MainWindow", "To"))
        self.pushButton_18.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "Books Report"))
        self.label_23.setText(_translate("MainWindow", "From"))
        self.label_24.setText(_translate("MainWindow", "To"))
        self.pushButton_19.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Books"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("MainWindow", "Students Report"))
        self.label_45.setText(_translate("MainWindow", "From"))
        self.label_46.setText(_translate("MainWindow", "To"))
        self.pushButton_39.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Name"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "From"))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "To"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_24), _translate("MainWindow", "Daily Movements Report"))
        self.pushButton_40.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Table"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Action"))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Operation Date"))
        self.label_47.setText(_translate("MainWindow", "To"))
        self.label_48.setText(_translate("MainWindow", "From"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_25), _translate("MainWindow", "Hitory Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Add Category"))
        self.label_33.setText(_translate("MainWindow", "Category Name"))
        self.pushButton_25.setText(_translate("MainWindow", "Add Category"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Add Author"))
        self.lineEdit_27.setPlaceholderText(_translate("MainWindow", "Author Location"))
        self.pushButton_26.setText(_translate("MainWindow", "Add Author"))
        self.lineEdit_29.setPlaceholderText(_translate("MainWindow", "Author Name"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Add Publisher"))
        self.lineEdit_28.setPlaceholderText(_translate("MainWindow", "Publisher Location"))
        self.pushButton_27.setText(_translate("MainWindow", "Add publisher"))
        self.lineEdit_36.setPlaceholderText(_translate("MainWindow", "Publisher Name"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), _translate("MainWindow", "Add Data"))
        self.groupBox.setTitle(_translate("MainWindow", "Add New Employee"))
        self.label_25.setText(_translate("MainWindow", "Employee Name"))
        self.label_26.setText(_translate("MainWindow", "Employee Mail"))
        self.label_27.setText(_translate("MainWindow", "Employee ID"))
        self.label_28.setText(_translate("MainWindow", "Employee Phone"))
        self.label_29.setText(_translate("MainWindow", "Employee Password"))
        self.label_30.setText(_translate("MainWindow", "Employee Password again"))
        self.pushButton_22.setText(_translate("MainWindow", "Add Employee"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Edit or Delete Employee"))
        self.label_37.setText(_translate("MainWindow", "Employee Name"))
        self.label_41.setText(_translate("MainWindow", "Employee Password"))
        self.pushButton_20.setText(_translate("MainWindow", "Check"))
        self.pushButton_21.setText(_translate("MainWindow", "forget password"))
        self.label_40.setText(_translate("MainWindow", "Employee Phone"))
        self.label_38.setText(_translate("MainWindow", "Employee Mail"))
        self.label_39.setText(_translate("MainWindow", "Employee ID"))
        self.label_42.setText(_translate("MainWindow", "Employee Password"))
        self.pushButton_24.setText(_translate("MainWindow", "Delete Employee"))
        self.pushButton_23.setText(_translate("MainWindow", "Save Employee Data"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("MainWindow", "Add or Edit Employee"))
        self.label_34.setText(_translate("MainWindow", "Category Name"))
        self.pushButton_28.setText(_translate("MainWindow", "Check"))
        self.groupBox_7.setTitle(_translate("MainWindow", "App Tabs"))
        self.checkBox.setText(_translate("MainWindow", "Books"))
        self.checkBox_2.setText(_translate("MainWindow", "Students"))
        self.checkBox_3.setText(_translate("MainWindow", "History"))
        self.checkBox_4.setText(_translate("MainWindow", "Reports"))
        self.checkBox_5.setText(_translate("MainWindow", "Settings"))
        self.checkBox_6.setText(_translate("MainWindow", "DataBase"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Books"))
        self.checkBox_7.setText(_translate("MainWindow", "Add Book"))
        self.checkBox_8.setText(_translate("MainWindow", "Edit Book"))
        self.checkBox_9.setText(_translate("MainWindow", "Delete Book"))
        self.checkBox_10.setText(_translate("MainWindow", "Export Book"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Clients"))
        self.checkBox_11.setText(_translate("MainWindow", "Add Client"))
        self.checkBox_12.setText(_translate("MainWindow", "Edit Client"))
        self.checkBox_13.setText(_translate("MainWindow", "Delete Client"))
        self.checkBox_14.setText(_translate("MainWindow", "Export Client"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Settings"))
        self.checkBox_15.setText(_translate("MainWindow", "Add Category"))
        self.checkBox_16.setText(_translate("MainWindow", "Add Author"))
        self.checkBox_17.setText(_translate("MainWindow", "Add Publisher"))
        self.checkBox_18.setText(_translate("MainWindow", "Add Employee"))
        self.checkBox_19.setText(_translate("MainWindow", "Edit Employee"))
        self.checkBox_20.setText(_translate("MainWindow", "Delete Employee"))
        self.checkBox_21.setText(_translate("MainWindow", "Set Employee as Admin"))
        self.pushButton_29.setText(_translate("MainWindow", "Apply"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MainWindow", "Add Employee Permissions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Addvsd0jvs), _translate("MainWindow", "Page"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book Code"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Publisher"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_7.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Description"))
        self.pushButton_36.setText(_translate("MainWindow", "Export"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_6), _translate("MainWindow", "Books"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        self.pushButton_35.setText(_translate("MainWindow", "Export"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_21), _translate("MainWindow", "Students"))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "National Id"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        self.pushButton_34.setText(_translate("MainWindow", "Export"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_22), _translate("MainWindow", "Employees"))
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        self.pushButton_33.setText(_translate("MainWindow", "Export"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_23), _translate("MainWindow", "Authors"))
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        self.pushButton_32.setText(_translate("MainWindow", "Export"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_20), _translate("MainWindow", "Publishers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
        self.pushButton_44.setText(_translate("MainWindow", "Save"))
        self.label_49.setText(_translate("MainWindow", "Code Of Sold (Book/Researche)"))
        self.checkBox_22.setText(_translate("MainWindow", "Sold To A Student"))
        self.comboBox_21.setItemText(0, _translate("MainWindow", "Book"))
        self.comboBox_21.setItemText(1, _translate("MainWindow", "Research"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_28), _translate("MainWindow", "Add Sale"))
        self.label_51.setText(_translate("MainWindow", "To"))
        self.label_52.setText(_translate("MainWindow", "From"))
        self.pushButton_45.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget_14.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_14.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget_14.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget_14.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sold To"))
        item = self.tableWidget_14.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget_14.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_29), _translate("MainWindow", "All Sales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_27), _translate("MainWindow", "Page"))
        item = self.tableWidget_15.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Research Title"))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject"))
        item = self.tableWidget_15.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Authors"))
        item = self.tableWidget_15.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Language"))
        item = self.tableWidget_15.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "- - - - - - - - - - - - -"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "Computer Science"))
        self.comboBox_14.setItemText(2, _translate("MainWindow", "Chemistry"))
        self.comboBox_14.setItemText(3, _translate("MainWindow", "Energy"))
        self.comboBox_14.setItemText(4, _translate("MainWindow", "Engineering"))
        self.comboBox_14.setItemText(5, _translate("MainWindow", "Mathematics"))
        self.comboBox_14.setItemText(6, _translate("MainWindow", "Physics and Astronomy"))
        self.label_53.setText(_translate("MainWindow", "Subjects"))
        self.pushButton_47.setText(_translate("MainWindow", "Search"))
        self.pushButton_48.setText(_translate("MainWindow", "Export"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_31), _translate("MainWindow", "All Researches"))
        self.lineEdit_40.setPlaceholderText(_translate("MainWindow", "Research Title"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Research Description"))
        self.label_54.setText(_translate("MainWindow", "Code"))
        self.label_58.setText(_translate("MainWindow", "Price"))
        self.pushButton_49.setText(_translate("MainWindow", "Add Research"))
        self.label_55.setText(_translate("MainWindow", "Subjects"))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "Computer Science"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "Chemistry"))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "Energy"))
        self.comboBox_17.setItemText(3, _translate("MainWindow", "Engineering"))
        self.comboBox_17.setItemText(4, _translate("MainWindow", "Mathematics"))
        self.comboBox_17.setItemText(5, _translate("MainWindow", "Physics and Astronomy"))
        self.label_56.setText(_translate("MainWindow", "Author"))
        self.label_57.setText(_translate("MainWindow", "Language"))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "Turkish"))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "Arabic"))
        self.comboBox_18.setItemText(3, _translate("MainWindow", "Germany"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_32), _translate("MainWindow", "Add New Research"))
        self.label_59.setText(_translate("MainWindow", "Code"))
        self.pushButton_50.setText(_translate("MainWindow", "Search"))
        self.lineEdit_44.setPlaceholderText(_translate("MainWindow", "Search Title"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Search Description"))
        self.pushButton_51.setText(_translate("MainWindow", "Save Research Data"))
        self.pushButton_52.setText(_translate("MainWindow", "Delete Research"))
        self.label_60.setText(_translate("MainWindow", "Author"))
        self.label_61.setText(_translate("MainWindow", "Subjects"))
        self.label_62.setText(_translate("MainWindow", "Code"))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "Computer Science"))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "Chemistry"))
        self.comboBox_19.setItemText(2, _translate("MainWindow", "Energy"))
        self.comboBox_19.setItemText(3, _translate("MainWindow", "Engineering"))
        self.comboBox_19.setItemText(4, _translate("MainWindow", "Mathematics"))
        self.comboBox_19.setItemText(5, _translate("MainWindow", "Physics and Astronomy"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Turkish"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "Arabic"))
        self.comboBox_20.setItemText(3, _translate("MainWindow", "Germany"))
        self.label_63.setText(_translate("MainWindow", "Price"))
        self.label_64.setText(_translate("MainWindow", "Language"))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_33), _translate("MainWindow", "Edit or Delete Research"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_30), _translate("MainWindow", "Page"))
        self.pushButton_3.setText(_translate("MainWindow", "Students"))
        self.pushButton_7.setText(_translate("MainWindow", "DataBase"))
        self.pushButton_2.setText(_translate("MainWindow", "Books"))
        self.pushButton.setText(_translate("MainWindow", "Today"))
        self.pushButton_4.setText(_translate("MainWindow", "History"))
        self.pushButton_5.setText(_translate("MainWindow", "Reports"))
        self.pushButton_6.setText(_translate("MainWindow", "Settings"))
        self.pushButton_43.setText(_translate("MainWindow", "Sales"))
        self.pushButton_46.setText(_translate("MainWindow", "Scientific Researches"))
        self.pushButton_67.setText(_translate("MainWindow", "Logout"))

import icons_rc
