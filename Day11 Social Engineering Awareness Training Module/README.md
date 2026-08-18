# Day 11 — Social Engineering Awareness Training Module

## Objective
Design and code an interactive SE awareness quiz.

## Theory
- Training is the #1 defense against social engineering.
- Effective training uses realistic scenarios, immediate feedback, and repetition.
- Phishing simulation programs (GoPhish, KnowBe4) reduce click rates by 70%+ in real-world use.

## What the script does
`se_awareness_quiz.py` runs a CLI quiz engine with 10 scenario-based social engineering questions. Each question gives immediate feedback (correct/incorrect with explanation) and the final score is saved to a JSON file.

## Tools used
- `json` (stdlib)

## Sample Result
```json
{
  "score": 9,
  "total": 10
}
```
9/10 — one incorrect answer triggered an explanation reinforcing why clicking an email link to "verify" a password is unsafe.

## Deliverable
Quiz with 10+ questions + score report saved to JSON file.