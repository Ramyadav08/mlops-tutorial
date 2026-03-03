from sklearn.metrics import confusion_matrix

# what actually data provided by the model
y_true = [0, 1, 1, 0, 1, 1, 0, 0, 1, 0]  # Actual labels
# what predicted by the model
y_pred = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0]  # Predicted labels

cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# output: is [[4 1],[1,4]]
# Explanation:
# The confusion matrix is a 2x2 table that summarizes the performance of a classification model.
# Each row of the matrix represents the actual class, while each column represents the predicted class.
# In this example, the confusion matrix is:
# [[4 1]
#  [1 4]]
# Here's what each element represents:
# True Negatives (TN) = 4: The model correctly predicted 4 instances as class 0 (negative class).
# False Positives (FP) = 1: The model incorrectly predicted 1 instance as class 1 (positive class) when it was actually class 0.    
# False Negatives (FN) = 1: The model incorrectly predicted 1 instance as class 0 when it was actually class 1. 
# True Positives (TP) = 4: The model correctly predicted 4 instances as class 1.