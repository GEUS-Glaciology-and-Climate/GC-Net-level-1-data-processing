# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
    import matplotlib.pyplot as plt
"""
%run GC-Net-level-0-data-processing.py
%run GC-Net-level-1-data-processing.py
%run tools/hs_steps.py
%run tools/compare_with_release.py
%run tools/calibration_overview.py
%run tools/hs_steps.py
