# Load necessary libraries
library('readr')
library('tidyverse')

# Read the text file and convert all character to lower case
txt <- read_file('lyrics/astley.txt')

# Convert to lower case
txt <- str_to_lower(txt)

# Replace all non alphabet with single space
txt <- str_replace_all(txt, '[^a-z]', ' ')

# Remove extra space
txt <- str_squish(txt)

# Split into words' vector
words <- str_split(txt, ' ')[[1]]

# Make tibble of words
words_df <- tibble(word = words)

# Tibble containing word count
word_count_df <- words_df |>
  group_by(word) |>
  summarize(count = n()) |>
  filter(count > 1) |>
  slice_max(count, n = 20)

# Plot the graph
graph <- ggplot(word_count_df, aes(x = reorder(word, -count), y = count)) +
  geom_col(
    aes(fill = word),
    show.legend = FALSE
  ) +
  labs(
    x = "Word",
    y = "Count",
    title = "Word Count"
  ) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 0.5))

# Save graph
ggsave(
  'lyrics.png',
  plot = graph
)
