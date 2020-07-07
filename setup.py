from distutils.core import setup
setup(
  name = 'package-track',         # How you named your package folder (MyLib)
  packages = ['package-track'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'command line tool to track packages using gmail api and selenium',   # Give a short description about your library
  author = 'Ian Macleod',                   # Type in your name
  author_email = 'idm2114@columbia.edu',      # Type in your E-Mail
  url = 'https://github.com/idm2114/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/idm2114/package-track/archive/v_02.tar.gz',    # I explain this later on
  keywords = ['tracking numbers', 'shipping', 'packages'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pickle',
          'os',
          'google-api-python-client',
          'google-auth-httplib2',
          'google-auth-oauthlib',
          'base64',
          'email',
          'bs4',
          're',
          'itertools',
          'selenium',
          'pandas',
          'csv',
          'pyfiglet',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
