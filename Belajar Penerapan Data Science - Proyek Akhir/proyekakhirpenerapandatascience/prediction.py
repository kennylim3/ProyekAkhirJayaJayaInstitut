import joblib
import numpy as np

model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    # Check for NaN values and handle them appropriately
    data = np.nan_to_num(data)

    # Ensure that data has the correct shape (2D array)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # Make predictions
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result