
'''
joint_pb = 1

# Loops through each person
for person in people:

    # Get person's gene count
    if person in one_gene:
        person_gene = 1
    elif person in two_genes:
        person_gene = 2
    else:
        person_gene = 0

    # Variable to temporary hold probabilities as we loop through categories
    pb = 0

    # Person's trait probability
    if person in have_trait:
        pb = PROBS['trait'][person_gene][True]
    else:
        pb = PROBS['trait'][person_gene][False]

    # Update joint probability
    joint_pb *= pb

    # Get parents of person if available
    mother = people[person]['mother']
    father = people[person]['father']

    if mother and father:
        # Probability that mother passes gene
        if mother in one_gene:
            m_pass_gene = 0.5
        elif mother in two_genes:
            m_pass_gene = 1 - PROBS['mutation']
        else:
            m_pass_gene = PROBS['mutation']
        # Probability that father passes gene
        if father in one_gene:
            f_pass_gene = 0.5
        elif father in two_genes:
            f_pass_gene = 1 - PROBS['mutation']
        else:
            f_pass_gene = PROBS['mutation']

    # One-gene probability
    if person in one_gene:
        # Person has parents
        if mother and father:
            pb = (m_pass_gene * (1 - f_pass_gene)) + ((1 - m_pass_gene) * f_pass_gene)
        # Person has no parents
        else:
            pb = PROBS['gene'][1]

    # Two-gene probability
    elif person in two_genes:
        # Person has parents
        if mother and father:
            pb = m_pass_gene * f_pass_gene
        # Person has no parents
        else:
            pb = PROBS['gene'][2]

    # Zero-gene probability
    else:
        # Person has parents
        if mother and father:
            pb = (1 - m_pass_gene) * (1 - f_pass_gene)
        # Person has no parents
        else:
            pb = PROBS['gene'][0]

    # Update joint probability
    joint_pb *= pb

# Returns the joint probabitlity
return joint_pb
'''
