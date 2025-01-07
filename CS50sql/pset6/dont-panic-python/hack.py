from cs50 import SQL

# Estabilish connection with database
db = SQL("sqlite:///dont-panic.db")

# Prompt for password
password = input("Enter Password: ")

# Change admin password
db.execute(
    """
    UPDATE users
    SET password = ?
    WHERE username = 'admin';
    """,
    password
)
