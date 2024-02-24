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
from gdt.missions.cgro.batse.catalogs import *


class TestBatseGrbCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseGrbCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 47)


class TestBatseGrb4bCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseGrb4bCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 47)


class TestBatseSpectralCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseSpectralCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 185)


class TestBatseBrightSpectralCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseBrightSpectralCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 31)


class TestBatseEarthOccultationCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseEarthOccultationCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 23)


class TestBatsePulsarCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatsePulsarCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 8)


class TestBatseTriggerCatalog(unittest.TestCase):
    
    def setUp(self):
        self.cat = BatseTriggerCatalog(cached=False)
    
    def test_num_cols(self):
        self.assertEqual(self.cat.num_cols, 9)


