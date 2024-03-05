Welcome!

This is a python script that uses Playwright to help you print the "pretty" version of Gong transcripts 

The transcripts that can be pulled from the api come out formatted in JSON

In testing when feeding transcripts to LLMs for analyzation we found the PDFs of the "pretty" printed transcripts worked better than the JSON formatted data

What you'll need:
- A CSV of just the call IDs for the calls you want to retrieve
- Your Gong's instance base pretty print url
  - For example -  https:/{Your companies url/call/pretty-transcript?call-id={Call ID variable}
