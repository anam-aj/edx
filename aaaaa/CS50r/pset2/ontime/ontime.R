# Load all data into 1 table
bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")
transport <- rbind(bus, rail)

# Get all route options
route_options <- unique(transport$route)

# Ask user choice
user_route <- readline("Route: ")
if (!user_route %in% route_options){
  cat("Invalid route")
} else {
  # Calculate peak and  off-peak percentages
  user_table <- subset(transport, route == user_route)
  peak_table <- subset(user_table, peak == "PEAK")
  off_peak_table <- subset(user_table, peak == "OFF_PEAK")
  peak_percent <- (peak_table$numerator / peak_table$denominator) * 100
  peak_percent <- round(mean(peak_percent))
  off_peak_percent <- (off_peak_table$numerator / off_peak_table$denominator) * 100
  off_peak_percent <- round(mean(off_peak_percent))
  # Display result to user
  cat("On time", paste(peak_percent, "%", sep = ""), "of the time during peak hours.\n")
  cat("On time", paste(off_peak_percent, "%", sep = ""), "of the time during off-peak hours.\n")
}