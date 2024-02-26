library(tidyverse)
library(gapminder)

gapminder |>
  filter(continent != "Oceania") |>
  ggplot(aes(x = year, y = lifeExp, group = country, color = country)) +
  geom_line(lwd = 1, show.legend = FALSE) +
  facet_wrap(~ continent) +
  # `country_colors` is an object included in gapminder
  scale_color_manual(values = country_colors) +
  theme_minimal(14) +
  theme(strip.text = element_text(size = rel(1.1)))
