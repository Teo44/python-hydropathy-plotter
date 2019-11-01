from logic import parse, fasta_parse
import plotly.express as px
import sys

# read amino acid sequence from a fasta file or from input
if len(sys.argv) == 2:
    seq_file = open(str(sys.argv[1]))
    seq = fasta_parse(seq_file)
else: 
    print('Amino acid sequence:')
    seq = input()
print('Window size:')
window_size = int(input())

# calculate the hydrophilicities per window
scores = parse(seq, window_size)

# draw a plotly graph from the results
fig = px.line(x=range(1, len(scores)+1), y=scores) 
fig.show()
