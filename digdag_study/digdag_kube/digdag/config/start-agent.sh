# Set gcp credentials

# Digdag起動前にgcloudをactivate
export GOOGLE_APPLICATION_CREDENTIALS=/secrets/digdag.json
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

# Start server
digdag server -c server.properties --disable-executor-loop