# Day 8 — USB Drop Attack Simulation

## Objective
Simulate a USB drop payload (for awareness purposes) using benign Python autorun-style logic.

## Theory
- USB drops: attackers deliberately leave infected USB drives in target locations, hoping curiosity leads someone to plug it in.
- AutoRun abuse: a malicious script could run automatically the moment a USB is inserted (historically on Windows); modern systems disable AutoRun by default.
- Defense: disable AutoRun, use endpoint DLP (Data Loss Prevention) tools, and train users to never plug in unknown USB drives.

## What the script does
`usb_payload_sim.py` simulates what a real USB payload might silently collect the moment it runs — timestamp, hostname, OS, OS version, current user, and current directory — and saves it to a local text file. No data is sent anywhere or altered; it only demonstrates the exposure risk.

## Tools used
- `platform`, `socket`, `os`, `datetime` (all stdlib)

## Demo Output
timestamp: 2026-08-12 13:08:48.181671
hostname: Yusra-Imran
os: Windows
version: 10.0.26200
user: DELL
cwd: D:\Sqrock IT Cybersecurity
This shows how quickly a malicious USB payload could fingerprint a machine — identifying the OS/version (to pick a matching exploit) and the username/hostname (for further targeting) — all without the user noticing anything happened.

## USB Drop Prevention Policy
1. **Disable AutoRun/AutoPlay** on all company devices via group policy.
2. **Never plug in unknown USB devices** — treat any found USB drive as suspicious, regardless of labeling.
3. **Report found USB drives** to IT/security instead of inspecting them personally.
4. **Use endpoint protection (DLP)** that flags or blocks unauthorized USB device activity.
5. **Awareness training** — periodic reminders that USB drops are a real, low-cost attack vector used in real-world penetration tests and breaches.

## Deliverable
Simulated output file + write-up on USB drop prevention policy.