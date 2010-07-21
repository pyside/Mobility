#!/bin/sh

# This is a nasty workaround of a CTest limitation
# of setting the environment variables for the test.

# $1: $PYTHONPATH
# $2: python executable
# $3: test file

export PYTHONPATH=$1:$PYTHONPATH
$2 $3

