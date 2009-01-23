# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/ConfigSvc/SConscript,v 1.1 2008/08/15 21:22:40 ecephas Exp $
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-02-09
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('ConfigSvcLib', depsOnly = 1)

ConfigSvc = libEnv.SharedLibrary('ConfigSvc', listFiles(['src/*.cxx','src/Dll/*.cxx']))

progEnv.Tool('ConfigSvcLib')

progEnv.Tool('registerObjects', package = 'ConfigSvc', libraries = [ConfigSvc], includes = ['ConfigSvc/IConfigSvc.h'])




