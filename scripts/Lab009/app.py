import numpy as np
from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models import Slider, Div
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes

n = 10000

x = np.random.normal(size=n)
y = np.random.normal(size=n)

hb = hexbin(x, y, 0.2)

fig = figure(width=400, aspect_ratio=1)
fig.grid.visible = False
fig.background_fill_color = all_palettes['Turbo'][256][0]

cmap = linear_cmap(field_name='counts', palette=all_palettes['Turbo'][256], low=min(hb.counts), high=max(hb.counts))
ht = fig.hex_tile(size=0.2, source=hb, fill_color=cmap, line_color=cmap)


s1 = Slider(title='N', start=1000, end=100000, value=n, step=1000, width=200)

div = Div(text='<h1>Hexbin Plot</h1>')

def update_data(attr, old, new):
    n = int(s1.value)

    x = np.random.normal(size=n)
    y = np.random.normal(size=n)

    hb = hexbin(x, y, 0.2)

    cmap = linear_cmap(field_name='counts', palette=all_palettes['Turbo'][256], low=min(hb.counts), high=max(hb.counts))
    ht.glyph.fill_color = cmap
    ht.glyph.line_color = cmap    

    ht.data_source.data = hb

#s1.on_change('value', update_data)
s1.on_change('value_throttled', update_data)

curdoc().add_root(column(div, row(s1, fig)))