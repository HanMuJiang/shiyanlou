# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:36:25 2018

@author: Administrator
"""

import sys

class Args:
    def __init__(self,args):
        self.args=args
    def __parse_arg(self,arg):
        try:
            value=self.args[self.args.index(arg)+1]
        except(ValueError,  IndexError):
            value=None
        return value
    def get_arg(self,arg):
        value=self.__parse_arg(arg)
        if value is None:
            raise ArgError("not found arg %s "% arg)
        return value
class SheBaoConfig:
    def __init__(self,file):
        self.jishu_low,self.jishu_high,self.total_rate=self.__parse_config(file)  
    def __parse_config(self,file):
        pass
class EmployeeData:
    def __init__(self,file):
        self.__file=open(file)
    def __iter__(self):
        pass
class Exporter:
    def __init__(self,file,append=False):
        self.__file=open(file,mode)
class Calculator:
    def __init__(self,config):
        self.config=config        
class Executor:
    def __init__(self,args):
        args=Args(args)
        config=SheBaoConfig(args.get_arg('-c'))
        self.employee_data=EmployeeData(args.get_arg('-d'))
        self.exporter=Exporter(args.get_arg('-o'))
        self.calculator=calculator(config)
    def execute(self):
        
        
    

if __name__=='__main__':
    executor=Executor(sys.argv[1:])
    executor.execute()    