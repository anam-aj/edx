import textwrap
from termcolor import colored

# Wrap your text
wrapped_text = textwrap.fill("Happy Halloweenasdasdasasdadasdasdadaddadadadadadad!", width=20)
print(wrapped_text)

# Colorize your text
colored_text = colored(wrapped_text, "red")

print(colored_text)
