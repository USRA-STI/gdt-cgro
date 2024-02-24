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
from gdt.missions.cgro.batse.headers import *


class TestPhaiiContHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiContHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'CDATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiContHeadersAlt1(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiContHeadersAlt1()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiContHeadersAlt2(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiContHeadersAlt2()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiDisclaHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiDisclaHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'CDATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiDisclaHeadersAlt1(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiDisclaHeadersAlt1()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiDisclaHeadersAlt2(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiDisclaHeadersAlt2()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'TJD' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'TIME_RES' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'SC-Z-LII' in hdr.keys()
        assert 'SC-Z-BII' in hdr.keys()
        assert 'SC-X-LII' in hdr.keys()
        assert 'SC-X-BII' in hdr.keys()
        assert 'QMASKDAT' in hdr.keys()
        assert 'QMASKHKG' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_CNTS'


class TestPhaiiTriggerHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiTriggerHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'OBJECT' in hdr.keys()
        assert 'BATSE_TR' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'TRIG-DAY' in hdr.keys()
        assert 'TRIG-TIM' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'OBJCTRA' in hdr.keys()
        assert 'OBJCTDEC' in hdr.keys()
        assert 'SC-X-POS' in hdr.keys()
        assert 'SC-Y-POS' in hdr.keys()
        assert 'SC-Z-POS' in hdr.keys()
        assert 'SRCE-AZ' in hdr.keys()
        assert 'SRCE-EL' in hdr.keys()
        assert 'GEOC-AZ' in hdr.keys()
        assert 'GEOC-EL' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE BURST SPECTRA'
        assert 'DSELECT' in hdr.keys()
        assert 'LO_CHAN' in hdr.keys()
        assert 'UP_CHAN' in hdr.keys()
        assert 'RF_511' in hdr.keys()
        assert 'R_EXP' in hdr.keys()
        assert 'DET_MODE' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'IS_SPEC' in hdr.keys()
        assert 'IS_ERROR' in hdr.keys()
        assert 'OVERFLW' in hdr.keys()
        assert 'LTIMECOR' in hdr.keys()
        assert 'BCKGSUBT' in hdr.keys()
        assert 'BSTACC' in hdr.keys()
        assert 'BASETIME' in hdr.keys()


class TestPhaiiTriggerTtsHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = PhaiiTriggerTtsHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'BATSE_TR' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'TRIG-DAY' in hdr.keys()
        assert 'TRIG-TIM' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'OBJCTRA' in hdr.keys()
        assert 'OBJCTDEC' in hdr.keys()
        assert 'SC-X-POS' in hdr.keys()
        assert 'SC-Y-POS' in hdr.keys()
        assert 'SC-Z-POS' in hdr.keys()
        assert 'SRCE-AZ' in hdr.keys()
        assert 'SRCE-EL' in hdr.keys()
        assert 'GEOC-AZ' in hdr.keys()
        assert 'GEOC-EL' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE BURST SPECTRA'
        assert 'DSELECT' in hdr.keys()
        assert 'LO_CHAN' in hdr.keys()
        assert 'UP_CHAN' in hdr.keys()
        assert 'RF_511' in hdr.keys()
        assert 'R_EXP' in hdr.keys()
        assert 'DET_MODE' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'IS_SPEC' in hdr.keys()
        assert 'IS_ERROR' in hdr.keys()
        assert 'OVERFLW' in hdr.keys()
        assert 'LTIMECOR' in hdr.keys()
        assert 'BCKGSUBT' in hdr.keys()
        assert 'BSTACC' in hdr.keys()
        assert 'COR_TTS' in hdr.keys()
        assert 'MAXTTSER' in hdr.keys()
        assert 'TOTTTSER' in hdr.keys()
        assert 'BASETIME' in hdr.keys()


class TestTteTriggerHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = TteTriggerHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'BATSE_TR' in hdr.keys()
        assert 'OBSERVER' in hdr.keys()
        assert hdr['OBSERVER'] == 'G. J. FISHMAN'
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'TRIG-DAY' in hdr.keys()
        assert 'TRIG-TIM' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'OBJCTRA' in hdr.keys()
        assert 'OBJCTDEC' in hdr.keys()
        assert 'SC-X-POS' in hdr.keys()
        assert 'SC-Y-POS' in hdr.keys()
        assert 'SC-Z-POS' in hdr.keys()
        assert 'SRCE-AZ' in hdr.keys()
        assert 'SRCE-EL' in hdr.keys()
        assert 'GEOC-AZ' in hdr.keys()
        assert 'GEOC-EL' in hdr.keys()
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
    
    def test_ecalib(self):
        hdr = self.headers[1]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE_E_CALIB'
    
    def test_counts(self):
        hdr = self.headers[2]
        assert 'EXTNAME' in hdr.keys()
        assert hdr['EXTNAME'] == 'BATSE PHOTON LIST'
        assert 'DSELECT' in hdr.keys()
        assert 'LO_CHAN' in hdr.keys()
        assert 'UP_CHAN' in hdr.keys()
        assert 'RF_511' in hdr.keys()
        assert 'R_EXP' in hdr.keys()
        assert 'DET_MODE' in hdr.keys()
        assert 'DATATYPE' in hdr.keys()
        assert 'IS_SPEC' in hdr.keys()
        assert 'IS_ERROR' in hdr.keys()
        assert 'OVERFLW' in hdr.keys()
        assert 'LTIMECOR' in hdr.keys()
        assert 'BCKGSUBT' in hdr.keys()
        assert 'BSTACC' in hdr.keys()
        assert 'BASETIME' in hdr.keys()


class TestRspHeaders(unittest.TestCase):
    def setUp(self):
        self.headers = RspHeaders()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'TRIG-DAY' in hdr.keys()
        assert 'TRIG-TIM' in hdr.keys()
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'OBJCTRA' in hdr.keys()
        assert 'OBJCTDEC' in hdr.keys()
        assert 'SC-X-POS' in hdr.keys()
        assert 'SC-Y-POS' in hdr.keys()
        assert 'SC-Z-POS' in hdr.keys()
        assert 'DET_MODE' in hdr.keys()
        assert 'ALPHA' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'N_E_BINS' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DEF_NML' in hdr.keys()
        assert 'USR_NML' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
            
    def test_drm(self):
        hdr = self.headers[1]
        assert 'EXTTYPE' in hdr.keys()
        assert hdr['EXTTYPE'] == 'BATSEDRM'


class TestRspHeadersAlt(unittest.TestCase):
    def setUp(self):
        self.headers = RspHeadersAlt()
    
    def test_primary(self):
        hdr = self.headers[0]
        assert 'TELESCOP' in hdr.keys()
        assert hdr['TELESCOP'] == 'COMPTON GRO'
        assert 'INSTRUME' in hdr.keys()
        assert hdr['INSTRUME'] == 'BATSE'
        assert 'ORIGIN' in hdr.keys()
        assert hdr['ORIGIN'] == 'MSFC'
        assert 'FILETYPE' in hdr.keys()
        assert 'OBJECT' in hdr.keys()
        assert 'STRT-DAY' in hdr.keys()
        assert 'STRT-TIM' in hdr.keys()
        assert 'END-DAY' in hdr.keys()
        assert 'END-TIM' in hdr.keys()
        assert 'TRIG-DAY' in hdr.keys()
        assert 'TRIG-TIM' in hdr.keys()
        assert 'SC-Z-RA' in hdr.keys()
        assert 'SC-Z-DEC' in hdr.keys()
        assert 'SC-X-RA' in hdr.keys()
        assert 'SC-X-DEC' in hdr.keys()
        assert 'OBJCTRA' in hdr.keys()
        assert 'OBJCTDEC' in hdr.keys()
        assert 'SC-X-POS' in hdr.keys()
        assert 'SC-Y-POS' in hdr.keys()
        assert 'SC-Z-POS' in hdr.keys()
        assert 'DET_MODE' in hdr.keys()
        assert 'ALPHA' in hdr.keys()
        assert 'N_E_CHAN' in hdr.keys()
        assert 'N_E_BINS' in hdr.keys()
        assert 'EQUINOX' in hdr.keys()
        assert hdr['EQUINOX'] == 2000.0
        assert 'FILE-ID' in hdr.keys()
        assert 'FILE-VER' in hdr.keys()
        assert 'FILENAME' in hdr.keys()
        assert 'DEF_NML' in hdr.keys()
        assert 'USR_NML' in hdr.keys()
        assert 'DATE' in hdr.keys()
        assert 'MNEMONIC' in hdr.keys()
        assert 'PRIMTYPE' in hdr.keys()
        assert hdr['PRIMTYPE'] == 'NONE'
            
    def test_drm(self):
        hdr = self.headers[1]
        assert 'EXTTYPE' in hdr.keys()
        assert hdr['EXTTYPE'] == 'BATSEDRM'


