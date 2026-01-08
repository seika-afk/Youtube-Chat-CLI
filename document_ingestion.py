from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from  urllib.parse import  urlparse,parse_qs
import sys
#first getting The transcripts for the video


class Get_transcription:

    def __init__(self,uri):
        self.uri=uri
        
    def get_transcript(self):
        try: 
            vid_id=parse_qs(urlparse(self.uri).query)["v"][0]
            transcripts= YouTubeTranscriptApi().fetch(vid_id,languages=["en"])
            return transcripts
        except TranscriptsDisabled:
            print("No Transcription Available for the Video")
            sys.exit("Please Provide other Youtube link.")
            

# main fn to be used as module
def execute(uri):
    x=Get_transcription(uri)
    return x.get_transcript()
        



