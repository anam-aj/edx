from termcolor import colored
import textwrap

# Colorize your text
colored_text = colored("Happy Halloween!", "red")

# Wrap your text
wrapped_text = textwrap.fill(colored_text, width=20)

print(wrapped_text)
