# CONTAINS TECHNICAL DATA/COMPUTER SOFTWARE DELIVERED TO THE U.S. GOVERNMENT 
# WITH UNLIMITED RIGHTS
#
# Grant No.: 80NSSC24M0035
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

import numpy as np

def batse_loc_systematic_4br():
    """The preferred localization systematic model for BATSE as estimated with
    burst localizations from the BATSE 4Br catalog.  A mixture of a 1.85 deg 
    Gaussian (78% weight) and a 5.1 deg Gaussian.
    
    References:
        Briggs, M. S. et al. 1999, ApJS, 122, 503
        <https://iopscience.iop.org/article/10.1086/313221>`_
    """
    sigma1 = np.deg2rad(1.85)
    sigma2 = np.deg2rad(5.1)
    frac1 = 0.78
    return ([sigma1, sigma2], [frac1])