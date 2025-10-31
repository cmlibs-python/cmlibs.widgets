.. _Material-Editor-Widget:

======================
Material Editor Widget
======================

The **material editor widget** enables interactive creation and editing of graphical materials which are used to control the colour and shading of graphics in 3-D visualizations.

.. _fig-cmlibs-widgets-material-editor-widget:

.. figure:: _images/material-editor-widget.png
   :alt: Material editor widget.
   :width: 75%

   Material editor widget.

Material list
-------------

Along the top of the material editor window are two buttons; create and delete.  You can create a new material, or delete an existing material using these buttons.  

Below these buttons is the list of currently defined materials.
These will contain the default materials, as well as any defined in any comfile that has been run.

You can rename the material by double-clicking on it.

.. figure:: _images/material-editor-rename.png
   :alt: Material editor rename material.
   :width: 50%

   Rename material.

Controls
--------

Below the material list is a panel containing four colour select buttons. These control the ambient, diffuse, emitted and specular colours.

* Ambient - The ambient colour is the "unlit" colour, or the colour of parts of the object that are in shadow.
* Diffuse - This is the overall colour of the material, the colour that the lit parts of the object will appear.
* Emitted - The emitted colour is the "glow" of a material; this colour will appear in both the lit and unlit parts of the material.
* Specular - This is the colour of the shine that appears on the material.  This shine appears as a glossy highlight.

.. figure:: _images/material-editor-select-color.png
   :alt: Material editor select colour.
   :width: 50%

   Select colour.

When you click the Select Colour button, a colour dialog will pop up, and you can select a colour in several ways. The background of these four buttons indicates the colour you choose.

Below the colour editors are further attributes controlling the rendering:

* *Alpha* sets the opacity, from 0.0 (transparent) to 1.0 (opaque) with corresponding variable translucency in between. Use of alpha \< 1.0 may require use of Sceneviewer Transparency modes ``slow`` or ``order independent`` for best results.
* *Shininess* sets the "tightness" or size of the specular highlights of a material, a value from 0.0 to 1.0. Generally, the higher the shininess, the smaller and harder-edged are the highlights. Use requires a non-black specular colour.
* *Texture* specifies up to 4 image fields from a region to be attached to the material for texture mapping and other special effects. Note at this time facilities for loading images and shaders which use these have not been exposed.

Preview panel
-------------

Below the surface editor is a panel that shows a preview of the currently edited material applied to a sphere. 
This panel displays a sphere, shaded with the selected material.

API
---

.. autoclass:: cmlibs.widgets.materialeditorwidget.MaterialEditorWidget
   :members:

.. autoclass:: cmlibs.widgets.materialeditorwidget.MaterialModel
   :members: