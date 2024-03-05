Welcome!

This is a python script that uses Playwright to help you print as PDFs the "pretty" version of Gong transcripts 

The transcripts that can be pulled from the api come out formatted in JSON which is fine but less useful when working with LLMs 

In testing when feeding transcripts to LLMs for analyzation we found the PDFs of the "pretty" printed transcripts worked better than the JSON formatted data

Therefore I wrote this short program that when you launch will bring you to the login screen for Gong, after logging-in and hitting enter the program will run through your CSV printing out as PDFs the call transcripts 

The transcripts should be stored in the directory that you run the program from

What you'll need:
- A CSV of just the call IDs for the calls you want to retrieve
- Your Gong's instance base pretty print url
  - For example -  https:/{Your companies url/call/pretty-transcript?call-id={Call ID variable}
