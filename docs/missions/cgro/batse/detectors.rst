.. _batse-detectors:
.. |BatseDetectors| replace:: :class:`~gdt.missions.cgro.batse.detectors.BatseDetectors`
.. |Detectors| replace:: :class:`~gdt.core.detector.Detectors`

************************************************************************
BATSE Detector Definitions (:mod:`gdt.missions.cgro.batse.detectors`)
************************************************************************
The |BatseDetectors| class contains the naming and orientation definitions of the
BATSE Large Area Detectors (LADs) and Spectroscopy Detectors (SDs).

The BATSE detectors have both an indexing and naming convention, with the 
naming convention being "LAD0," "LAD1," etc. and "SD0," "SD1," etc.

We can easily retrieve a detector definition by using standard "dot" notation:

    >>> from gdt.missions.cgro.batse.detectors import BatseDetectors
    >>> BatseDetectors.LAD0
    <BatseDetectors: LAD0>

We can retrieve the string name of the detector:

    >>> BatseDetectors.SD7.name
    'SD7'

There is also a standard detector indexing scheme that is used for all BATSE 
detectors:

    >>> BatseDetectors.LAD3.number
    3

Since the |BatseDetectors| class inherits from the |Detectors| base class, we 
can also retrieve the pointing information of a BATSE detector:

    >>> # detector azimuth, zenith
    >>> BatseDetectors.from_str('LAD2').pointing()
    (<Quantity 225. deg>, <Quantity 35.26 deg>)
    
    >>> # detector elevation
    BatseDetectors.SD5.elevation
    <Quantity -35.73 deg>

We can also iterate over all BATSE detectors:
    
    >>> # the list of detector names
    >>> print([det.name for det in BatseDetectors])
    ['LAD0', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', 'LAD7', 'SD0', 
     'SD1', 'SD2', 'SD3', 'SD4', 'SD5', 'SD6', 'SD7']

And we can get the list of LAD (or SD) detectors:

    >>> BatseDetectors.all_lads()
    [<BatseDetectors: LAD0>, <BatseDetectors: LAD1>, <BatseDetectors: LAD2>,
     <BatseDetectors: LAD3>, <BatseDetectors: LAD4>, <BatseDetectors: LAD5>,
     <BatseDetectors: LAD6>, <BatseDetectors: LAD7>]]

And we can test if a particular detector is a LAD or SD detector:

    >>> print([det.is_sd() for det in BatseDetectors])
    [False, False, False, False, False, False, False, False, True, True, True, 
     True, True, True, True, True]


Reference/API
=============

.. automodapi:: gdt.missions.cgro.batse.detectors
   :inherited-members:

