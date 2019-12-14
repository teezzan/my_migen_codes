#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:59:24 2019

@author: gal3li0
"""

from migen import *
from migen.fhdl import verilog
import math
import random

class Mux(Module):
    def __init__(self,n=2):
        self.bus1 = bus1 =Signal(n)
        self.bus2 = bus2 =Signal(n)
        self.outbus = outbus =Signal(n)
        
        self.choice = choice = Signal()
        
        ###
        
        self.comb += [
            If(choice == 0,
               outbus.eq(bus1)
               ).Elif(choice == 1,
               outbus.eq(bus2)
                       )
        ]
        
        
class Mux2(Module):
    def __init__(self,n=2,wb=2):
        self.busarray =busarray = Array(Signal(n) for a in range(wb))
        self.outbus = outbus =Signal(n)
        
        self.choice = choice = Signal(math.ceil(math.log2(wb)))
        
        ###
        
        self.comb += outbus.eq(busarray[choice])
        
        
def mux_test(dut):
    yield dut.bus1.eq(1)
    yield dut.bus2.eq(3)
    yield dut.choice.eq(0)
    for i in range(5):
        print("A-{}  B-{}  Out- {}".format((yield dut.bus1),(yield dut.bus2),(yield dut.outbus)))
        yield
    yield dut.bus1.eq(2)
    yield dut.bus2.eq(0)
    yield dut.choice.eq(1)
    for i in range(5):
        print("A-{}  B-{}  Out- {}".format((yield dut.bus1),(yield dut.bus2),(yield dut.outbus)))
        yield
        
        
def mux2_test(dut, wb=8):
    for i in range(wb):
        yield dut.busarray[i].eq(8-i)
        
    for i in range(10):
        print("choice-{} Out- {}".format((yield dut.choice),(yield dut.outbus)))
        yield dut.choice.eq(random.randint(0,4))
        yield

        


if __name__ == "__main__":
    print(verilog.convert(Mux2(3,8)))
    dut = Mux2(3,8)
    run_simulation(dut, mux2_test(dut), vcd_name="mux2_test.vcd")
        