Graphing
================
Mira Flynn, Hazel Smith

-   [Original Paper Replication](#original-paper-replication)

``` r
library(tidyverse)
```

    ## -- Attaching packages --------------------------------------- tidyverse 1.3.1 --

    ## v ggplot2 3.3.5     v purrr   0.3.4
    ## v tibble  3.1.2     v dplyr   1.0.7
    ## v tidyr   1.1.3     v stringr 1.4.0
    ## v readr   1.4.0     v forcats 0.5.1

    ## -- Conflicts ------------------------------------------ tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(viridis)
```

    ## Warning: package 'viridis' was built under R version 4.1.1

    ## Loading required package: viridisLite

## Original Paper Replication

``` r
df_ultimatum <- read.csv("data/data.csv")
```

``` r
df_ultimatum %>%
  ggplot() +
  geom_line(aes(x = w, y = mean_p, color = "mean_p"), size = 1) +
  geom_line(aes(x = w, y = mean_q, color = "mean_q"), size = 1) +
  geom_point(aes(x = w, y = mean_p, color = "mean_p"), size = 2) +
  geom_point(aes(x = w, y = mean_q, color = "mean_q"), size = 2) +
  theme_common()
```

![](graphing_files/figure-gfm/original-replication-graph-1.png)<!-- -->
