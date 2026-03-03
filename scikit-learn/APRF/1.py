from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# accuracy_score: It measures the overall correctness of the model by calculating the ratio of correctly predicted instances to the total instances.
# example: If a model correctly predicts 90 out of 100 instances, the accuracy score would be 0.9 or 90%.

# precision_score: It measures the accuracy of positive predictions by calculating the ratio of true positive predictions to the total predicted positives.
# example: If a model predicts 50 instances as positive, and out of those, 40 are actually positive, the precision score would be 0.8 or 80%.
# recall_score: It measures the model's ability to identify all relevant instances by calculating the ratio of true positive predictions to the total actual positives.
# example: If there are 100 actual positive instances, and the model correctly predicts 70 of them, the recall score would be 0.7 or 70%.

# f1_score: It is the harmonic mean of precision and recall, providing a single metric that balances both aspects of model performance.
# example: If a model has a precision of 0.8 and a recall of 0.6, the f1 score would be approximately 0.69.
# f1 score = 2 * (precision * recall) / (precision + recall)

# what actually data provided by the model

y_true = [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]  # Actual labels

# what predicted by the model
y_pred = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0]  # Predicted labels

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")