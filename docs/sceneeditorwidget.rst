.. _Scene-Editor-Widget:

===================
Scene Editor Widget
===================

The **Scene Editor Widget** is a control to add, remove, and modify the graphics of a scene.

.. _fig-opencmiss-zincwidgets-scene-editor-widget:

.. figure:: _images/scene-editor-widget.png
   :alt: Scene editor widget.
   :width: 75%

   Scene editor widget.

Graphics list
-------------

Along the top of the scene editor window is a region selector that allows you to select the region of current scene.

Below the selector is the list of currently defined graphics.
The graphics list displays all the defined graphics in the current scene, each with a checkbox in front of it. 
This checkbox allows you to set whether to display this graphic.
This graphics list can also be reordered via drag and drop. Graphics at the top have higher display priority.
The name of the graph shows the graph type followed by the domain type and subgroup field, which can be changed in the settings editor below.

Below the list of graphics, there is a drop-down menu that allows you to add a new graphic, and a button to delete the selected existing graphic.


Settings editor
---------------
Below the graphics list is the settings editor where each graphical setting can be edited. 
When a graphical setting is selected from the list, all of its editable properties appear in this area. 
The range of editable properties will vary depending on the :ref:`type of graphics <types-of-graphics>` currently selected.