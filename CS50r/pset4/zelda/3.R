# Load the tibble
load("zelda.RData")

# Get the first release of each title
zelda <- zelda |>
  group_by(title) |>
  filter(year == min(year)) |>
  arrange(year, title, system)

# Save the tibble
save(zelda, file = "3.RData")
