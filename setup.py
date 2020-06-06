from setuptools import setup, find_packages


VERSION = '0.0.1'

with open('README.md', 'r') as f:
    long_desc = f.read()

setup(
    name='wavecar2unk',
    version=VERSION,
    author='Mark E. Turiansky',
    author_email='mturiansky@physics.ucsb.edu',
    description=('converts VASP WAVECAR file into UNK files for wannier90'),
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/mturiansky/wavecar2unk',
    packages=find_packages(),
    install_requires=['pymatgen > 2020.4.29', 'click >= 7.1.2'],
    keywords=[
        'physics', 'materials', 'science', 'VASP', 'WAVECAR', 'wannier90'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points='''
        [console_scripts]
        wavecar2unk=wavecar2unk:cli
    ''',
)
