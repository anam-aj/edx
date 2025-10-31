roll_dice <- function(num_dice = 1) {
  # Validate input
  if (!is.numeric(num_dice) || num_dice <= 0) {
    stop("Number of dice must be a positive number.")
  }

  # Roll the dice (6 sides fixed)
  rolls <- sample(1:6, num_dice, replace = TRUE)

  # Return the results
  return(paste(rolls, collapse = " "))
}
