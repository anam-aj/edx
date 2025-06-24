import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # Pages linked to current page
    linked_pages = corpus[page]
    if not linked_pages:
        linked_pages = corpus.keys()

    # Unlinked probability of each page
    unlinked_pb = (1 - damping_factor) / len(corpus)

    # Empty dictionary to hold probabilty of each page
    pages_probability = {}

    # Loop through pages and create probability distribution
    for p in corpus:
        if p in linked_pages:
            linked_pb = damping_factor / len(linked_pages)
        else:
            linked_pb = 0

        # Calculate probabilty of page
        probability = linked_pb + unlinked_pb
        pages_probability[p] = probability

    return pages_probability


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # List of pages
    pages = list(corpus.keys())

    # Pages and thier count in sampling
    page_count = {}
    for page in pages:
        page_count[page] = 0

    # First random page
    page = random.choice(pages)
    page_count[page] += 1

    # Create the samples
    for _ in range(n - 1):
        # Get the next page
        pb_distribution = transition_model(corpus, page, damping_factor)
        pages = list(pb_distribution.keys())
        probs = list(pb_distribution.values())
        next_page = random.choices(pages, probs, k=1)[0]
        # Update page count
        page_count[next_page] += 1
        page = next_page

    # Convert page count to probability
    for page in page_count:
        pb = page_count[page] / n
        page_count[page] = pb

    # Probability distribution of pages
    pb_dist = page_count

    return pb_dist


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Probability distribution of pages
    old_pb_dist = {}
    num_of_pages = len(corpus)
    for page in corpus:
        old_pb_dist[page] = 1 / num_of_pages

    # Probability of choosing page directly
    p_direct = (1 - damping_factor) / num_of_pages

    # Loops and updates probabilities untill values converge
    while True:
        new_pb_dist = {}
        # Loops through all pages
        for page in old_pb_dist:
            # Initiazlize linked probability to 0
            p_linked = 0
            for p in corpus:
                # Pages linked to current page
                linked_pages = corpus[p]
                if not linked_pages:
                    linked_pages = corpus.keys()
                # Generate and add the linked probability
                if page in linked_pages:
                    num_of_links = len(linked_pages)
                    prob = 1 / num_of_links
                    p_linked += damping_factor * old_pb_dist[p] * prob

            # Update probability of page in probability distribution dictionary
            new_pb = p_direct + p_linked
            new_pb_dist[page] = new_pb

        # Check for convergence
        converged = True
        for page in old_pb_dist:
            if abs(old_pb_dist[page] - new_pb_dist[page]) > 0.001:
                converged = False
                break

        if converged:
            return new_pb_dist
        else:
            old_pb_dist = new_pb_dist


if __name__ == "__main__":
    main()
