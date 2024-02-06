# Airflow

A DAG (Directed Acyclic Graph) is the core concept of Airflow, collecting Tasks together, organized with dependencies and relationships to say how they should run.
Airflow DAGs can be deployed on tllihpcmind6 and other MSK-MIND servers.


## Steps to Running a DAG
- Clone the DAG repo from [cdm-dags](https://github.com/clinical-data-mining/dags) and create a new branch.
- Duplicate the DAG template file `cdm_TEMPLATE.py` and change the filename (no spaces)
- Within your new DAG file, change `<<<<<CREATE DAG ID>>>>>` to the exact filename, minus .py
- Change `<<<<<YOUR EMAIL>>>>>` to your email to receive updates on errors
- Write your DAG
- From the command line, perform chmod 777 on your DAG file `chmod 777 /mind_data/<my_workspace>/cdm-dags/my_dag.py`
- Copy the DAG you created in your workspace, and paste into the shared Airflow folders (ex. `cp /mind_data/<my_workspace>/cdm-dags/my_dag.py /mind_data/airflow/dags/curation/my_dag.py`) 
  - AVOID MODIFYING FILES WITHIN THE SHARED AIRFLOW FOLDER. THIS CAN RESULT IN WORK STOPPAGE FOR ALL USERS.
- After a few moments, the DAG should appear in the [Airflow UI](https://tllihpcmind6/airflow/home)
- Once you have a functioning dag, commit the dag changes back to the cdm-dag repo. Merge your branch if needed.
