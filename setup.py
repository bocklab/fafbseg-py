from setuptools import setup, find_packages
import re


VERSIONFILE = "fafbseg/__version__.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    requirements = [l for l in requirements if not l.startswith('#')]

setup(
    name='fafbseg',
    version=verstr,
    packages=find_packages(),
    license='GNU GPL V3',
    description='Tools to work with auto-segmented FAFB data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://fafbseg-py.readthedocs.io',
    project_urls={
     "Documentation": "https://fafbseg-py.readthedocs.io",
     "Source": "https://github.com/navis-org/fafbseg-py",
     "Changelog": "https://github.com/navis-org/fafbseg-py/releases",
    },
    author='Philipp Schlegel',
    author_email='pms70@cam.ac.uk',
    keywords='FAFB neuron segmentation FlyWire Google synapses',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=requirements,
    extras_require={},
    python_requires='>=3.7',
    zip_safe=False,
    include_package_data=True
)
