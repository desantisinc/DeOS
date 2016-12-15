#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from subprocess import call, check_output


EXEC=lambda x:print('\n%s'%check_output(x.split(' ')))
PRINT=lambda x:print('\n%s\n'%x)
SHELL=lambda x:call(x.split(' '))


CMD={'Δ':'\x1b[32;01mΔ \x1b[0m'}
CMD['down']=lambda:SHELL('make down')
CMD['help']=lambda:PRINT('help')
CMD['ls']=lambda:EXEC('ls')
CMD['clear']=lambda:EXEC('clear')
CMD['vm.ls']=lambda:SHELL('make vm.ls')
CMD['build']=lambda:SHELL('make build')
CMD['test']=lambda:PRINT('test')
CMD['vm']=lambda:SHELL('make vm')


if __name__ == "__main__":
    while not((lambda c:1 if c=='quit' else CMD[c]())(raw_input(CMD['Δ']))):
        pass