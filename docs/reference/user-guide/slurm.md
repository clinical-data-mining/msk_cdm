# Slurm GPU Job Scheduler

## Introduction

SLURM (Simple Linux Utility for Resource Management) is a powerful and flexible workload manager and job scheduler. It is used to allocate resources, submit, monitor, and manage jobs on high-performance computing clusters.

This guide covers the basics of using SLURM, including submitting jobs, requesting resources, and monitoring their execution.

---

## Table of Contents
- [Submitting a Job with SLURM](#submitting-a-job-with-slurm)
- [Basic SLURM Directives](#basic-slurm-directives)
- [Example SLURM Job Script](#example-slurm-job-script)
- [Running Array Jobs](#running-array-jobs)
- [Monitoring Jobs](#monitoring-jobs)
- [Canceling Jobs](#canceling-jobs)
- [Common SLURM Commands](#common-slurm-commands)

---

## Submitting a Job with SLURM

To submit a job in SLURM, you create a job script that includes directives telling SLURM what resources your job needs, how long it will take, where to write output, etc. This script is submitted using the `sbatch` command.

```bash
sbatch job_script.slurm
```

---

## Basic SLURM Directives

In the job script, directives are defined using the `#SBATCH` prefix, followed by the resource requests or configurations you need for your job.

Here are some common SLURM directives:

| Directive            | Description                                           |
|----------------------|-------------------------------------------------------|
| `--job-name=<name>`   | Sets the job name for easier identification           |
| `--output=<file>`     | File to store standard output (use `%j` for job ID)   |
| `--error=<file>`      | File to store standard error (use `%j` for job ID)    |
| `--ntasks=<num>`      | Number of tasks (CPU cores) required                  |
| `--mem=<size>`        | Memory required for the job (e.g., 4G, 10G, etc.)     |
| `--time=<time>`       | Maximum run time (format: `days-hours:minutes:seconds`) |
| `--partition=<name>`  | Specify the partition or queue to use                 |
| `--gpus=<num>`        | Number of GPUs required                               |
| `--array=<range>`     | Job array (e.g., `0-10`, creates 11 tasks)            |

---

## Example SLURM Job Script

Below is a simple example of a SLURM job script.

```bash
#!/bin/bash
#SBATCH --job-name=train_RoBERTa_infer  # Job name
#SBATCH --output=/gpfs/mindphidata/cdm_repos/github/progression-predict/slurm/logs/log.infer.%j.out  # Output file
#SBATCH --error=/gpfs/mindphidata/cdm_repos/github/progression-predict/slurm/logs/log.infer.%j.err   # Error file
#SBATCH --ntasks=1                      # Run on a single CPU
#SBATCH --mem=10G                       # Memory request
#SBATCH --gpus=1                        # Number of GPUs

# Run the executable with the provided arguments (you may need to adapt this if different arguments are required)
srun ./run_infer_mlflow.sh $SLURM_ARRAY_TASK_ID
```

In this script:
- The `#SBATCH` directives configure the job's resources.
- The `srun` command launches the program, which in this case runs a Python script.



---

## Running Array Jobs

Array jobs allow you to submit multiple similar jobs with one submission. You can specify an array with the `--array` directive.

```bash
#SBATCH --array=0-10  # Submits 11 tasks, with IDs ranging from 0 to 10
```

In your script, you can use the environment variable `$SLURM_ARRAY_TASK_ID` to differentiate tasks in the array.

Example:

```bash
#!/bin/bash
#SBATCH --job-name=array_job
#SBATCH --array=0-10
#SBATCH --output=logs/job_%A_%a.out  # %A is the job ID, %a is the array index

# Command that varies based on the array task ID
srun ./process_data.sh input_file_$SLURM_ARRAY_TASK_ID.txt
```

---

## Monitoring Jobs

To monitor your submitted jobs, you can use the following commands:

- **`squeue`**: Shows the status of all jobs in the queue.
  ```bash
  squeue -u <username>
  ```

- **`scontrol show job <job_id>`**: Shows detailed information about a specific job.

- **`sacct`**: Displays accounting information for your completed jobs.
  ```bash
  sacct -j <job_id>
  ```

---

## Canceling Jobs

You can cancel a running or pending job using the `scancel` command:

```bash
scancel <job_id>
```

To cancel an entire job array, you can omit the task ID, or use the specific task ID to cancel only one task:

```bash
scancel <job_id>               # Cancels the entire array
scancel <job_id>_<task_id>      # Cancels a specific task in the array
```

---

## Common SLURM Commands

- **`sbatch`**: Submits a job script.
  ```bash
  sbatch my_job_script.slurm
  ```

- **`squeue`**: Displays information about jobs in the queue.
  ```bash
  squeue -u <username>
  ```

- **`scancel`**: Cancels a job or set of jobs.
  ```bash
  scancel <job_id>
  ```

- **`sinfo`**: Shows the status of partitions and nodes.
  ```bash
  sinfo
  ```

- **`scontrol`**: Allows you to manage jobs and resources (e.g., show job details).
  ```bash
  scontrol show job <job_id>
  ```

- **`srun`**: Runs parallel tasks within a SLURM job (not typically needed for single-node jobs).

---

## Additional Guides

For further details and advanced usage, consult the official [SLURM documentation](https://slurm.schedmd.com/documentation.html).

