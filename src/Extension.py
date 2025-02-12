#!/usr/bin/env python3

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     Extension.py
    Project:       RandomForest (Non-GPU)
    Description:   Class file that contains the static Strings for the valid
                   file extensions as well as two static lists, each containing
                   the extensions that are valid for feature data files and
                   target data files, respectively.
"""


# Initializing Extension class and its variables for file_valid logic
# Designed to allow for smooth implementation of other file types
class Extension:
    FEAT_ODF_EXT = ".feat.odf"
    PRED_ODF_EXT = ".pred.odf"
    GCT_EXT = ".gct"
    CLS_EXT = ".cls"
    MODEL_EXT = ".pkl"
    FEAT_EXT =  [GCT_EXT]
    TAR_EXT = [CLS_EXT]
    MODEL_EXT = [MODEL_EXT]