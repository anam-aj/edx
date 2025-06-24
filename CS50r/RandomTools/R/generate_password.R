generate_password <- function(length = 8, use_special = TRUE) {
  # Validate length input
  if (!is.numeric(length) || length <= 0) {
    stop("Length must be a positive number.")
  }

  # Character sets
  lower <- letters
  upper <- LETTERS
  digits <- as.character(0:9)
  special <- c("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=")

  # Combine based on user choices
  all_chars <- c(lower, upper, digits)
  if (use_special) {
    all_chars <- c(all_chars, special)
  }

  # Generate password
  password <- paste0(sample(all_chars, length, replace = TRUE), collapse = "")

  # Return the generated password
  return(password)
}