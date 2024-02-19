# MLSP_Data

The public data and evaluation scripts for the MLSP 2024 Shared Task

The Trial Data is found in Data/Trial/

The All/ folder contains the aggregated data for all languages. There are also subfolders for each language with their own data.

Each folder contains 3 files:
 - multilex_SPLIT_LANG_combined - containing Lexical Complexity Prediction and Lexical Simplification data on identical targets and contexts
 - multilex_SPLIT_LANG_lcp - containing Lexical Complexity Prediction data only on targets and contexts taken from the combined data
 - multilex_SPLIT_LANG_ls - containing Lexical Simplification data only on targets and contexts taken from the combined data

The scripts folder contains 2 scripts for evaluation
 - lcp_evaluate.py - the script used for the LCP 2021 shared task. Info on running it is here: https://github.com/MMU-TDMLab/CompLex/
 - ls_evaluate.py - the script used for the TSAR 2022 shared task. Info on running it is here: https://github.com/LaSTUS-TALN-UPF/TSAR-2022-Shared-Task/tree/main

All Trial Data has now been released. Please register your interest in the task to receive updates (registration form at the task website here: https://sites.google.com/view/mlsp-sharedtask-2024/home?authuser=0)

Test Data will be released for all languages by 15th March 2024.
