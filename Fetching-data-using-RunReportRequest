from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
from google.oauth2 import service_account

# Path to your service account key JSON file
KEY_PATH = "service_key.json"

# Replace with your GA4 property ID
PROPERTY_ID = "123456789" #for security reasons it changes after execution(only for screenshot)

# Create credentials from the service account file
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

# Initialize the client with credentials
client = BetaAnalyticsDataClient(credentials=credentials)

# Build the report request
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    dimensions=[{"name": "country"}],
    metrics=[{"name": "activeUsers"}],
    date_ranges=[{"start_date": "7daysAgo", "end_date": "today"}],
)

# Run the report
response = client.run_report(request)


# Process results into list of dicts
results = []
for row in response.rows:
    row_data = {}

    # Add dimensions
    for idx, dim in enumerate(response.dimension_headers or []):
        row_data[dim.name] = row.dimension_values[idx].value

    # Add metrics
    for idx, metric in enumerate(response.metric_headers):
        value_str = row.metric_values[idx].value
        try:
            # Convert to int or float if possible
            row_data[metric.name] = float(value_str) if "." in value_str else int(value_str)
        except ValueError:
            row_data[metric.name] = value_str  # fallback as string

    results.append(row_data)

# Print the results
print("\n✅ Active Users by Country:")
for row in results:
    print(row)
