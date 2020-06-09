'''
wavecar2unk
'''

from pathlib import Path

import click
from pymatgen.io.vasp.outputs import Wavecar


__version__ = '0.0.2'


@click.command()
@click.option('-i', '--input_file', default='WAVECAR',
              type=click.Path(exists=True, dir_okay=False),
              help='input wavecar file (default = ./WAVECAR)')
@click.option('-o', '--output-directory', default=str(Path.cwd()),
              type=click.Path(exists=True, file_okay=False),
              help='output directory where UNKs are written (default = .)')
@click.option('-v', '--verbose', is_flag=True,
              help='verbose output (default = False)')
def cli(input_file: Path, output_directory: Path, verbose: bool) -> None:
    '''
    Converts the VASP WAVECAR to UNK files for wannier90.

    Args:
        input_file (Path): path to WAVECAR file (default='./WAVECAR')
        output_directory (Path): directory where UNKs ar ewritten (default = .)
        verbose (bool): verbose output (default = False)
    '''
    Wavecar(input_file, verbose=verbose).write_unks(output_directory)


if __name__ == '__main__':
    cli()
