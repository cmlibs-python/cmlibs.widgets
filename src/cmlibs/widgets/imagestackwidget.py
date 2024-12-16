
from PySide6 import QtCore, QtGui, QtWidgets

from cmlibs.widgets.ui.ui_imagestackwidget import Ui_ImageStackWidget


INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ImageStackWidget(QtWidgets.QWidget):

    scale_updated = QtCore.Signal(list)

    def __init__(self, dimensions, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self._ui = Ui_ImageStackWidget()
        self._ui.setupUi(self)

        self._number_of_dimensions = len(dimensions)
        display_dimensions = ", ".join([f"{d}" for d in dimensions])
        self._ui.imagePixelOutputLabel.setText(f"{display_dimensions} px")

        self._set_scale_validator()
        self._make_connections()

    def _set_scale_validator(self):
        regex = QtCore.QRegularExpression(f"^[0-9.]+(, ?[0-9.]+){{{self._number_of_dimensions - 1}}}$")
        validator = QtGui.QRegularExpressionValidator(regex)
        self._ui.scalingLineEdit.setValidator(validator)

    def _make_connections(self):
        self._ui.scalingLineEdit.editingFinished.connect(self.update_scale)
        self._ui.scalingLineEdit.textChanged.connect(self._update_style_sheets)

    def _update_style_sheets(self):
        if not self._ui.scalingLineEdit.hasAcceptableInput():
            self._ui.scalingLineEdit.setStyleSheet(INVALID_STYLE_SHEET)
        else:
            self._ui.scalingLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)

    def update_scale(self):
        self._ui.scalingLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)

        text = self._ui.scalingLineEdit.text()
        scale = [float(x.strip()) for x in text.split(',')]
        self.scale_updated.emit(scale)

    def get_scaling(self):
        return self._ui.scalingLineEdit.text()

    def set_scaling(self, scaling):
        self._ui.scalingLineEdit.setText(scaling)

    def scaling_overridden(self):
        return self._ui.overrideScalingCheckBox.isChecked()

    def override_scaling(self, override):
        self._ui.overrideScalingCheckBox.setChecked(override)
