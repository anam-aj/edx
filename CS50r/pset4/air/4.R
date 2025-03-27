load("air.RData")

air <- air |>
  filter(county == "OR - Baker") |>
  arrange(desc(emissions))

save(air, file = "4.RData")