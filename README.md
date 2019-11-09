# QM Question Library

This is a collection of scripts for generating mathematics
questions for my university students.

Scripts are added in an ad hoc basis, and will probably not
be refactored before next academic year.

## Use

    python3 <module_name.py>

## Requirements

*   pandoc is used to convert .markdown to .docx

*   pandoc is called as a linux `os.system` call.

## Modules so far:

### inverse_matrix.py

Generates matrices and their inverse.
*   The user is asked for dimension of the
    square matrix (e.g. `3` would give a
    3x3 matrix.

*   The user is asked for the number of
    questions required.

*   The user is asked how many sybolic characters they
    want in the matrix. Entering 0 would make all the
    matrix elements integers; Entering 1 would cause
    one character to be include an unknown e.g. (a-1).

*   A Word document is saved to questionsheets/ with
    the questions on it.

### system_solve.py

Generates a system of matrices which
represent a system of simultaneous equations.

*   The user is asked for the dimensions (i.e.
    the number of equations/rows in the matrix.
    NOTE: The dimensions are limited to 6 by the
    number of symbolic variables. This seems more
    than sufficient. An error message will be
    sent for anything larger.

*   The user is asked for the number of
    questions required.

*   A Word document is saved to questionsheets/ with
    the questions on it.
