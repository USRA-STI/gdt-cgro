.. _cgro-time:

.. |from_day_time()| replace:: :class:`~gdt.missions.cgro.time.from_day_time`
.. |to_day_time()| replace:: :class:`~gdt.missions.cgro.time.to_day_time`
*****************************************************
CGRO Mission Epoch  (:mod:`gdt.missions.cgro.time`)
*****************************************************

The CGRO Mission time is typically expressed as the Truncated Julian Date (TJD),
which has an epoch of May 24, 1968 00:00:00 UTC. We have defined a specialized 
epoch to work with Astropy ``Time`` objects so that the CGRO mission time can be 
easily converted to/from other formats and time scales.

To use this, we simply import and create an astropy Time object with a `'cgro'`
format:

    >>> from gdt.missions.cgro.time import Time
    >>> cgro_met = Time(9983.5, format='cgro')
    >>> cgro_met
    <Time object: scale='utc' format='cgro' value=9983.5>
    
Now, say we want to retrieve the GPS timestamp:

    >>> cgro_met.gps
    495892810.0

The Astropy ``Time`` object readily converts it for us. We can also do the 
reverse conversion:

    >>> gps_time = Time(cgro_met.gps, format='gps')
    >>> gps_time
    <Time object: scale='tai' format='gps' value=495892810.0>
    
    >>> gps_time.cgro
    9983.5

And we should, of course, get back the CGRO mission time we started with.  
This enables you do do any time conversions already provided by Astropy, as 
well as time conversions between other missions within the GDT.

In addition to time conversions, all time formatting available in Astropy is 
also available here.  For example, we can format the CGRO mission time in ISO 
format:

    >>> cgro_met.iso
    '1995-09-23 12:00:00.000'

Additionally, there are some time utilities available to convert date/time 
formats found within BATSE files into the CGRO mission time standard.  BATSE
data files often have time definitions that are formatted as two numbers:
a float whose integer is the year and fractional part is the day of the year; 
and another float that represents the number of seconds from the start of the 
UTC day.  We can convert this representation into a ``Time`` object by using
the |from_day_time()| function:
    
    >>> from gdt.missions.cgro.time import from_day_time
    >>> batse_time = from_day_time(1995.266, 43200.0)
    >>> batse_time
    <Time object: scale='utc' format='datetime' value=1995-09-23 12:00:00>
    >>> batse_time.cgro
    9983.5

And by using the |to_day_time()| utility, we can convert a ``Time`` object into
the BATSE format:

    >>> from gdt.missions.cgro.time import to_day_time
    >>> batse_day, batse_secs = to_day_time(batse_time)
    >>> batse_day, batse_secs
    (1995.266, 43200.0)

    
Reference/API
=============

.. automodapi:: gdt.missions.cgro.time
   :inherited-members:


