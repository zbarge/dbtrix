"""
MIT License

Copyright (c) 2016 Zeke Barge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import logging
from zeex.core.compat import QtGui, QtCore
from zeex.core.ui.actions.export_ui import Ui_ExportFileDialog
from zeex.core.utility.widgets import configure_combo_box, get_ok_msg_box
from zeex.core.ctrls.dataframe import DataFrameModelManager, ENCODINGS, SEPARATORS
from zeex.core.utility.ostools import path_incremented


class DataFrameModelExportDialog(QtGui.QDialog, Ui_ExportFileDialog):
    signalExported = QtCore.Signal(str, str) # original_path, new_path

    def __init__(self, df_manager: DataFrameModelManager, filename: str=None, allow_multi_source=True, **kwargs):
        self.df_manager = df_manager
        if allow_multi_source:
            self.df_manager.signalNewModelRead.connect(self.append_source_filename)

        if filename is None:

            if df_manager.last_path_updated is not None:
                self._default_path = df_manager.last_path_updated
            else:
                self._default_path = df_manager.last_path_read

        else:
            self._default_path = filename
            assert filename in df_manager.file_paths, "Invalid filename {} not in DataFrameModelManager paths: {}".format(
                                                       filename, df_manager.file_paths)

        QtGui.QDialog.__init__(self, **kwargs)
        self.setupUi(self)
        self.configure()

    def configure(self):
        self.btnBrowseDestination.clicked.connect(self.browse_destination)
        self.btnBrowseSource.clicked.connect(self.browse_source)
        self.btnOverwrite.clicked.connect(self.set_destination_path_from_source)
        configure_combo_box(self.comboBoxSource, self.df_manager.file_paths, self._default_path)
        configure_combo_box(self.comboBoxSeparator, list(SEPARATORS.keys()), 'Comma')
        configure_combo_box(self.comboBoxEncoding, list(ENCODINGS.keys()), 'ISO-8859-1')
        self.buttonBox.accepted.connect(self.export)

        if self._default_path is not None:
            self.lineEditDestination.setText(path_incremented(self._default_path, overwrite=False))

    def browse_destination(self):
        source = self.comboBoxSource.currentText()
        if os.path.isfile(source):
            kwargs = dict(dir=os.path.dirname(source))
        else:
            kwargs = dict()
        filename = QtGui.QFileDialog.getSaveFileName(self, **kwargs)[0]
        if os.path.isfile(filename):
            self.lineEditDestination.setText(filename)

    def set_separator(self, sep):
        try:
            SEPARATORS[sep]
        except KeyError:
            mapper = {v:k for k,v in SEPARATORS.items()}
            try:
                sep = mapper[sep]
            except KeyError:
                self.radioBtnOtherSeparator.setChecked(True)
                return self.lineEditOtherSeparator.setText(sep)

        self.comboBoxSeparator.setCurrentIndex(self.comboBoxSeparator.findText(sep))

    def set_encoding(self, en):
        try:
            ENCODINGS[en]
        except KeyError as e:
            mapper = {v:k for k,v in ENCODINGS.items()}
            try:
                en = mapper[en]
            except KeyError as e:
                raise KeyError("Invalid Encoding {}".format(e))
        self.comboBoxEncoding.setCurrentIndex(self.comboBoxEncoding.findText(en))

    def set_destination_path_from_source(self):
        self.lineEditDestination.setText(self.comboBoxSource.currentText())

    def browse_source(self):
        source = self.comboBoxSource.currentText()
        if os.path.isfile(source):
            kwargs = dict(dir=os.path.dirname(source))
        else:
            kwargs = dict()
        filename = QtGui.QFileDialog.getOpenFileName(self, **kwargs)[0]
        if filename not in self.df_manager.file_paths:
            self.df_manager.read_file(filename)
        idx = self.comboBoxSource.findText(filename)
        self.comboBoxSource.setCurrentIndex(idx)

    @QtCore.Slot(str)
    def append_source_filename(self, filename: str):
        self.comboBoxSource.addItem(filename)

    def export(self):
        source_path = self.comboBoxSource.currentText()
        file_path = self.lineEditDestination.text()
        encoding = self.comboBoxEncoding.currentText()

        if self.radioBtnOtherSeparator.isChecked():
            sep = self.lineEditOtherSeparator.text()
        else:
            sep = self.comboBoxSeparator.currentText()

        kwargs = dict(index=False)
        kwargs['encoding'] = ENCODINGS[encoding]
        kwargs['sep'] = SEPARATORS[sep]

        self.df_manager.save_file(source_path, save_as=file_path, keep_orig=True, **kwargs)
        self.signalExported.emit(source_path, file_path)
        self.hide()
        #box = get_ok_msg_box(self.parent, "Exported {}!".format(file_path))
        #box.show()
        logging.info("Exported {} to {}".format(source_path, file_path))





