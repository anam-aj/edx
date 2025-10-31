# Load the tibble
load("zelda.RData")

# Get the first release of each title by more than one producers
zelda <- zelda |>
  group_by(title) |>
  filter(year == min(year) & str_detect(producers, ",")) |>
  arrange(year, title, system)

# Save the tibble
save(zelda, file = "5.RData")