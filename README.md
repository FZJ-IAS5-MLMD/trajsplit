# Trajsplit
Split Gromacs TRR and CPMD energy files.

To install:
- git clone this repo locally
- navigate to the directory
- run ```pip install .```

To run type trajsplit <input_file>

Input file format:
- Space separated list of paths of TPR/TRR files
- Space separated list of paths of CPMD energy files
- Number of output files required
- Suffix for output TRR file names
- Suffix for output CPMD energy file

Example:

```
md1/md1.tpr md1/md1.trr md2/md2.trr md3/md3.trr
md1/ENERGIES md2/ENERGIES md3/ENERGIES
1000
traj
ENERGIES

```