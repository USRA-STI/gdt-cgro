.. _batse-headers:

**************************************************************
BATSE FITS Headers (:mod:`gdt.missions.cgro.batse.headers`)
**************************************************************
This module defines all of the FITS headers for the public data files. While
these classes are not usually directly called by the user, we may load one up
and see the contents and default values.  For example, here is the set of 
header definitions for triggered PHAII files:

    >>> from gdt.missions.cgro.batse.headers import PhaiiTriggerHeaders
    >>> hdrs = PhaiiTriggerHeaders()
    >>> hdrs
    <PhaiiTriggerHeaders: 3 headers>
    
Here is the ``PRIMARY`` header and default values (retrieved by index):

    >>> hdrs[0]
    TELESCOP= 'COMPTON GRO'                                                         
    INSTRUME= 'BATSE   '                                                            
    ORIGIN  = 'MSFC    '           / Tape writing institution                       
    FILETYPE= ''                                                                    
    OBJECT  = ''                                                                    
    BATSE_TR=                    0 / BATSE trigger number                           
    OBSERVER= 'G. J. FISHMAN'      / Principal investigator (256) 544-7691          
    STRT-DAY=                  0.0 / YYYY.DDD at start of data                      
    STRT-TIM=                  0.0 / seconds of day at start of data                
    END-DAY =                  0.0 / YYYY.DDD at end of data                        
    END-TIM =                  0.0 / seconds of day at end of data                  
    TRIG-DAY=                  0.0 / YYYY.DDD at burst trigger                      
    TRIG-TIM=                  0.0 / seconds of day at burst trigger                
    EQUINOX =               2000.0 / J2000 coordinates                              
    SC-Z-RA =                  0.0 / Z axis RA in degrees                           
    SC-Z-DEC=                  0.0 / Z axis Dec in degrees                          
    SC-X-RA =                  0.0 / X axis RA in degrees                           
    SC-X-DEC=                  0.0 / X axis Dec in degrees                          
    OBJCTRA =                  0.0 / J2000 RA of source, degrees                    
    OBJCTDEC=                  0.0 / J2000 DEC of source, degrees                   
    SC-X-POS=                  0.0 / Spacecraft position at time of trigger (km)    
    SC-Y-POS=                  0.0                                                  
    SC-Z-POS=                  0.0                                                  
    SRCE-AZ =                  0.0 / Source Azimuth in GRO coords, degrees          
    SRCE-EL =                  0.0 / Source Elevation in GRO coords, degrees        
    GEOC-AZ =                  0.0 / Geocenter Azimuth in GRO coords, degrees       
    GEOC-EL =                  0.0 / Geocenter Elevation in GRO coords, degrees     
    FILE-ID = '' / Name of FITS file                                                
    FILE-VER= '' / Version of FITS file format                                      
    DATE    = '2024-01-31T19:10:14.909' / FITS file creation date (dd/mm/yy)        
    MNEMONIC= 'Gamma-ray Data Tools 2.0.2' / Program creating this file             
    PRIMTYPE= 'NONE    '           / No primary array                               
    COMMENT FITS (Flexible Image Transport System) format defined in Astronomy and  
    COMMENT Astrophysics Supplement Series v44/p363, v44/p371, v73/p359, v73/p365.  
    COMMENT Contact the NASA Science Office of Standards and Technology for the     
    COMMENT FITS Definition document #100 and other FITS information.               
    COMMENT This file contains BATSE time-sequenced spectral data                  

And here is the ``BATSE BURST SPECTRA`` header and default values:

    >>> hdrs['BATSE BURST SPECTRA']
    EXTNAME = 'BATSE BURST SPECTRA' / name of this binary table extension           
    DSELECT = '' / Detectors summed in order [76543210]                             
    LO_CHAN =                    0 / Lower channel                                  
    UP_CHAN =                    0 / Upper channel                                  
    RF_511  =                  0.0 / Resolution fraction at 511 keV (LADs)          
    R_EXP   =                  0.0 / Power-law exponent of resolution model (LADs)  
    DET_MODE= '' / LAD or SD Detectors                                              
    DATATYPE= '' / BATSE data types used                                            
    IS_SPEC =                    T / Set to T if RATES field is not empty           
    IS_ERROR=                    T / Set to T if ERRORS field is not empty          
    OVERFLW =                    F / Set to T if HER_COR or SHER_COR was used       
    LTIMECOR=                    T / Set to T if deadtime correction was used       
    BCKGSUBT=                    F / Set to T if background was subtracted          
    BSTACC  =                    0 / Packets in a burst readout (DISCSC,HERB,SHERB) 
    BASETIME=                  0.0 / Reference epoch, days past JD 2440000.5        
    NOTE    = 'Burst number:   {}'                                                  
    NOTE    = 'Detectors:  {}'                                                      
    NOTE    = 'Data types: {}'                                                      
    NOTE    = 'Start day:  {}'                                                      
    NOTE    = 'Start sec:  {}'                                                      
    NOTE    = 'Min. Resolution (s):   {}'                                           
    NOTE    = 'Creation time: {}'                                                   
    COMMENT Bad or missing data indicated by IEEE NAN in Rate errors.              

See :external:ref:`Data File Headers<core-headers>` for more information about 
creating and using FITS headers.
    
Reference/API
=============

.. automodapi:: gdt.missions.cgro.batse.headers
   :inherited-members:


