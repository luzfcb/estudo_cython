try:
    from setuptools import setup, Extension, Distribution
except ImportError:
    from distutils.core import setup, Extension, Distribution

from Cython.Distutils import build_ext

#from distutils.core import setup
#from distutils.extension import Extension

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

ext_modules=[
    Extension("nbioapi",
              ["nitgen/nbioapi.pyx"],
              include_dirs=['nitgen', 'nitgen/headers', 'libs/linux_x86_x64'],
              extra_link_args=['nitgen/libNBioBSP.so'],
              libraries=["m"]) # Unix-like specific
]

setup(
  name = "nbioapi",
  version='0.0.0',
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules,
  zip_safe=False,
  package_dir = {'': 'nitgen'},
  distclass=BinaryDistribution,
  include_package_data=True,
)
