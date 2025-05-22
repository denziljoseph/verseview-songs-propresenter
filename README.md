# Convert VerseView Malayalam songs into Propresenter slides

## Prerequisites
- Download protoc.exe from https://github.com/protocolbuffers/protobuf/releases
unzip the protoc-win64.zip and extract protoc.exe
- Download the proto files from: https://github.com/greyshirtguy/ProPresenter7-Proto

## Decode a file
Change the directory to /proto

`../protoc/protoc.exe --decode="rv.data.Presentation" propresenter.proto < /Path/To/ProPresenter/PresentationFile`

## Encode a file
Change the directory to /proto

`../protoc/protoc.exe --encode="rv.data.Presentation" propresenter.proto < "C:\Projects\verseview-songs-propresenter\songs\Unarvin varam labhippaan"`

## Decode and Encode the VW db in bulk
- run `main.py`
- output will be generated in the songs folder
- import the song in Propresenter 7 library
- test
