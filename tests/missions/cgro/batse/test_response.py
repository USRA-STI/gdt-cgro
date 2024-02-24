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
from gdt.missions.cgro.batse.detectors import BatseDetectors
from gdt.missions.cgro.batse.response import *
from gdt.core.spectra.functions import PowerLaw

cont_file = data_path / 'cgro-batse/cont_drm_3_105.fits.gz'
discsc_file = data_path / 'cgro-batse/discsc_drm_105.fits.gz'

@unittest.skipIf(not cont_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatseRsp(unittest.TestCase):
    
    def setUp(self):
        self.rsp = BatseRsp.open(cont_file)
        self.trigtime = 8367.384765717592
    
    def test_detector(self):
        assert self.rsp.detector == 'LAD3'

    def test_filename(self):
        assert self.rsp.filename == 'cont_drm_3_105.fits.gz'
    
    def test_num_chans(self):
        assert self.rsp.num_chans == 16

    def test_num_ebins(self):
        assert self.rsp.num_ebins == 62

    def test_tcent(self):
        self.assertAlmostEqual(self.rsp.tcent, (8367.384291597222-self.trigtime),
                               places=6)

    def test_trigtime(self):
        assert self.rsp.trigtime == self.trigtime

    def test_tstart(self):
        self.assertAlmostEqual(self.rsp.tstart, 8367.383367129629-self.trigtime,
                               places=6)

    def test_tstop(self):
        self.assertAlmostEqual(self.rsp.tstop, 8367.385216064815-self.trigtime,
                               places=6)

    def test_fold_spectrum(self):
        ebins = self.rsp.fold_spectrum(PowerLaw().fit_eval, (0.01, -2.2), exposure=2.0)
        assert ebins.size == self.rsp.num_chans
        assert ebins.exposure[0] == 2.0

    def test_rebin(self):
        rsp = self.rsp.rebin(factor=2)
        assert rsp.num_chans == self.rsp.num_chans // 2
        assert rsp.num_ebins == self.rsp.num_ebins

    def test_resample(self):
        rsp = self.rsp.resample(num_photon_bins=31)
        assert rsp.num_chans == rsp.num_chans
        assert rsp.num_ebins == self.rsp.num_ebins // 2


@unittest.skipIf(not discsc_file.exists(), "test files aren't downloaded. run gdt-data download.")
class TestBatseRspMulti(unittest.TestCase):
    
    def setUp(self):
        self.rsp_collection = BatseRspMulti.open(discsc_file)
        self.trigtime = 8367.384765717592
    
    def test_detectors(self):
        assert self.rsp_collection.detectors == ['LAD3', 'LAD7']

    def test_num_dets(self):
        assert self.rsp_collection.num_dets == 2

    def test_get_detector(self):
        # from detector name
        rsp3 = self.rsp_collection.get_detector('LAD3')
        assert rsp3.detector == 'LAD3'
        assert rsp3.num_chans == 4
        assert rsp3.num_ebins == 30
        assert rsp3.trigtime == self.trigtime
        assert rsp3.filename == 'discsc_drm_3_105.fits.gz'
        test_edges = [2.3739225e+01, 6.5462227e+01, 1.1396066e+02, 3.2341464e+02]
        for i, edge in enumerate(rsp3.ebounds.low_edges()):
            self.assertAlmostEqual(edge, test_edges[i], places=5)
        
        # from detector number
        rsp7 = self.rsp_collection.get_detector(7)
        assert rsp7.detector == 'LAD7'
        assert rsp7.num_chans == 4
        assert rsp7.num_ebins == 30
        assert rsp7.trigtime == self.trigtime
        assert rsp7.filename == 'discsc_drm_7_105.fits.gz'
        test_edges = [1.4457939e+01, 6.0348976e+01, 1.1112445e+02, 3.2305414e+02]
        for i, edge in enumerate(rsp7.ebounds.low_edges()):
            self.assertAlmostEqual(edge, test_edges[i], places=5)

        # from detector object
        det = BatseDetectors.LAD3
        rsp3 = self.rsp_collection.get_detector(det)
        assert rsp3.detector == 'LAD3'
       