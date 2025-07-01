import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    # Open CSV file
    with open(filename, newline='') as file:
        rows = csv.DictReader(file)

        # Empty 'evidence' list and 'label' list
        evidence = []
        label = []

        # Dictionary to map months to index
        months = {
            "Jan": 0,
            "Feb": 1,
            "Mar": 2,
            "Apr": 3,
            "May": 4,
            "June": 5,
            "Jul": 6,
            "Aug": 7,
            "Sep": 8,
            "Oct": 9,
            "Nov": 10,
            "Dec": 11
        }

        for row in rows:

            # Empty list to hold one evidence
            curr_evidence = []

            # Populate one piece of evidence
            curr_evidence.append(int(row['Administrative']))
            curr_evidence.append(float(row['Administrative_Duration']))
            curr_evidence.append(int(row['Informational']))
            curr_evidence.append(float(row['Informational_Duration']))
            curr_evidence.append(int(row['ProductRelated']))
            curr_evidence.append(float(row['ProductRelated_Duration']))
            curr_evidence.append(float(row['BounceRates']))
            curr_evidence.append(float(row['ExitRates']))
            curr_evidence.append(float(row['PageValues']))
            curr_evidence.append(float(row['SpecialDay']))
            curr_evidence.append(months[row["Month"]])
            curr_evidence.append(int(row['OperatingSystems']))
            curr_evidence.append(int(row['Browser']))
            curr_evidence.append(int(row['Region']))
            curr_evidence.append(int(row['TrafficType']))

            # Add 'visitor type' value
            if row['VisitorType'] == 'Returning_Visitor':
                curr_evidence.append(1)
            else:
                curr_evidence.append(0)

            # Add 'weekend' value
            if row['Weekend'] == 'TRUE':
                curr_evidence.append(1)
            else:
                curr_evidence.append(0)

            # Add 'current evidence' to 'evidence list'
            evidence.append(curr_evidence)

            # Add label
            if row['Revenue'] == 'TRUE':
                label.append(1)
            else:
                label.append(0)

        return (evidence, label)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """

    # Select model
    model = KNeighborsClassifier(n_neighbors=1)

    # Fit model
    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    # Total positive and negatives
    total_pos = sum(labels)
    total_neg = len(labels) - total_pos

    # True positives and negatives
    true_pos = 0
    true_neg = 0

    for i in range(len(labels)):
        if labels[i] == 1 and predictions[i] == 1:
            true_pos += 1
        elif labels[i] == 0 and predictions[i] == 0:
            true_neg += 1

    sensitivity = true_pos / total_pos
    specificity = true_neg / total_neg

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
