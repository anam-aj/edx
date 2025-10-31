# Get file name from user
file <- readline('Enter filename: ')

# Make table from csv file
table <- read.csv(file)

# Get the required values
total_pit_stops <- length(table$team)
longest_pit_stop <- max(table$time)
shortest_pit_stop <- min(table$time)
total_time <- sum(table$time)

# Print the value
print(paste("Total pit stops:", total_pit_stops))
print(paste("Longest pit stop:", longest_pit_stop))
print(paste("Shortest pit stop:", shortest_pit_stop))
print(paste("Total time:", total_time))
