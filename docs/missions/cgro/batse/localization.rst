.. _batse-loc:

************************************************************************
BATSE Localization (:mod:`gdt.missions.cgro.batse.localization`)
************************************************************************
Currently this module contains the preferred localization systematic model
as estimated from the BATSE 4Br catalog.

This systematic can by applied to a :external:ref:`HealPixLocalization<core-healpix>`
object, which will convolve the model with the existing localization posterior.

>>> from gdt.core.healpix import HealPixLocalization
>>> from gdt.missions.cgro.batse.localization import batse_loc_systematic_4br
>>>
>>> # create a test HEALPix localization, Gaussian of 3 deg at RA, Dec = (20, 30)
>>> hpx1 = HealPixLocalization.from_gaussian(20, 30, 3.0)
>>> # convolve with BATSE systematic
>>> hpx2 = hpx1.convolve(batse_loc_systematic_4br)
>>> 
>>> # compare the 50% containment areas of the two localizations
>>> print(hpx1.area(0.5))
39.13206620797066
>>> print(hpx2.area(0.5))
65.46490432647101


Reference/API
=============

.. automodapi:: gdt.missions.cgro.batse.localization
   :inherited-members:

