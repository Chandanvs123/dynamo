#!/bin/bash

# Run pytest and generate the CTRF JSON report so the platform can parse the results correctly.
pytest /tests/test_outputs.py -rA --ctrf