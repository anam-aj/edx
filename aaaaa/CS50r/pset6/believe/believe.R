vol_cuboid <- function(dimensions) {
  # Check if input is a vector of length 3
  if (length(dimensions) != 3) {
    stop("Error: Exactly 3 arguments required (length, breadth, height).")
  }
  
  # Try to convert all elements to numeric
  numeric_dims <- suppressWarnings(as.numeric(dimensions))
  
  # Check for NA (conversion failure)
  if (any(is.na(numeric_dims))) {
    stop("Error: Invalid argument(s). All values must be convertible to numbers.")
  }
  
  # Calculate volume
  volume <- prod(numeric_dims)
  return(volume)
}

