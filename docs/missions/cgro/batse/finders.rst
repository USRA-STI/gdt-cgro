.. _batse-finders:
.. |BatseTriggerFtp| replace:: :class:`~gdt.missions.cgro.batse.finders.BatseTriggerFtp`
.. |BatseContinuousFtp| replace:: :class:`~gdt.missions.cgro.batse.finders.BatseContinuousFtp`

**************************************************************
BATSE Data Finders (:mod:`gdt.missions.cgro.batse.finders`)
**************************************************************
A natural question may be: "Where do I find the data I need?" Well, you're in 
luck, because this will show you how to find the data you seek. BATSE Data is 
hosted publicly at the High Energy Astrophysics Science Archive Research Center 
(HEASARC) on a FTP server. But instead of having to navigate a winding maze of 
FTP directories, we provide a couple of classes built to retrieve the data you 
want. First, you need to decide if you want trigger data (say, from a GRB) or 
continuous data. 

Finding Triggered BATSE Data
============================

Let's start with trigger data, and assume you know the trigger number you're 
interested in (6526):

    >>> from gdt.missions.cgro.batse.finders import BatseTriggerFtp
    >>> trig_finder = BatseTriggerFtp(6526)
    <BatseTriggerFtp: 06526>
    >>> trig_finder.num_files
    131

We don't really care about the directory structure, we just want the data. So 
this quickly gets us to the directory we need. There are 131 files associated 
with this trigger. Say we want CONT data. Is there CONT data available?

    >>> trig_finder.ls_cont()
    ['cont_bfits_4_6526.fits.gz',
     'cont_bfits_5_6526.fits.gz',
     'cont_bfits_6_6526.fits.gz',
     'cont_bfits_7_6526.fits.gz']

Great, there is CONT data available for four detectors. How about TTE data?


    >>> trig_finder.ls_tte()
    ['tte_bfits_6526.fits.gz']

What if we want to move on to another trigger? You don't have to create a new 
|BatseTriggerFTP| object, you can just used ``cd()``:

    >>> trig_finder.cd(105)
    >>> trig_finder
    <BatseTriggerFtp: 00105>
    >>> trig_finder.num_files
    113

Of course, you don't want to just list the files in a directory, you want to 
download them. Let's download the lightcurve image files:

    >>> trig_finder.get_lightcurves('.', verbose=True)
    105_4ch.gif ━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 21.8/21.8 kB • 6.1 MB/s • 0:00:00
    105_sum.gif ━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 13.2/13.2 kB • 76.7 MB/s • 0:00:00

Finding Continuous BATSE Data
=============================
Now we want some continuous data. There aren't any trigger numbers for 
continuous data. Continuous (CONT) and LAD discriminator (DISCLA) data are 
available in files that cover a whole day (relative to UTC). To find data, 
you need to create a |BatseContinuousFtp| object by specifying a time using Astropy 
Time:

    >>> from gdt.missions.cgro.batse.finders import BatseContinuousFtp
    >>> from gdt.missions.cgro.time import Time
    >>> time = Time('1995-09-23 12:00:00', scale='utc', format='iso')
    >>> cont_finder = BatseContinuousFtp(time)
    >>> cont_finder
    <BatseContinuousFtp: 1995-09-23 12:00:00.000>
    >>> cont_finder.num_files
    18

Let's list the CONT and DISCLA files that are available:

    >>> cont_finder.ls_cont()
    ['cont_09983.fits.gz']
    >>> cont_finder.ls_discla()
    ['discla_09983.fits.gz']


Similar to the trigger finder, you can use the same object to search at 
different times:

    >>> new_time = Time('1999-01-01 00:00:01', scale='utc', format='iso')
    >>> cont_finder.cd(new_time)
    >>> cont_finder
    <BatseContinuousFtp: 1999-01-01 00:00:01.000>

Now how about downloading the position history file for this time:

    >>> cont_finder.get_cont('.', verbose=True)
    cont_11179.fits.gz ━━━━━━━━━━━━━━━━━━━ 100.0% • 8.0/8.0 MB • 3.6 MB/s • 0:00:00


See :external:ref:`The FtpFinder Class<core-heasarc-finder>` for more details 
on using data finders.

Reference/API
=============

.. automodapi:: gdt.missions.cgro.batse.finders
   :inherited-members:


