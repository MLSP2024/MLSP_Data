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

Test Data is now released. Metadata for each subset is included in the Table below:


 language       | age         | years in education  | nr. of L2-languages | hours reading/week | number of native annotators | number of non-native annotators | L1-languages
 ---            | ---         | ---                 |---                  | ---                | ---                         | ---                             | ---
Catalan (trial) | 56.9 (11.0) | 20.9 (4.3)          | 2.7 (1.6)           | 20.1 (31.9)        | 5                           | 5                               | Catalan (5), Spanish (4), German (1) 
Catalan (test)  | 34.8 (15.2) | 17.2 (3.6)          | 2.1 (0.9)           | 7.7 (7.1)          | 21                          | 53                              | Spanish (56), Basque (1), English (1), German (1) | 
English         | 22.6 (3.9)  | 16.1 (2.5)          | 2.2 (0.8)           | 16.0 (14.2)        | 10                          | 11                              | English (10), Chinese (3), Urdu (3), Persian (2), Assamese(1), Italian(1), Kurdish (1)
Filipino        | 26.4 (5.9)  | 15.6 (0.8)          | 2.2 (0.4)           | 17.3 (12.9)        | 10                          | 0                               | Filipino (10)
French (LCP)    | 26.7 (3.7)  | 21.4 (2.9)          | 3.2 (1.3)           | 13.1 (8.5)         | 0                           | 10                              | Arabic (2), Mandarin (2), German (1), Hindi (1), Italian (1), Japanese (1), Spanish (1), Turkish (1)
French (LS)     | 22.7 (1)    | 19.8 (1.1)          | 2.4 (0.5)           | 5.6 (2.1)          | 10                          | 0                               | French (10)
German          | 29.3 (7.1)  | 18.5 (2.3)          | 3.3 (2.1)           | 10.2 (8.0)         | 10                          | 0                               | German (10)
Italian         | 35.7 (7.4)  | 19.25 (2.1)         | 2.1 (0.7)           | 5.8 (4.1)          | 20                          | 0                               | Italian (20)
Japanese (LCP)  | 40.8 (9.1)  | 18.4 (3.7)          | 1.8 (0.6)           | 5.7 (7.6)          | 0                           | 10                              | English (5), Portuguese & English (1), French (1), French & English (1), Basque & Spanish (1), Swedish (1)
Japanese (LS)   | 54.1 (5.5)  | 16.8 (2.8)          | 1.4 (0.8)           | 15.9 (14.5)        | 10                          | 0                               | Japanese (10)
Portuguese      | -           | -                   | -                   | -                  | 10                          | 0                               | Brazilian Portuguese (10)
Sinhala         | 28.5        | -                   | -                   | -                  | 10                          | -                               | Sinhala (10)
Spanish (trial) | 43.4 (14.2) | 21.8 (3.3)          | 3.0 (1.2)           | 23.6 (33.83)       | 7                           | 3                               | Spanish (7), Polish (1), Italian (1), German (1) 
Spanish (test)  | 18.0 (1.4) | 12.3 (1.5)           | 0.9 (0.5)           | 2.7 (2.8)          | 60                          | 0                               | Spanish (60)

