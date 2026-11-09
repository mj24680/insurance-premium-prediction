import pickle
import pandas as pd

# improvement : seperate model logic

# import the ML model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# improvement
# generally model version comes form MLFlow software usign Model registry component which tracks your model version
MODEL_VERSION = '1.0.0'

# improvement : for confidence score
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    # prdict the class
    predicted_class = model.predict(input_df)[0]

    # get probabilities for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }