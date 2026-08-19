# Day 12 — Phishing Email Detection with ML

## Objective
Train a basic Naive Bayes classifier to detect phishing emails.

## Theory
- NLP + ML can classify emails with 95%+ accuracy when trained properly.
- Key features: keyword frequency, URL count, sender domain, urgency-driven language.
- Naive Bayes is fast and works well for text classification tasks.

## What the script does
`phishing_ml_classifier.py` trains a Naive Bayes model on a 50-email dataset (20 phishing, 30 legitimate), using word-frequency features (`CountVectorizer`). It's evaluated on a held-out test set, then tested on 4 brand-new emails it has never seen.

## Tools used
- `scikit-learn` (CountVectorizer, MultinomialNB, Pipeline, train_test_split, metrics)

## Results

**Confusion Matrix:**
[[8 0]
[1 6]]
- 8 legitimate emails correctly identified, 0 false alarms
- 6 phishing emails correctly caught, 1 phishing email missed (misclassified as legit)

**Accuracy:** 93.33%

**Classification Report:**
| Class | Precision | Recall | F1-score |
|---|---|---|---|
| Legit | 0.89 | 1.00 | 0.94 |
| Phishing | 1.00 | 0.86 | 0.92 |

**Predictions on unseen emails:**
| Email | Prediction |
|---|---|
| "Please verify your PayPal login immediately" | PHISHING |
| "Meeting notes from yesterday" | LEGIT |
| "Your account will be suspended, click here now" | PHISHING |
| "Can you send me the report by tomorrow" | LEGIT |

All 4 new, unseen emails were classified correctly, showing the model generalizes beyond its training data.

## Deliverable
Trained model + confusion matrix + accuracy report on 50-sample dataset.