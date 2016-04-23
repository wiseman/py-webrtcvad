from setuptools import setup, find_packages, Extension
import glob
import os.path


C_SRC_PREFIX = os.path.join('cbits', 'webrtc', 'common_audio')

c_sources = (
    [os.path.join(
        'cbits', 'pywebrtcvad.c')]
    + glob.glob(
        os.path.join(
            C_SRC_PREFIX,
            'signal_processing',
            '*.c'))
    + glob.glob(
        os.path.join(
            C_SRC_PREFIX,
            'vad',
            '*.c')))


module = Extension('_webrtcvad',
                   define_macros=[('WEBRTC_POSIX', None)],
                   sources=c_sources,
                   include_dirs=['cbits'])


setup(
    name='PackageName',
    version='1.0',
    description='This is a demo package',
    ext_modules=[module],
    py_modules=['webrtcvad'],
    test_suite='nose.collector',
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['nose', 'check-manifest', 'unittest2', 'zest.releaser']
    })
