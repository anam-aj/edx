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