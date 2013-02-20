import os
import sys
from setuptools import setup, find_packages
from extras import RunFlakesCommand

guardian = __import__('guardian')
readme_file = os.path.join(os.path.dirname(__file__), 'README.rst')
try:
    long_description = open(readme_file).read()
except IOError as err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

if sys.version_info >= (3,):
    extra_kwargs = {'use_2to3': True}
else:
    extra_kwargs = {}

setup(
    name = 'django-guardian',
    version = guardian.get_version(),
    url = 'http://github.com/lukaszb/django-guardian',
    author = 'Lukasz Balcerzak',
    author_email = 'lukaszbalcerzak@gmail.com',
    download_url='https://github.com/lukaszb/django-guardian/tags',
    description = guardian.__doc__.strip(),
    long_description = long_description,
    zip_safe = False,
    packages = find_packages(),
    include_package_data = True,
    license = 'BSD',
    install_requires = [
        'Django>=1.2',
    ],
    tests_require = [
        'mock',
    ],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Security',
    ],
    test_suite='tests.main',
    cmdclass={'flakes': RunFlakesCommand},
    **extra_kwargs
)

