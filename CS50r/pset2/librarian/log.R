# Create data frames of books and authors
books <- read.csv('books.csv')
authors <- read.csv('authors.csv')

# View data frames to get an idea of its structure
View(books)
View(authors)

# Book for writer
filter <- tolower(books$author) == "mia morgan"
books_by_mia_morgan <- books[filter, ]
View(books_by_mia_morgan)

# Book for musician
filter <- books$year == 1613 & books$topic == "Music"
book_for_musician <- books[filter, ]
View(book_for_musician)

# Book for traveler
filter <- books$year == 1775 & (books$author == "Elena Petrova" | books$author == "Lysandra Silverleaf")
book_for_traveler <- books[filter, ]
View(book_for_traveler)

# Book for painter
filter <- books$topic == "Art" & (books$pages >= 200 & books$pages <= 300) & (books$year == 1990 | books$year == 1992)
book_for_painter <- books[filter,]
View(book_for_painter)

# Book for scientist
filter <- grepl("Quantum Mechanics", books$title)
book_for_scientist <- books[filter, ]
View(book_for_scientist)

# Book for teacher
authors_from_zenthia <- authors$hometown == "Zenthia"
authors_list <- authors$author[authors_from_zenthia]
View(authors_list)

filter <- (books$year >= 1700 & books$year < 1800) & (books$topic == "Education") & (books$author %in% authors_list)
book_for_teacher <- books[filter, ]
View(book_for_teacher)

