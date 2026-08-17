# Day 9 — Social Media Impersonation & Fake Profile Detection

## Objective
Detect fake/bot social profiles using behavioral heuristics.

## Theory
- Fake profiles are used to build trust before launching a social engineering attack.
- Bot signals: low follower:following ratio, generic/no profile picture, very new account, minimal posts.
- Impersonation: cloned profile photos or usernames similar to a real person's.

## What the script does
`fake_profile_detector.py` takes profile data (account age, followers, following, profile picture presence, post count, bio status) and calculates a fake-probability score (0-100%) using five weighted heuristics.

## Scoring Factors
| Factor | Points | Why it's suspicious |
|---|---|---|
| Account age < 30 days | +30 | New accounts are more likely to be bots or throwaway profiles |
| Following:Followers ratio > 10 | +25 | Bots often mass-follow to appear active |
| No profile picture | +20 | Genuine users typically set a profile photo |
| Fewer than 5 posts | +15 | Bots rarely post original content |
| Default/empty bio | +10 | Real users usually personalize their bio |

## Tools used
- Python (stdlib only)

## Test Results (5 profiles)
| Profile | Age (days) | Followers | Following | Posts | Fake Score |
|---|---|---|---|---|---|
| 1 | 7 | 2 | 900 | 1 | 100% |
| 2 | 1200 | 4500 | 320 | 870 | 0% |
| 3 (my Instagram) | 365 | 26 | 13 | 0 | 15% |
| 4 | 600 | 250 | 180 | 45 | 0% |
| 5 | 3 | 1 | 500 | 0 | 100% |

## Analysis
Profiles 1 and 5 show classic bot patterns — brand-new accounts, extreme follow ratios, no posts, no profile picture. Profiles 2 and 4 show healthy, established activity and scored 0%. Profile 3 (a real personal account) scored only 15%, flagged solely for zero posts — showing the scorer doesn't overreact to a single factor and reflects genuine, low-risk accounts accurately.

## Deliverable
Script + analysis of 5 (anonymized) profile samples.