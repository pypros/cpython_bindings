from distutils import sysconfig
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import os

class custom_build_ext(build_ext):
    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        suffix = sysconfig.get_config_var('EXT_SUFFIX')
        ext = os.path.splitext(filename)[1]
        return filename.replace(suffix, "") + ext


setup(
    name='spam',
    version='0.1.0',
    packages=find_packages(),
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            name='spam',
            # the files to compile into our module relative to ``setup.py``
            sources=['spammodule.c'],     
         ),
    ],
    cmdclass={"build_ext": custom_build_ext},
)

