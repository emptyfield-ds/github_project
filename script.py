import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
from gapminder import gapminder

gapminder = pl.from_pandas(gapminder)

life_exp_plot = sns.relplot(
  gapminder.filter(pl.col("continent") != "Oceania"), 
  x="year", 
  y="lifeExp", 
  kind="line", 
  hue="country", 
  col="continent", 
  legend=False, 
  col_wrap=3, 
  palette="Spectral", 
  linewidth=1, 
  facet_kws={'sharex': False, 'sharey': False}
)

life_exp_plot.fig.suptitle('Life Expectancy Over Years by Country and Continent', fontsize=16)
life_exp_plot.set_titles("{col_name}", size=14)  
life_exp_plot.set_axis_labels("Year", "Life Expectancy") 
life_exp_plot.tight_layout()
sns.set_theme(style="whitegrid")  
