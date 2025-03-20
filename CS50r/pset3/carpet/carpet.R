calculate_growth_rate <- function(years, visitors) {
  # TODO: Calculate yearly growth of visitors
  visitor_growth <- visitors[length(visitors)] - visitors[1]
  number_of_years <- years[length(years)] - years[1]

  growth_rate <- visitor_growth / number_of_years
}

predict_visitors <- function(years, visitors, year) {
  # TODO: Predict visitors in given year
  if (year > years[length(years)]) {
    years_passed <- year - years[length(years)]
    predicted_number <- visitors[length(visitors)] + calculate_growth_rate(years, visitors) * years_passed
  } else {
    predicted_number <- visitors[which(years == year)]
  }
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
