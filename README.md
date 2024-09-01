# SRT-GEN is a Simple Subtitle Maker

This project is a web-based application that allows users to generate subtitles (SRT files) for audio or video files using the Groq API and Whisper model. The application is built using Python and Gradio, making it easy to interact with the model and generate subtitles through a user-friendly interface.

## Features

- **Upload Audio/Video Files**: Users can upload audio or video files for subtitle generation.
- **Generate Subtitles**: With a single click, generate subtitles using the Whisper model provided by Groq.
- **Download SRT File**: After the subtitles are generated, the user can download the SRT file for further use.

## Requirements

- Python 3.7+
- The following Python packages:
  - `gradio`
  - `groq`
  - `python-dotenv`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/100percentBAKA/srt-gen.git
   cd srt-gen
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Groq API key to the `.env` file:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Access the interface:**
   - Open a web browser and go to the URL provided by Gradio (usually `http://localhost:7860/`).
   - Upload an audio or video file.
   - Click "Generate Subtitles" to create an SRT file.

3. **Download the SRT file:**
   - Once the subtitles are generated, you can download the SRT file from the interface.

## Code Explanation

- `format_time(seconds)`: Converts a time value in seconds to the SRT format (hours:minutes:seconds,milliseconds).
- `json_to_srt(transcription_json)`: Converts the transcription JSON from Groq into the SRT format.
- `generate_subtitles(input_file)`: Handles the entire process of reading the uploaded file, generating the transcription via the Groq API, converting it to SRT, and saving the file.
- The Gradio interface is built with `gr.Blocks`, allowing users to upload files, generate subtitles, and download the output.
