from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:   Sean Kim
SID:    500563706
Unikey: skim8609

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # TODO: Check if emitters' pulse sequence are correctly set up
    assert ...

    # don't forget to close the file
    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    pass    


if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence_2.in')
    # You should have more below...


