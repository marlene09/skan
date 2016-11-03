from __future__ import absolute_import
from setuptools import setup

descr = """skan: skeleton analysis in Python.

Inspired by the "Analyze skeletons" Fiji plugin, by Ignacio Arganda-Carreras.
"""

DISTNAME            = 'skan'
DESCRIPTION         = 'Analysis of object skeletons'
LONG_DESCRIPTION    = descr
MAINTAINER          = 'Juan Nunez-Iglesias'
MAINTAINER_EMAIL    = 'juan.n@unimelb.edu.au'
URL                 = 'https://github.com/jni/skeleton-analysis'
LICENSE             = 'BSD 3-clause'
DOWNLOAD_URL        = 'https://github.com/jni/skeleton-analysis'
VERSION             = '0.1-dev'
PYTHON_VERSION      = (3, 5)
INST_DEPENDENCIES   = {} 


if __name__ == '__main__':

    setup(name=DISTNAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        license=LICENSE,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
        ],
        packages=['skan'],
        package_data={},
        install_requires=INST_DEPENDENCIES,
        scripts=[]
    )
