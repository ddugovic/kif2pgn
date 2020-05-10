#!/usr/bin/python3
# -*- coding: utf-8 -*-
    
import kif2psn
    

def test_as_psn():
    assert kif2psn.header + '\n' == kif2psn.as_psn([])
