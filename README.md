# Matrix Transformation

A small python library for performing 2D matrix transformations. This project was a side quest - I was trying to solve the magic 3x3 magic square problem on hackerrank and the brute force solution was to compare a given matrix against all possible rotations and reflections.
I could have done these rotations using built in functions such as zip or I could have used external libraries such as numpy. But I ended up implementing these operations manually to understand how things were moving under the hood.

## Current Transformations

At the moment, this project has only been tested on 3x3 2D matrices and can perform the following transformations:

- 90 degree rotation
- 180 degree rotation
- 270 degree rotation
- Horizontal reflection
- Vertical reflection
- Main diagonal reflection
- Anti diagonal reflection

## Installation

Clone the repository:

`git clone https://github.com/Aishakhan17/Matrix-Transformations.git`
`cd Matrix-Transformations`

Create and activate a virtual environment:

`python3 -m venv .venv`
`source .venv/bin/activate`

Install the package in editable mode:

`pip install -e .`
Usage

Once installed, transformations can be imported from the package:

from matrix_transformations import rotate_90

## Why This Project?

The idea wasn't/isn't to simply provide another way to rotate a matrix; it was/is to explore and understand how matrix transformations work at the indexing level.

The implementation intentionally avoids convenient built-in operations so that the movement of individual elements can be understood explicitly.

Future versions may generalise the transformations to matrices of arbitrary size and provide visual or interactive explanations of how each transformation works. Maybe.
