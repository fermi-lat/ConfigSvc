# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/ConfigSvc/SConscript,v 1.10 2011/12/12 20:46:04 heather Exp $
# Authors: Eric Charles <echarles@slac.stanford.edu>
# Version: ConfigSvc-00-04-00

Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package='ConfigSvc', toBuild='component')

ConfigSvc = libEnv.ComponentLibrary('ConfigSvc',
                                    listFiles(['src/*.cxx']))

progEnv.Tool('ConfigSvcLib')

progEnv.Tool('registerTargets', package = 'ConfigSvc',
             libraryCxts = [[ConfigSvc, libEnv]],
             includes = ['ConfigSvc/IConfigSvc.h'],
             xml =listFiles(['xml/*.xml']),
             jo = ['src/configOptions_moot.txt',
                   'src/configOptions_noMoot.txt'])




