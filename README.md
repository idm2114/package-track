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

I recognize that this is a ridiculous number of dependencies for a package to function. However, I hope that most (or at least some) of these libraries are already installed. If you are looking to install any of these, simply use 
```sh 
$ pip install [package-name] 
```
and insert the name of the package listed above. 

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
 - Enable opt-in email access
 - Add more shipping providers

License
----

MIT


**thank you**

