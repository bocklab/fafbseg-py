FAFBseg tools
=============

``fafbseg`` is a set of Python tools to work with various kinds of segmentation
data in the "full adult fly brain" (FAFB) dataset:

1. `FlyWire <https://flywire.ai/>`_ by the Seung/Murthy labs in Princeton
2. `Google's auto-segmentation <https://fafb-dot-neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B4e-9%2C%22m%22%5D%2C%22y%22:%5B4e-9%2C%22m%22%5D%2C%22z%22:%5B4e-8%2C%22m%22%5D%7D%2C%22position%22:%5B123022.25%2C45724.984375%2C3412.796630859375%5D%2C%22crossSectionScale%22:1.2648787172897942%2C%22projectionOrientation%22:%5B0.0484076552093029%2C-0.029186638072133064%2C-0.02020242065191269%2C-0.9981967210769653%5D%2C%22projectionScale%22:171027.18606363493%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_clahe%22%2C%22name%22:%22fafb_v14_clahe%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22brainmaps://772153499790:fafb_v14:fafb-ffn1-20200412-rc4%22%2C%22tab%22:%22source%22%2C%22segments%22:%5B%22710435991%22%5D%2C%22name%22:%22fafb-ffn1-20200412-rc4%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%22precomputed://gs://fafb-ffn1-20190805/segmentation%22%2C%22segments%22:%5B%22710435991%22%5D%2C%22name%22:%22fafb-ffn1-20190805%22%7D%2C%7B%22type%22:%22annotation%22%2C%22source%22:%22precomputed://gs://neuroglancer-20191211_fafbv14_buhmann2019_li20190805%22%2C%22tab%22:%22rendering%22%2C%22annotationColor%22:%22#cecd11%22%2C%22shader%22:%22#uicontrol%20vec3%20preColor%20color%28default=%5C%22blue%5C%22%29%5Cn#uicontrol%20vec3%20postColor%20color%28default=%5C%22red%5C%22%29%5Cn#uicontrol%20float%20scorethr%20slider%28min=0%2C%20max=1000%29%5Cn#uicontrol%20int%20showautapse%20slider%28min=0%2C%20max=1%29%5Cn%5Cnvoid%20main%28%29%20%7B%5Cn%20%20setColor%28defaultColor%28%29%29%3B%5Cn%20%20setEndpointMarkerColor%28%5Cn%20%20%20%20vec4%28preColor%2C%200.5%29%2C%5Cn%20%20%20%20vec4%28postColor%2C%200.5%29%29%3B%5Cn%20%20setEndpointMarkerSize%285.0%2C%205.0%29%3B%5Cn%20%20setLineWidth%282.0%29%3B%5Cn%20%20if%20%28int%28prop_autapse%28%29%29%20%3E%20showautapse%29%20discard%3B%5Cn%20%20if%20%28prop_score%28%29%3Cscorethr%29%20discard%3B%5Cn%7D%5Cn%5Cn%22%2C%22shaderControls%22:%7B%22scorethr%22:80%7D%2C%22linkedSegmentationLayer%22:%7B%22pre_segment%22:%22fafb-ffn1-20190805%22%2C%22post_segment%22:%22fafb-ffn1-20190805%22%7D%2C%22filterBySegmentation%22:%5B%22post_segment%22%2C%22pre_segment%22%5D%2C%22name%22:%22synapses_buhmann2019%22%2C%22visible%22:false%7D%5D%2C%22showSlices%22:false%2C%22selectedLayer%22:%7B%22layer%22:%22fafb-ffn1-20200412-rc4%22%2C%22visible%22:true%7D%2C%22layout%22:%22xy-3d%22%7D>`_
3. `Buhmann et al. (2021) <https://www.nature.com/articles/s41592-021-01183-7>`_ synapse predictions

Check out the :ref:`introduction<introduction>` for a brief overview of the FAFB
dataset and the :ref:`tutorials<tutorials>` for code examples.


Features
--------
Here are just some of the things you can do with ``fafbseg``:

* map locations or supervoxels to segmentation IDs
* load neuron meshes and skeletons
* generate high quality neuron meshes and skeletons from scratch
* query connectivity and annotations
* parse and generate FlyWire neuroglancer URLs
* transform neurons from FAFB/FlyWire space to other brains spaces (e.g. hemibrain)

For a full list of features please see the :ref:`API documentation <api>`.


Analyses
--------
``fafbseg`` is built on top of `navis <http://navis.readthedocs.io>`_, a library
for general neuroanatomical analyses and visualisation. Objects (i.e. skeletons,
meshes, etc.) can be directly plugged into ``navis``' functions. This in turn
enables you among other things to:

* extract morphometrics (length, Strahler order, etc.)
* split neurons into axon and dendrites
* run morphological clustering/matching using NBLAST
* plot neurons in 2D and 3D
* import neurons into Blender 3D e.g. for making high quality renderings
* export to various file formats
* ...

See the `navis` `tutorials <https://navis.readthedocs.io/en/latest/source/gallery.html>`_
for examples.


How to cite
-----------
If you use ``fafbseg`` for your publication, please cite the two FlyWire papers
and the original FAFB dataset publication.

1. "*Whole-brain annotation and multi-connectome cell typing quantifies circuit stereotypy in Drosophila*" Schlegel *et al.*, bioRxiv (2023); https://doi.org/10.1101/2023.06.27.546055
2. "*Neuronal wiring diagram of an adult brain*" Dorkenwald *et al.*, bioRxiv (2023); https://doi.org/10.1101/2023.06.27.546656
3. "*A Complete Electron Microscopy Volume of the Brain of Adult Drosophila melanogaster*" Zheng *et al.*, Cell (2018); https://doi.org/10.1016/j.cell.2018.06.019

Questions/Issues?
-----------------
Open an `issue <https://github.com/navis-org/fafbseg-py/issues>`_ in ``fafbseg``'s
Github repository.


.. toctree::
   :hidden:
   :maxdepth: 2

   source/intro
   source/install
   source/gallery
   source/api


.. toctree::
   :caption: Development
   :hidden:

   GitHub Repository <https://github.com/navis-org/fafbseg-py>
