# Authors: Robert Luke <mail@robertluke.net>
#
# License: BSD (3-clause)

import numpy as np


def extract_isi(raw):
    """
    Extract inter stimulus interval information.

    Extracts the ISI from provided file. It reports the difference between
    each trigger. If you wish to get the ISI for a subset of triggers then
    first remove unwanted triggers.

    Parameters
    ----------
    raw : instance of Raw
        fNIRS data.

    Returns
    -------
    isi_info : Summary of file ISI
        Array containing all the ISIs.
    """

    return np.diff(raw.annotations.onset)
