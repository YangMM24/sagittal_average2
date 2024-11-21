import numpy as np
from pathlib import Path
import pytest
from sagittal_average.sagittal_brain import run_averages

TEST_DIR = Path(__file__).parent

def test_run_averages():
    data_input = np.zeros((20, 20), dtype=int)
    data_input[-1, :] = 1 
    input_file = TEST_DIR / "brain_sample.csv"
    np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

    expected = np.zeros(20, dtype=float)
    expected[-1] = 1.0

    output_file = TEST_DIR / "brain_average.csv"
    run_averages(file_input=str(input_file), file_output=str(output_file))

    result = np.loadtxt(output_file, delimiter=',')

    np.testing.assert_array_equal(result, expected)

    input_file.unlink(missing_ok=True)
    output_file.unlink(missing_ok=True)