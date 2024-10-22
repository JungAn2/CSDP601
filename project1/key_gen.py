import mainWindow

# create a pyqt5 application
app = mainWindow.QApplication([])
window = mainWindow.MainWindow()
window.show()

app.exec()