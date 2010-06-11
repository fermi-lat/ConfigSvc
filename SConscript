# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/ConfigSvc/SConscript,v 1.5 2009/11/10 20:02:43 jrb Exp $
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-02-10
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package='ConfigSvc', toBuild='component')

ConfigSvc = libEnv.SharedLibrary('ConfigSvc',
                                 listFiles(['src/*.cxx','src/Dll/*.cxx']))

progEnv.Tool('ConfigSvcLib')

progEnv.Tool('registerTargets', package = 'ConfigSvc',
             libraryCxts = [[ConfigSvc, libEnv]],
             includes = ['ConfigSvc/IConfigSvc.h'],
             jo = ['src/configOptions_moot.txt',
                   'src/configOptions_noMoot.txt'])




