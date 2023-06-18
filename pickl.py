from pickle import load

with open('mh_rf_model.pkl2', 'rb') as f:
    data = load(f)
    print(data)