# JupyterHub
## Location

[JupyterHub URL for CDM Development](https://tllihpcmind6/jupyter)

**Login**: MSK credentials. If you are unable to log in, please contact one of the MIND engineers to have you added as a linux user of the pllimsksparky2 machine and you must log into this machine once using the terminal in order to set up your home directory. The first time you log in, jupyterhub may take a minute or so to spawn the user server and jupyter lab environment. Since an MSK self-signed certificate is being used, your browser may warn you that the connection is insecure, but the connection is secure (https encrpyted) and only lacks trust verification with a third-party certificate authority which is not needed for security in the internal MSK network. On Chrome click on the 'Advanced' button to continue to proceed to using the web application. 

**Base Directory**: The directory under which jupyterhub's file view launches is `/mind_data/shared_data_folder`. You may choose to create a sub-directory under this directory with your username and store your notebooks in there. You may control access to your notebooks via linux file permissions. Please contact one of the MIND engineers to set up the sub-directory for you.




## Creating Python Virtual Environments

> Note: These instructures are for creating virtual environments in Jupyterhub only. For Python environments on the terminal, please see Python.

Virtual environments [ref1] help you to isolate your execution environment from other notebooks and other users. You may use virtual environment to select specific version of python and its of libraries without having to worry about collisions. Follow these instructions below to setup, test and teardown your virtual environments for notebooks on Jupyterhub.

### Setup

Open a terminal in your Jupyter environment by selecting File -> New -> Terminal and execute the following commands. 

$ cd [LOCATION-WHERE-YOU-WANT-TO-CREATE-THE-VIRTUAL-ENV]
#### Creating a Virtual Environment
```
# create the virtual environment
python3 -m venv my-test-venv

# activate the virtual environment
$ source my-test-venv/bin/activate

# upgrade pip
$ python3 -m pip install --upgrade pip

# install ipykernel
$ pip install ipykernel

# Register this env with jupyter lab. It will now show up in the
# launcher & kernels list once you refresh the page
$ python3 -m ipykernel install --user --name my-test-venv --display-name "my test virtual env"

# List kernels to ensure it was created successfully
$ jupyter kernelspec list

my-test-venv    /home/pashaa/.local/share/jupyter/kernels/my-test-venv
python3      /gpfs/mskmindhdp_emc/sw/env/share/jupyter/kernels/python3

# for testing purposes, install a specific package into this environment
$ pip install fire

# ensure the package installed successfully
$ pip list | grep fire

fire                0.4.0

# deactivate the virtual environment in the terminal
$ deactivate
```
### Test

Now, apply the new kernel to your notebook by first selecting the default kernel (which is typically "Python 3") from the top right corner of your notebook and then selecting your new kernel "my test virtual env". NOTE: It may take a minute for the drop-down list to update. 

Test your new environment by running the following commands in your notebook code cells. 

Verify that you are using python from your virtual env
```
import sys
print(sys.executable)

/gpfs/mskmindhdp_emc/user/pashaa/my-test-venv/bin/python
```
Verify you are able to import the test package and that it belongs to your virtual env
```
import fire
print(fire.__file__)
print(fire.__version__)

'/gpfs/mskmindhdp_emc/user/pashaa/my-test-venv/lib64/python3.6/site-packages/fire/__init__.py'
 0.4.0
```
Alternatively, you can check your dependencies by listing the installed libraries, or checking the details of a specific library.
```
%pip list
or
%pip show pip
```
You can install libraries in your virtual env within your notebook by using the % operator.
```
%pip install <new-lib>
```
### Teardown

Execute the following commands in your jupyter terminal.
#### Uninstall Virtual Environment
```
$ jupyter kernelspec uninstall my-test-venv
$ rm -rf my-test-venv
```



## Creating R Virtual Environments
### Setup

R packages are installed into libraries, which are directories in the file system containing a subdirectory for each package installed there [ref 2]. Users can have one or more libraries, normally specified by the environment variable R_LIBS_USER, if the corresponding directory actually exists (which by default it will not).

Users may set up separate directories for these libraries for separate projects and install project specific libraries into these directories as shown below. 

First, use a terminal to create a project directory in your user space.
```
$ mkdir /gpfs/mskmind_ess/pashaa/my_R_libs_prj1
```
Next, open a Jupyter notebook in Jupyterhub, select the system-wide R kernel and configure R to use this directory as a user libs directory.  
#### R Script in Jupyter IRKernel
```
[1] Sys.getenv('R_LIBS_USER')

	 '~/R/x86_64-pc-linux-gnu-library/4.0'

[2] .libPaths()

	 '/opt/R/4.0.5/lib/R/library'

[3] Sys.setenv(R_LIBS_USER="/gpfs/mskmind_ess/pashaa/my_R_libs_prj1")
[4] .libPaths(c( Sys.getenv('R_LIBS_USER'), .libPaths()  ))
```
### Test

Test your IRKernel environment. 
> NOTE: You may change the order of the paths to make R pick libraries from the system-wide project directory first by changing the order of the libraries in the .libPaths() setup call above. But, in general you may find it beneficial to give precedence to the libraries that you have installed for your project. 
```
[5] Sys.getenv('R_LIBS_USER')

'/gpfs/mskmind_ess/pashaa/my_R_libs_prj1'

[6] .libPaths()

	 '/gpfs/mskmind_ess/pashaa/my_R_libs_prj1''/opt/R/4.0.5/lib/R/library'
```
List the current set of packages, then install a package and list packages again to check if the package has been installed. Note when loading the packages, you must specify the "lib.loc" library location to ensure you are loading from your library. 
```
[7] my_packages <- library()$results[,1]
[8] print(my_packages)

		[1] "bslib"         "cachem"        "commonmark"    "httpuv"       
  		[5] "jquerylib"     "later"         "promises"      "sass"         
  		[9] "sourcetools"   "xtable"        "askpass"       "assertthat"   
		...
		[125] "utf8"          "utils"         "uuid"          "vctrs"        
		[129] "viridisLite"   "vroom"         "withr"         "xfun"         
		[133] "yaml"

[9] install.packages('shiny', lib="/gpfs/mskmind_ess/pashaa/my_R_libs_prj1")

	 	Installing package into ‘/gpfs/mskmind_ess/pashaa/my_R_libs_prj1’
      	(as ‘lib’ is unspecified)

[10] my_packages <- library()$results[,1]
[11] print(my_packages)

	 	[1] "bslib"         "cachem"        "commonmark"    "httpuv"       
  		[5] "jquerylib"     "later"         "promises"      "sass"         
  		[9] "sourcetools"   "xtable"        "askpass"       "assertthat"   
		...
		[125] "utf8"          "utils"         "uuid"          "vctrs"        
		[129] "viridisLite"   "vroom"         "withr"         "xfun"         
		[133] "yaml"          "shiny"

[12] library("shiny", lib.loc="/gpfs/mskmind_ess/pashaa/my_R_libs_prj1")
```
On the terminal, you may check to see if the package and its dependencies have been installed in your project location. 
#### Terminal
```
$ ls /gpfs/mskmind_ess/pashaa/my_R_libs_prj1
bslib  cachem  commonmark  httpuv  jquerylib  later  promises  sass  shiny  sourcetools  xtable
```
More than 1 project directory may be set up in this manner. However, it is advisable to configure R to use one user lib directory at a time so there is no confusion as to where libraries are being installed or uninstalled from. 

### Teardown

You may uninstall a package as follows.
#### R Script in Jupyter IRKernel
```
[12] remove.packages('shiny')
```
For a full teardown, reset the R configuration and remove the project directory. 
```
[13] Sys.setenv(R_LIBS_USER="~/R/x86_64-pc-linux-gnu-library/4.0")
[14] .libPaths(.libPaths()[2])
```
```
$ rm -rf /gpfs/mskmind_ess/pashaa/my_R_libs_prj1
```
## Pre-installed R Packages

For ease of use there is already a set of commonly used packages installed in the base R installation on pllimsksparky2. In addition to the libraries that come with R, we have explicitly installed the following:

* tidyverse
* tidyr
* ggplot2
* tidymodels
* mgcv
* nlme
* car
* randomForest
* multcomp
* glmnet
* survival
* caret
* shiny
* rmarkdown
* BiocManager
* flowCore

Chances are that even if the package you're looking for isn't on the above list, it was probably installed as a dependency. To see a complete list of all installed libraries, open an R terminal and run the following:
#### R script in Jupyter IRKernel
```
> print(library()$results[,1])
```
If you're interested in using a package and can't install it in a virtual environment due to core system dependencies or any other issues, let the MIND Engineering team know.

## Troubleshooting
* **Notebook cells are not executing or are hanging**: Simply restart the kernel by selecting menu item Kernel → Restart Kernel
* **Notbook and terminal not working in Safari**: Make sure you have Safari version 15.4 or higher, and add untrusted cert to keychain to make it trusted (https://github.com/jupyterhub/jupyterhub/issues/292)
* **"Unexpected error while saving file: <notebook_name>.ipynb attempt to write a readonly database"**: Restart your server by going to File→Hub Control Panel. 
* **Trouble initiating Jupyterhub in Safari**: Try Google Chrome
* **Trouble loading, saving, or creating new jupyter notebooks**: Try restarting the Jupyterhub service by:
Going to File -> Hub Control Panel
Click Start My Server




## References
1. [Creating a kernel for virtual environments](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)
2. [R Admin - Managing Libraries](https://cran.r-project.org/doc/manuals/r-release/R-admin.html)
3. [List R packages](https://rpubs.com/Mentors_Ubiqum/list_packages)
4. [Using Virtual Environments in Jupyter Notebook and Python](https://janakiev.com/blog/jupyter-virtual-envs/)

---
[Documentation adapted from MSK-MIND](https://mskconfluence.mskcc.org/display/MM/JupyterHub)