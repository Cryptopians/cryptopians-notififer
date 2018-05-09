from setuptools import find_packages, setup


test_require = [
    'flake8',
    'isort',
    'pytest',
    'pytest-mock',
]

setup(
    name='cryptopians-notifier',
    version='0.1.0',
    description='Cryptopians Notifier.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    entry_points={
        'console_scripts': [
            'cn=cn.core.management.command_line:main'
        ]
    },
    extras_require={
        'test': test_require
    },
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
