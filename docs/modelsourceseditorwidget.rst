.. _Model-Sources-Editor-Widget:

===========================
Model Sources Editor Widget
===========================

The **Model Sources Editor Widget** is a control to add and remove source files.

.. _fig-cmlibs-widgets-model-sources-editor-widget:

.. figure:: _images/model-sources-editor-widget.png
   :alt: Model sources editor widget.
   :width: 75%

   Model sources editor widget.

Model Source Table
------------------

The Model Sources editor allows you to add the resources from a file into the visualization of the scaffold map. 
This editor lists all the available resources that have been provided to the step. 
You must load a file into a region, if the Add/Remove column contains a grey-colored plus icon this indicates 
that a region has not been assigned for the corresponding file resource.
 
You can use the Model Sources editor to load a file into a region. 
To assign a region to load a file into, first click inside the Region column cell and a Field chooser will appear from which you can choose an existing region.
When a region has been assigned to a field resource the Add icon changes from grey to green to signify that it is now enabled. 
If you click on the green-colored plus (Add) icon the file resource will be loaded into the assigned region. 
The red-colored minus (Remove) icon signifies that we have applied the file to the assigned region.
For the demonstration dataset we want to load the organ scaffold into the root region (/) and the embedded data into the data region (/data). Use the Model Sources editor to do this by assigning the appropriate region to each file resource and clicking the green-colored plus (Add) (for both file sources).

Note: Click the red-colored minus (Remove) icon to remove a file from the assigned region. 
But this operation is fraught with error and it is best not to use this functionality.

API
---

.. autoclass:: cmlibs.widgets.modelsourceseditorwidget.ModelSourcesEditorWidget
   :members:

.. autoclass:: cmlibs.widgets.modelsourceseditorwidget.ModelSourcesModel
   :members: