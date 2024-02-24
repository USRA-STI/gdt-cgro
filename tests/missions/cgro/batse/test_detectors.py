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

from gdt.missions.cgro.batse.detectors import *


class TestBatseDetectors(unittest.TestCase):
    
    def test_LAD0(self):
        det = BatseDetectors.LAD0
        assert det.full_name == 'LAD0'
        assert det.number == 0
        assert det.azimuth.value == 45.00
        assert det.zenith.value == 35.26

    def test_LAD1(self):
        det = BatseDetectors.LAD1
        assert det.full_name == 'LAD1'
        assert det.number == 1
        assert det.azimuth.value == 135.00
        assert det.zenith.value == 35.26

    def test_LAD2(self):
        det = BatseDetectors.LAD2
        assert det.full_name == 'LAD2'
        assert det.number == 2
        assert det.azimuth.value == 225.00
        assert det.zenith.value == 35.26

    def test_LAD3(self):
        det = BatseDetectors.LAD3
        assert det.full_name == 'LAD3'
        assert det.number == 3
        assert det.azimuth.value == 315.00
        assert det.zenith.value == 35.26

    def test_LAD4(self):
        det = BatseDetectors.LAD4
        assert det.full_name == 'LAD4'
        assert det.number == 4
        assert det.azimuth.value == 45.00
        assert det.zenith.value == 144.73

    def test_LAD5(self):
        det = BatseDetectors.LAD5
        assert det.full_name == 'LAD5'
        assert det.number == 5
        assert det.azimuth.value == 135.00
        assert det.zenith.value == 144.73

    def test_LAD6(self):
        det = BatseDetectors.LAD6
        assert det.full_name == 'LAD6'
        assert det.number == 6
        assert det.azimuth.value == 225.00
        assert det.zenith.value == 144.73

    def test_LAD7(self):
        det = BatseDetectors.LAD7
        assert det.full_name == 'LAD7'
        assert det.number == 7
        assert det.azimuth.value == 315.00
        assert det.zenith.value == 144.73

    def test_SD0(self):
        det = BatseDetectors.SD0
        assert det.full_name == 'SD0'
        assert det.number == 8
        assert det.azimuth.value == 45.00
        assert det.zenith.value == 54.26

    def test_SD1(self):
        det = BatseDetectors.SD1
        assert det.full_name == 'SD1'
        assert det.number == 9
        assert det.azimuth.value == 135.00
        assert det.zenith.value == 54.26

    def test_SD2(self):
        det = BatseDetectors.SD2
        assert det.full_name == 'SD2'
        assert det.number == 10
        assert det.azimuth.value == 225.00
        assert det.zenith.value == 54.26

    def test_SD3(self):
        det = BatseDetectors.SD3
        assert det.full_name == 'SD3'
        assert det.number == 11
        assert det.azimuth.value == 315.00
        assert det.zenith.value == 54.26

    def test_SD4(self):
        det = BatseDetectors.SD4
        assert det.full_name == 'SD4'
        assert det.number == 12
        assert det.azimuth.value == 45.00
        assert det.zenith.value == 125.73

    def test_SD5(self):
        det = BatseDetectors.SD5
        assert det.full_name == 'SD5'
        assert det.number == 13
        assert det.azimuth.value == 135.00
        assert det.zenith.value == 125.73

    def test_SD6(self):
        det = BatseDetectors.SD6
        assert det.full_name == 'SD6'
        assert det.number == 14
        assert det.azimuth.value == 225.00
        assert det.zenith.value == 125.73

    def test_SD7(self):
        det = BatseDetectors.SD7
        assert det.full_name == 'SD7'
        assert det.number == 15
        assert det.azimuth.value == 315.00
        assert det.zenith.value == 125.73
    
    def test_all_lads(self):
        lads = [det.name for det in BatseDetectors.all_lads()]
        self.assertListEqual(lads, ['LAD0', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 
                                    'LAD5', 'LAD6', 'LAD7'])

    def test_all_sds(self):
        sds = [det.name for det in BatseDetectors.all_sds()]
        self.assertListEqual(sds, ['SD0', 'SD1', 'SD2', 'SD3', 'SD4', 
                                   'SD5', 'SD6', 'SD7'])
      
    def test_is_lad(self):
        assert BatseDetectors.LAD0.is_lad() == True
        assert BatseDetectors.SD0.is_lad() == False

    def test_is_sd(self):
        assert BatseDetectors.LAD0.is_sd() == False
        assert BatseDetectors.SD0.is_sd() == True
    
