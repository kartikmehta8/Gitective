import subprocess


def clone_repository(url, username, password, destination):
    command = ["git", "clone", url, destination]

    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        input_data = username + "\n" + password + "\n"

        output, error = process.communicate(input=input_data)

        if process.returncode == 0:
            print("Repository cloned successfully.")
        else:
            print(f"Error cloning repository: {error}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
