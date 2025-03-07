.. _Graphics-Editor-Widget:

======================
Graphics Editor Widget
======================

The **Graphics Editor Widget** is where each graphical setting can be edited. 
When a graphical setting is selected from the list, all of its editable properties appear in this area. 
The range of editable properties will vary depending on the type of graphics currently selected.

.. _fig-cmlibs-widgets-graphics-editor-widget:

.. figure:: _images/graphics-editor-widget.png
   :alt: Graphics editor widget.
   :width: 75%

   Graphics editor widget.

This widget is normally used within the Scene Editor Widget. The content changes depending on the type of graphics selected in graphic list on Scene Editor Widget.

.. _curl: http://www.math.umn.edu/~nykamp/m2374/readings/divcurl/

General description of graphics
-------------------------------

Graphics are the building blocks used to create any visualization displayed in the :ref:`sceneviewer widget <Sceneviewer-Widget>`. 
They are created, edited, re-ordered and deleted from within the :ref:`scene editor widget <Scene-Editor-Widget>`, or via the Zinc API. Most graphics have the following settings in common:

* Domain: The model domain ``point/nodes/datapoints/mesh1d/mesh2d/mesh3d`` which graphics are built from. Some graphics types support multiple domain types. Special domain ``mesh highest dimension`` uses the highest dimension mesh present in the region.

* Subgroup: Optional group or field returning non-zero/true to limit graphics display to.
 
* Coordinate field: This setting has a drop-down menu showing a list of fields that can be selected as the coordinate field for the selected graphic. This is usually a geometric coordinate field from the model, but any field with up to 3 real components is usable and can be quite powerful: for example, using the principal strain field (over elements points) plots a strain space diagram.

* Coordinate System: This setting can be used to render the graphic according to a range of different coordinate systems. This is useful for creating "static" overlays of data on visualizations.

* Boundary mode: This drop-down menu allows you to select a boundary, and automatically only render glyphs on the select boundary of a mesh. Options allow display on boundary or interior of mesh or subgroup.

* Select mode: This drop-down menu allows you to select different selection behaviours for the graphic:

  * select_on - The default setting; graphics are able to be selected and selected items are highlighted by rendering in the *default_selected* material.
  * no_select - No selection or highlighting of the graphic.
  * draw_selected - only selected items are drawn, in the *default_selected* material.
  * draw_unselected - only unselected items are drawn.

* Wireframe: This checkbox, if checked shows surface graphics as a wireframe mesh, otherwise shaded surfaces are shown.

* Material: This drop-down menu allows you to select which material should be used to render the graphic. Materials are defined and edited in the :ref:`material editor Widget <Material-Editor-Widget>`.

* Selected material: This drop-down menu allows you to set which material will be used to render parts of the graphic which are selected.

* Data: This setting has a drop-down menu, allowing you to select which field will be mapped on to the graphic. This enables you to colour the graphic according to the values of some field, for example. The check box also activates the *spectrum* drop-down menu.

* Spectrum: This drop-down menu is used to select which spectrum is to be used to colour the graphical element according to the field selected in the *data* setting. Spectrums are edited in the :ref:`spectrum editor widget <Spectrum-Editor-Widget>`.

* Tessellation: Tessellation settings are used to set the number of polygons or line segments used to approximate curves in the object. Higher tessellations give greater image quality at the expense of rendering time.

* Tessellation field: This setting has a drop-down menu showing a list of fields that can be selected as the tessellation field for the selected graphic. This approximates element curves with the native resolution of this field multiplied by the resolution from the Tessellation.

* Line width: This value sets the width of line graphics in pixels including line glyphs.

* Point size: This value sets the size of point glyphs in pixels.

.. _types-of-graphics:

The types of graphics
---------------------

