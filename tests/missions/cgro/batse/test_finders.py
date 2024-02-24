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
import numpy as np
import unittest

from gdt.missions.cgro.time import *
from gdt.missions.cgro.batse.finders import *

download_dir = data_dir = os.path.dirname(os.path.abspath(__file__))


class TestTriggerFtp(unittest.TestCase):
    
    finder = BatseTriggerFtp(105)
    
    def test_cd(self):
        self.assertEqual(self.finder.num_files, 113)
        self.finder.cd(5671)
        self.assertEqual(self.finder.num_files, 96)
        self.finder.cd(105)

    def test_ls_cont(self):
        for file in self.finder.ls_cont():
            assert 'cont' in file
    
    def test_ls_discsc(self):
        for file in self.finder.ls_discsc():
            assert 'discsc' in file

    def test_ls_discsp(self):
        for file in self.finder.ls_discsp():
            assert 'discsp' in file
    
    def test_ls_dsherb(self):
        for file in self.finder.ls_dsherb():
            assert 'dsherb' in file

    def test_ls_drm(self):
        for file in self.finder.ls_drm():
            assert 'drm' in file

    def test_ls_her(self):
        for file in self.finder.ls_her():
            assert 'her' in file
            assert 'herb' not in file

    def test_ls_herb(self):
        for file in self.finder.ls_herb():
            assert 'her' in file
            assert 'sherb' not in file

    def test_ls_ibdb(self):
        for file in self.finder.ls_ibdb():
            assert 'ibdb' in file
    
    def test_ls_lightcurve(self):
        for file in self.finder.ls_lightcurve():
            assert 'gif' in file

    def test_ls_mer(self):
        for file in self.finder.ls_mer():
            assert 'mer' in file
    
    def test_ls_sdisc(self):
        for file in self.finder.ls_sdisc():
            assert 'sdisc' in file

    def test_ls_sher(self):
        for file in self.finder.ls_sher():
            assert 'sher' in file
            assert 'sherb' not in file

    def test_ls_sherb(self):
        for file in self.finder.ls_sherb():
            assert 'sherb' in file
            assert 'dsherb' not in file

    def test_ls_tte(self):
        for file in self.finder.ls_tte():
            assert 'tte' in file

    def test_ls_tts(self):
        for file in self.finder.ls_tts():
            assert 'tts' in file

    def test_get_cont(self):
        fnames = self.finder.get_cont(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_cont(download_dir, dets=[1])
        assert len(fnames) == 0

    def test_get_discsc(self):
        fnames = self.finder.get_discsc(download_dir)
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_discsp(self):
        fnames = self.finder.get_discsp(download_dir, dets=[0])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_discsp(download_dir, dets=[8])
        assert len(fnames) == 0

    def test_get_dsherb(self):
        fnames = self.finder.get_dsherb(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_dsherb(download_dir, dets=[1])
        assert len(fnames) == 0

    def test_get_drm(self):
        fnames = self.finder.get_drm(download_dir, drm_type='cont', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        
        fnames = self.finder.get_drm(download_dir, drm_type='discsc')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='discsp', dets=[0])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='dsherb', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='her', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='herb', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='mer')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='sher', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='sherb', dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='stte_list')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_drm(download_dir, drm_type='tte')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_her(self):
        fnames = self.finder.get_her(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_her(download_dir, dets=[1])
        assert len(fnames) == 0
    
    def test_get_herb(self):
        fnames = self.finder.get_herb(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_herb(download_dir, dets=[1])
        assert len(fnames) == 0
    
    def test_get_ibdb(self):
        fnames = self.finder.get_ibdb(download_dir, ibdb_type='continuous')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='discla')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='discsc')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='discsp')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='herb')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='info')
        assert len(fnames) == 3
        for fname in fnames:
            os.remove(os.path.join(download_dir, fname))
        
        fnames = self.finder.get_ibdb(download_dir, ibdb_type='mer')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='preb')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='sherb')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='stte')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='tte')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

        fnames = self.finder.get_ibdb(download_dir, ibdb_type='stte')
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
    
    def test_get_lightcurves(self):
        fnames = self.finder.get_lightcurves(download_dir)
        assert len(fnames) == 2
        for fname in fnames:
            os.remove(os.path.join(download_dir, fname))
  
    def test_get_mer(self):
        fnames = self.finder.get_mer(download_dir)
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_sdisc(self):
        fnames = self.finder.get_sdisc(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_sdisc(download_dir, dets=[1])
        assert len(fnames) == 0

    def test_get_sher(self):
        fnames = self.finder.get_sher(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_sher(download_dir, dets=[1])
        assert len(fnames) == 0

    def test_get_sherb(self):
        fnames = self.finder.get_sherb(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_sherb(download_dir, dets=[1])
        assert len(fnames) == 0

    def test_get_tte(self):
        fnames = self.finder.get_tte(download_dir)
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_tts(self):
        fnames = self.finder.get_tts(download_dir, dets=[3])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_tts(download_dir, dets=[5])
        assert len(fnames) == 0

                
class TestContinuousFtp(unittest.TestCase):
    finder = BatseContinuousFtp(Time('1992-01-01 12:00:00', format='iso'))
    
    def test_cd(self):
        self.assertEqual(self.finder.num_files, 18)
        time = Time('1993-01-01 12:00:00', format='iso')
        self.finder.cd(time)
        self.assertEqual(self.finder.num_files, 18)
        time = Time('1992-01-01 12:00:00', format='iso')
        self.finder.cd(time)

    def test_ls_cont(self):
        for file in self.finder.ls_cont():
            assert 'cont' in file

    def test_ls_discla(self):
        for file in self.finder.ls_discla():
            assert 'discla' in file

    def test_ls_her(self):
        for file in self.finder.ls_her():
            assert 'her' in file
            assert 'sher' not in file

    def test_ls_sher(self):
        for file in self.finder.ls_sher():
            assert 'sher' in file
    
    def test_get_cont(self):
        fnames = self.finder.get_cont(download_dir)
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_discla(self):
        fnames = self.finder.get_discla(download_dir)
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))

    def test_get_her(self):
        fnames = self.finder.get_her(download_dir, dets=[1])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_her(download_dir, dets=[8])
        assert len(fnames) == 0

    def test_get_sher(self):
        fnames = self.finder.get_sher(download_dir, dets=[1])
        assert len(fnames) == 1
        os.remove(os.path.join(download_dir, fnames[0]))
        fnames = self.finder.get_sher(download_dir, dets=[8])
        assert len(fnames) == 0
    
