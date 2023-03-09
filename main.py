import whisper
import pysrt

model = whisper.load_model("base")
audio_file = ("YOUR AUDIO FILE PATH")
result = model.transcribe(audio_file, language='en')

subs = pysrt.SubRipFile()
sub_idx = 1

for i in range(len(result["segments"])):
    start_time = result["segments"][i]["start"]
    end_time = result["segments"][i]["end"]
    duration = end_time - start_time
    timestamp = f"{start_time:.3f} - {end_time:.3f}"
    text = result["segments"][i]["text"]
    
    sub = pysrt.SubRipItem(index=sub_idx, start=pysrt.SubRipTime(seconds=start_time), 
                           end=pysrt.SubRipTime(seconds=end_time), text=text)
    subs.append(sub)
    sub_idx += 1
    
subs.save("output.srt")
