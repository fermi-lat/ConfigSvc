# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/ConfigSvc/SConscript,v 1.4 2009/11/10 01:56:22 jrb Exp $
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-02-10
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('ConfigSvcLib', depsOnly = 1)

ConfigSvc = libEnv.SharedLibrary('ConfigSvc',
                                 listFiles(['src/*.cxx','src/Dll/*.cxx']))

progEnv.Tool('ConfigSvcLib')

progEnv.Tool('registerTargets', package = 'ConfigSvc',
             libraryCxts = [[ConfigSvc, libEnv]],
             includes = ['ConfigSvc/IConfigSvc.h'])




