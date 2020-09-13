import MDAnalysis as mda
from tqdm import tqdm
import sys

def load_ener(files):
    s = ''
    for file in files:
        with open(file, 'r') as f:
            s += f.read()
    return s.splitlines()

def read_ip(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        return mda.Universe(*lines[0].split()), load_ener(lines[1].split()), int(lines[2]), lines[3], lines[4]
        
def main():
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '-help':
        print("\nUsage: trajsplit <input_file>\n")
        print("Input file format:\nSpace separated list of paths of TPR/TRR files\nSpace separated list of paths of CPMD energy files")
        print("Number of output files required\nSuffix for output TRR file names\nSuffix for output CPMD energy file names\n")
        sys.exit(0)
    else:
        ips = read_ip(sys.argv[1])
        
        u, ener, n, trr_sufix, ener_sufix = ips
        
        print(f"Number of frames in TRR: {len(u.trajectory)}")
        
        print(f"Number of frames in ENERGIES: {len(ener)}")
        
        if len(ener) > len(u.trajectory):
            print("Warning: Number of frames in ENERGIES more than TRR, truncating ENERGIES")
            ener = ener[:len(u.trajectory)]
        elif len(ener) < len(u.trajectory):
            print("Error: Number of frames in ENERGIES less than TRR!\nexiting")
            exit(1)
        
        j, k = len(u.trajectory)//n, len(u.trajectory)%n
        lst = [(i * j + min(i, k), (i + 1) * j + min(i + 1, k)) for i in range(n)]
        print(f"Number of frames to be written in each file: {lst[0][1]}")
    
        pbar = tqdm(total=len(lst), position=0, leave=True)

        for i,l in enumerate(lst):
            with open(f'{ener_sufix}{i}', 'w') as f:
                f.write('\n'.join(ener[l[0]:l[1]]))

            with mda.Writer(f'{trr_sufix}{i}.trr', len(u.atoms)) as W:
                for ts in u.trajectory[l[0]:l[1]]:
                    W.write(u)
            
            pbar.update(1)
        
        pbar.close()
        
        exit(0)
        
    
if __name__ == '__main__': main()