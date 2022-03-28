import subprocess

# def speak(text):
#     subprocess.call(['espeak', '-v', 'en-us', text])

def speak(text):
    subprocess.Popen(['./scripts/festival.sh', text], stdin=subprocess.PIPE)
    # subprocess.Popen(['echo',text,'|','festival','--tts'],shell=True)
