import pandas as pd
import csv
import argparse

'''
% python Scripts/ls_stats.py Data/Trial/*/multilex_trial_*_ls.tsv
File	Context Length	#Unique Subs
Data/Trial/All/multilex_trial_all_ls.tsv	145.363 (77.646)	7.423 (4.924)
Data/Trial/Catalan/multilex_trial_ca_ls.tsv	239.533 (70.128)	13.167 (3.354)
Data/Trial/English/multilex_trial_en_ls.tsv	111.000 (36.992)	4.500 (1.871)
Data/Trial/Filipino/multilex_trial_fil_ls.tsv	64.067 (22.137)	1.967 (1.098)
Data/Trial/French/multilex_trial_fr_ls.tsv	129.100 (45.564)	8.267 (3.667)
Data/Trial/German/multilex_trial_de_ls.tsv	195.733 (59.604)	7.067 (2.791)
Data/Trial/Italian/multilex_trial_it_ls.tsv	168.400 (67.614)	6.700 (3.075)
Data/Trial/Japanese/multilex_trial_ja_ls.tsv	37.800 (7.303)	14.933 (4.586)
Data/Trial/Portuguese/multilex_trial_pt_ls.tsv	165.900 (74.062)	4.333 (1.269)
Data/Trial/Sinhala/multilex_trial_si_ls.tsv	163.400 (52.554)	3.333 (0.606)
Data/Trial/Spanish/multilex_trial_es_ls.tsv	178.700 (48.075)	9.867 (3.785)
'''


# Column indices in TSAR LS format
MAX_COLS = 32       # Python would yell at us if it's not enough
COLUMNS = range(0, MAX_COLS)
C_CONTEXT = 0
C_TARGET = 1
C_SUBS = range(2, MAX_COLS)


def main(args: argparse.Namespace):

    print('File\tContext Length\t#Unique Subs')
    for input_file in args.input_files:
        df = pd.read_table(
            input_file,
            quoting=csv.QUOTE_NONE,                     # no quoting
            na_values=[''], keep_default_na=False,      # only empty strings are NA
            header=None, names=COLUMNS, engine='python'
            )

        context_length = df[C_CONTEXT].str.len()

        subs = df[[c for c in C_SUBS]]
        not_target = subs.apply(lambda subs: subs!=df[C_TARGET])
        unique_subs = subs.where(not_target).nunique(axis=1, dropna=True)

        print(
            f'{input_file}\t'
            f'{context_length.mean():.3f} ({context_length.std():.3f})\t'
            f'{unique_subs.mean():.3f} ({unique_subs.std():.3f})'
            )

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_files', nargs='+'
        )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse()
    main(args)
