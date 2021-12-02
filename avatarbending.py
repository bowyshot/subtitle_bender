
### Variables

language = "es_core_news_sm" # Currently set to Spanish. English = "en_core_web_sm"; other languages see https://spacy.io/usage/models
output = '/Users/Olivia/Desktop/' ## Location to save output file

### Code
def bender(vtt_input, language, output):
    ## imports
    import webvtt
    import spacy

    ## Extract plain text transcript from vtt file [CREDITS TO TERENCE EDEN: https://shkspr.mobi/blog/2018/09/convert-webvtt-to-a-transcript-using-python/]
    vtt = webvtt.read(vtt_input)
    transcript = ""

    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    previous = None
    for line in lines:
        if line == previous:
           continue
        transcript += " " + line
        previous = line

    print(transcript)

    ## Split Transcript into sentences
    nlp = spacy.load(language)
    doc = nlp(transcript)

    ## Write Transcript (in sentences) into File
    f = open(output, 'w')

    for sent in doc.sents:
        f.write(str(sent)+"\n")

    f.close()

### Run Code
n=1
while True:
    vtt_input = input("Enter Vtt File Path")
    bender(vtt_input, language, output+str(n)+".txt")
    n+=1
