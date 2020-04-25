import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt


def run_logreg(x, y):
    """
    :param x: pandas.DataFrame with explanatory variables data
    :param y: pandas.DataFrame with dependent variable data
    :return: None
    """

    # ------------------- implementing the model -------------------
    logit_model = sm.Logit(y, x)
    result = logit_model.fit()
    print(result.summary2())

    # ------------------- logistic regression model fitting -------------------
    ## randomly splits the data into train and test subsets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    ## predicting values of y on test subset of x
    y_pred = logreg.predict(x_test)
    acc = logreg.score(x_test, y_test)
    print("Accuracy on test set: {}".format(acc))

    ## confusion matrix
    confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(confusion_matrix)
    correct_pred = confusion_matrix[0][0] + confusion_matrix[1][1]
    incorrect_pred = confusion_matrix[0][1] + confusion_matrix[1][0]
    print("Correct predictions: {}".format(correct_pred))
    print("Incorrect predictions: {}".format(incorrect_pred))

    ## classification report
    print(classification_report(y_test, y_pred))

    ## ROC curve
    logit_roc_auc = roc_auc_score(y_test, logreg.predict(x_test))
    fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(x_test)[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.savefig('plots/Log_ROC')
    plt.show()
