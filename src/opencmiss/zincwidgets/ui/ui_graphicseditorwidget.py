# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graphicseditorwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.fieldchooserwidget import FieldChooserWidget
from opencmiss.zincwidgets.materialchooserwidget import MaterialChooserWidget
from opencmiss.zincwidgets.glyphchooserwidget import GlyphChooserWidget
from opencmiss.zincwidgets.spectrumchooserwidget import SpectrumChooserWidget
from opencmiss.zincwidgets.tessellationchooserwidget import TessellationChooserWidget


class Ui_GraphicsEditorWidget(object):
    def setupUi(self, GraphicsEditorWidget):
        if not GraphicsEditorWidget.objectName():
            GraphicsEditorWidget.setObjectName(u"GraphicsEditorWidget")
        GraphicsEditorWidget.setEnabled(True)
        GraphicsEditorWidget.resize(298, 964)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphicsEditorWidget.sizePolicy().hasHeightForWidth())
        GraphicsEditorWidget.setSizePolicy(sizePolicy)
        GraphicsEditorWidget.setMinimumSize(QSize(180, 0))
        self.verticalLayout = QVBoxLayout(GraphicsEditorWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.general_groupbox = QGroupBox(GraphicsEditorWidget)
        self.general_groupbox.setObjectName(u"general_groupbox")
        self.general_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.general_groupbox.setCheckable(False)
        self.formLayout_3 = QFormLayout(self.general_groupbox)
        self.formLayout_3.setContentsMargins(7, 7, 7, 7)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.coordinate_field_label = QLabel(self.general_groupbox)
        self.coordinate_field_label.setObjectName(u"coordinate_field_label")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.coordinate_field_label)

        self.coordinate_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.coordinate_field_chooser.setObjectName(u"coordinate_field_chooser")
        self.coordinate_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.coordinate_field_chooser)

        self.scenecoordinatesystem_label = QLabel(self.general_groupbox)
        self.scenecoordinatesystem_label.setObjectName(u"scenecoordinatesystem_label")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.scenecoordinatesystem_label)

        self.scenecoordinatesystem_combobox = QComboBox(self.general_groupbox)
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.addItem("")
        self.scenecoordinatesystem_combobox.setObjectName(u"scenecoordinatesystem_combobox")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.scenecoordinatesystem_combobox)

        self.exterior_checkbox = QCheckBox(self.general_groupbox)
        self.exterior_checkbox.setObjectName(u"exterior_checkbox")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.exterior_checkbox)

        self.face_label = QLabel(self.general_groupbox)
        self.face_label.setObjectName(u"face_label")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.face_label)

        self.face_combobox = QComboBox(self.general_groupbox)
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.addItem("")
        self.face_combobox.setObjectName(u"face_combobox")
        self.face_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.face_combobox)

        self.material_label = QLabel(self.general_groupbox)
        self.material_label.setObjectName(u"material_label")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.material_label)

        self.material_chooser = MaterialChooserWidget(self.general_groupbox)
        self.material_chooser.setObjectName(u"material_chooser")
        self.material_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.material_chooser)

        self.data_field_label = QLabel(self.general_groupbox)
        self.data_field_label.setObjectName(u"data_field_label")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.data_field_label)

        self.data_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.data_field_chooser.setObjectName(u"data_field_chooser")
        self.data_field_chooser.setEditable(False)
        self.data_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.data_field_chooser)

        self.spectrum_label = QLabel(self.general_groupbox)
        self.spectrum_label.setObjectName(u"spectrum_label")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.spectrum_label)

        self.spectrum_chooser = SpectrumChooserWidget(self.general_groupbox)
        self.spectrum_chooser.setObjectName(u"spectrum_chooser")

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.spectrum_chooser)

        self.wireframe_checkbox = QCheckBox(self.general_groupbox)
        self.wireframe_checkbox.setObjectName(u"wireframe_checkbox")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.wireframe_checkbox)

        self.tessellation_chooser = TessellationChooserWidget(self.general_groupbox)
        self.tessellation_chooser.setObjectName(u"tessellation_chooser")

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.tessellation_chooser)

        self.tessellation_label = QLabel(self.general_groupbox)
        self.tessellation_label.setObjectName(u"tessellation_label")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.tessellation_label)

        self.subgroup_field_label = QLabel(self.general_groupbox)
        self.subgroup_field_label.setObjectName(u"subgroup_field_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.subgroup_field_label)

        self.subgroup_field_chooser = FieldChooserWidget(self.general_groupbox)
        self.subgroup_field_chooser.setObjectName(u"subgroup_field_chooser")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.subgroup_field_chooser)


        self.verticalLayout.addWidget(self.general_groupbox)

        self.contours_groupbox = QGroupBox(GraphicsEditorWidget)
        self.contours_groupbox.setObjectName(u"contours_groupbox")
        self.contours_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.contours_groupbox.setFlat(False)
        self.formLayout_2 = QFormLayout(self.contours_groupbox)
        self.formLayout_2.setContentsMargins(7, 7, 7, 7)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setHorizontalSpacing(7)
        self.formLayout_2.setVerticalSpacing(7)
        self.isovalues_lineedit = QLineEdit(self.contours_groupbox)
        self.isovalues_lineedit.setObjectName(u"isovalues_lineedit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.isovalues_lineedit)

        self.isoscalar_field_label = QLabel(self.contours_groupbox)
        self.isoscalar_field_label.setObjectName(u"isoscalar_field_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.isoscalar_field_label)

        self.isoscalar_field_chooser = FieldChooserWidget(self.contours_groupbox)
        self.isoscalar_field_chooser.setObjectName(u"isoscalar_field_chooser")
        self.isoscalar_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.isoscalar_field_chooser)

        self.isovalues_label = QLabel(self.contours_groupbox)
        self.isovalues_label.setObjectName(u"isovalues_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.isovalues_label)


        self.verticalLayout.addWidget(self.contours_groupbox)

        self.streamlines_groupbox = QGroupBox(GraphicsEditorWidget)
        self.streamlines_groupbox.setObjectName(u"streamlines_groupbox")
        self.formLayout_5 = QFormLayout(self.streamlines_groupbox)
        self.formLayout_5.setContentsMargins(7, 7, 7, 7)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.stream_vector_field_label = QLabel(self.streamlines_groupbox)
        self.stream_vector_field_label.setObjectName(u"stream_vector_field_label")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.stream_vector_field_label)

        self.stream_vector_field_chooser = FieldChooserWidget(self.streamlines_groupbox)
        self.stream_vector_field_chooser.setObjectName(u"stream_vector_field_chooser")
        self.stream_vector_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.stream_vector_field_chooser)

        self.streamlines_track_length_label = QLabel(self.streamlines_groupbox)
        self.streamlines_track_length_label.setObjectName(u"streamlines_track_length_label")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.streamlines_track_length_label)

        self.streamlines_track_length_lineedit = QLineEdit(self.streamlines_groupbox)
        self.streamlines_track_length_lineedit.setObjectName(u"streamlines_track_length_lineedit")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.streamlines_track_length_lineedit)

        self.streamline_track_direction_label = QLabel(self.streamlines_groupbox)
        self.streamline_track_direction_label.setObjectName(u"streamline_track_direction_label")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.streamline_track_direction_label)

        self.streamlines_track_direction_combobox = QComboBox(self.streamlines_groupbox)
        self.streamlines_track_direction_combobox.addItem("")
        self.streamlines_track_direction_combobox.addItem("")
        self.streamlines_track_direction_combobox.setObjectName(u"streamlines_track_direction_combobox")
        self.streamlines_track_direction_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.streamlines_track_direction_combobox)

        self.streamlines_colour_data_type_label = QLabel(self.streamlines_groupbox)
        self.streamlines_colour_data_type_label.setObjectName(u"streamlines_colour_data_type_label")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.streamlines_colour_data_type_label)

        self.streamlines_colour_data_type_combobox = QComboBox(self.streamlines_groupbox)
        self.streamlines_colour_data_type_combobox.addItem("")
        self.streamlines_colour_data_type_combobox.addItem("")
        self.streamlines_colour_data_type_combobox.addItem("")
        self.streamlines_colour_data_type_combobox.setObjectName(u"streamlines_colour_data_type_combobox")
        self.streamlines_colour_data_type_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.streamlines_colour_data_type_combobox)


        self.verticalLayout.addWidget(self.streamlines_groupbox)

        self.lines_groupbox = QGroupBox(GraphicsEditorWidget)
        self.lines_groupbox.setObjectName(u"lines_groupbox")
        self.formLayout_4 = QFormLayout(self.lines_groupbox)
        self.formLayout_4.setContentsMargins(7, 7, 7, 7)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.line_shape_label = QLabel(self.lines_groupbox)
        self.line_shape_label.setObjectName(u"line_shape_label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.line_shape_label)

        self.line_shape_combobox = QComboBox(self.lines_groupbox)
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.addItem("")
        self.line_shape_combobox.setObjectName(u"line_shape_combobox")
        self.line_shape_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.line_shape_combobox)

        self.line_base_size_label = QLabel(self.lines_groupbox)
        self.line_base_size_label.setObjectName(u"line_base_size_label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.line_base_size_label)

        self.line_base_size_lineedit = QLineEdit(self.lines_groupbox)
        self.line_base_size_lineedit.setObjectName(u"line_base_size_lineedit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.line_base_size_lineedit)

        self.line_orientation_scale_field_label = QLabel(self.lines_groupbox)
        self.line_orientation_scale_field_label.setObjectName(u"line_orientation_scale_field_label")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.line_orientation_scale_field_label)

        self.line_orientation_scale_field_chooser = FieldChooserWidget(self.lines_groupbox)
        self.line_orientation_scale_field_chooser.setObjectName(u"line_orientation_scale_field_chooser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_orientation_scale_field_chooser.sizePolicy().hasHeightForWidth())
        self.line_orientation_scale_field_chooser.setSizePolicy(sizePolicy1)
        self.line_orientation_scale_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.line_orientation_scale_field_chooser)

        self.line_scale_factors_label = QLabel(self.lines_groupbox)
        self.line_scale_factors_label.setObjectName(u"line_scale_factors_label")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.line_scale_factors_label)

        self.line_scale_factors_lineedit = QLineEdit(self.lines_groupbox)
        self.line_scale_factors_lineedit.setObjectName(u"line_scale_factors_lineedit")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.line_scale_factors_lineedit)


        self.verticalLayout.addWidget(self.lines_groupbox)

        self.points_groupbox = QGroupBox(GraphicsEditorWidget)
        self.points_groupbox.setObjectName(u"points_groupbox")
        self.points_groupbox.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout = QFormLayout(self.points_groupbox)
        self.formLayout.setContentsMargins(7, 7, 7, 7)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.glyph_label = QLabel(self.points_groupbox)
        self.glyph_label.setObjectName(u"glyph_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.glyph_label)

        self.glyph_chooser = GlyphChooserWidget(self.points_groupbox)
        self.glyph_chooser.setObjectName(u"glyph_chooser")
        self.glyph_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.glyph_chooser)

        self.point_base_size_label = QLabel(self.points_groupbox)
        self.point_base_size_label.setObjectName(u"point_base_size_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.point_base_size_label)

        self.point_base_size_lineedit = QLineEdit(self.points_groupbox)
        self.point_base_size_lineedit.setObjectName(u"point_base_size_lineedit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.point_base_size_lineedit)

        self.point_orientation_scale_field_label = QLabel(self.points_groupbox)
        self.point_orientation_scale_field_label.setObjectName(u"point_orientation_scale_field_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.point_orientation_scale_field_label)

        self.point_orientation_scale_field_chooser = FieldChooserWidget(self.points_groupbox)
        self.point_orientation_scale_field_chooser.setObjectName(u"point_orientation_scale_field_chooser")
        self.point_orientation_scale_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.point_orientation_scale_field_chooser)

        self.point_scale_factors_label = QLabel(self.points_groupbox)
        self.point_scale_factors_label.setObjectName(u"point_scale_factors_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.point_scale_factors_label)

        self.label_field_label = QLabel(self.points_groupbox)
        self.label_field_label.setObjectName(u"label_field_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_field_label)

        self.label_field_chooser = FieldChooserWidget(self.points_groupbox)
        self.label_field_chooser.setObjectName(u"label_field_chooser")
        self.label_field_chooser.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_field_chooser)

        self.point_scale_factors_lineedit = QLineEdit(self.points_groupbox)
        self.point_scale_factors_lineedit.setObjectName(u"point_scale_factors_lineedit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.point_scale_factors_lineedit)


        self.verticalLayout.addWidget(self.points_groupbox)

        self.sampling_groupbox = QGroupBox(GraphicsEditorWidget)
        self.sampling_groupbox.setObjectName(u"sampling_groupbox")
        self.formLayout_6 = QFormLayout(self.sampling_groupbox)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.sampling_mode_label = QLabel(self.sampling_groupbox)
        self.sampling_mode_label.setObjectName(u"sampling_mode_label")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.sampling_mode_label)

        self.sampling_mode_combobox = QComboBox(self.sampling_groupbox)
        self.sampling_mode_combobox.addItem("")
        self.sampling_mode_combobox.addItem("")
        self.sampling_mode_combobox.setObjectName(u"sampling_mode_combobox")
        self.sampling_mode_combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.sampling_mode_combobox)


        self.verticalLayout.addWidget(self.sampling_groupbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(GraphicsEditorWidget)
        self.data_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.dataFieldChanged)
        self.material_chooser.currentIndexChanged.connect(GraphicsEditorWidget.materialChanged)
        self.glyph_chooser.currentIndexChanged.connect(GraphicsEditorWidget.glyphChanged)
        self.point_base_size_lineedit.editingFinished.connect(GraphicsEditorWidget.pointBaseSizeEntered)
        self.point_scale_factors_lineedit.editingFinished.connect(GraphicsEditorWidget.pointScaleFactorsEntered)
        self.point_orientation_scale_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.pointOrientationScaleFieldChanged)
        self.label_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.labelFieldChanged)
        self.exterior_checkbox.clicked.connect(GraphicsEditorWidget.exteriorClicked)
        self.isoscalar_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.isoscalarFieldChanged)
        self.face_combobox.currentIndexChanged.connect(GraphicsEditorWidget.faceChanged)
        self.wireframe_checkbox.clicked.connect(GraphicsEditorWidget.wireframeClicked)
        self.isovalues_lineedit.editingFinished.connect(GraphicsEditorWidget.isovaluesEntered)
        self.line_base_size_lineedit.editingFinished.connect(GraphicsEditorWidget.lineBaseSizeEntered)
        self.line_orientation_scale_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.lineOrientationScaleFieldChanged)
        self.line_scale_factors_lineedit.editingFinished.connect(GraphicsEditorWidget.lineScaleFactorsEntered)
        self.line_shape_combobox.currentIndexChanged.connect(GraphicsEditorWidget.lineShapeChanged)
        self.stream_vector_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.streamVectorFieldChanged)
        self.streamlines_track_length_lineedit.editingFinished.connect(GraphicsEditorWidget.streamlinesTrackLengthEntered)
        self.streamlines_track_direction_combobox.currentIndexChanged.connect(GraphicsEditorWidget.streamlinesTrackDirectionChanged)
        self.coordinate_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.coordinateFieldChanged)
        self.sampling_mode_combobox.currentIndexChanged.connect(GraphicsEditorWidget.samplingModeChanged)
        self.streamlines_colour_data_type_combobox.currentIndexChanged.connect(GraphicsEditorWidget.streamlinesColourDataTypeChanged)
        self.spectrum_chooser.currentIndexChanged.connect(GraphicsEditorWidget.spectrumChanged)
        self.scenecoordinatesystem_combobox.currentIndexChanged.connect(GraphicsEditorWidget.scenecoordinatesystemChanged)
        self.tessellation_chooser.currentIndexChanged.connect(GraphicsEditorWidget.tessellationChanged)
        self.subgroup_field_chooser.currentIndexChanged.connect(GraphicsEditorWidget.subgroupFieldChanged)

        QMetaObject.connectSlotsByName(GraphicsEditorWidget)
    # setupUi

    def retranslateUi(self, GraphicsEditorWidget):
        GraphicsEditorWidget.setWindowTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Graphics Editor", None))
        self.general_groupbox.setTitle("")
        self.coordinate_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Coordinates:", None))
        self.scenecoordinatesystem_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Coord System:", None))
        self.scenecoordinatesystem_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"LOCAL", None))
        self.scenecoordinatesystem_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"WORLD", None))
        self.scenecoordinatesystem_combobox.setItemText(2, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FILL", None))
        self.scenecoordinatesystem_combobox.setItemText(3, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FIT_CENTRE", None))
        self.scenecoordinatesystem_combobox.setItemText(4, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FIT_LEFT", None))
        self.scenecoordinatesystem_combobox.setItemText(5, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FIT_RIGHT", None))
        self.scenecoordinatesystem_combobox.setItemText(6, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FIT_BOTTOM", None))
        self.scenecoordinatesystem_combobox.setItemText(7, QCoreApplication.translate("GraphicsEditorWidget", u"NORMALISED_WINDOW_FIT_TOP", None))
        self.scenecoordinatesystem_combobox.setItemText(8, QCoreApplication.translate("GraphicsEditorWidget", u"WINDOW_PIXEL_BOTTOM_LEFT", None))
        self.scenecoordinatesystem_combobox.setItemText(9, QCoreApplication.translate("GraphicsEditorWidget", u"WINDOW_PIXEL_TOP_LEFT", None))

        self.exterior_checkbox.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Exterior", None))
        self.face_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Face:", None))
        self.face_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"all", None))
        self.face_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"any face", None))
        self.face_combobox.setItemText(2, QCoreApplication.translate("GraphicsEditorWidget", u"no face", None))
        self.face_combobox.setItemText(3, QCoreApplication.translate("GraphicsEditorWidget", u"xi1 = 0", None))
        self.face_combobox.setItemText(4, QCoreApplication.translate("GraphicsEditorWidget", u"xi1 = 1", None))
        self.face_combobox.setItemText(5, QCoreApplication.translate("GraphicsEditorWidget", u"xi2 = 0", None))
        self.face_combobox.setItemText(6, QCoreApplication.translate("GraphicsEditorWidget", u"xi2 = 1", None))
        self.face_combobox.setItemText(7, QCoreApplication.translate("GraphicsEditorWidget", u"xi3 = 0", None))
        self.face_combobox.setItemText(8, QCoreApplication.translate("GraphicsEditorWidget", u"xi3 = 1", None))

        self.material_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Material:", None))
        self.data_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Data field:", None))
        self.spectrum_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Spectrum:", None))
        self.wireframe_checkbox.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Wireframe", None))
        self.tessellation_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Tessellation:", None))
        self.subgroup_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Subgroup:", None))
        self.contours_groupbox.setTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Contours:", None))
        self.isoscalar_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Scalar field:", None))
        self.isovalues_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Isovalues:", None))
        self.streamlines_groupbox.setTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Streamlines:", None))
        self.stream_vector_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Vector field:", None))
        self.streamlines_track_length_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Time length:", None))
        self.streamline_track_direction_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Direction:", None))
        self.streamlines_track_direction_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"forward", None))
        self.streamlines_track_direction_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"reverse", None))

        self.streamlines_colour_data_type_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Colour data:", None))
        self.streamlines_colour_data_type_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"field", None))
        self.streamlines_colour_data_type_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"magnitude", None))
        self.streamlines_colour_data_type_combobox.setItemText(2, QCoreApplication.translate("GraphicsEditorWidget", u"travel time", None))

        self.lines_groupbox.setTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Lines:", None))
        self.line_shape_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Shape:", None))
        self.line_shape_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"line", None))
        self.line_shape_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"ribbon", None))
        self.line_shape_combobox.setItemText(2, QCoreApplication.translate("GraphicsEditorWidget", u"circle extrusion", None))
        self.line_shape_combobox.setItemText(3, QCoreApplication.translate("GraphicsEditorWidget", u"square extrusion", None))

        self.line_base_size_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Base size:", None))
        self.line_orientation_scale_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Scale field:", None))
        self.line_scale_factors_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Scaling:", None))
        self.points_groupbox.setTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Points:", None))
        self.glyph_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Glyph:", None))
        self.point_base_size_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Base size:", None))
        self.point_orientation_scale_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Scale field:", None))
        self.point_scale_factors_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Scaling:", None))
        self.label_field_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Label field:", None))
        self.sampling_groupbox.setTitle(QCoreApplication.translate("GraphicsEditorWidget", u"Sampling:", None))
        self.sampling_mode_label.setText(QCoreApplication.translate("GraphicsEditorWidget", u"Mode:", None))
        self.sampling_mode_combobox.setItemText(0, QCoreApplication.translate("GraphicsEditorWidget", u"cell centres", None))
        self.sampling_mode_combobox.setItemText(1, QCoreApplication.translate("GraphicsEditorWidget", u"cell corners", None))

    # retranslateUi

