# R User Guide


In a conda env, do

`conda install -c conda-forge r-base`

using default `r-base` from conda will install old R version (3.6)




## Package Installation
```
# list installed packages
$ R -e "installed.packages()"

# list all packages where an update is available
$ R -e "old.packages()"

# to update only a specific package use install.packages()
$ R -e "install.packages("plotly")"

# to update all packages, without prompts for permission/clarification
$ R -e "update.packages(ask = FALSE)"
```

---
[Documentation adapted from MSK-MIND](https://mskconfluence.mskcc.org/display/MM/R) 

