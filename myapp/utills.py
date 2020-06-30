# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:58:32 2020

@author: routm1
"""

import os

def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_instance_folder_path():
    return os.path.join(get_app_base_path(), "instance")