from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='Markdown Tracker',
      version='0.1.1',
      description='Tools for tracking Markdown & Taskpaper files',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='markdown statistics',
      url='https://github.com/jykim/mdt',
      author='Jin Young Kim',
      author_email='lifidea@gmail.com',
      license='MIT',
      packages=['mdt'],
      install_requires=[
          'numpy', 'pandas'
      ],
      scripts=['mdt/mdt'],
      test_suite='TestMDT',
      include_package_data=True,
      zip_safe=False)