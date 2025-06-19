# Key Concepts in Probability and Random Variables

This notebook summarizes essential concepts in probability and random variables, drawing from the provided text.

## 1. Joint Probability

- **Definition:** The probability of two or more events occurring simultaneously. Represented as $P(A \cap B)$.
- **Multiplicative Rule:**
  $$P(A \cap B) = P(A|B) \times P(B)$$
  $$P(A \cap B) = P(B|A) \times P(A)$$

## 2. Conditional Probability

- **Definition:** The probability of an event occurring given that another event has already occurred. Denoted as $P(B|A)$, representing the probability of event B given that event A has occurred.
- **Example (Defective Toys - Without Replacement):**
  - Probability of the first toy being defective: $P(A) = 25/1000 = 0.025$.
  - Probability of the second toy being defective given the first was defective: $P(B|A) = 24/999 \approx 0.024$.
  - Probability of both being defective: $P(A \cap B) = P(B|A) \times P(A) \approx 0.0006$.
  - Similar logic applies to calculating the probability of both toys being non-defective.

## 3. Dependence and Independence of Events

- Events can be either dependent (the occurrence of one affects the probability of the other) or independent (the occurrence of one does not affect the probability of the other).
- The example "In p wing champions you attendingall classesof smh trophy" suggests a dependency between winning and attending classes.
- The notations "PCS ME 8 o IND Winn Ct" and "PCS ME 80 becks SML Ct are indepa" likely indicate probabilities of certain events being independent.

## 4. Bayes' Theorem

- **Purpose:** A method to update the probability of a hypothesis based on new evidence.
- **Formula:**
  $$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$
  where:
    - $P(A|B)$ is the posterior probability.
    - $P(B|A)$ is the likelihood.
    - $P(A)$ is the prior probability.
    - $P(B)$ is the probability of the evidence.
- **Example (Spam Email Detection):**
  - Prior probability of spam: $P(\text{Spam}) = 0.4$.
  - Likelihood of flag given spam: $P(\text{Flag}|\text{Spam}) = 0.8$.
  - Likelihood of flag given not spam (false alarm): $P(\text{Flag}|\text{Not Spam}) = 0.1$.
  - Probability of the flag being set (using law of total probability): $P(\text{Flag}) = P(\text{Flag}|\text{Spam})P(\text{Spam}) + P(\text{Flag}|\text{Not Spam})P(\text{Not Spam})$.
  - Posterior probability of spam given the flag: $P(\text{Spam}|\text{Flag}) = \frac{P(\text{Flag}|\text{Spam}) \times P(\text{Spam})}{P(\text{Flag})} \approx 0.31$.

## 5. Random Variables

- **Definition:** A variable whose value is a numerical outcome of a random phenomenon. It maps outcomes of an experiment to real numbers.
- **Contrast with Deterministic Variables:** Deterministic variables have fixed, predictable values.
- **Examples:**
  - Coin toss: Mapping Heads (H) to 2, Tails (T) to 1.
  - Dice throw: Mapping faces 1 to 6 to their respective numbers, or using a custom mapping rule (e.g., 1->1, 2->2, 3->1, 4->0, 5->1, 6->2).

## 6. Probability Mass Function (PMF) and Probability Density Function (PDF)

- The text touches upon assigning probabilities to the values of a random variable.
- For a discrete random variable (like the coin toss example), the probability of each specific value is considered (e.g., $P(X=1)$ when Tails occurs, $P(X=2)$ when Heads occurs), with the sum of probabilities equaling 1.
- For the dice example with a custom mapping, probabilities for each resulting value of the random variable D are implied. Defining these probabilities constitutes a complete description of the random variable's behavior.

## 7. Cumulative Distribution Function (CDF)

- **Definition:** The probability that a random variable $X$ takes on a value less than or equal to a certain value $w$. Denoted as $F_X(w) = P(X \le w)$.
- The notation in the source ($Fx w 9 Pr w$) represents this definition.
- An example involving the CDF for a dice throw is mentioned with specific probability values, illustrating the cumulative probability concept.

## Key Terms

- **Joint Probability:** Probability of multiple events occurring together.
- **Conditional Probability:** Probability of an event given another has occurred.
- **Without Replacement:** Sampling where selected items are not returned.
- **Bayes' Rule:** Updating probability based on new evidence.
- **Prior Probability:** Initial probability before evidence.
- **Likelihood:** Probability of evidence given a hypothesis.
- **Posterior Probability:** Updated probability after considering evidence.
- **Random Variable:** Variable with non-deterministic numerical outcomes.
- **Deterministic Variable:** Variable with fixed, predictable values.
- **Mapping Rule:** Assigns numerical values to experimental outcomes.
- **Probability Mass Function (PMF):** Probability of discrete random variable values.
- **Discrete Random Variable:** Finite or countably infinite values.
- **Continuous Random Variable:** Any value within a range.
- **Cumulative Distribution Function (CDF):** $P(X \le w)$.
- **Event:** A set of outcomes.
- **Sample Space:** All possible outcomes.

