import setuptools
import os


long_description = ('Hopps is a python module implementing the RabbitMQ API with an easy-to-use interface.')

setuptools.setup(
    name='hopps',
    version='1.0.0',
    description='Hopps Python API Client Library',
    long_description=open('README.md').read(),
    maintainer='Itamar Knafo',
    maintainer_email='itamarkn60@gmail.com',
    # url='https://pika.readthedocs.io',
    project_urls={
        'Source': 'https://github.com/itamadev/hopps',
    },
    packages=setuptools.find_packages(include=['hopps', 'hopps.*']),
    license='Apache',
    install_requires=requirements,
    package_data={'': ['LICENSE', 'README.md']},
    # extras_require={
    #     'gevent': ['gevent'],
    #     'tornado': ['tornado'],
    #     'twisted': ['twisted'],
    # },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Communications', 'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
    ],
    zip_safe=True)
