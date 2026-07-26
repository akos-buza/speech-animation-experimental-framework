import json
import base64
import os

INPUT_FILE = "/Users/abuza/Downloads/study_result_26/comp-result_26/data.txt"
OUTPUT_FOLDER = "/Users/abuza/Downloads/extracted_audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0

for trial in data:

    if (
        trial.get("trial_type") == "html-audio-response"
        and "response" in trial
        and trial["response"]
    ):

        filename = os.path.join(
            OUTPUT_FOLDER,
            trial["recording_name"] + ".ogg"
        )

        audio_bytes = base64.b64decode(
            trial["response"]
        )

        with open(filename, "wb") as out:
            out.write(audio_bytes)

        print("saved:", filename)

        count += 1

print()
print("Finished.")
print("Extracted", count, "audio files.")
