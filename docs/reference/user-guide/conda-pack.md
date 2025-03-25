# Using `conda-pack` for Packing and Unpacking Conda Environments

This guide explains how to install `conda-pack`, pack an existing Conda environment, unpack it, and set it up under a new name in a specified Conda installation.


## Installing `conda-pack`
`conda-pack` is not included by default in Conda. To install it, use:

```bash
conda install -c conda-forge conda-pack
```

or 

Install from PyPI:

```bash
pip install conda-pack
```

## Packing an Existing Conda Environment
To create a packed Conda environment archive, use the following command:

```bash
conda pack -n my_env -o my_env.tar.gz
```

Replace `my_env` with the name of your existing Conda environment. This will generate a `.tar.gz` file that can be transferred and unpacked elsewhere.

## Unpacking and Registering the Environment

### Prerequisites
- You have a packed Conda environment as a `.tar.gz` file, e.g., `conda-env-cdm.tar.gz`.
- You want to unpack this environment under a new name in a specific Conda installation.

### 1. Navigate to the Conda `envs` Directory
Move to the `envs` directory inside your Conda installation where you want to unpack the environment:

```bash
cd /username/miniconda3/envs
```

### 2. Create a Directory for the New Environment
Make a directory with the desired environment name:

```bash
mkdir new-env-name
```

### 3. Unpack the Conda Environment
Extract the `.tar.gz` file into the newly created directory:

```bash
tar -xzf /gpfs/mindphidata/fongc2/conda-env-cdm.tar.gz -C new-env-name
```

### 4. Run `conda-unpack`
This step ensures that any hardcoded paths in the environment are fixed:

```bash
source new-env-name/bin/activate
conda-unpack
```

### 5. Verify the Environment is Recognized
Check whether Conda detects the new environment:

```bash
conda env list
```

If the new environment does not appear, manually register it by appending its directory:

```bash
conda config --append envs_dirs /username/miniconda3/envs
```

### 6. Activate the Environment
Once the setup is complete, activate the new environment:

```bash
conda activate new-env-name
```

