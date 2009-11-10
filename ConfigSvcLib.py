#$Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/ConfigSvc/ConfigSvcLib.py,v 1.1 2008/08/15 21:42:34 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['ConfigSvc'])

    env.Tool('configDataLib')
    env.Tool('MootSvcLib')
    env.Tool('EventLib')
    env.Tool('LdfEventLib')
    env.Tool('addLibrary', library = env['gaudiLibs'])

def exists(env):
    return 1;
