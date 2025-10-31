# Load the tibble
load("zelda.RData")

# Get the first release of each title by "Shigeru Miyamoto"
zelda <- zelda |>
  group_by(title) |>
  filter(year == min(year) & str_detect(producers, "Shigeru Miyamoto")) |>
  arrange(year, title, system)

# Save the tibble
save(zelda, file = "4.RData")