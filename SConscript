# -*- python -*-
# $Header$
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-02-08
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('ConfigSvcLib', depsOnly = 1)

ConfigSvc = libEnv.SharedLibrary('ConfigSvc', listFiles(['src/*.cxx']) + listFiles(['src/Dll/*.cxx']))

progEnv.Tool('ConfigSvcLib')

progEnv.Tool('registerObjects', package = 'ConfigSvc', libraries = [ConfigSvc], includes = ['ConfigSvc/IConfigSvc.h'])
