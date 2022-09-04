## Federal Benefits

This directory contains files related to extracting Federal benefit amounts from each data report.

### Files

#### "fed_benefs_extraction.ipynb"
> This notebook outlines the process for extracting the Federal Payment Table from each report. There are two distinct forms that this table may take, depending on the report year. The first structure is found in reports between 1990 and 2000, inclusively. The second structure is found in all later reports, 2004 to 2011.

#### "fed_benefs_joining.ipynb"
> This notebook outlines the process for reshapping and joining the two different forms of Federal Payment Tables. This notebook uses the two output *csv* files from the *fed_benefs_extraction.ipynb* notebook.

#### "1990_2000_fed_benefits.csv"
> This file contains the Federal benefits for the report years 1990 through 2000. 

| Year | Living Arrangement            | Individual | Couple | 
| -----|:----------------------------: | -----------| -------|
| 1990 | Living independently          |            |        |
| 1990 | Living in household of another|            |        |
| 1990 | Medicaid facility             |            |        |
| 1990 | Essential person              |            |        |

#### "2004_2011_fed_benefits.csv"
> This file contains the Federal benefits for the report years 2004 through 2011.

| Year | Living Arrangement            | Individual | Couple | Essential Person | 
| -----|:----------------------------: | -----------| -------| -----------------|
| 2004 | Living independently          |            |        |                  |
| 2004 | Living in household of another|            |        |                  |
| 2004 | Medicaid facility             |            |        |                  |

#### "federal_benefits_joined.csv"
> This file contains the Federal benefits for all years, restructured to matching form. This is the output file of *fed_benefs_joining.ipynb*. 


