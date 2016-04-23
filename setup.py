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
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
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
