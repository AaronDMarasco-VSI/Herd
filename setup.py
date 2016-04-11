from setuptools import setup
import os
import subprocess

import distutils.command.bdist_rpm as orig

class bdist_rpm(orig.bdist_rpm):
  """Custom bdist_rpm command - regenerate herd/bittornado.tar.gz"""

  def run(self):
    try:
      os.unlink('herd/bittornado.tar.gz')
    except:
      pass
    owd = os.getcwd()
    os.chdir('herd')
    args = ['tar', 'czf', 'bittornado.tar.gz', 'BitTornado']
    subprocess.call(args)
    os.chdir(owd)
    orig.bdist_rpm.run(self)

setup(
    name='Herd',
    version='0.1.1',
    author='Russ Garret',
    author_email='russ@garrett.co.uk',
    packages=['herd', 'herd.BitTornado', 'herd.BitTornado.BT1'],
    scripts=[],
    url='https://github.com/russss/Herd',
    description='A simpler implementation of Twitter Murder in python.  Deploy files distributedly using the Torrent protocol.',
    long_description=open('README.md').read(),
    install_requires=[],
    cmdclass={
      'bdist_rpm': bdist_rpm,
    },
    entry_points={
        'console_scripts': [
            'herd = herd.herd:entry_point',
            ],
        },
    data_files=[('herd', ['herd/bittornado.tar.gz'])]
)
