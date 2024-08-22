from ..loader import DatasetLoader
from sklearn.utils import Bunch

_loader = DatasetLoader()

def load_data_clinical_patient()  -> Bunch:
    """Load and return the MSK-IMPACT clinical patient dataset (deidentified).

    Returns:
        data: Dictionary-like object, with the following attributes.
            data: pandas DataFrame
                The data matrix.
            description_columns: list
                The names of the dataset columns.  (Future release)
            description_dataset: str
                The full description of the dataset.  (Future release)
            filename: str
                The path to the location of the data.  (Future release)

    Examples
    --------
    - TODO, maybe: Link to a jupyter notebook
    """
    df = _loader._load_impact_data_clinical_patient()
    output = Bunch(data=df)
    return output

def load_data_clinical_sample():
    """Load and return the MSK-IMPACT clinical sample dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_clinical_sample()
    output = Bunch(data=df)
    return output

def load_data_timeline_surgery():
    """Load and return the MSK-IMPACT surgical timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_surgery()
    output = Bunch(data=df)
    return output

def load_data_timeline_radiation():
    """Load and return the MSK-IMPACT radiation therapy timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_radiation()
    output = Bunch(data=df)
    return output

def load_data_timeline_treatment():
    """Load and return the MSK-IMPACT treatment timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_treatment()
    output = Bunch(data=df)
    return output

def load_data_timeline_diagnosis():
    """Load and return the MSK-IMPACT diagnosis timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_diagnosis()
    output = Bunch(data=df)
    return output

def load_data_timeline_specimen():
    """Load and return the MSK-IMPACT specimen timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_specimen()
    output = Bunch(data=df)
    return output

def load_data_timeline_specimen_surgery():
    """Load and return the MSK-IMPACT specimen surgery timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_specimen_surgery()
    output = Bunch(data=df)
    return output

def load_data_timeline_gleason():
    """Load and return the MSK-IMPACT Gleason score timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_gleason()
    output = Bunch(data=df)
    return output

def load_data_timeline_pdl1():
    """Load and return the MSK-IMPACT PD-L1 timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_pdl1()
    output = Bunch(data=df)
    return output

def load_data_timeline_mmr():
    """Load and return the MSK-IMPACT MMR timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_mmr()
    output = Bunch(data=df)
    return output

def load_data_timeline_prior_meds():
    """Load and return the MSK-IMPACT prior medications timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_prior_meds()
    output = Bunch(data=df)
    return output

def load_data_timeline_tumor_sites():
    """Load and return the MSK-IMPACT tumor sites timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_tumor_sites()
    output = Bunch(data=df)
    return output

def load_data_timeline_follow_up():
    """Load and return the MSK-IMPACT follow-up timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_follow_up()
    output = Bunch(data=df)
    return output

def load_data_timeline_progression():
    """Load and return the MSK-IMPACT progression timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_progression()
    output = Bunch(data=df)
    return output

def load_data_timeline_cancer_presence():
    """Load and return the MSK-IMPACT cancer presence timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_cancer_presence()
    output = Bunch(data=df)
    return output

def load_data_timeline_ecog_kps():
    """Load and return the MSK-IMPACT ECOG-KPS timeline dataset (deidentified).

    Returns
    -------
    data : :class:`~sklearn.utils.Bunch`
        Dictionary-like object, with the following attributes.

        data : pandas DataFrame
            The data matrix.
        description_columns (Future release): list
            The names of the dataset columns.
        description_dataset (Future release): str
            The full description of the dataset.
        filename (Future release): str
            The path to the location of the data.
    """
    df = _loader._load_impact_data_timeline_ecog_kps()
    output = Bunch(data=df)
    return output
