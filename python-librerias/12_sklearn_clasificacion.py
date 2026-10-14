"""Librería: scikit-learn
Entrena un clasificador KNN con el dataset Iris y evalúa su precisión."""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    modelo = KNeighborsClassifier(n_neighbors=3)
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)

    print(f"Precisión: {accuracy_score(y_test, predicciones):.2%}\n")
    print(classification_report(y_test, predicciones, target_names=iris.target_names))

    flor = [[5.1, 3.5, 1.4, 0.2]]
    print("Predicción para", flor[0], "→", iris.target_names[modelo.predict(flor)[0]])


if __name__ == "__main__":
    main()
