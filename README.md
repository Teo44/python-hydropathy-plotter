# python-hydropathy-plotter

A Python tool to generate simple hydrophilicity plots from amino acid sequences.

## Installation

Enter a virtual Python environment
```
python3 -m venv venv
source venv/bin/activate
```

Download the dependencies 
```
pip install -r requirements.txt
```

## Usage

Enter an amino acid sequence in the terminal...
```
python3 run.py
```

...or read an amino acid sequence from a [FASTA](https://en.wikipedia.org/wiki/FASTA_format) file...
```
python3 run.py path/to/file
```

and the graph will open in a browser.
