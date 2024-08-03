import os
from dotenv import load_dotenv
import gradio as gr
from groq import Groq

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def json_to_srt(transcription_json):
    srt_lines = []
    for segment in transcription_json:
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text']
        srt_line = f"{segment['id']+1}\n{start_time} --> {end_time}\n{text}\n"
        srt_lines.append(srt_line)
    return '\n'.join(srt_lines)

def generate_subtitles(input_file):
    try:
        with open(input_file.name, "rb") as file:
            transcription_json_response = client.audio.transcriptions.create(
                file=(os.path.basename(input_file.name), file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
            )
        transcription_json = transcription_json_response.segments
        srt_content = json_to_srt(transcription_json)
        temp_srt_path = os.path.splitext(input_file.name)[0] + ".srt"
        with open(temp_srt_path, "w", encoding="utf-8") as temp_srt_file:
            temp_srt_file.write(srt_content)
        return temp_srt_path
    except Exception as e:
        raise gr.Error(f"Error creating SRT file: {e}")

with gr.Blocks() as demo:
    gr.Markdown("# Simple Subtitle Maker")
    input_file = gr.File(label="Upload Audio/Video")
    transcribe_button = gr.Button("Generate Subtitles")
    srt_output = gr.File(label="SRT Output File")

    transcribe_button.click(
        fn=generate_subtitles,
        inputs=[input_file],
        outputs=[srt_output],
    )

demo.launch()