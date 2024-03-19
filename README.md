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

All Test Data is now released in full. Participant submissions should be made via the [MLSP_Participants](https://github.com/MLSP2024/MLSP_Participants) Repository.

Metadata for the annotators of each subset is included in the Table below:

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

Further metadata on the texts in each subset is below. The summary statistics are based solely on the Trial data and are not guaranteed to be the same for the Test data.


 language       |  Target Group        | Text Genre           | Mean Complexity | Mean Context Length | Mean Unique Subs
 ---            | ---                  | ---                  |---              | ---                 | ---                  
Catalan         | Varied               | News                 | 0.487 (0.125)   | 239.5 (70.1)        | 14.2 (3.4) 
English         | University Students  | Wikibooks            | 0.200 (0.201)   | 111.0 (37.0)        |  6.2 (1.9) 
Filipino        | University Staff     | Educational Books    | 0.171 (0.126)   |  64.1 (22.1)        |  4.0 (1.1) 
French          | Language Learners    | Varied               | 0.371 (0.229)   | 129.1 (45.6)        | 10.1 (3.5) 
German          | High-School Students | Wiki / Literary      | 0.413 (0.191)   | 195.7 (59.6)        |  8.1 (2.8) 
Italian         | Native Speakers      | Wikibooks/Wikiquote  | 0.248 (0.168)   | 168.4 (67.6)        |  7.8 (3.0) 
Japanese        | Language Learners    | Varied               | 0.259 (0.173)   |  37.8 (7.3)         | 15.8 (4.6)
Portuguese      | MTurk Workers        | Varied               | 0.273 (0.165)   | 165.9 (74.1)        |  5.4 (1.2)
Sinhala         | University Staff     | News / Religious     | 0.243 (0.214)   | 163.4 (52.6)        |  4.3 (0.6)
Spanish         | Varied               | Educational Books    | 0.449 (0.233)   | 178.7 (48.1)        | 10.9 (3.8)




