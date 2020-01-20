# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal

from .eda_findpeaks import eda_findpeaks
from .eda_fixpeaks import eda_fixpeaks
from ..signal import signal_formatpeaks
from ..misc import findclosest


def eda_peaks(eda_phasic, sampling_rate=1000, method="neurokit", amplitude_min=0.1):
    """Identify Skin Conductance Responses (SCR) in Electrodermal Activity (EDA).

    Identify Skin Conductance Responses (SCR) peaks in the phasic component of
    Electrodermal Activity (EDA) with different possible methods, such as:

    - `Gamboa, H. (2008)
    <http://www.lx.it.pt/~afred/pub/thesisHugoGamboa.pdf>`_
    - `Kim et al. (2004)
    <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.7385&rep=rep1&type=pdf>`_

    Parameters
    ----------
    eda_phasic : list, array or Series
        The phasic component of the EDA signal (from `eda_phasic()`).
    sampling_rate : int
        The sampling frequency of the EDA signal (in Hz, i.e., samples/second).
    method : str
        The processing pipeline to apply. Can be one of "neurokit" (default),
        "gamboa2008" or "kim2004" (the default in BioSPPy).
    amplitude_min : float
        Only used if 'method' is 'neurokit' or 'kim2004'. Minimum threshold by which to exclude SCRs (peaks) as relative to the largest amplitude in the signal.

    Returns
    -------
    info : dict
        A dictionary containing additional information, in this case the
        aplitude of the SCR, the samples at which the SCR onset and the
        SCR peaks occur. Accessible with the keys "SCR_Amplitude", "SCR_Onset",
        and "SCR_Peaks" respectively.
    signals : DataFrame
        A DataFrame of same length as the input signal in which occurences of
        SCR peaks are marked as "1" in lists of zeros with the same length as
        `eda_cleaned`. Accessible with the keys "SCR_Peaks".

    See Also
    --------
    eda_simulate, eda_clean, eda_phasic, eda_process, eda_plot



    Examples
    ---------
    >>> import neurokit2 as nk
    >>>
    >>> # Get phasic component
    >>> eda_signal = nk.eda_simulate(duration=30, n_scr=5, drift=0.1, noise=0)
    >>> eda_cleaned = nk.eda_clean(eda_signal)
    >>> eda = nk.eda_phasic(eda_cleaned)
    >>> eda_phasic = eda["EDA_Phasic"].values
    >>>
    >>> # Find peaks
    >>> gamboa2008, _ = nk.eda_peaks(eda_phasic, method="gamboa2008")
    >>> kim2004, _ = nk.eda_peaks(eda_phasic, method="kim2004")
    >>> neurokit, _ = nk.eda_peaks(eda_phasic, method="neurokit")
    >>> nk.events_plot([gamboa2008["SCR_Peaks"],
                        kim2004["SCR_Peaks"],
                        neurokit["SCR_Peaks"]], eda_phasic)

    References
    ----------
    - Gamboa, H. (2008). Multi-modal behavioral biometrics based on hci and electrophysiology. PhD ThesisUniversidade.
    - Kim, K. H., Bang, S. W., & Kim, S. R. (2004). Emotion recognition system using short-term monitoring of physiological signals. Medical and biological engineering and computing, 42(3), 419-427.
    """
    # Get basic
    info = eda_findpeaks(eda_phasic, sampling_rate=sampling_rate, method=method, amplitude_min=0.1)
    info = eda_fixpeaks(info, sampling_rate=sampling_rate)

    # Get additional features (recovery time, rise time etc.)
    info = _eda_peaks_getfeatures(info, eda_phasic, sampling_rate)

    # Prepare output.
    peak_signal = signal_formatpeaks(info,
                                     desired_length=len(eda_phasic),
                                     peak_indices=info["SCR_Peaks"])

    return info, peak_signal






# =============================================================================
# Utility
# =============================================================================

def _eda_peaks_getfeatures(info, eda_phasic, sampling_rate=1000):

    # Onset
    onset = info['SCR_Onsets']
    notnull = ~np.isnan(onset)
    onset_int = onset[notnull].astype(np.int)

    # Amplitudes
    amplitude = np.full(len(info["SCR_Height"]), np.nan)
    amplitude[notnull] = info["SCR_Height"][notnull] - eda_phasic[onset_int]

    # Rise times
    risetime = np.full(len(info["SCR_Peaks"]), np.nan)
    risetime[notnull] = (info["SCR_Peaks"][notnull] - onset[notnull]) / sampling_rate

    # (Half) Recovery times
    recovery = np.full(len(info["SCR_Peaks"]), np.nan)
    recovery_time = np.full(len(info["SCR_Peaks"]), np.nan)
    recovery_values = amplitude / 2
    for i, peak_index in enumerate(info["SCR_Peaks"]):
        try:
            segment = eda_phasic[peak_index:info["SCR_Peaks"][i+1]]
        except IndexError:
            segment = eda_phasic[peak_index::]
        recovery_value = findclosest(recovery_values[i], segment, direction="smaller", strictly=False)
        if np.abs(recovery_values[i]-recovery_value) < recovery_values[i] / 100:
            segment_index = np.where(segment == recovery_value)[0]
            recovery[i] = peak_index + segment_index
            recovery_time[i] = segment_index / sampling_rate


    info["SCR_Amplitude"] = amplitude
    info["SCR_RiseTime"] = risetime
    info["SCR_Recovery"] = recovery
    info["SCR_RecoveryTime"] = recovery_time

    return info