
from distutils.core import setup
setup(
  name = 'mbs_sys',         # How you named your package folder (MyLib)
  packages = ['mbs_sys'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='Apache 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library gets the system info.',   # Give a short description about your library
  author = 'Muhammad Bilal Shaikh',                   # Type in your name
  author_email = 'mbs.techy@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/mbilalshaikh',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mbilalshaikh/mbs_sys/archive/refs/tags/v_04.tar.gz',    # I explain this later on
  keywords = ['system-info', 'ip-address', 'mac-address'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
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
    'Programming Language :: Python :: 3.8',
  ],
)
