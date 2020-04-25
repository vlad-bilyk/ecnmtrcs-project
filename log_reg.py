from statistics import mean
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def run_logreg(x, y):
    """
    :param x: pandas.DataFrame with explanatory variables data
    :param y: pandas.DataFrame with dependent variable data
    :return: None
    """

    # ------------------- creating a model -------------------
    logit_model = sm.Logit(y, x)
    result = logit_model.fit()
    print(result.summary2())

    # ------------------- fitting the model -------------------
    ## randomly splits the data into train and test subsets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    ## predicting values of y on test subset of x
    y_pred = logreg.predict(x_test)
    ## predicting probability of y = 1
    y_prob = logreg.predict_proba(x_test)
    y_prob_win = list(map(lambda x: x[1], y_prob))

    # ------------------- results -------------------
    ## accuracy of predictions
    acc = logreg.score(x_test, y_test)
    print("Accuracy on test set: {}".format(acc))

    errors = [abs(yt - yp) for yt, yp in zip(y_test, y_prob_win)]
    n = range(len(errors))

    plt.plot(n, errors, 'o', markersize=1)
    plt.title("Radiant win probability: prediction errors")
    plt.savefig('plots/errors')
    plt.show()

    print("Predicted radiant win probability average error: {}".format(mean(errors)))

    ## confusion matrix
    confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
    print(confusion_matrix)
    correct_pred = confusion_matrix[0][0] + confusion_matrix[1][1]
    incorrect_pred = confusion_matrix[0][1] + confusion_matrix[1][0]
    print("Correct predictions: {}".format(correct_pred))
    print("Incorrect predictions: {}".format(incorrect_pred))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(confusion_matrix)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, confusion_matrix[i, j], ha='center', va='center', color='red')
    plt.savefig('plots/cmatrix')
    plt.show()
