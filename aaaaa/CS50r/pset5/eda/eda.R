# Load necessary libraries
library('readr')
library('tidyverse')

# Read the text file and convert all character to lower case
file_name <- c('astley', 'beatles', 'chapman', 'robinson', 'summerwind', 'swift')
text <- ''
for (name in file_name) {
  file <- paste0('fold/', name, '.txt')
  text <- paste0(text, read_file(file), ' ')
}

# Convert to lower case
text <- str_to_lower(text)

# Replace all non alphabet with single space
text <- str_replace_all(text, '[^a-z]', ' ')

# Remove extra space
text <- str_squish(text)

# Split into words' vector
words <- str_split(text, ' ')[[1]]

# Remove single character entries
filter <- nchar(words) > 1
words <- words[filter]

# Initials' vector
initials <- substr(words, 1, 1)

# Make tibble of words
letters <- tibble(letter = initials)

# Tibble containing word count
letters_count_df <- letters |>
  group_by(letter) |>
  summarize(count = n())

# Plot the graph
graph <- ggplot(letters_count_df, aes(x = letter, y = count)) +
  geom_col(
    aes(fill = letter),
    show.legend = FALSE
  ) +
  labs(
    x = "Letter",
    y = "Count",
    title = "Letter Count"
  ) +
  theme_classic()

# Save graph
ggsave(
  'visualization.png',
  plot = graph
)
