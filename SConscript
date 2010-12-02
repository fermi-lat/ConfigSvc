# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/ConfigSvc/SConscript,v 1.8 2010/06/12 17:21:40 jrb Exp $
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-02-12
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
             xml =listFiles(['xml/*.xml']),
             jo = ['src/configOptions_moot.txt',
                   'src/configOptions_noMoot.txt'])