# Summary of formulas

# Further Concepts in Probability

This notebook expands on fundamental probability concepts, including joint and conditional probabilities, Bayes' Theorem, and the Cumulative Distribution Function.

## Joint and Conditional Probability

- **Joint Probability:** The probability of two events A and B occurring together.
  - $P(A \text{ and } B)$
  - $P(A \cap B)$

- **Conditional Probability:** The probability of event A occurring given that event B has already occurred.
  - $P(A|B) = \frac{P(A \cap B)}{P(B)}$
  - $P(A|B) = \frac{P(A \text{ and } B)}{P(B)}$
  - $P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$ (Bayes' Rule)

- **Relationship between Joint and Conditional Probability:**
  - $P(A \cap B) = P(A|B) \times P(B) = P(B|A) \times P(A)$

## Example: Probability of Defective Toys (Without Replacement)

Consider a scenario with 1000 toys, where 25 are defective. We want to calculate the probability of picking two defective toys in a row without replacement.

- **Probability of the first toy being defective (Event A):**
  $$P(A) = \frac{25}{1000} = 0.025$$

- **Probability of the second toy being defective given the first was defective (Event B|A):**
  After picking one defective toy, there are 24 defective toys left and 999 total toys.
  $$P(B|A) = \frac{24}{999} \approx 0.024$$

- **Probability of both toys being defective (P(A and B)):**
  $$P(A \text{ and } B) = P(B|A) \times P(A) \approx 0.024 \times 0.025 = 0.0006$$

## Example: Probability of Non-Defective Toys (Without Replacement)

Now, let's calculate the probability of picking two non-defective toys in a row without replacement.

- **Probability of the first toy not being defective (Event Ā):**
  There are $1000 - 25 = 975$ non-defective toys.
  $$P(\bar{A}) = \frac{975}{1000} = 0.975$$

- **Probability of the second toy not being defective given the first was not defective (Event B̄|Ā):**
  After picking one non-defective toy, there are 974 non-defective toys left and 999 total toys.
  $$P(\bar{B}|\bar{A}) = \frac{974}{999} \approx 0.974$$

- **Probability of both toys being non-defective (P(Ā and B̄)):**
  $$P(\bar{A} \text{ and } \bar{B}) = P(\bar{B}|\bar{A}) \times P(\bar{A}) \approx 0.974 \times 0.975 \approx 0.950$$

## Bayes' Theorem

Bayes' Theorem provides a way to update the probability of an event based on new evidence. It is expressed in several forms:

- $$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$
- $$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$
- $$P(A|B) = \frac{P(B|A) \times P(A)}{P(B|A)P(A) + P(B|\bar{A})P(\bar{A})} \quad \text{(Implied using Law of Total Probability)}$$

## Example: Spam Email Detection using Bayes' Theorem

Let's consider a spam email detection scenario:

- $P(A|B) = 0.8$ (Probability of the flag being set as spam given the email is spam)
- $P(B) = 0.4$ (Prior probability that an email is spam)
- $P(\bar{A}) = 1 - P(B) = 0.6$ (Prior probability that an email is not spam)
- $P(A|\bar{A}) = 0.1$ (Probability of the flag being set as spam given the email is not spam - false alarm)

We want to find the probability that an email is spam given that the flag is set ($P(B|A)$).

- **Probability of the flag being set (P(A)) using the Law of Total Probability:**
  $$P(A) = P(A|B)P(B) + P(A|\bar{A})P(\bar{A}) = (0.8 \times 0.4) + (0.1 \times 0.6) = 0.32 + 0.06 = 0.38$$

- **Probability that an email is spam given the flag is set (P(B|A)):**
  $$P(B|A) = \frac{P(A|B) \times P(B)}{P(A)} = \frac{0.8 \times 0.4}{0.38} \approx 0.842$$

## Cumulative Distribution Function (CDF)

For a random variable X, the Cumulative Distribution Function (CDF), denoted by $F_X(w)$, gives the probability that X takes on a value less than or equal to $w$.

- $$F_X(w) = Pr(X \leq w)$$

The CDF, $F_X(w)$, is a non-decreasing function.