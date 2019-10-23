from distutils.core import setup
setup(
  name = 'TimeBetweenBusinessHours',
  packages = ['TimeBetweenBusinessHours'],
  version = '0.1',
  license='MIT',
  description = 'Get the Time Between Business Hours',
  author = 'AndreJambersi',
  author_email = 'andrejambersi@gmail.com',
  url = 'https://github.com/AndreJambersi/TimeBetweenBusinessHours',
  download_url = 'https://github.com/AndreJambersi/TimeBetweenBusinessHours/archive/v_01.tar.gz',
  keywords = ['JOB', 'TIME', 'DATE'],
  install_requires=[
          'TimeBetweenBusinessHours',
          'datetime',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
