# FFMPEG Guide for Me

## Installation
Windows:
```
winget install ffmpeg
```
Linux:
```
sudo apt install ffmpeg
```
## MKV to iPhone mp4:
For iPhone convert to H.264+AAC
```
ffmpeg -i input.mkv -c:v libx264 -c:a aac output.mp4
```

## MKV to iPhone mp3:
For iPhone convert to AAC
```
ffmpeg -i input.mkv -map 0:a -c:a aac output.m4a
```

## Trimming:
Trim the video with re-encoding so there there is no blackout. 
Also, `to hh:mm:ss` is length of video.
```
ffmpeg -ss 00:30:00 -i input.mp4 -to 00:00:10 -c:v libx264 -c:a aac -map 0:v -map 0:a output.mp4
```

Extract subtitles:
```
ffmpeg -ss 00:20:12 -i input.mkv -to 00:01:00 -map 0:s output.ass
```
Reencoding should be 1sec per 1sec of video.

Trimm subtitles to `.ass` extension so that sync is preserved.
```
ffmpeg -ss 00:30:00 -i input.srt -to 00:00:10 output.ass
```

## Subtitiles
Converting srt to ass so as to hardcode
```
ffmpeg -i input.srt input.ass
```
Hard code subtitles into video. USE .ASS (Read trimming subtitles)
```
ffmpeg -i input.mp4 -vf subtitles=input.ass output.mp4
```

## Error : Too many packets buffered for output
Add this option at the end of your video options to increase the queue size:
```
-max_muxing_queue_size 1024
```