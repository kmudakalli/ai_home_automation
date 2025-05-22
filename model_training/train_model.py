import joblib
from sklearn.ensemble import RandomForestClassifier

X = [[17, 0], [18, 1], [19, 2], [20, 3], [21, 4], [14, 5], [12, 6]]
y = [1, 1, 1, 1, 1, 0, 0]

clf = RandomForestClassifier()
clf.fit(X, y)
joblib.dump(clf, "home_return_model.pkl")
