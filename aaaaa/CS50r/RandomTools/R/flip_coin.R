flip_coin <- function(num_flips = 1) {
  # Validate input
  if (!is.numeric(num_flips) || num_flips <= 0) {
    stop("Number of flips must be a positive number.")
  }

  # Perform coin flips
  results <- sample(c("Heads", "Tails"), num_flips, replace = TRUE)

  # Return the results
  return(paste(results, collapse = " "))
}
