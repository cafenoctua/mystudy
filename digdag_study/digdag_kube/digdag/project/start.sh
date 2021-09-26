# Set gcp credentials

# Digdag起動前にgcloudをactivate
export GOOGLE_APPLICATION_CREDENTIALS=/secrets/digdag.json
# echo $GOOGLE_APPLICATION_CREDENTIALS_JSON >> $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

# render configuration files using environment variables
# envsubst < /etc/server.properties.template > /etc/server.properties
# envsubst < /etc/.bigqueryrc.template > /root/.bigqueryrc

# Start server
digdag server --port 65432 -c server.properties