* **point**

  Points are created in one of 4 sub-types which also sets the associated *Domain*:

  * **point** - Show a single point in the scene. Assumes coordinate 0, 0, 0 if no coordinate field is specified.
  
  * **node points** - Visualize each node point, usually representing vertexes on a mesh.

  * **data points** - Visualize the second set of points, usually representing point data separate from the model.

  * **element points** - Visualize points sampled across elements of 1 to 3 dimensions.

  Points graphics have additional **Point attributes** specifying:

  * The *Glyph* used to visualize the point, a selectable graphic e.g. point, sphere, cube, arrows etc.
  * The *Base size* of the glyph prior to scaling.
  * The *Scale field* orienting and scaling the glyph.
  * The *Scaling* values multiplying the scale field.
  * The *Signed scale field* multiplying the scale but allowing e.g. inward/outward arrows with repeat mode mirror.
  * The *Glyph offset* allows the glyph origin to be offset relative to the scaled axes at the point.
  * The *Repeat mode* allows multiple glyphs to be rendered to make custom glyphs by mirroring or laying out on 2 or 3 axes.
  * The *Label field* specifies a field whose values are written beside the point. Use special field cmiss_number to show node/datapoint/element numbers.
  * The *Label text* allows fixed text strings to be written prior to the label field, with up to 3 strings for different glyph repeat modes.
  * The *Label text offset* allows the label origin to be offset relative to the scaled axes at the point.
  * The *Font* allows different fonts to be chosen for the labels, where supported.

  Points on mesh domains have additional **Sampling attributes**:

  * *Sampling mode* controls number and location of sampled points in terms of tessellation:
    * *cell centres* specifies points at centres of tessellation 'cells'.
    * *cell corners* specifies points at corners of tessellation 'cells'.
    * *cell poisson* randomly generates points in the tessellation 'cells' according to the Density field sampled at the centre along with the volume/surface area/length.
    * *set location* uses a single set element location.
    * *gaussian quadrature* specifies points at standard Gaussian quadrature locations for the element shape and tessellation, currently limited to be up to 4 points in each direction.
  * *Sample location* specifies a single comma-separated element 'xi' coordinates, used with sampling mode *set location*.
  * *Density field* specifies a field giving the density for use with sampling mode *cell* poisson.

* **lines**

  Lines are used to visualize 1D elements, or the edges of 2D or 3D elements. They may be drawn as simple unshaded lines of fixed width, or rendered as surfaces with extruded shapes.

  Lines have the following **Line attributes**:

  * *Shape*: This drop down menu allows you to select the profile of the line: line, ribbon, circle extrusion or square extrusion, with the following only applying to non-line shapes:
  * *Base size*: This base lateral size of the cross section of the line shape, formatted as number*number.
  * *Scale field*: Optional field to scale lateral size of the cross section of the line shape.
  * *Scaling*: Real-valued multiplier on scale field, formatted as number*number.

* **contours**

  Contours show surfaces (with Domain ``mesh3d``) or lines (with Domain ``mesh2d``) at which the selected Scalar field has the chosen fixed values ("iso-values"), alternatively known as iso-surfaces and iso-lines.

  Contours have the following **Contour attributes**:

  * The *Scalar field* specifies the single-valued real field whose iso-values are to be rendered.
  * The *Range number*, if checked allows the number of isovalues to be specified across a range. If not checked a list of fixed values is specified.
  * The *Isovalues* contains a comma-separated list of iso-values to use, either 2 representing the minimum and maximum if a range is used (and values are sampled regularly between them) or a variable list of a range is not used.

* **surfaces**

  Surfaces are used to visualize 2D elements or the faces of 3D elements.

  Surfaces have no additional settings.

* **streamlines**

  Streamlines visualize the path a point follows if it tracks along a vector field over the domain, for example, the velocity in a fluid flow solution.

  Streamlines use both **Line attributes** and **Sampling attributes** defined earlier.

  Streamlines have the following **Streamline attributes**:

  * The *Vector field* specifies the field to track along, either a 3, 6 or 9 component vector fields for a 3 dimensional mesh. Streamlines align along their length according to the first vector of a vector field, and across their "width" (eg the width of the *ribbon* or *extruded square* line shape) to the second vector. For single vector (3 component) vector fields, the width direction of the shape rotates according to the curl of the vector field. Tip: Using a fibre field allows muscle fibre orientations to be viewed with ribbon or extruded square shape.
  * *Track length* specifies the distance the streamline is tracked along before finishing.
  * *Track direction* specifies forward or reverse tracking.
  * *Colour data* allows special colouring modes:
    * *field* uses the regular *Data field* sampled along its length, at the centre of the shape.
    * *magnitude* gives the magnitude of the vector in the primary direction.
    * *travel time* integrates the time/distance along the streamline to each point.

API
---

.. autoclass:: cmlibs.widgets.graphicseditorwidget.GraphicsEditorWidget
   :members: