# Set gcp credentials
digdag secrets --local --set gcp.credential=@/secrets/digdag.json

# Start server
digdag server -m