#!/bin/bash

# Script to capture image names when a new image is updated on Docker

# Start capturing Docker events in the background
docker events --format '{{.Type}} {{.Actor.Attributes.name}}' | while read -r event; do
  # Extract the event type and image name
  event_type=$(echo "$event" | awk '{print $1}')
  image_name=$(echo "$event" | awk '{print $2}')

  # Check if a new image is updated
  if [ "$event_type" == "image" ] && [ "$image_name" != "" ]; then
    echo "New image updated: $image_name"

    # Add your logic here to perform actions with the image name, such as logging or storing in a file/database
    # ...

    # Example: Append the image name to a file
    echo "$image_name" >> updated_images.txt
  fi
done
