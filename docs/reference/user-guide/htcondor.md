### HTCondor Guide

This guide provides instructions for using HTCondor, including cluster setup, job submission, troubleshooting, and useful commands.

---

### Cluster Setup

#### Pool 1 - Research
- **Central manager node**: `pllimskhpc1`
- **Submit and Execute nodes**: `pllimskhpc123`

#### Pool 2 - Engineering
- **Central manager node**: `pllimsksparky1`
- **Submit and Execute nodes**: `pllimsksparky1234`

---

### Example Submit File

Below is an example `.sub` file for submitting a training job with HTCondor:

```plaintext
# HTCondor submit file to train RoBERTa
universe = vanilla
executable = run_irae_nlp_clinical_longformer.sh
arguments = $(Process)

# Specify job length: "short" (~12 hrs), "medium" (~24 hrs), "long" (~7 days)
+GPUJobLength = "short"

# GPU and memory requirements
request_gpus = 1
request_memory = 10GB

# Output, log, and error file paths
output = logs/log.infer.$(Cluster)_$(Process).out
log = logs/log.infer.$(Cluster)_$(Process).log
error = logs/log.infer.$(Cluster)_$(Process).err

# Submit job
queue 1
```

---



### Example Workflow

1. Prepare an executable (e.g., shell script, Python script, or Docker container) and a `.sub` file.
2. Submit your job:
   ```bash
   condor_submit submit.sub
   ```
3. Monitor job status:
   ```bash
   condor_q
   ```
4. View detailed job analysis:
   ```bash
   condor_q -better-analyze <job_id>
   ```
5. Check output and logs (specified in the `.sub` file).
6. Terminate a job:
   ```bash
   condor_rm <job_id>
   ```

---


### Common HTCondor Commands

#### Check Nodes
```bash
condor_status
condor_status -compact
condor_status -compact -constraint 'TotalSlotGpus > 0'
condor_status -claimed
```

#### Check Jobs
```bash
condor_q
condor_q -all
condor_history
```

#### Debugging Jobs
```bash
condor_q -better-analyze <job_id>
```


---

### Job Submission Notes

- To prevent overloading the cluster, set the following properties in your submit file:
    - `max_idle`: Maximum number of idle jobs in the queue.
    - `max_materialize`: Maximum number of jobs to execute simultaneously.

- To ensure compatibility with shared filesystems:
```plaintext
Requirements = TARGET.UidDomain == "mskcc.org" && \
               TARGET.FileSystemDomain == "mskcc.org"
```

- To disable specific nodes:
```plaintext
Requirements = (Machine != "pllimsksparky2.mskcc.org")
```

---

### Troubleshooting

- **Exec format error**: Ensure the script starts with the correct shebang (e.g., `#!/bin/bash` for Bash scripts).
- **MemoryError**: Increase memory allocation in the submit file:
  ```plaintext
  request_memory = 16GB
  ```
- **Job stuck in hold**: Use the following command to find the issue:
  ```bash
  condor_q -l
  ```
  Check the `HoldReason` key for details.

---

### Useful Guides

- [HTCondor Full Manual](https://htcondor.readthedocs.io/en/v8_8/)
- [Running Jobs Steps](https://htcondor.readthedocs.io/en/v8_8/users-manual/running-a-job-steps.html)
- [Submitting Multiple Jobs](https://chtc.cs.wisc.edu/uw-research-computing/multiple-jobs)
- [GPU Jobs](https://chtc.cs.wisc.edu/gpu-jobs.shtml)
- [Using a Shared Filesystem](https://htcondor.readthedocs.io/en/v8_8/users-manual/submitting-a-job.html#submitting-jobs-using-a-shared-file-system)

---

> **_Caution_**: Always test your submit file and program with a small number of jobs before scaling up to prevent resource waste and low submission priority. Use `condor_submit -dry-run` for debugging.