# Ask user for Milk choice
milk_choice <- readline("Milk: ")
if (!milk_choice %in% c("Yes", "No")) {
  cat("Enter either 'Yes' or 'No' for milk")
  # Recommend tea to user
} else if (milk_choice == "No") {
  cat("Black Tea")
} else if (milk_choice == "Yes") {
  cat("Indian tea")
}

