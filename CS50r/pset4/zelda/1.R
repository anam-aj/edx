# Create tibble from CSV
zelda <- read_csv("zelda.csv")

# Split "release" column into  year and system
zelda <- separate(zelda, release, into = c("year", "system"), sep = "-")

# Tidy the tibble
zelda <- pivot_wider(
  zelda,
  id_cols = c(title, year, system),
  names_from = role,
  values_from = names
)

# Rename the columns to lower case
zelda <- zelda |>
  rename_with(tolower)

# Remove trailing spaces
zelda <- zelda |>
  mutate(across(everything(), str_trim))

# Convert data type of "year" column
zelda$year <- as.integer(zelda$year)

# Save the tibble
save(zelda, file = "zelda.RData")
