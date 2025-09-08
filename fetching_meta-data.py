from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.oauth2 import service_account

# Path to your service account key JSON file
KEY_PATH = "service_key.json"

# Create credentials from the service account file
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

# Initialize the client with credentials
client = BetaAnalyticsDataClient(credentials=credentials)

# List metadata for a property
#for security reasons it changes after execution(only for screenshot)
property_id = "123456789"
metadata = client.get_metadata(name=f"properties/{property_id}/metadata")

print("Available Dimensions:")
for dim in metadata.dimensions:
    print(f"- {dim.api_name} ({dim.ui_name})")

print("\nAvailable Metrics:")
for met in metadata.metrics:
    print(f"- {met.api_name} ({met.ui_name})")
