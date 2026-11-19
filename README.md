# Tanglish to English Translator

A small Tkinter desktop app: type Tamil written in English letters (Tanglish), and it shows the English meaning and reads it aloud with Google Text-to-Speech.

Built as a short assignment (Task 2) in February 2025. `Output.mkv` is a screen recording of the app running.

## How it works

- `dictionary.py` holds a hand-written map of 35 common Tanglish words and phrases to English.
- `test.py` is the app. It translates word by word using that map, shows the result, then plays it with gTTS and pygame.

Because translation is a word-by-word lookup, multi-word entries such as "epdi iruka" are not matched yet, and unknown words are passed through unchanged.

## Running it

Requires Python 3 with Tkinter (included with the python.org installers on Windows and macOS; on Linux install `python3-tk`) and an internet connection for gTTS.

```bash
pip install -r requirements.txt
python test.py
```
