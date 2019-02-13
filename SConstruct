import sys

VariantDir('cpp_build', 'src', duplicate=0)

if sys.platform == 'win32':
	env = Environment(MSVC_VERSION='10.0', TARGET_ARCH='x86', CCFLAGS=["/MD", "/EHsc", "-O2"])
	env.Program('cpp_build/temperature.exe', Glob('cpp_build/*/*.cpp') + ['cpp_build/main.cpp'], LIBS=['Temperature'], LIBPATH='src/Libs')
elif sys.platform == 'darwin':
    env = Environment(CPPFLAGS=['-std=c++11', "-O2"])
    env.Program('cpp_build/temperature.exe', Glob('cpp_build/*/*.cpp') + ['cpp_build/main.cpp'], LIBS=['Temperature'], LIBPATH='src/Libs')
else:
    env = Environment(CXX='g++-4.9', CPPFLAGS=['-std=c++11', '-pthread', "-O2"])
    env.Program('cpp_build/temperature.exe', Glob('cpp_build/*/*.cpp') + ['cpp_build/main.cpp'], LIBS=['Temperature', 'pthread'], LIBPATH='src/Libs')
