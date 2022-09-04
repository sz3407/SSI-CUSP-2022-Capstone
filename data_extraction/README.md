## Data Extraction

This directory contains files related to the data extraction pipeline designed for this project.

### Files

#### "example_parser.ipynb"
> This notebook outlines the extraction process used to rebuild the State Payment Tables. Note this file is dependent on certain directory structure and may not run by default. This notebook is intended to be representative of the process performed. To repeat exactly, one may have to define their own notebook environment.

### "util" directory

#### "state_constants.csv"
> This file contains several String forms of representation for the fifty states and D.C. to be used in the parser.

#### "errata_list.py"
> This file contains a list of known misrecognition strings and the "correct" forms for Regex replacement.

#### "benef_hc" directory
> This directory contains files for *benefits fixes* for each report year.

#### "benef_patterns" directory
> This directory contains files for *benefits patterns* base structure and adjustments for each report year.

#### "liv_arr_hc" directory
> This directory contains files for *living arrangements fixes* for each report year.

#### "subcats" directory
> This directory contains files for *subcategories adjustments* base structure and adjustments for each report year.
