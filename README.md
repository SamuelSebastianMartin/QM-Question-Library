# QM Question Library

This is a collection of scripts for generating mathematics
questions for my university course.

Scripts are added in an ad hoc basis, and will probably not
be refactored before next academic year.

## Use

    python3 <module_name.py>

## Requirements

*   pandoc is used to convert .markdown to .docx

*   pandoc is called as a linux `os.system` call.

## Modules so far:
### inverse_matrix_question_generator.py

Generates matrices and their inverse.
*   The user is asked for dimension of the
    square matrix (e.g. `3` would give a
    3x3 matrix.

*   The user is asked for the number of
    questions required.

*   A Word document is saved to $PWD with
    the questions on it.

### simultaneous_matrix_eq_generator.py

Generates a system of matrices which
represent a system of simultaneous equations.

*   The user is asked for the dimensions (i.e.
    the number of equations/rows in the matrix.

*   The user is asked for the number of
    questions required.

*   A Word document is saved to $PWD with
    the questions on it.
