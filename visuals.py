from bokeh.charts import Bar, output_file, save
import pandas as pd
import numpy as np

#Comparing all Values
data = pd.read_csv('data.csv')
vis_a = Bar(
            data,
            label = 'State',
            values = ' Crude Rate',
            title = 'Average Number of Deaths by State Per Year',
            group = ' Gender',
            xlabel = "State",
            ylabel = 'Deaths',
            width = 1450
            )
output_file('vis_a.html')
save(vis_a)

#Female
data = pd.read_csv('data_f.csv')
vis_b = Bar(
            data,
            label = 'State',
            values = ' Crude Rate',
            title = 'Average Number of Female Deaths by State Per Year',
            group = ' Gender',
            xlabel = "State",
            ylabel = 'Deaths',
            width = 1450,
            color = "magenta"
            )
output_file('vis_b.html')
save(vis_b)

#Total
data = pd.read_csv('data_t.csv')
vis_c = Bar(
            data,
            label = 'State',
            values = ' Crude Rate',
            title = 'Average Number of Total Deaths by State Per Year',
            group = ' Gender',
            xlabel = "State",
            ylabel = 'Deaths',
            width = 1450,
            color = "orange"
            )
output_file('vis_c.html')
save(vis_c)

#Male
data = pd.read_csv('data_m.csv')
vis_d = Bar(
            data,
            label = 'State',
            values = ' Crude Rate',
            title = 'Average Number of Male Deaths by State Per Year',
            group = ' Gender',
            xlabel = "State",
            ylabel = 'Deaths',
            width = 1450,
            color = "blue"
            )
output_file('vis_d.html')
save(vis_d)