.. _batse-catalogs:

***********************************************************
BATSE Catalogs (:mod:`gdt.missions.cgro.batse.catalogs`)
***********************************************************


The HEASARC hosts several BATSE catalogs, including a Trigger Catalog that 
contains information about every BATSE trigger, a Burst Catalog that contains 
standard analysis of every triggered GRB, and spectroscopy catalogs. HEASARC 
provides a way to search these catalogs online through their Browse interface, 
but we offer a way to do it in Python through the Data Tools.

Let's look at the trigger catalog first:

    >>> from gdt.missions.cgro.batse.catalogs import BatseTriggerCatalog
    >>> trigcat = BatseTriggerCatalog()
    Sending request and awaiting response from HEASARC...
    Downloading batsetrigs from HEASARC via w3query.pl...
    Finished in 4 s
    >>> trigcat
    <BatseTriggerCatalog: 9 columns, 5372 rows>
    
Depending on your connection, initialization may take a few seconds. You can 
see what columns are available in the catalog:

    >>> print(trigcat.columns)
    ('OBSID', 'TRIGGER_ID', 'START_TIME', 'STOP_TIME', 'RA', 'DEC', 'TRIG_TYPE', 
    'BII', 'LII')

You can also return the range of values for a given column:

    >>> trigcat.column_range('TRIGGER_ID')
    ('00105', '08088')

If you only care about specific columns in the table, you can return a numpy 
record array with only those columns. Let's return a table with the trigger 
name and time for every trigger:

    >>> trigcat.get_table(columns=('TRIGGER_ID', 'START_TIME'))
    rec.array([('00105', '48367.3847801'), 
               ('00114', '48373.3787384'),
               ('00160', '48383.6050579'), ..., 
               ('03934', ' 50058.363285'),
               ('06985', ' 51035.774646'), 
               ('06986', ' 51036.281345')],
              dtype=[('TRIGGER_ID', '<U5'), ('START_TIME', '<U13')])

Importantly, we can make slices of the catalog based on conditionals. Let's 
only select triggers with positive declinations:

    >>> sliced_trigcat = trigcat.slice('DEC', lo=0.0, hi=90.0)
    >>> sliced_trigcat
    <BatseTriggerCatalog: 9 columns, 1870 rows>
    
    >>> sliced_trigcat.get_table(columns=('TRIGGER_ID', 'RA', 'DEC'))
    rec.array([('00105', 269.3  , 26.5  ), 
               ('00171', 340.2  , 39.6  ),
               ('00179', 266.5  , 57.2  ), ..., 
               ('02580', 301.862, 11.093),
               ('06985', 349.934, 24.645), 
               ('06986', 266.796,  3.509)],
              dtype=[('TRIGGER_ID', '<U5'), ('RA', '<f8'), ('DEC', '<f8')])
          
You can also slice on multiple conditionals, simultaneously. Select everything 
that has a positive declination *and* a is classified as a 'burst':

    >>> sliced_trigcat2 = trigcat.slices([('DEC', 0.0, 90.0), 
    >>>                                   ('TRIG_TYPE', 'burst', 'burst')])
    >>> sliced_trigcat2
    <BatseTriggerCatalog: 9 columns, 1254 rows>

    >>> sliced_trigcat2.get_table(columns=('trigger_name', 'trigger_time', 'error_radius'))
    rec.array([('00105', 'burst      ', 269.3  , 26.5  ),
               ('00171', 'burst      ', 340.2  , 39.6  ),
               ('00179', 'burst      ', 266.5  , 57.2  ), ...,
               ('02580', 'burst      ', 301.862, 11.093),
               ('06985', 'burst      ', 349.934, 24.645),
               ('06986', 'burst      ', 266.796,  3.509)],
              dtype=[('TRIGGER_ID', '<U5'), ('TRIG_TYPE', '<U11'), ('RA', '<f8'), ('DEC', '<f8')])

You'll notice in the table listing that there are multiple datatypes.

We can connect to the other catalogs in the same way. For example, here is the 
spectral catalog:

    >>> from gdt.missions.cgro.batse.catalogs import BatseSpectralCatalog
    >>> spec_cat = BatseSpectralCatalog()
    Sending request and awaiting response from HEASARC...
    Downloading bat5bgrbsp from HEASARC via w3query.pl...
    Finished in 21 s
    >>> spec_at
    <BatseSpectralCatalog: 185 columns, 2145 rows>

Again, this may take several seconds, largely because of how the HEASARC perl 
API works.

For more information on working with catalogs, see 
:external:ref:`The BrowseCatalog Class<core-heasarc-browse>`.

Reference/API
=============

.. automodapi:: gdt.missions.cgro.batse.catalogs
   :inherited-members:


