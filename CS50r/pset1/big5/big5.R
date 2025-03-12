# Convert TSV file into Table
table = read.table(
  'tests.tsv',
  sep = '\t',
  header = TRUE
)

# Convert gender column values to corresponding levels
table$gender <- factor(
  table$gender,
  labels = c('unanswered', 'male', 'female', 'other')
)

# Create the new columns
table$extroversion <- round(((table$E1 + table$E2 + table$E3) / 15), digit = 2)
table$neuroticism <- round(((table$N1 + table$N2 + table$N3)/ 15), digit = 2)
table$agreeableness <- round(((table$A1 + table$A2 + table$A3)/ 15), digit = 2)
table$conscientiousness <- round(((table$C1 + table$C2 + table$C3)/ 15), digit = 2)
table$openness <- round(((table$O1 + table$O2 + table$O3)/ 15), digit = 2)

# Write the table to CSV file
write.csv(table, 'analysis.csv', row.names = FALSE)