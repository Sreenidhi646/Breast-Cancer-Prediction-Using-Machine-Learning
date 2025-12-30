from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Robust model loader

def load_model(path):
    """Try multiple strategies to load the model to handle pickles created with
    different tools / Python versions.
    """
    import os

    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")

    # 1) Try normal pickle load
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except Exception as e1:
        # 2) Try pickle with latin1 encoding (useful for numpy arrays / py2 -> py3)
        try:
            with open(path, "rb") as f:
                return pickle.load(f, encoding="latin1")
        except Exception as e2:
            # 3) Try joblib as a last resort (model may have been saved with joblib)
            try:
                import joblib
            except Exception:
                try:
                    # older scikit-learn exposed joblib here
                    from sklearn.externals import joblib
                except Exception:
                    raise RuntimeError(
                        "Model load failed: pickle errors: {}, {}. Also couldn't import joblib.".format(e1, e2)
                    )
            try:
                return joblib.load(path)
            except Exception as e3:
                raise RuntimeError(
                    "All model loading attempts failed. Errors: {}, {}, {}".format(e1, e2, e3)
                )

# Load the model at startup; fail fast with a clear message if loading fails
try:
    model = load_model("model/Breastcancer.pkl")
except Exception as e:
    import traceback, sys

    traceback.print_exc()
    print(f"ERROR: Unable to load ML model: {e}")
    sys.exit(1)

# Load dataset to get feature names
# Normalize column names and drop serial-number column (S/N) if present
df = pd.read_csv("data/breast-cancer-dataset.csv")
# strip whitespace from column names
df.columns = df.columns.str.strip()
# remove serial number column to avoid showing it on the form
if 'S/N' in df.columns:
    df = df.drop(columns=['S/N'])

# Assume last column is target
feature_names = df.columns[:-1]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_features = []

        for feature in feature_names:
            value = float(request.form[feature])
            input_features.append(value)

        final_features = np.array([input_features])
        prediction = model.predict(final_features)

        result = "Malignant (Cancer Detected)" if prediction[0] == 1 else "Benign (No Cancer)"

        return render_template("result.html", result=result)

    return render_template("index.html", feature_names=feature_names)

if __name__ == "__main__":
    app.run(debug=True)
