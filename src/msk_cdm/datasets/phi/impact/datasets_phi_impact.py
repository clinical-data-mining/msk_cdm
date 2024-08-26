from ...loader import DatasetLoader
from sklearn.utils import Bunch

_loader = DatasetLoader()

def load_data_timeline_surgery_phi() -> Bunch:
    """Load and return the surgery timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_surgery_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_surgery = load_data_timeline_surgery_phi()
    df = df_timeline_surgery['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_surgery()
    data = Bunch(data=df)
    return data

def load_data_timeline_radiation_phi() -> Bunch:
    """Load and return the radiation timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_radiation_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_radiation = load_data_timeline_radiation_phi()
    df = df_timeline_radiation['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_radiation()
    data = Bunch(data=df)
    return data

def load_data_timeline_treatment_phi() -> Bunch:
    """Load and return the treatment timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_treatment_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_treatment = load_data_timeline_treatment_phi()
    df = df_timeline_treatment['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_treatment()
    data = Bunch(data=df)
    return data

def load_data_timeline_diagnosis_phi() -> Bunch:
    """Load and return the diagnosis timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_diagnosis_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_diagnosis = load_data_timeline_diagnosis_phi()
    df = df_timeline_diagnosis['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_diagnosis()
    data = Bunch(data=df)
    return data

def load_data_timeline_specimen_phi() -> Bunch:
    """Load and return the specimen timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_specimen_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_specimen = load_data_timeline_specimen_phi()
    df = df_timeline_specimen['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_specimen()
    data = Bunch(data=df)
    return data

def load_data_timeline_specimen_surgery_phi() -> Bunch:
    """Load and return the specimen-surgery timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_specimen_surgery_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_specimen_surgery = load_data_timeline_specimen_surgery_phi()
    df = df_timeline_specimen_surgery['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_specimen_surgery()
    data = Bunch(data=df)
    return data

def load_data_timeline_gleason_phi() -> Bunch:
    """Load and return the Gleason score timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_gleason_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_gleason = load_data_timeline_gleason_phi()
    df = df_timeline_gleason['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_gleason()
    data = Bunch(data=df)
    return data

def load_data_timeline_pdl1_phi() -> Bunch:
    """Load and return the PD-L1 timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_pdl1_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_pdl1 = load_data_timeline_pdl1_phi()
    df = df_timeline_pdl1['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_pdl1()
    data = Bunch(data=df)
    return data

def load_data_timeline_prior_meds_phi() -> Bunch:
    """Load and return the prior medications timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_prior_meds_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_prior_meds = load_data_timeline_prior_meds_phi()
    df = df_timeline_prior_meds['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_prior_meds()
    data = Bunch(data=df)
    return data

def load_data_timeline_tumor_sites_phi() -> Bunch:
    """Load and return the tumor sites timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_tumor_sites_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_tumor_sites = load_data_timeline_tumor_sites_phi()
    df = df_timeline_tumor_sites['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_tumor_sites()
    data = Bunch(data=df)
    return data

def load_data_timeline_follow_up_phi() -> Bunch:
    """Load and return the follow-up timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_follow_up_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_follow_up = load_data_timeline_follow_up_phi()
    df = df_timeline_follow_up['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_follow_up()
    data = Bunch(data=df)
    return data

def load_data_timeline_progression_phi() -> Bunch:
    """Load and return the progression timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_progression_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_progression = load_data_timeline_progression_phi()
    df = df_timeline_progression['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_progression()
    data = Bunch(data=df)
    return data

def load_data_timeline_mmr_phi() -> Bunch:
    """Load and return the MMR timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_mmr_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_mmr = load_data_timeline_mmr_phi()
    df = df_timeline_mmr['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_mmr()
    data = Bunch(data=df)
    return data

def load_data_timeline_cancer_presence_phi() -> Bunch:
    """Load and return the cancer presence timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_cancer_presence_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_cancer_presence = load_data_timeline_cancer_presence_phi()
    df = df_timeline_cancer_presence['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_cancer_presence()
    data = Bunch(data=df)
    return data

def load_data_timeline_ecog_kps_phi() -> Bunch:
    """Load and return the ECOG/KPS timeline dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_timeline_ecog_kps_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_timeline_ecog_kps = load_data_timeline_ecog_kps_phi()
    df = df_timeline_ecog_kps['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_data_timeline_ecog_kps()
    data = Bunch(data=df)
    return data

def load_data_id_mapping_phi() -> Bunch:
    """Load and return the ID mapping dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_id_mapping_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_id_mapping = load_data_id_mapping_phi()
    df = df_id_mapping['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_id_mapping()
    data = Bunch(data=df)
    return data

def load_data_anchor_dates_phi() -> Bunch:
    """Load and return the anchor dates dataset (PHI).

    Returns:
        data: Dictionary-like object, with the following attributes.

            - **data** : pandas DataFrame
                The data matrix.

    Examples
    --------
    ```python
    from msk_cdm.datasets import connect_to_db
    from msk_cdm.datasets.impact import load_data_anchor_dates_phi

    auth_file = 'path/to/config.txt'
    connect_to_db(auth_file=auth_file)

    df_anchor_dates = load_data_anchor_dates_phi()
    df = df_anchor_dates['data']

    print(df.head())
    ```
    """
    df = _loader._load_phi_impact_anchor_dates()
    data = Bunch(data=df)
    return data

