from ..loader import DatasetLoader
from sklearn.utils import Bunch

_loader = DatasetLoader()

def load_data_clinical_patient() -> Bunch:
    """Load and return the MSK-IMPACT clinical patient dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** : list
            The names of the dataset columns. (Future release)
        - **description_dataset** : str
            The full description of the dataset. (Future release)
        - **filename** : str
            The path to the location of the data. (Future release)

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_clinical_patient

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_clinical_patient = load_data_clinical_patient()

    # Access the data
    df_clin_p = df_clinical_patient['data']

    # Display the first few rows of the data
    print(df_clin_p.head())
    ```
    """
    df = _loader._load_impact_data_clinical_patient()
    output = Bunch(data=df)
    return output

def load_data_clinical_sample() -> Bunch:
    """Load and return the MSK-IMPACT clinical sample dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    -
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_clinical_sample

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_clinical_sample = load_data_clinical_sample()

    # Access the data
    df_clin_s = df_clinical_sample['data']

    # Display the first few rows of the data
    print(df_clin_s.head())
    ```
    """
    df = _loader._load_impact_data_clinical_sample()
    output = Bunch(data=df)
    return output

def load_data_timeline_surgery() -> Bunch:
    """Load and return the MSK-IMPACT surgical timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_surgery

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_surgery = load_data_timeline_surgery()

    # Access the data
    df_surg = df_timeline_surgery['data']

    # Display the first few rows of the data
    print(df_surg.head())
    ```
    """
    df = _loader._load_impact_data_timeline_surgery()
    output = Bunch(data=df)
    return output

def load_data_timeline_radiation() -> Bunch:
    """Load and return the MSK-IMPACT radiation therapy timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_radiation

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_radiation = load_data_timeline_radiation()

    # Access the data
    df_rad = df_timeline_radiation['data']

    # Display the first few rows of the data
    print(df_rad.head())
    ```
    """
    df = _loader._load_impact_data_timeline_radiation()
    output = Bunch(data=df)
    return output

def load_data_timeline_treatment() -> Bunch:
    """Load and return the MSK-IMPACT treatment timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_treatment

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_treatment = load_data_timeline_treatment()

    # Access the data
    df_treat = df_timeline_treatment['data']

    # Display the first few rows of the data
    print(df_treat.head())
    ```
    """
    df = _loader._load_impact_data_timeline_treatment()
    output = Bunch(data=df)
    return output

def load_data_timeline_diagnosis() -> Bunch:
    """Load and return the MSK-IMPACT diagnosis timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_diagnosis

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_diagnosis = load_data_timeline_diagnosis()

    # Access the data
    df_diag = df_timeline_diagnosis['data']

    # Display the first few rows of the data
    print(df_diag.head())
    ```
    """
    df = _loader._load_impact_data_timeline_diagnosis()
    output = Bunch(data=df)
    return output

def load_data_timeline_specimen() -> Bunch:
    """Load and return the MSK-IMPACT specimen timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_specimen

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_specimen = load_data_timeline_specimen()

    # Access the data
    df_spec = df_timeline_specimen['data']

    # Display the first few rows of the data
    print(df_spec.head())
    ```
    """
    df = _loader._load_impact_data_timeline_specimen()
    output = Bunch(data=df)
    return output

def load_data_timeline_specimen_surgery() -> Bunch:
    """Load and return the MSK-IMPACT specimen surgery timeline dataset (deidentified).

    Returns
        data : Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_specimen_surgery

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_specimen_surgery = load_data_timeline_specimen_surgery()

    # Access the data
    df_spec_surg = df_timeline_specimen_surgery['data']

    # Display the first few rows of the data
    print(df_spec_surg.head())
    ```
    """
    df = _loader._load_impact_data_timeline_specimen_surgery()
    output = Bunch(data=df)
    return output

def load_data_timeline_radiation() -> Bunch:
    """Load and return the MSK-IMPACT radiation therapy timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_radiation

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_radiation = load_data_timeline_radiation()

    # Access the data
    df_rad = df_timeline_radiation['data']

    # Display the first few rows of the data
    print(df_rad.head())
    ```
    """
    df = _loader._load_impact_data_timeline_radiation()
    output = Bunch(data=df)
    return output

def load_data_timeline_treatment() -> Bunch:
    """Load and return the MSK-IMPACT treatment timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_treatment

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_treatment = load_data_timeline_treatment()

    # Access the data
    df_treat = df_timeline_treatment['data']

    # Display the first few rows of the data
    print(df_treat.head())
    ```
    """
    df = _loader._load_impact_data_timeline_treatment()
    output = Bunch(data=df)
    return output


def load_data_timeline_specimen() -> Bunch:
    """Load and return the MSK-IMPACT specimen timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_specimen
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_specimen = load_data_timeline_specimen()
    >>> df_spec = df_timeline_specimen['data']
    >>> df_spec.head()
    """
    df = _loader._load_impact_data_timeline_specimen()
    output = Bunch(data=df)
    return output

