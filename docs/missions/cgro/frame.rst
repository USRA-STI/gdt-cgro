.. _cgro-frame:
.. |CgroFrame| replace:: :class:`~gdt.missions.cgro.frame.CgroFrame`
.. |Quaternion| replace:: :class:`~gdt.core.coords.Quaternion`
.. |BatsePhaiiMulti| replace:: :class:`~gdt.missions.cgro.batse.phaii.BatsePhaiiMulti`
.. |SpacecraftAxes| replace:: :class:`~gdt.core.coords.SpacecraftAxes`

******************************************************
CGRO Spacecraft Frame (:mod:`gdt.missions.cgro.frame`)
******************************************************

The CGRO spacecraft frame, |CgroFrame|, is the frame that is aligned
with the CGRO spacecraft coordinate frame, and is represented by a 
quaternion that defines the rotation from spacecraft coordinates to the ICRS
coordinate frame.  This frame takes advantage of the Astropy coordinate frame
design, so we can use the FermiFrame to convert Astropy SkyCoord objects 
between the CGRO Frame and any celestial frame.

Manually Initializing a Frame
=============================
While the |CgroFrame| is typically initialized when reading from a continuous
data file, such as a CONT or DISCLA file (see |BatsePhaiiMulti|) instead of 
manually by a user, we can manually define the frame as follows.

Since the CGRO spacecraft frame is not natively specified by a quaternion, but
instead the pointing of the X and Z spacecraft axes in the ICRS frame, we must 
specify those pointings, and the |CgroFrame| will perform the conversion into a 
quaternion.  First, we specify the axes pointings using Astropy SkyCoord:

    >>> from astropy.coordinates import SkyCoord
    >>> x_pointing = SkyCoord(19.090958, 8.04433, unit='deg')
    >>> z_pointing = SkyCoord(108.162994, -6.5431795, unit='deg')
    
Next, we create a |SpacecraftAxes| object that will enable the conversion to 
quaternions:
    
    >>> from gdt.core.coords import SpacecraftAxes
    >>> axes = SpacecraftAxes(x_pointing=x_pointing, z_pointing=z_pointing)
    >>> axes
    <SpacecraftAxes>
    X axis: RA 19.090958, Dec 8.04433
    Z axis: RA 108.162994, Dec -6.5431795

Finally, we initialize a |CgroFrame| with the |SpacecraftAxes| object:
    
    >>> from gdt.missions.cgro.frame import *
    >>> cgro_frame = CgroFrame(axes=axes)
    >>> cgro_frame
    <CgroFrame: 1 frames;
     obstime=[J2000.000]
     obsgeoloc=[(0., 0., 0.) m]
     obsgeovel=[(0., 0., 0.) m / s]
     quaternion=[(x, y, z, w) [[-0.72679576, -0.16954026,  0.05838548,  0.66303481]]]>

Notice that we can also define the frame with an ``obstime``, which is useful
for transforming between the |CgroFrame| and a non-inertial time-dependent frame; 
an ``obsgeoloc``, which can define the spacecraft location in orbit; and
``obsgeovel``, which defines the spacecraft orbital velocity.

Now let us define a SkyCoord of some object of interest in RA and Dec:

    >>> coord = SkyCoord(100.0, -30.0, unit='deg')
    
And we can simply rotate this into the CGRO frame with the following:
    
    >>> cgro_coord = coord.transform_to(cgro_frame)
    >>> (cgro_coord.az, cgro_coord.el)
    (<Longitude [80.97197099] deg>, <Latitude [65.318497] deg>)

We can also transform from the CGRO frame to other frames.  For example, we
define a coordinate in the CGRO frame this way:

    >>> cgro_coord = SkyCoord(50.0, 25.0, frame=cgro_frame[0], unit='deg')
    
Now we can tranform to ICRS coordinates:

    >>> cgro_coord.icrs
    <SkyCoord (ICRS): (ra, dec) in deg
        [(45.64562925, -40.50375436)]>

or Galactic coordinates:

    >>> cgro_coord.galactic
    <SkyCoord (Galactic): (l, b) in deg
        [(247.76916678, -59.8909959)]>
        
or any other coordinate frames provided by Astropy.

Reading a CGRO Frame from a file
================================
BATSE continuous data files contain, in addition to science data, the spacecraft
position and pointing history for the duration of the file.  This information
can be accessed by opening one of these files and extracting the spacecraft 
frame information.  For example:

    >>> from gdt.core import data_path
    >>> from gdt.missions.cgro.batse.phaii import BatsePhaii
    >>> filepath = data_path / 'cgro-batse' / 'cont_08362.fits.gz'
    >>> phaii_multi = BatsePhaii.open(filepath)
    >>> phaii_multi
    <BatsePhaiiMulti: 8 detectors>

While this is a PHAII file containing data from multiple detectors (see 
:ref:`BATSE PHAII data<batse-phaii>`), we can extract the spacecraft frame in
the following way:

    >>> sc_frame = phaii_multi.get_spacecraft_frame()
    <CgroFrame: 4485 frames;
     obstime=[8362.557352358903, ...]
     obsgeoloc=[(-6225507.5, -1948474., 1982118.6) m, ...]
     quaternion=[(x, y, z, w) [-0.72679577, -0.16954023,  0.05838548,  0.66303481], ...]>

Notice that this |CgroFrame| object contains 4485 different frames, each defined
at a particular ``obstime``.  This set of frames can be used in all of the 
examples above.  For example, we can convert our sky coordinate in ICRS to 
the CGRO frame for each frame in our set:

    >>> coord.transform_to(sc_frame).az
    <Longitude [80.97197307, 80.97197307, 80.97197307, ..., 81.18042599,
                81.18042599, 81.18042599] deg>
    >>> coord.transform_to(sc_frame).el
    <Latitude [65.31849764, 65.31849764, 65.31849764, ..., 65.33970109,
               65.33970109, 65.33970109] deg>

We can also retrieve the spacecraft location in orbit relative to the geocenter:

    >>> # latitude
    >>> sc_frame.earth_location.lat
    <Latitude [ 17.04653897,  17.09930368,  17.15127236, ..., -17.69539073,
               -17.6445087 , -17.59379511] deg>
    >>> # longitude
    >>> sc_frame.earth_location.lon
    <Longitude [152.43654264, 152.5548671 , 152.67359296, ..., -79.55513331,
                -79.43726847, -79.3188411 ] deg>
    >>> # altitude
    >>> sc_frame.earth_location.height
    <Quantity [441479.46545959, 441596.96456853, 441599.6645819 , ...,
               451512.55025588, 451510.48598044, 451444.92918256] m>

We can also extract a single frame or slice multiple frames:

    >>> sc_frame[100]
    <CgroFrame: 1 frames;
     obstime=[8362.623936062606]
     obsgeoloc=[(-5727814., -2828583.5, 2380704.8) m]
     obsgeovel=[(0., 0., 0.) m / s]
     quaternion=[(x, y, z, w) [-0.72643957, -0.16960178,  0.05835929,  0.66341163]]>

    >>> sc_frame[100:110]
    <CgroFrame: 10 frames;
     obstime=[8362.623936062606, ...]
     obsgeoloc=[(-5727814., -2828583.5, 2380704.8) m, ...]
     quaternion=[(x, y, z, w) [-0.72643957, -0.16960178,  0.05835929,  0.66341163], ...]>

For more details about working with spacecraft frames, see 
:external:ref:`Spacecraft Attitude, Position, and Coordinates<core-coords>`.


Reference/API
=============

.. automodapi:: gdt.missions.cgro.frame
   :inherited-members:


