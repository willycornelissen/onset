import sys,os
import freesound
import argparse

parser = argparse.ArgumentParser(description='Download audio from freesound.org')
parser.add_argument('searchString', metavar='N', nargs='+', help='Search term.')
args = parser.parse_args()

client = freesound.FreesoundClient()
#You are expected to place your token in the line below
client.set_token("zMubTd74c7ShQ7W8rT0b2MZyQw5ZL93i90VlawbA","token")

maxNumFilePerInst=10

print("Searching for ", args.searchString)
results = client.text_search(query=args.searchString[0],fields="id,name,previews,tags")
cnt=0
for sound in results:
    sound.retrieve_preview(".",sound.name+".wav")
    filename='download/' + str(args.searchString[0]) + str(cnt) + ".wav"
    os.rename(sound.name+".wav",filename)
    print(filename)
    cnt=cnt+1
    if cnt>=maxNumFilePerInst:
        break
print("Files copied!")
