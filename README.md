[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# wavecar2unk

Converts the VASP WAVECAR to UNK files for wannier90.
This works for non-collinear WAVECARs, which is needed for spin-orbit coupling in wannier90 >= v2.0.0.
However, to use this code, the full k-point grid needs to be contained in the WAVECAR file (i.e., you should run a nscf calculation with ISYM=-1 or already include the tag as recommended in the case of spin-orbit coupling).
To use non-collinear calculations with wannier90, you need to enable support for v2 in VASP.
The steps are as follows:
1. [Install](#Installation) wavecar2unk using `pip`.
2. Apply the patch `mlwf.patch` from [Chengcheng-Xiao/VASP2WAN90_v2_fix](https://github.com/Chengcheng-Xiao/VASP2WAN90_v2_fix). E.g.,
```
curl https://raw.githubusercontent.com/Chengcheng-Xiao/VASP2WAN90_v2_fix/master/mlwf.patch | patch -p0
```
3. Compile VASP with the `-DVASP2WANNIER90v2` in `CPP_OPTIONS` and the path to your compiled wannier90 library `libwannier.a`. E.g.,
```
CPP_OPTIONS= -DHOST=\"LinuxIFC\"\
             -DMPI -DMPI_BLOCK=8000 \
             -Duse_collective \
             -DscaLAPACK \
             -DCACHE_SIZE=4000 \
             -Davoidalloc \
             -Duse_bse_te \
             -Dtbdyn \
             -Duse_shmem \
    	     -DVASP2WANNIER90v2

LLIBS      = /home/user/compile/wannier90-2.1/libwannier.a $(SCALAPACK) $(LAPACK) $(BLAS)
```
4. Use the generated VASP binary to run a SCF calculation.
5. Setup up a calculation for wannier90.
6. Run `wavecar2unk` in the calculation directory where the `wannier90.win` and `WAVECAR` files are.
7. Run VASP with no need for `LWRITE_UNK = True` in the `INCAR` or, more usefully, for the case of non-collinear, where `LWRITE_UNK = True` doesn't work.

## Installation
wavecar2unk is implemented in python and can be installed through `pip`.
Dependencies are kept to a minimum and include standard packages, such as `click` and `pymatgen`.

#### With pip
As always with python, it is highly recommended to use a virtual environment.
To install wavecar2unk, issue the following command,
```
$ pip install wavecar2unk
```
or to install directly from github,
```
$ pip install git+https://github.com/mturiansky/wavecar2unk
```

## Usage
```
Usage: wavecar2unk [OPTIONS]

  Converts the VASP WAVECAR to UNK files for wannier90.

  Args:     input_file (Path): path to WAVECAR file (default='./WAVECAR')
  output_directory (Path): directory where UNKs ar ewritten (default = .)
  verbose (bool): verbose output (default = False)

Options:
  -i, --input_file FILE           input wavecar file (default = ./WAVECAR)
  -o, --output-directory DIRECTORY
                                  output directory where UNKs are written
                                  (default = .)

  -v, --verbose BOOLEAN           verbose output (default = False)
  --help                          Show this message and exit.
```

## Contributing
Contributions are welcome and any potential change or improvement should be submitted as a pull request on [Github](https://github.com/mturiansky/wavecar2unk/pulls) or to [pymatgen](https://github.com/materialsproject/pymatgen/pulls), directly.
