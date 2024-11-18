import numpy as np
from tempfile import NamedTemporaryFile
import os
from sagittal_brain import run_averages

def test_run_averages():

    test_input = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [0, 0, 0],
        [7, 8, 9]
    ])
    expected_output = np.array([[3.0, 3.8, 4.5]])  

    input_file = NamedTemporaryFile(delete=False, suffix=".csv", mode='w')
    output_file = NamedTemporaryFile(delete=False, suffix=".csv", mode='w')

    try:
        np.savetxt(input_file.name, test_input, fmt='%d', delimiter=',')
        input_file.close() 

        run_averages(file_input=input_file.name, file_output=output_file.name)

        actual_output = np.loadtxt(output_file.name, delimiter=',')
        output_file.close() 

        assert np.allclose(actual_output, expected_output, atol=1e-2), (
            f"Test failed: expected {expected_output}, got {actual_output}"
        )
        print("Test passed: run_averages produces the correct output.")

    finally:
        os.remove(input_file.name)
        os.remove(output_file.name)


if __name__ == "__main__":
    test_run_averages()
