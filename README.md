# package-track

package-track is an easy to use package tracker that can automate the process of tracking your deliveries and shipments. The release is currently limited to tracking deliveries from USPS, UPS, FEDEX, and other major logistics providers that ship within the United States. 

# Things to know:

  - When you first run the program, package-track will ask you to grant email access through Gmail. **We do not store any of your email information.** We have simply built on top of the Gmail API to allow your terminal to have access to your emails. If you don't enable this functionality, the program will not work correctly. The scope and API information is available here: https://developers.google.com/gmail/api/guides.
  - package-track is cobbled together from a bunch of different dependencies. Please ensure that you have them all installed or the program will not work correctly.

# Dependencies

### For Gmail's API Functionality: 
- pickle, os, google-api-python-client, google-auth-httplib2, google-auth-oauthlib, email, and base64  

### For Online Searching / Web Scraping: 
- selenium, bs4   

### For everything else: 
- pandas, csv, re, itertools 

# Authentication

- **To allow package-track to automatically find tracking numbers from emails you need to set up the Gmail API and authenticate and authorize your application.**

### Using OAuth Client ID

- This is the case where your application or a script is accessing spreadsheets on behalf of an end user. When you use this scenario, your application or a script will ask the end user (or yourself if you’re running it) to grant access to the user’s data.

- Enable API Access for a Project if you haven’t done it yet by using this link: https://developers.google.com/gmail/api/quickstart/python.
- Click "Enable the Gmail API".
- When prompted to configure your OAuth Client, select "Desktop app" from the dropdown menu.
- A message will appear telling you that the credentials have been created successfully.
- Download the credentials by clicking the Download button.
- Move the downloaded file to ```~/.package-track/bin/credentials.json```.
- *Note: The default name for this OAuth client is Quickstart. We recommend changing the name to package-track, but it is by no means necessary for the functionality of the program.

### Installation

package-track requires [Python](https://www.python.org) v3+ to run.

To install package-track, simply use pip install: 
```sh
$ pip install package-track
```

### Development

Want to contribute? Great!

package-track could definitely use some help. Feel free to email me at idm2114@columbia.edu or send a pull request to the github repository. 


### Todos

 - Refactor code
 - Add more shipping providers

License
----

MIT


**thank you**

