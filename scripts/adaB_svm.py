<<<<<<< HEAD
def run():
        import numpy as np
        from sklearn.svm import SVC
        svc=SVC(probability=True, kernel='linear')
        import pandas as pd
        import matplotlib.pyplot as pyplot
        import seaborn as sns
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import AdaBoostClassifier
        from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score

        #Reading In The Data
        df = pd.read_table("/home/kshitij/PS/data/australian.csv", sep='\s+', header=None)

        #15th colums is class attribute

        y = df[14]
        X = df.drop(columns = 14)
        y.value_counts()

        # Split features and target into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y, test_size = 0.8)

        #Training with base classifier as svm
        adaB = AdaBoostClassifier(random_state=1, base_estimator=svc)
        adaB.fit(X_train, y_train)

        # Make predictions for the test set
        y_pred_test = adaB.predict(X_test)


        # View accuracy score
        accuracy_score(y_test, y_pred_test, normalize=True)
        print(classification_report(y_test, y_pred_test))

        adaB_probs = adaB.predict_proba(X_test)
        # keep probabilities for the positive outcome only
        adaB_probs = adaB_probs[:, 1]
        # calculate scores
        adaB_auc = roc_auc_score(y_test, adaB_probs)
        # summarize scores
        print('AdaB_svm: ROC AUC=%.3f' % (adaB_auc))
        print("accuracy_score is %.3f" % (accuracy_score(y_test, y_pred_test, normalize=True)))
        # calculate roc curves
        adaB_fpr, adaB_tpr, _ = roc_curve(y_test, adaB_probs)

        # plot the roc curve for the model
        pyplot.plot(adaB_fpr, adaB_tpr, marker='.', label='AdaB_svm')
        # axis labels
        pyplot.xlabel('False Positive Rate')
        pyplot.ylabel('True Positive Rate')
        # show the legend
        pyplot.legend()
        # show the plot
        pyplot.show()
=======
import numpy as np
from sklearn.svm import SVC
svc=SVC(probability=True, kernel='linear')
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score

#Reading In The Data
df = pd.read_table("../data/australian.csv", sep='\s+', header=None)

#15th colums is class attribute

y = df[14]
X = df.drop(columns = 14)
y.value_counts()

# Split features and target into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y, test_size = 0.8)

#Training with base classifier as svm
adaB = AdaBoostClassifier(random_state=1, base_estimator=svc)
adaB.fit(X_train, y_train)

# Make predictions for the test set
y_pred_test = adaB.predict(X_test)


# View accuracy score
accuracy_score(y_test, y_pred_test, normalize=True)
print(classification_report(y_test, y_pred_test))

adaB_probs = adaB.predict_proba(X_test)
# keep probabilities for the positive outcome only
adaB_probs = adaB_probs[:, 1]
# calculate scores
adaB_auc = roc_auc_score(y_test, adaB_probs)
# summarize scores
print('AdaB_svm: ROC AUC=%.3f' % (adaB_auc))
# calculate roc curves
adaB_fpr, adaB_tpr, _ = roc_curve(y_test, adaB_probs)

# plot the roc curve for the model
pyplot.plot(adaB_fpr, adaB_tpr, marker='.', label='AdaB_svm')
# axis labels
pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')
# show the legend
pyplot.legend()
# show the plot
pyplot.show()
>>>>>>> f01b1bf2592c9d821a9f4ab12c14250e32f10e4d
