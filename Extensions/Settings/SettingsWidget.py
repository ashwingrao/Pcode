from PyQt4 import QtCore, QtGui

from Extensions.Settings.ColorScheme.ColorScheme import ColorScheme
from Extensions.Settings.Keymap import Keymap
from Extensions.Settings.SnippetsManager import SnippetsManager
from Extensions.Settings.GeneralSettings import GeneralSettings
from Extensions.Settings.ModuleCompletion import ModuleCompletion


class SettingsWidget(QtGui.QDialog):

    def __init__(self, useData, mainApp, projectWindowStack, libraryViewer, parent=None):
        QtGui.QDialog.__init__(self, parent, QtCore.Qt.Window |
                               QtCore.Qt.WindowCloseButtonHint)

        self.setWindowTitle("Settings")

        self.useData = useData
        self.libraryViewer = libraryViewer
        self.projectWindowStack = projectWindowStack

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setMargin(0)
        self.setLayout(mainLayout)

        self.settingsTab = QtGui.QTabWidget()
        self.settingsTab.setObjectName("settingsTab")
        mainLayout.addWidget(self.settingsTab)

        self.generalSettings = GeneralSettings(useData, mainApp, projectWindowStack)
        self.settingsTab.addTab(self.generalSettings, "General")

        self.snippetEditor = SnippetsManager(
            self.useData.appPathDict["snippetsdir"], self)
        self.settingsTab.addTab(self.snippetEditor, "Snippets")

        self.keymapWidget = Keymap(self.useData, projectWindowStack, self)
        self.settingsTab.addTab(self.keymapWidget, "Shortcuts")

        self.colorScheme = ColorScheme(self.useData, projectWindowStack,
                                       libraryViewer)
        self.settingsTab.addTab(self.colorScheme, "Color Scheme")

        self.libraries = ModuleCompletion(self.useData)
        self.settingsTab.addTab(self.libraries, "Module Completion")
