from logic import parse
import plotly.express as px

print('Amino acid sequence:')
seq = input()
print('Window size:')
window_size = int(input())

scores = parse(seq, window_size)

fig = px.line(x=range(1, len(scores)+1), y=scores) 
fig.show()
