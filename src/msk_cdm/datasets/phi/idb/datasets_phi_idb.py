
from ...loader import DatasetLoader
from sklearn.utils import Bunch

_loader = DatasetLoader()

def load_demographics_idb() -> Bunch:
    """Load and return the IDB demographics dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_demographics_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_demographics = load_demographics_idb()

    # Access the data
    df = df_demographics['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_demographics()
    data = Bunch(data=df)
    return data

def load_radiology_reports_idb() -> Bunch:
    """Load and return the IDB radiology reports dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_radiology_reports_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_radiology_reports = load_radiology_reports_idb()

    # Access the data
    df = df_radiology_reports['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_radiology_reports()
    data = Bunch(data=df)
    return data

def load_pathology_reports_idb() -> Bunch:
    """Load and return the IDB pathology reports dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_pathology_reports_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_pathology_reports = load_pathology_reports_idb()

    # Access the data
    df = df_pathology_reports['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_pathology_reports()
    data = Bunch(data=df)
    return data

def load_surgeries_idb() -> Bunch:
    """Load and return the IDB surgeries dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_surgeries_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_surgeries = load_surgeries_idb()

    # Access the data
    df = df_surgeries['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_surgeries()
    data = Bunch(data=df)
    return data

def load_diagnosis_idb() -> Bunch:
    """Load and return the IDB diagnosis dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_diagnosis_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_diagnosis = load_diagnosis_idb()

    # Access the data
    df = df_diagnosis['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_diagnosis()
    data = Bunch(data=df)
    return data

def load_medications_idb() -> Bunch:
    """Load and return the IDB medications dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_medications_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_medications = load_medications_idb()

    # Access the data
    df = df_medications['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_medications()
    data = Bunch(data=df)
    return data

def load_radiation_idb() -> Bunch:
    """Load and return the IDB radiation dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_radiation_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_radiation = load_radiation_idb()

    # Access the data
    df = df_radiation['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_radiation()
    data = Bunch(data=df)
    return data

def load_interventional_radiology_idb() -> Bunch:
    """Load and return the IDB interventional radiology dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_interventional_radiology_idb

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_interventional_radiology = load_interventional_radiology_idb()

    # Access the data
    df = df_interventional_radiology['data']

    # Display the first few rows of the data
    print(df.head())
    ```
    """
    df = _loader._load_phi_idb_interventional_radiology()
    data = Bunch(data=df)
    return data
