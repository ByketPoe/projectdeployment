# Flask Project Deployment - Emma Farrell 2025

Web application is hosted on PythonAnywhere and can be accessed here: https://g00398267.pythonanywhere.com/

Any modules required to run the application are listed in requirements.txt.

I tried to do an API call to an external website that had data for fish nursery locations in the seas around Ireland. To map the results, I needed to use a module called folium. This worked on my local machine, but PythonAnywhere could not recognise the location of the module in order for it to be imported, and this brought down the whole web app, so I removed it. The web app has a link to an annotated map I created locally, and it links to the source of the data. 