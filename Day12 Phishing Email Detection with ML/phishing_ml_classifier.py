
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 50-sample dataset: mix of phishing (1) and legit (0) emails
emails = [
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediately",
    "Urgent: update your bank details to avoid closure",
    "Your PayPal account has been limited, verify now",
    "Confirm your identity within 24 hours or lose access",
    "Your password will expire today, click to reset",
    "Congratulations! You've won a free iPhone, claim now",
    "Security alert: unusual login detected, verify immediately",
    "Your invoice payment failed, update billing info now",
    "Action required: your subscription will be cancelled",
    "You have a pending refund, click to receive it",
    "Your account has been compromised, act now",
    "Final notice: your package delivery failed, reschedule now",
    "Your tax refund is ready, verify your details to claim",
    "Immediate action needed: unusual activity on your account",
    "Your email storage is full, upgrade now to avoid loss",
    "Click below to unlock your frozen account",
    "You must verify your identity to avoid account suspension",
    "Your credit card has been charged, dispute now",
    "Your document is ready for e-signature, click here",
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready for review",
    "Meeting notes from yesterday's sync",
    "Lunch tomorrow? Let me know what time works",
    "Here's the report you asked for last week",
    "Reminder: project deadline is next Friday",
    "Happy birthday! Hope you have a great day",
    "The quarterly numbers look good this month",
    "Can you review this document before our call",
    "Thanks for your help with the presentation",
    "Let's schedule a call to discuss the proposal",
    "Attached is the updated project timeline",
    "Please find the minutes from today's meeting",
    "Your order has shipped and will arrive Friday",
    "Weekly newsletter: company updates and news",
    "Great job on the project, well done team",
    "Can we reschedule our meeting to next week",
    "Here's the invoice for last month's services",
    "The office will be closed for the holiday",
    "Your subscription renewal receipt is attached",
    "New blog post published on our website",
    "Reminder to submit your timesheet by Friday",
    "Welcome to the team, looking forward to working with you",
    "Please review and approve the attached budget",
    "Conference call scheduled for 10am tomorrow",
    "Your flight booking confirmation and itinerary",
    "The parking lot will be repaved next week",
    "Feedback requested on the new design mockups",
    "Company picnic is scheduled for next Saturday",
    "Your monthly bank statement is now available",
]

labels = [1]*20 + [0]*30  # first 20 phishing, remaining 30 legit

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    emails, labels, test_size=0.3, random_state=42
)

# Build and train the model
pipe = Pipeline([
    ("vec", CountVectorizer()),
    ("clf", MultinomialNB()),
])
pipe.fit(X_train, y_train)

# Evaluate on test set
predictions = pipe.predict(X_test)

print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, predictions))

print("\n=== Accuracy ===")
print(f"{accuracy_score(y_test, predictions) * 100:.2f}%")

print("\n=== Classification Report ===")
print(classification_report(y_test, predictions, target_names=["Legit", "Phishing"]))

# Test on new, unseen examples
print("\n=== Predictions on New Emails ===")
tests = [
    "Please verify your PayPal login immediately",
    "Meeting notes from yesterday",
    "Your account will be suspended, click here now",
    "Can you send me the report by tomorrow",
]
for t in tests:
    pred = pipe.predict([t])[0]
    print(f"{'PHISHING' if pred else 'LEGIT'}: {t}")