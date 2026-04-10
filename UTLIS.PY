import os

def validate_audio(file_path):
    if not os.path.exists(file_path):
        return False, "File does not exist"

    if not file_path.endswith(".wav"):
        return False, "Only WAV format supported"

    return True, "Valid file"