def load_data_timeline_specimen_surgery() -> Bunch:
    """Load and return the MSK-IMPACT specimen surgery timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_specimen_surgery

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_specimen_surgery = load_data_timeline_specimen_surgery()

    # Access the data
    df_specimen_surgery = df_timeline_specimen_surgery['data']

    # Display the first few rows of the data
    print(df_specimen_surgery.head())
    ```
    """
    df = _loader._load_impact_data_timeline_specimen_surgery()
    output = Bunch(data=df)
    return output

def load_data_timeline_gleason() -> Bunch:
    """Load and return the MSK-IMPACT Gleason score timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_gleason
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_gleason = load_data_timeline_gleason()
    >>> df_gleason = df_timeline_gleason['data']
    >>> df_gleason.head()
    """
    df = _loader._load_impact_data_timeline_gleason()
    output = Bunch(data=df)
    return output

def load_data_timeline_pdl1() -> Bunch:
    """Load and return the MSK-IMPACT PD-L1 timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_pdl1
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_pdl1 = load_data_timeline_pdl1()
    >>> df_pdl1 = df_timeline_pdl1['data']
    >>> df_pdl1.head()
    """
    df = _loader._load_impact_data_timeline_pdl1()
    output = Bunch(data=df)
    return output

def load_data_timeline_mmr() -> Bunch:
    """Load and return the MSK-IMPACT MMR timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_mmr
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_mmr = load_data_timeline_mmr()
    >>> df_mmr = df_timeline_mmr['data']
    >>> df_mmr.head()
    """
    df = _loader._load_impact_data_timeline_mmr()
    output = Bunch(data=df)
    return output

def load_data_timeline_prior_meds() -> Bunch:
    """Load and return the MSK-IMPACT prior medications timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_prior_meds
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_prior_meds = load_data_timeline_prior_meds()
    >>> df_prior_meds = df_timeline_prior_meds['data']
    >>> df_prior_meds.head()
    """
    df = _loader._load_impact_data_timeline_prior_meds()
    output = Bunch(data=df)
    return output

def load_data_timeline_tumor_sites() -> Bunch:
    """Load and return the MSK-IMPACT tumor sites timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_tumor_sites
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_tumor_sites = load_data_timeline_tumor_sites()
    >>> df_tumor_sites = df_timeline_tumor_sites['data']
    >>> df_tumor_sites.head()
    """
    df = _loader._load_impact_data_timeline_tumor_sites()
    output = Bunch(data=df)
    return output

def load_data_timeline_follow_up() -> Bunch:
    """Load and return the MSK-IMPACT follow-up timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_follow_up
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_follow_up = load_data_timeline_follow_up()
    >>> df_follow_up = df_timeline_follow_up['data']
    >>> df_follow_up.head()
    """
    df = _loader._load_impact_data_timeline_follow_up()
    output = Bunch(data=df)
    return output

def load_data_timeline_progression() -> Bunch:
    """Load and return the MSK-IMPACT progression timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_progression
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_progression = load_data_timeline_progression()
    >>> df_progression = df_timeline_progression['data']
    >>> df_progression.head()
    """
    df = _loader._load_impact_data_timeline_progression()
    output = Bunch(data=df)
    return output

def load_data_timeline_cancer_presence() -> Bunch:
    """Load and return the MSK-IMPACT cancer presence timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_cancer_presence

    # Connect to the database
    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    # Load the dataset
    df_timeline_cancer_presence = load_data_timeline_cancer_presence()

    # Access the data
    df_cancer_presence = df_timeline_cancer_presence['data']

    # Display the first few rows of the data
    print(df_cancer_presence.head())
    """
    df = _loader._load_impact_data_timeline_cancer_presence()
    output = Bunch(data=df)
    return output

def load_data_timeline_ecog_kps() -> Bunch:
    """Load and return the MSK-IMPACT ECOG-KPS timeline dataset (deidentified).

    Returns
        data: Dictionary-like object, with the following attributes.

        - **data** : pandas DataFrame
            The data matrix.
        - **description_columns** (Future release) : list
            The names of the dataset columns.
        - **description_dataset** (Future release) : str
            The full description of the dataset.
        - **filename** (Future release) : str
            The path to the location of the data.

    Examples
    --------
    >>> from msk_cdm.datasets import connect_to_db
    >>> from msk_cdm.datasets.impact import load_data_timeline_ecog_kps
    >>>
    >>> auth_file='path/to/config.txt'
    >>> connect_to_db(auth_file=auth_file)
    >>> df_timeline_ecog_kps = load_data_timeline_ecog_kps()
    >>> df_ecog_kps = df_timeline_ecog_kps['data']
    >>> df_ecog_kps.head()
    """
    df = _loader._load_impact_data_timeline_ecog_kps()
    output = Bunch(data=df)
    return output

