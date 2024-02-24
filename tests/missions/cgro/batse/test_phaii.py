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
import numpy as np
from tempfile import TemporaryDirectory
from gdt.core import data_path
from gdt.missions.cgro.frame import *
from gdt.missions.cgro.batse.detectors import BatseDetectors
from gdt.missions.cgro.batse.phaii import *
from gdt.core.binning.binned import combine_by_factor

cont_file = data_path / 'cgro-batse/cont_08362.fits.gz'
discla_file = data_path / 'cgro-batse/discla_08362.fits.gz'
trigger_file = data_path / 'cgro-batse/cont_bfits_3_105.fits.gz'

@unittest.skipIf(not cont_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatsePhaiiCont(unittest.TestCase):
    
    def setUp(self):
        self.phaii_collection = BatsePhaii.open(cont_file)
    
    def test_detectors(self):
        assert self.phaii_collection.detectors == list(range(8))
    
    def test_filename(self):
        assert self.phaii_collection.filename == cont_file.name
    
    def test_headers(self):
        assert self.phaii_collection.headers.num_headers == 3

    def test_num_dets(self):
        assert self.phaii_collection.num_dets == 8

    def test_get_detector(self):
        # from number
        phaii = self.phaii_collection.get_detector(0)
        assert phaii.detector.number == 0
        
        # from string
        phaii = self.phaii_collection.get_detector('LAD1')
        assert phaii.detector.number == 1

        # from object
        det = BatseDetectors.from_str('LAD2')
        phaii = self.phaii_collection.get_detector(det)
        assert phaii.detector.number == 2
        
        # incorrect input
        with self.assertRaises(TypeError):
            self.phaii_collection.get_detector(0.0)

    def test_sum_detectors(self):
    
        # sum all by default
        phaii_sum = self.phaii_collection.sum_detectors()
        assert len(phaii_sum.detector) == 8
        for i in range(8):
            assert phaii_sum.detector[i].number == i
        
        phaii_sum = self.phaii_collection.sum_detectors([0,1])
        assert len(phaii_sum.detector) == 2
        assert phaii_sum.detector[0].number == 0
        assert phaii_sum.detector[1].number == 1
        
        phaii0 = self.phaii_collection.get_detector(0)
        phaii1 = self.phaii_collection.get_detector(1)
        
        counts0 = phaii0.data.counts.flatten()
        counts1 = phaii1.data.counts.flatten()
        for i, bin in enumerate(phaii_sum.data.counts.flatten()):
            assert bin == counts0[i] + counts1[i]
        
        expo0 = phaii0.data.exposure.flatten()
        expo1 = phaii1.data.exposure.flatten()
        for i, bin in enumerate(phaii_sum.data.exposure.flatten()):
            assert bin == (expo0[i] + expo1[i]) / 2
                
    def test_get_spacecraft_frame(self):
        frame = self.phaii_collection.get_spacecraft_frame()
        assert isinstance(frame, CgroFrame)
        assert frame.shape == (4485,)
        assert frame.obstime[0].cgro == 8362.557352358903
        assert frame.obstime[-1].cgro == 8362.997601247791
        
        test_vals = [-6225.5073, -1948.474, 1982.1187]
        vals = frame.obsgeoloc[0].xyz.value
        for i in range(3):
            self.assertAlmostEqual(vals[i], test_vals[i]*1000.0, places=0)

        test_vals = [-3691.6064, 5363.311, -2055.1482]
        vals = frame.obsgeoloc[-1].xyz.value
        for i in range(3):
            self.assertAlmostEqual(vals[i], test_vals[i]*1000.0, places=0)

    def test_detector(self):
        phaii = self.phaii_collection.get_detector(3)
        assert phaii.detector.number == 3

    def test_headers(self):
        assert self.phaii_collection.headers.num_headers == 3


@unittest.skipIf(not cont_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatsePhaiiContOneDet(unittest.TestCase):

    def setUp(self):
        phaii_collection = BatsePhaii.open(cont_file)
        self.phaii = phaii_collection.get_detector(3)

    def test_detector(self):
        assert self.phaii.detector.number == 3

    def test_headers(self):
        assert self.phaii.headers.num_headers == 3

    def test_energy_range(self):
        self.assertAlmostEqual(self.phaii.energy_range[0], 21.8, places=5)
        self.assertAlmostEqual(self.phaii.energy_range[1], 4000.0, places=3)

    def test_num_chans(self):
        assert self.phaii.num_chans == 16

    def test_time_range(self):
        t0, t1 = self.phaii.time_range
        self.assertAlmostEqual(t0, 8362.557340507052, places=6)
        self.assertAlmostEqual(t1, 8362.997613099642, places=6)

    def test_trigtime(self):
        assert self.phaii.trigtime is None

    def test_rebin_energy(self):
        phaii2 = self.phaii.rebin_energy(combine_by_factor, 2)
        assert phaii2.num_chans == self.phaii.num_chans // 2
        assert phaii2.ecalib is not None

    def test_rebin_time(self):
        phaii2 = self.phaii.rebin_time(combine_by_factor, 2)
        # note: this is not exatly half because of the number if disjoint segments
        assert phaii2.data.num_times == 2240
        assert phaii2.ecalib is not None

    def test_slice_energy(self):
        phaii2 = self.phaii.slice_energy((50.0, 300.0))
        emin, emax = phaii2.energy_range
        self.assertAlmostEqual(emin, 21.8, places=5)
        self.assertAlmostEqual(emax, 323.15576, places=5)
        assert phaii2.ecalib is not None

    def test_slice_time(self):
        phaii2 = self.phaii.slice_time((8362.6, 8362.7))
        t0, t1 = phaii2.time_range
        self.assertAlmostEqual(t0, 8362.557814581125, places=6)
        self.assertAlmostEqual(t1, 8362.700013099642, places=6)
        assert phaii2.ecalib is not None
        lc = self.phaii.to_lightcurve()
        assert self.phaii.data.num_times == lc.size

    def test_to_lightcurve(self):
        lc = self.phaii.to_lightcurve()
        assert self.phaii.data.num_times == lc.size

    def test_to_pha(self):
        pha = self.phaii.to_pha()
        assert self.phaii.num_chans == pha.num_chans

    def test_to_spectrum(self):
        spec = self.phaii.to_spectrum()
        assert self.phaii.num_chans == spec.size

    def test_ecalib(self):
        assert isinstance(self.phaii.ecalib, BatseEnergyCalib)


@unittest.skipIf(not discla_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatsePhaiiDiscla(unittest.TestCase):
    
    def setUp(self):
        self.phaii_collection = BatsePhaii.open(discla_file)
    
    def test_detectors(self):
        assert self.phaii_collection.detectors == list(range(8))
    
    def test_filename(self):
        assert self.phaii_collection.filename == discla_file.name
    
    def test_headers(self):
        assert self.phaii_collection.headers.num_headers == 3

    def test_num_dets(self):
        assert self.phaii_collection.num_dets == 8

    def test_get_detector(self):
        # from number
        phaii = self.phaii_collection.get_detector(0)
        assert phaii.detector.number == 0
        
        # from string
        phaii = self.phaii_collection.get_detector('LAD1')
        assert phaii.detector.number == 1

        # from object
        det = BatseDetectors.from_str('LAD2')
        phaii = self.phaii_collection.get_detector(det)
        assert phaii.detector.number == 2
        
        # incorrect input
        with self.assertRaises(TypeError):
            self.phaii_collection.get_detector(0.0)

    def test_sum_detectors(self):
    
        # sum all by default
        phaii_sum = self.phaii_collection.sum_detectors()
        assert len(phaii_sum.detector) == 8
        for i in range(8):
            assert phaii_sum.detector[i].number == i
        
        phaii_sum = self.phaii_collection.sum_detectors([0,1])
        assert len(phaii_sum.detector) == 2
        assert phaii_sum.detector[0].number == 0
        assert phaii_sum.detector[1].number == 1
        
        phaii0 = self.phaii_collection.get_detector(0)
        phaii1 = self.phaii_collection.get_detector(1)
        
        counts0 = phaii0.data.counts.flatten()
        counts1 = phaii1.data.counts.flatten()
        for i, bin in enumerate(phaii_sum.data.counts.flatten()):
            assert bin == counts0[i] + counts1[i]
        
        expo0 = phaii0.data.exposure.flatten()
        expo1 = phaii1.data.exposure.flatten()
        for i, bin in enumerate(phaii_sum.data.exposure.flatten()):
            assert bin == (expo0[i] + expo1[i]) / 2
                
    def test_lad_lightcurve(self):
        lad_lc0 = self.phaii_collection.get_detector(0).lad_lightcurve
        lad_lc1 = self.phaii_collection.get_detector(1).lad_lightcurve
        assert lad_lc0.size == 8970
        assert lad_lc1.size == 8970
        
        lad_lc_sum = self.phaii_collection.sum_detectors([0,1]).lad_lightcurve
        counts0 = lad_lc0.counts
        counts1 = lad_lc1.counts
        for i, bin in enumerate(lad_lc_sum.counts):
            assert bin == counts0[i] + counts1[i]

    def test_cpd_lightcurve(self):
        cpd_lc0 = self.phaii_collection.get_detector(0).cpd_lightcurve
        cpd_lc1 = self.phaii_collection.get_detector(1).cpd_lightcurve
        assert cpd_lc0.size == 8970
        assert cpd_lc1.size == 8970
        
        cpd_lc_sum = self.phaii_collection.sum_detectors([0,1]).cpd_lightcurve
        counts0 = cpd_lc0.counts
        counts1 = cpd_lc1.counts
        for i, bin in enumerate(cpd_lc_sum.counts):
            assert bin == counts0[i] + counts1[i]

    def test_get_spacecraft_frame(self):
        frame = self.phaii_collection.get_spacecraft_frame()
        assert isinstance(frame, CgroFrame)
        assert frame.shape == (8970,)
        assert frame.obstime[0].cgro == 8362.557346432975
        assert frame.obstime[-1].cgro == 8362.997607173716
        
        test_vals = [-6227.0, -1945.1599, 1980.6166]
        vals = frame.obsgeoloc[0].xyz.value
        for i in range(3):
            self.assertAlmostEqual(vals[i], test_vals[i]*1000.0, places=0)

        test_vals = [-3694.8606, 5361.6294, -2053.713]
        vals = frame.obsgeoloc[-1].xyz.value
        for i in range(3):
            self.assertAlmostEqual(vals[i], test_vals[i]*1000.0, places=0)


@unittest.skipIf(not discla_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatsePhaiiDisclaOneDet(unittest.TestCase):

    def setUp(self):
        phaii_collection = BatsePhaii.open(discla_file)
        self.phaii = phaii_collection.get_detector(3)
    
    def test_detector(self):
        assert self.phaii.detector.number == 3

    def test_headers(self):
        assert self.phaii.headers.num_headers == 3
    
    def test_energy_range(self):
        self.assertAlmostEqual(self.phaii.energy_range[0], 21.8, places=5)
        self.assertAlmostEqual(self.phaii.energy_range[1], 4000.0, places=3)
    
    def test_num_chans(self):
        assert self.phaii.num_chans == 4

    def test_time_range(self):
        t0, t1 = self.phaii.time_range
        self.assertAlmostEqual(t0, 8362.557340507052, places=6)
        self.assertAlmostEqual(t1, 8362.997613099642, places=6)

    def test_trigtime(self):
        assert self.phaii.trigtime is None

    def test_rebin_energy(self):
        phaii2 = self.phaii.rebin_energy(combine_by_factor, 2)
        assert phaii2.num_chans == self.phaii.num_chans // 2
        assert phaii2.ecalib is not None
        assert phaii2.cpd_lightcurve.size == self.phaii.cpd_lightcurve.size
        assert phaii2.lad_lightcurve.size == self.phaii.lad_lightcurve.size

    def test_rebin_time(self):
        phaii2 = self.phaii.rebin_time(combine_by_factor, 2)
        assert phaii2.data.num_times == self.phaii.data.num_times // 2
        assert phaii2.ecalib is not None
        assert phaii2.cpd_lightcurve.size == self.phaii.cpd_lightcurve.size // 2
        assert phaii2.lad_lightcurve.size == self.phaii.lad_lightcurve.size // 2

    def test_slice_energy(self):
        phaii2 = self.phaii.slice_energy((50.0, 300.0))
        emin, emax = phaii2.energy_range
        self.assertAlmostEqual(emin, 21.8, places=5)
        self.assertAlmostEqual(emax, 320.0, places=5)
        assert phaii2.ecalib is not None
        assert phaii2.cpd_lightcurve.size == self.phaii.cpd_lightcurve.size
        assert phaii2.lad_lightcurve.size == self.phaii.lad_lightcurve.size

    def test_slice_time(self):
        phaii2 = self.phaii.slice_time((8362.6, 8362.7))
        t0, t1 = phaii2.time_range
        self.assertAlmostEqual(t0, 8362.557826432976, places=6)
        self.assertAlmostEqual(t1, 8362.700001247791, places=6)
        assert phaii2.ecalib is not None
        assert phaii2.cpd_lightcurve.size == phaii2.data.num_times
        assert phaii2.lad_lightcurve.size == phaii2.data.num_times
    
    def test_to_lightcurve(self):
        lc = self.phaii.to_lightcurve()
        assert self.phaii.data.num_times == lc.size

    def test_to_pha(self):
        pha = self.phaii.to_pha()
        assert self.phaii.num_chans == pha.num_chans

    def test_to_spectrum(self):
        spec = self.phaii.to_spectrum()
        assert self.phaii.num_chans == spec.size

    def test_ecalib(self):
        assert isinstance(self.phaii.ecalib, BatseEnergyCalib)


@unittest.skipIf(not trigger_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatsePhaiiTrigger(unittest.TestCase):
    
    def setUp(self):
        self.phaii = BatsePhaii.open(trigger_file)
    
    def test_detector(self):
        assert self.phaii.detector.number == 3
    
    def test_filename(self):
        assert self.phaii.filename == trigger_file.name
    
    def test_headers(self):
        assert self.phaii.headers.num_headers == 3

    def test_energy_range(self):
        self.assertAlmostEqual(self.phaii.energy_range[0], 13.140961, places=6)
        self.assertAlmostEqual(self.phaii.energy_range[1], 100000.0, places=6)

    def test_num_chans(self):
        assert self.phaii.num_chans == 16

    def test_time_range(self):
        t0, t1 = self.phaii.time_range
        self.assertAlmostEqual(t0, -120.832, places=3)
        self.assertAlmostEqual(t1, 38.912, places=3)
    
    def test_trigtime(self):
        self.assertAlmostEqual(self.phaii.trigtime, 8367.384765694444, places=6)
    
    def test_rebin_energy(self):
        phaii2 = self.phaii.rebin_energy(combine_by_factor, 2)
        assert phaii2.num_chans == self.phaii.num_chans // 2
    
    def test_rebin_time(self):
        phaii2 = self.phaii.rebin_time(combine_by_factor, 2)
        assert phaii2.data.num_times == self.phaii.data.num_times // 2

    def test_slice_energy(self):
        phaii2 = self.phaii.slice_energy((50.0, 300.0))
        emin, emax = phaii2.energy_range
        self.assertAlmostEqual(emin, 44.175056, places=5)
        self.assertAlmostEqual(emax, 318.02216, places=5)

    def test_slice_time(self):
        phaii2 = self.phaii.slice_time((10.0, 20.0))
        t0, t1 = phaii2.time_range
        self.assertAlmostEqual(t0, 8.192, places=3)
        self.assertAlmostEqual(t1, 20.48, places=3)
    
    def test_to_lightcurve(self):
        lc = self.phaii.to_lightcurve()
        assert self.phaii.data.num_times == lc.size

    def test_to_pha(self):
        pha = self.phaii.to_pha()
        assert self.phaii.num_chans == pha.num_chans

    def test_to_spectrum(self):
        spec = self.phaii.to_spectrum()
        assert self.phaii.num_chans == spec.size
    
    def test_ecalib(self):
        assert isinstance(self.phaii.ecalib, BatseEnergyCalib)


@unittest.skipIf(not cont_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatseEnergyCalib(unittest.TestCase):

    def setUp(self):
        self.ecalib = BatsePhaii.open(cont_file)._ecalib
    
    def test_detectors(self):
        assert self.ecalib.detectors == list(range(8))

    def num_dets(self):
        assert self.ecalib.num_dets == 8
    
    def test_num_times(self):
        assert self.ecalib.num_times == 12

    def test_get_detector(self):
        ecalib0 = self.ecalib.get_detector(0)
        assert ecalib0.detectors == [0]
        assert ecalib0.num_times == 12

    def test_combine_detector(self):
        ecalib0 = self.ecalib.get_detector(0)
        ecalib1 = self.ecalib.get_detector(1)
        
        ecalib_combo = self.ecalib.combine_detectors([ecalib0, ecalib1])
        edges0 = ecalib0._data['E_EDGES'].flatten()
        edges1 = ecalib1._data['E_EDGES'].flatten()
        for i, bin in enumerate(ecalib_combo._data['E_EDGES'].flatten()):
            assert bin == np.sqrt(edges0[i] * edges1[i])
    
    def test_edges_at_time(self):
        t0 =  8362.695
        det = 0
        edges = self.ecalib.edges_at_time(det, t0)
        test_edges = [23.8, 49.22601, 58.337082, 67.5833, 76.94139, 91.15164,  
                      105.53314, 129.80481, 164.27374, 224.3067, 300.492,  
                      398.21323, 554.33374, 796.45776, 1264.9601, 1866.8799, 
                      4000.]
        for i, edge in enumerate(edges):
            self.assertAlmostEqual(edge, test_edges[i], places=4)
    
    def test_edges_over_timespan(self):
        
        # t0 prior to first calibration, t1 prior to last calibration
        t0 = 8362.000
        t1 = 8362.695
        edges = self.ecalib.edges_over_timespan(0, t0, t1)
        test_edges = [23.8, 48.26681, 57.189587, 66.24471, 75.4094, 89.32597, 
                      103.41024, 127.18029, 160.93686, 219.72908, 294.33987, 
                      390.04153, 542.9355, 780.0556, 1238.8752, 1828.3555, 4000.]
        
        for i, edge in enumerate(edges):
            self.assertAlmostEqual(edge, test_edges[i], places=4)
        
        
        # t0 after first calibration, t1 prior to last calibration
        t0 = 8362.625
        t1 = 8362.695
        edges = self.ecalib.edges_over_timespan(0, t0, t1)
        test_edges = [23.8, 48.52175, 57.49457, 66.60049, 75.81658, 89.81121, 
                      103.97447, 127.87785, 161.82375, 220.94574, 295.97504, 
                      392.21344, 545.96497, 784.41504, 1245.8082, 1838.5947, 
                      3999.9998]
        for i, edge in enumerate(edges):
            self.assertAlmostEqual(edge, test_edges[i], places=4)

        # t0 after first calibration, t1 after last calibration
        t0 = 8362.980
        t1 = 8363.000
        edges = self.ecalib.edges_over_timespan(0, t0, t1)
        test_edges = [23.8, 50.683517, 60.08071, 69.617294, 79.269264, 93.92577,  
                      108.758896, 133.7928, 169.34418, 231.26239, 309.84027, 
                      410.63028, 571.65356, 821.3812, 1304.5962, 1925.4187, 
                      4000.]
        for i, edge in enumerate(edges):
            self.assertAlmostEqual(edge, test_edges[i], places=4)
        
        # full range
        t0 = self.ecalib._data['CAL_STRT'][0]
        t1 = self.ecalib._data['CAL_STOP'][11]
        edges = self.ecalib.edges_over_timespan(0, t0, t1)
        test_edges = [  23.800005,   49.934483,   59.18463 ,   68.572   ,   78.072945,
        92.50011 ,  107.10114 ,  131.74332 ,  166.73842 ,  227.68774 ,
        305.03607 ,  404.24896 ,  562.7527  ,  808.5727  , 1284.2267  ,
        1895.335   , 4000.      ]

        for i, edge in enumerate(edges):
            self.assertAlmostEqual(edge, test_edges[i], places=4)
