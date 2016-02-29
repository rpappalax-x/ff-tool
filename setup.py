import io
import os

from fftool import __version__
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    README = f.read()
with io.open(os.path.join(here, 'CHANGELOG.md'), encoding='utf8') as f:
    CHANGES = f.read()

extra_options = {
    'packages': find_packages(),
}


setup(name='ff-tool',
      version=__version__,
      description='Firefox CLI test setup tool',
      long_description=README + '\n\n' + CHANGES,
      classifiers=['Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7'
                   'Programming Language :: Python :: 3.4'
                   ],
      keywords='[firefox, test, pref, profile, download, install]',
      author='Johnny Quest',
      author_email='cloud-services-qa@mozilla.org',
      license='MPL2',
      include_package_data=True,
      zip_safe=False,
      entry_points='''
      [console_scripts]
      ff = fftool.main:main
      ''',
      **extra_options
      )
