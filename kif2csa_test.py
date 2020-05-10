#!/usr/bin/python3
# -*- coding: utf-8 -*-
    
import kif2csa
    

def test_as_csa():
    assert kif2csa.header + '\n' == kif2csa.as_csa([])
