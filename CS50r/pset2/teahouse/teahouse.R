# Ask user for flavor
flavor_choice <- readline("Flavor: ")
if (!flavor_choice %in% c("Light", "Bold")) {
  cat("Enter either 'Light' or 'Bold' for flavor")
} else {
  # Ask user for caffeine
  caffeine_choice <- readline("Caffeine: ")
  if (!caffeine_choice %in% c("Yes", "No")) {
    cat("Enter either 'Yes' or 'No' for caffeine")
  # Recommend tea to user
  } else if (flavor_choice == "Light" && caffeine_choice == "No") {
    cat("chamomile tea")
  } else if (flavor_choice == "Light" && caffeine_choice == "Yes") {
    cat("green tea")
  } else if (flavor_choice == "Bold" && caffeine_choice == "No") {
    cat("rooibos tea")
  } else if (flavor_choice == "Bold" && caffeine_choice == "Yes") {
    cat("black tea")
  }
}



