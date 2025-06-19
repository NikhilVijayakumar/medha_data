# Fundamental Concepts in Probability and Statistics

This notebook provides definitions and explanations of fundamental concepts in probability and statistics, as described in the source.

## Core Concepts

- **Probability:** A measure of the likeliness of an event occurring, quantifying uncertainty.

- **States Favourable:** The specific outcomes of an experiment that align with the event being considered.

- **Statistics:** The science of collecting, analysing, interpreting, and presenting data to provide insights over time.

- **Machine Learning (ML):** Algorithms that learn from data to make predictions or decisions. Probability and statistics are foundational for handling uncertainty in ML.

- **Population:** The entire group of individuals or items of interest in a study.

- **Sample:** A smaller, selected subset of a population used for analysis to draw inferences about the larger group.

- **Uncertainty:** The state of having limited knowledge about an outcome or event. Probability provides a framework for quantifying and managing uncertainty.

- **Information:** What is gained when uncertainty is reduced. Information is inversely proportional to the probability of an event; less probable events provide more information when they occur.

## Events and Outcomes

- **Event:** A specific outcome or set of outcomes of a random experiment.

- **Outcome:** A possible result of a random experiment (e.g., Heads, Tails).

- **Sample Space:** The set of all possible outcomes of a random experiment.

## Probability Measures and Approaches

- **Probability of Occurrence (P(A)):** The numerical measure of the likelihood of an event A happening, ranging from 0 (impossible) to 1 (certain).

- **Frequentist Approach:** Defines probability as the long-run relative frequency of an event in a large number of repeated trials.

- **Bayesian Approach:** Defines probability as a degree of belief about an event, allowing for incorporating prior knowledge and updating beliefs with new evidence.

- **A Priori Probability:** The initial probability assigned to an event before considering new evidence (Bayesian approach).

- **Posteriori Probability:** The updated probability of an event after new evidence is considered (Bayesian approach).

- **Fundamental Rules of Probability:** Basic principles governing probability calculations and combinations.

## Probability Notation and Types of Events

- **Notation P(A):** Represents the probability of event A.

- **Impossible Event:** An event with a probability of 0; it will never happen.

- **Certain Event:** An event with a probability of 1; it will definitely happen.

## Combining Probabilities

- **Complement of an Event (A'):** The event that A does not occur.
  $$P(A') = 1 - P(A)$$

- **Union of Events (A ∪ B):** The event that either A occurs, or B occurs, or both occur.

- **Intersection of Events (A ∩ B):** The event that both A and B occur simultaneously.

- **Mutually Exclusive Events:** Events that cannot occur at the same time.
  - For mutually exclusive events:
    $$P(A \cap B) = 0$$
    $$P(A \cup B) = P(A) + P(B)$$

- **Joint Probability (P(A ∩ B)):** The probability of two or more events occurring together.

- **Conditional Probability (P(A|B)):** The probability of event A occurring given that event B has already occurred.
  $$P(A|B) = \frac{P(A \cap B)}{P(B)}, \text{ provided } P(B) > 0$$

- **Marginal Probability:** The probability of a single event occurring, summed over all possible outcomes of other related events.
  - For example:
    $$P(A) = \sum P(A \cap B_i) \quad \text{for all possible outcomes } B_i$$

- **Independent Events:** Two events A and B are independent if the occurrence of one does not affect the probability of the other.
  - If A and B are independent:
    $$P(A \cap B) = P(A) \times P(B)$$
    $$P(A|B) = P(A)$$

# Formula summary

# Fundamental Concepts of Probability

This notebook summarizes key concepts in probability theory.

## Basic Probability

- The probability of an event A is denoted as $P(A)$.

## Complement of an Event

- The probability of an event A *not* occurring is given by:
  $$P(\text{not } A) = 1 - P(A)$$
  This can also be written as:
  $$P(A^c) = 1 - P(A)$$

## Mutually Exclusive Events

- For two mutually exclusive events A and B, the probability of their union (either A or B occurring) is the sum of their individual probabilities:
  $$P(A \cup B) = P(A) + P(B)$$
- For mutually exclusive events, the probability of their intersection (both A and B occurring) is 0:
  $$P(A \cap B) = 0$$

## Joint Probability

- The probability of the joint occurrence of two events A and B is denoted as $P(A, B)$ or $P(A \cap B)$.

## Conditional Probability

- The conditional probability of event A occurring given that event B has occurred is denoted as $P(A|B)$ and is defined as:
  $$P(A|B) = \frac{P(A \cap B)}{P(B)}, \text{ provided that } P(B) \neq 0$$
- Similarly, the conditional probability of event B occurring given that event A has occurred is:
  $$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

## Marginal Probability

- From the joint probability $P(A \cap B)$, the marginal probabilities $P(A)$ and $P(B)$ can be found as follows:
  - $$P(A) = \sum P(A \cap B_i), \text{ where the sum is over all possible values of B } (b_1, b_2, ..., b_n)$$
  - $$P(B) = \sum P(A_i \cap B), \text{ where the sum is over all possible values of A } (a_1, a_2, ..., a_n)$$

## Independent Events

- For independent events A and B, the conditional probability of A given B is simply the probability of A:
  $$P(A|B) = P(A)$$
- This also implies that for independent events, the joint probability is the product of their individual probabilities:
  $$P(A \cap B) = P(A) \times P(B)$$

## Information and Probability

- Information (I) is mentioned to be inversely proportional to probability (p), and a logarithmic relationship is suggested:
  $$I \propto -\log(p)$$
  This is represented as:
  $$I_E = -\log(P)$$

## Frequentist Approach to Probability

- The frequentist approach to probability defines the probability of an event (e.g., H for heads in a coin toss) as the limit of the ratio of the number of times the event occurs ($N_H$) to the total number of trials ($N$) as the number of trials approaches infinity:
  $$P(H) \approx \frac{N_H}{N} \text{ (for a large number of trials)}$$
