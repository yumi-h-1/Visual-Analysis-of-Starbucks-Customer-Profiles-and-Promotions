import pandas as pd

# Function to extract 'reward' and 'offer_id' / 'offer id'
def extract_values(value_dict):
  # Directly extract offer_id or offer id, with reward defaulting to 0
  offer_id = value_dict.get('offer_id') or value_dict.get('offer id')  # Check both keys
  reward = value_dict.get('reward', 0)  # Default to 0 if 'reward' is not present
  return pd.Series([offer_id, reward])  # Return as a Series