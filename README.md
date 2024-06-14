# WINTER corrections

A package for implementing nonlinearity corrections for WINTER.
- Current implementation is with a rational function with 8 parameters.
- Also has the ability to generate/fit polynomial and other rational functions.

TODO: add more to the bad pixel masking. 
- Currently it only masks pixels which fail the rational fit or are tied high.
- To add: dead pixel and highly nonlinear pixels to the mask.

## Installation

```bash
pip install -e ".[dev]"
pre-commit install
```

Set the directory 

## Get Started

You can use winternlc directly from the command line. 

```bash
winternlc-apply /path/to/data.fits
```

This will apply the nonlinearity correction to the data and save the corrected data to a new file.

You can also run the correction on multiple files at once.

```bash
winternlc-apply /path/to/data1.fits /path/to/data2.fits
```

Alternatively, you can specify a directory and all the files in the directory will be corrected.

```bash
winternlc-apply /path/to/directory
```

In all cases, you can also specify the output directory.

```bash
winternlc-apply /path/to/data.fits --output-dir /path/to/output
```

If you do not specify an output directory, the corrected files will be saved in the same directory as the input files.

See the help message for more information.

```bash
winternlc --help
```

