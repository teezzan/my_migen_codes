#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:38:09 2019

@author: gal3li0
"""

from migen import *
from migen.fhdl import verilog
import random

class shift_reg(Module):
    def __init__(self,n=4,wb=4):
        self.busarray =busarray = Array(Signal(n) for a in range(wb))
        self.inbus = inbus = Signal(n)
        
#        self.choice = choice = Signal(math.ceil(math.log2(wb)))
        
        ###
        
        self.sync += [ 
                busarray[3].eq(busarray[2]),
                      busarray[2].eq(busarray[1]),
                      busarray[1].eq(busarray[0]),
                      busarray[0].eq(inbus)
                    ]
        
def testbench(dut):
    for i in range(15):
        yield dut.inbus.eq(random.randint(0,12))
        print("0{}  ->  1{}  ->  2{}  ->3{}".format((yield dut.busarray[0]),(yield dut.busarray[1]),(yield dut.busarray[2]),(yield dut.busarray[3])))
        yield
if __name__ == "__main__":
    print(verilog.convert(shift_reg()))
    dut = shift_reg()
    run_simulation(dut, testbench(dut), vcd_name="shiftreg_test.vcd")