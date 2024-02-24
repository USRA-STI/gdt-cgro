# CONTAINS TECHNICAL DATA/COMPUTER SOFTWARE DELIVERED TO THE U.S. GOVERNMENT 
# WITH UNLIMITED RIGHTS
#
# Grant No.: 80NSSC21K0651
# Grantee Name: Universities Space Research Association
# Grantee Address: 425 3rd Street SW, Suite 950, Washington DC 20024
#
# Copyright 2024 by Universities Space Research Association (USRA). All rights 
# reserved.
#
# Developed by: Adam Goldstein
#               Universities Space Research Association
#               Science and Technology Institute
#               https://sti.usra.edu
#
# This work is a derivative of the Gamma-ray Data Tools (GDT), including the 
# Core and Fermi packages, originally developed by the following:
#
#     William Cleveland and Adam Goldstein
#     Universities Space Research Association
#     Science and Technology Institute
#     https://sti.usra.edu
#     
#     Daniel Kocevski
#     National Aeronautics and Space Administration (NASA)
#     Marshall Space Flight Center
#     Astrophysics Branch (ST-12)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not 
# use this file except in compliance with the License. You may obtain a copy of 
# the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
# License for the specific language governing permissions and limitations under 
# the License.

import unittest
from gdt.missions.cgro.time import *

# trigger time from cont_bfits_3_105.fits
met1 = 8367.384765694444
utc_str1 = '1991-04-21 09:14:03.756'
trig_day1 = 1991.111
trig_tim1 = 33243.756

# trigger time from cont_bfits_4_5671.fits
met2 = 10403.683342326389
utc_str2 = '1996-11-16 16:24:00.777'
trig_day2 = 1996.321
trig_tim2 = 59040.777

# trigger time from cont_bfits_1_8121.fits
met3 = 11690.417751030092
utc_str3 = '2000-05-26 10:01:33.689'
trig_day3 = 2000.147
trig_tim3 = 36093.689

class TestTime():
    
    def test_to_utc(self):
        assert Time(met1, format='cgro').iso == utc_str1
        assert Time(met2, format='cgro').iso == utc_str2
        assert Time(met3, format='cgro').iso == utc_str3

    def test_to_cgro(self):
        assert Time(utc_str1, format='iso', scale='utc').cgro == met1
        assert Time(utc_str2, format='iso', scale='utc').cgro == met2
        assert Time(utc_str3, format='iso', scale='utc').cgro == met3
        
    def test_from_day_time(self):
        assert from_day_time(trig_day1, trig_tim1).cgro == met1
        assert from_day_time(trig_day2, trig_tim2).cgro == met2
        assert from_day_time(trig_day3, trig_tim3).cgro == met3
    
    def test_to_day_time(self):
        d1, t1 = to_day_time(Time(met1, format='cgro'))
        assert d1 == trig_day1
        assert t1 == trig_tim1
        
        d2, t2 = to_day_time(Time(met2, format='cgro'))
        assert d2 == trig_day2
        assert t2 == trig_tim2
        
        d3, t3 = to_day_time(Time(met3, format='cgro'))
        assert d3 == trig_day3
        assert t3 == trig_tim3
    
