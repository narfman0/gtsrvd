from setuptools import setup, find_packages


setup(
    name='gtsrvd',
    version='0.1.0',
    description=('gtsrvd proxies localhost to public internet'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: MIT',
        'License :: OSI Approved :: Whatever I really dont care what you do',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='aws ngrok serveo',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/gtsrvd',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    test_suite='tests',
)
