for (a in c(2020:2024)) {
  name <- paste0("year_", a)
  name <- read.csv(paste0(a, ".csv"))
}