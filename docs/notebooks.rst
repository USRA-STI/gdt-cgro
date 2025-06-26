.. _notebooks:


Jupyter Notebook Tutorials
==========================
* :download:`Finding BATSE Data Tutorial <notebooks/Finding_BATSE_Data_Tutorial.ipynb.tar>`
  
  BATSE Data is hosted publicly on the HEASARC FTP server via the Fermi Science 
  Support Center and via Amazon Webservices (AWS), and is stored in a consistent 
  directory structure. Learn how to earch the HEASARC FTP server or AWS for trigger 
  data and continuous data, as well as how to search the BATSE catalogs.

----

* :download:`Exploring CGRO Times <notebooks/Exploring_CGRO_times.ipynb.tar>`

  This quick tutorial explores the CGRO/BATSE mission time system and how to convert 
  CGRO times to other time systems.  

----

* :download:`Exploring BATSE PHAII Data <notebooks/Exploring_BATSE_Phaii_Data.ipynb.tar>`
  
  PHAII data is one of the primary types of science data provided by BATSE, and 
  is temporally pre-binned. The two continuous types of PHAII data are CONT and DISCLA, 
  where CONT has 16 energy channels and DISCLA has 4 energy channels. These continusou
  data are stored in multi-detector PHAII files.Snippets of these data types are also
  provided for the time around triggers. These files are typically stored one per
  detector.Learn how to plot the lightcurves and count spectra of gamma-ray bursts 
  using CONT and DISCLA data. 

----

* :download:`Exploring BATSE TTE Data <notebooks/Exploring_BATSE_TTE_data.ipynb.tar>`
  
  TTE (Time-Tagged Event) data is one of the primary types of science data 
  provided by BATSE, and is temporally unbinned. Learn how to plot the lightcurves
  and count spectra of gamma-ray bursts using TTE data.

----

* :download:`Exploring BATSE Detector Responses <notebooks/Exploring_BATSE_detector_response_files.ipynb.tar>`
  
  Detector response files allow you to compare a theoretical photon spectrum to 
  an observed count spectrum. One file contains one or more detector response matrices,
  encoding the energy dispersion and calibration of incoming photons at different energies
  to to recodered energy channels. This matrix encodes the effective area of the detection
  as a function of energy for a given source posiion.Learn how to read, manipulate, and
  plot detector response matrices in files containing a single detctor or multiple
  detectors.

----

* :download:`Plotting_BATSE_trigger_lightcurves <notebooks/Plotting_BATSE_trigger_lightcurves.ipynb.tar>`
  
  BATSE has numerous trigger data types with several different time and energy
  resolutions. Trigger data files starting with s come from the smaller spectroscopy
  detectors while the rest of the files are from the LAD detectors. Learn to retrieve
  and plot data for the various trigger data types in this tutorial.

----
    
* :download:`BATSE Spectral fitting tutorial: single detector <notebooks/BATSE_Spectral_Analysis_Tutorial_single_detector.ipynb.tar>`
  
  Often, one would like to perform a spectral fit on BATSE data. The following 
  workflow will guide you through a simple example of this process. Learn how 
  to fit BATSE spectral data, generating a background fit, extracting a source 
  spectrum, and using the detector response to fit a model to the spectrum for a single
  detector.

----

* :download:`BATSE Spectral fitting tutorial multiple detectors <notebooks/BATSE_Spectral_fitting_Tutorial_multiple_detectors.ipynb.tar>`
  
  This tutorial builds on the BATSE single detector spectral analysis tutorial and
  demonstrates how a user can employ tools within the gdt-core package to combine data
  from multiple BATSE detectors into a single fit.

----

* :download:`BATSE Detector Definitions tutorial <notebooks/BATSE_Detector_Definitions.ipynb.tar>`
  
  BATSE had 16 detectors, 8 large area detectors (LADs) and 8 Spectroscopy Detectors (SDs).
  This brief tutorial demonstrates options for listing and referring to BATSE detectors.

----

* :download:`CGRO Spacecraft Frame tutorial <notebooks/CGRO_Spacecraft_frame.ipynb.tar>`
  
  This brief tutorial allows users to explore manually defining the CGRO spacecraft frame.
  This is done automatically when reading in CGRO data.

----

* :download:`BATSE FITS Headers tutorial <notebooks/BATSE_FITS_Headers.ipynb.tar>`
  
  This brief tutorial allows users to explore default values for BATSE FITS headers. These
  headers are automatically read in when using BATSE data.
