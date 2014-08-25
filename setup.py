from setuptools import setup, find_packages, Extension

import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), 'src/'))
import py_qcode as pq

squoct_dist = Extension('squoct_dist', 
						sources = ['src/c/squoct_dist.c'])

setup(
    name='py_qcode',
    version='{0}.{1}.{2}'.format(*pq.__version__),
    url='http://bcriger.github.com/py_qcode/',
    author='Ben Criger',
    author_email='bcriger@gmail.com',
    package_dir={'': 'src'},
    packages=['py_qcode'],
    include_package_data=False,
    ext_modules=[squoct_dist]
)
