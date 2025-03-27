# Load the tibble
load("zelda.RData")

# Give number of title release year wise
zelda <- zelda |>
  group_by(year) |>
  summarize(releases = n()) |>
  arrange(desc(releases))

# Save the tibble
save(zelda, file = "2.RData")