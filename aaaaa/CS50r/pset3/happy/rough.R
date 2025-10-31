# Empty data frame
report <- data.frame()
report_temp <- data.frame()

# Read CSVs into report data frame
for (year in c(2020:2024)) {
  file_name <- paste0(year, ".csv")
  report_temp <- read.csv(file_name)
  report_temp$year <- year
  report <- rbind(report, report_temp)
}

# Ask user the name of country
user_country <- readline("Country: ")

# Output the happiness score year wise
for (current_year in c(2020:2024)) {
  df <- subset(report, year == current_year)
  if (user_country %in% df$country) {
    country_row <- subset(df, country == user_country)
    print(country_row)
  }
}
