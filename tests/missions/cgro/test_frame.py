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
from astropy.coordinates import SkyCoord
import astropy.coordinates.representation as r
from gdt.core.coords import SpacecraftAxes
from gdt.missions.cgro.frame import *
from gdt.missions.cgro.time import Time
from gdt.missions.cgro.batse.detectors import BatseDetectors

# taken from the first position/attitude sample in cont_08362.fits
x_pointing = SkyCoord(19.090958, 8.04433, unit='deg')
z_pointing = SkyCoord(108.162994, -6.5431795, unit='deg')
time = 8362.55735236
geoloc = r.CartesianRepresentation(x=-6225.5073, y=-1948.474, z=1982.1187, unit='km')
geo_az = 24.978275
geo_el = 1.1531982421875 # this is 90-GEO_EL in the file, because actually 
                         # records the zenith but erroneously calls it elevation


class TestCgroFrame(unittest.TestCase):
    
    def setUp(self):
        axes = SpacecraftAxes(x_pointing=x_pointing, z_pointing=z_pointing)
        self.frame = CgroFrame(axes=axes, obstime=Time(time, format='cgro'),
                               obsgeoloc=geoloc, detectors=BatseDetectors)
    
    def test_to_cgro_frame(self):
        # z-axis should be at zen=0 (el=90)
        zaxis = z_pointing.transform_to(self.frame)
        self.assertAlmostEqual(zaxis.el.value[0], 90.0, places=2)
        # x-axis should be at az=0, zen=90 (el=0)        
        xaxis = x_pointing.transform_to(self.frame)
        self.assertAlmostEqual(xaxis.az.value[0], 0.0, places=2)
        self.assertAlmostEqual(xaxis.el.value[0], 0.0, places=2)

    def test_to_icrs_frame(self):
        z_coord = SkyCoord(0.0, 90.0, unit='deg', frame=self.frame[0]).icrs
        self.assertAlmostEqual(z_coord.ra.value[0], z_pointing.ra.value, places=2)
        self.assertAlmostEqual(z_coord.dec.value[0], z_pointing.dec.value, places=2)

        x_coord = SkyCoord(0.0, 0.0, unit='deg', frame=self.frame[0]).icrs
        self.assertAlmostEqual(x_coord.ra.value[0], x_pointing.ra.value, places=2)
        self.assertAlmostEqual(x_coord.dec.value[0], x_pointing.dec.value, places=2)
    
    def test_geocenter(self):
        geo_icrs = SkyCoord(self.frame.geocenter.ra, self.frame.geocenter.dec, 
                            frame='gcrs').icrs
        geo_cgro = geo_icrs.transform_to(self.frame[0])
        self.assertAlmostEqual(geo_cgro.az.value[0], geo_az, places=2)
        self.assertAlmostEqual(geo_cgro.el.value[0], geo_el, places=2)
    
    def test_detectors(self):
        self.assertTrue(isinstance(self.frame.detectors.LAD0, BatseDetectors))
    