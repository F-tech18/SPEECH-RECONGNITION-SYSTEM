from fastapi import FastAPI, UploadFile, File
import shutil
from speech_to_text import SpeechToText
from utils import validate_audio

app = FastAPI(title="Speech-to-Text API")

model = SpeechToText()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    valid, message = validate_audio(file_location)
    if not valid:
        return {"error": message}

    result = model.transcribe_audio(file_location)

    return result
