.. _gdt-cgro:

**********************************************************
Welcome to the Compton Gamma-ray Data Tools Documentation!
**********************************************************

The Compton Gamma-ray Data Tools is a toolkit for Compton data, primarily 
from the BATSE instrument, built on the 
:external:ref:`GDT Core Package<gdt-core>`.

.. figure:: https://astrobiology.nasa.gov/uploads/filer_public_thumbnails/filer_public/41/39/41395c7e-fd8a-49a6-855e-e13cd2509151/compton_flies_free_sts037-96-009.jpg__1240x510_q85_crop_subject_location-620%2C254_subsampling-2.jpg

The Compton Gamma-Ray Observatory (CGRO) was deployed from Space Shuttle 
Atlantis on April 5, 1991 and was de-orbited on June 4, 2000. CGRO contained
four instruments: the Burst and Transient Source Experiment (BATSE), the 
Oriented Scintillation Spectrometer Experiment (OSSE), Imaging Compton Telescope 
(COMPTEL), and the Energetic Gamma Ray Experiment Telescope (EGRET).  These
data tools primarily address BATSE data but also contain functionality to 
determine orbit and pointing of the CGRO spacecraft as well as the time 
conversions to/from the CGRO mission epoch.

.. figure:: https://astrobiology.nasa.gov/uploads/filer_public_thumbnails/filer_public/c7/e9/c7e957ae-c91c-4594-867e-8b3a62c5d8f7/gro_cutaway_labels_1080.jpg__930x580_q85_crop_subsampling-2.jpg

.. rubric:: Citing

If you use the Compton Gamma-ray Data Tools in your research and publications, 
we would definitely appreciate an appropriate acknowledgment and citation! We 
suggest including the following BibTex entries:

::

 @misc{GDT-CGRO,
       author = {Adam Goldstein},
       title = {CGRO Gamma-ray Data Tools: v1.0.0},
       year = 2024,
       url = {https://github.com/USRA-STI/gdt-cgro}
 }

 @misc{GDT-CORE,
       author = {Adam Goldstein and William H. Cleveland and Daniel Kocevski},
       title = {Gamma-ray Data Tools Core: v2.0.1},
       year = 2024,
       url = {https://github.com/USRA-STI/gdt-core}
 }
  

.. rubric:: Acknowledgments

The creation of the Compton Gamma-ray Data Tools were funded by the NASA's
Astrophysics Data Analysis Program (ADAP) via grant number 80NSSC21K0651.


***************
Getting Started
***************
.. toctree::
   :maxdepth: 1

   install

******************
User Documentation
******************

CGRO Definitions
=================
.. toctree::
   :maxdepth: 1

   missions/cgro/time
   missions/cgro/frame

BATSE
=====

Instrument Definitions
----------------------

.. toctree::
   :maxdepth: 1

   missions/cgro/batse/detectors
   missions/cgro/batse/headers

Data Types
----------

.. toctree::
   :maxdepth: 1

   missions/cgro/batse/gallery
   missions/cgro/batse/phaii
   missions/cgro/batse/tte
   missions/cgro/batse/response

Data Finders and Catalogs
-------------------------

.. toctree::
   :maxdepth: 1

   missions/cgro/batse/finders
   missions/cgro/batse/catalogs

----

*******
License
*******
.. toctree::
   :maxdepth: 1
   
   license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. figure:: https://astrobiology.nasa.gov/uploads/filer_public_thumbnails/filer_public/26/ad/26adba29-eb29-4197-98fd-24779ff3cd9a/jay_apt_sts-37_eva_gro_040791_sts037-51-021.jpg__930x580_q85_crop_subject_location-465%2C290_subsampling-2.jpg
