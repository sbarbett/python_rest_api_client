from setuptools import setup

setup(
    name='ultra_rest_client',
    version='0.2.2',
    description='A sample Python client for communicating with the UltraDNS REST API',
    url='https://github.com/ultradns/python_rest_api_client',
    author='UltraDNS',
    author_email='ultrassp-oss@vercara.com',
    license='Apache License, Version 2.0',
    keywords='ultra_rest_client',
    packages=['ultra_rest_client'],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'Topic :: Internet :: Name Service (DNS)',
        'License :: OSI Approved :: Apache Software License',
    ],
    zip_safe=False
)
