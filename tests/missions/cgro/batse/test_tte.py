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

import os
import unittest
from tempfile import TemporaryDirectory
from gdt.core import data_path
from gdt.core.binning.binned import combine_by_factor
from gdt.core.binning.unbinned import bin_by_time
from gdt.missions.cgro.batse.detectors import BatseDetectors
from gdt.missions.cgro.batse.tte import *

tte_file = data_path / 'cgro-batse/tte_list_105.fits.gz'

@unittest.skipIf(not tte_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatseTteMulti(unittest.TestCase):
    
    def setUp(self):
        self.tte_collection = BatseTte.open(tte_file)
        self.trigtime = 8367.384765717592
    
    def test_detectors(self):
        assert self.tte_collection.detectors == list(range(8))

    def test_filename(self):
        assert self.tte_collection.filename == tte_file.name

    def test_headers(self):
        assert self.tte_collection.headers.num_headers == 3

    def test_num_dets(self):
        assert self.tte_collection.num_dets == 8
        
    def test_get_detector(self):
        # get by detector number
        tte0 = self.tte_collection.get_detector(0)
        assert tte0.detector.name == 'LAD0'

        # get by detector name
        tte1 = self.tte_collection.get_detector('LAD1')
        assert tte1.detector.name == 'LAD1'

        # get by detector object
        det = BatseDetectors.LAD2
        tte2 = self.tte_collection.get_detector(det)
        assert tte2.detector.name == 'LAD2'

        # incorrect input
        with self.assertRaises(TypeError):
            self.tte_collection.get_detector(0.0)

    def test_sum_detectors(self):
        tte0 = self.tte_collection.get_detector(0)
        tte1 = self.tte_collection.get_detector(1)
        
        tte_sum = self.tte_collection.sum_detectors([0,1])
        assert len(tte_sum.detector) == 2
        assert tte_sum.detector[0].number == 0
        assert tte_sum.detector[1].number == 1

        assert tte_sum.data.size == tte0.data.size + tte1.data.size
        for evt in tte_sum.data.times:
            assert (evt in tte0.data.times) or (evt in tte1.data.times)


@unittest.skipIf(not tte_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatseTte(unittest.TestCase):
    
    def setUp(self):
        self.tte = BatseTte.open(tte_file).get_detector(5)
    
    def test_detector(self):
        assert self.tte.detector.name == 'LAD5'
    
    def test_energy_range(self):
        self.assertAlmostEqual(self.tte.energy_range[0], 24.494627, places=6)
        self.assertAlmostEqual(self.tte.energy_range[1], 100000.0, places=6)

    def test_event_deadtime(self):
        self.assertEqual(self.tte.event_deadtime, 3.3e-6)

    def test_filename(self):
        assert self.tte.filename == 'tte_list_5_105.fits.gz'
    
    def test_headers(self):
        assert self.tte.headers.num_headers == 3
    
    def test_num_chans(self):
        assert self.tte.num_chans == 4
    
    def test_overflow_deadtime(self):
        assert self.tte.overflow_deadtime == 3.3e-6
    
    def test_time_range(self):
        t0, t1 = self.tte.time_range
        self.assertAlmostEqual(t0, -0.17732711)
        self.assertAlmostEqual(t1, 1.403729)
            
    def test_trigtime(self):
        self.assertAlmostEqual(self.tte.trigtime, 8367.384765694444)     
    
    def test_rebin_energy(self):
        tte2 = self.tte.rebin_energy(combine_by_factor, 2)
        assert tte2.num_chans == self.tte.num_chans // 2
    
    def test_to_phaii(self):
        phaii = self.tte.to_phaii(bin_by_time, 0.016)
        assert phaii.data.num_times == 99
        assert phaii.detector == self.tte.detector
        assert phaii.headers[0]['FILETYPE'] == 'PHAII'
        assert phaii.headers[0]['STRT-DAY'] == self.tte.headers[0]['STRT-DAY']
        assert phaii.headers[0]['STRT-TIM'] == self.tte.headers[0]['STRT-TIM']
        assert phaii.headers[0]['END-DAY'] == self.tte.headers[0]['END-DAY']
        assert phaii.headers[0]['END-TIM'] == self.tte.headers[0]['END-TIM']
        assert phaii.headers[0]['TRIG-DAY'] == self.tte.headers[0]['TRIG-DAY']
        assert phaii.headers[0]['TRIG-TIM'] == self.tte.headers[0]['TRIG-TIM']
        assert phaii.headers[0]['OBJECT'] == self.tte.headers[0]['OBJECT']
        assert phaii.headers[0]['OBJCTRA'] == self.tte.headers[0]['OBJCTRA']
        assert phaii.headers[0]['OBJCTDEC'] == self.tte.headers[0]['OBJCTDEC']
        
    def test_slice_energy(self):
        tte2 = self.tte.slice_energy((50.0, 300.0))
        emin, emax = tte2.energy_range
        self.assertAlmostEqual(emin, 24.494627, places=5)
        self.assertAlmostEqual(emax, 317.48706, places=5)
        assert tte2.detector == self.tte.detector
        
    def test_slice_time(self):
        tte2 = self.tte.slice_time((0.0, 0.03))
        t0, t1 = tte2.time_range
        self.assertAlmostEqual(t0, 7.287863991223276e-05, places=6)
        self.assertAlmostEqual(t1, 0.029956873506307602, places=6)
        assert tte2.detector == self.tte.detector
        
    def test_to_pha(self):
        pha = self.tte.to_pha()
        assert pha.num_chans == self.tte.num_chans

    def test_to_spectrum(self):
        spec = self.tte.to_spectrum()
        assert spec.size == self.tte.num_chans


