import subprocess

# Function to capture image names when a new image is updated on Docker
def capture_docker_image_names():
    # Start capturing Docker events
    docker_events = subprocess.Popen(['docker', 'events', '--format', '{{.Type}} {{.Actor.Attributes.name}}'], stdout=subprocess.PIPE)

    # Process the event stream
    for event in iter(docker_events.stdout.readline, b''):
        event = event.decode().rstrip()

        # Extract the event type and image name
        event_type, image_name = event.split(' ', 1)

        # Check if a new image is updated
        if event_type == 'image' and image_name:
            print(f"New image updated: {image_name}")

            # Add your logic here to perform actions with the image name, such as logging or storing in a file/database
            # ...

            # Example: Append the image name to a file
            with open('updated_images.txt', 'a') as file:
                file.write(image_name + '\n')

# Call the function to start capturing Docker image updates
capture_docker_image_names()
