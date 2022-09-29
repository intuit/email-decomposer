import setuptools, os, sys

from setuptools.command.install import install

VERSION = "0.0.1"

with open('README.md') as f:
    README = f.read()

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")

with open("test_requirements.txt", "r") as f:
    test_reqs = f.read().split("\n")

setuptools.setup(
    author="Elhanan Mishraky",
    author_email="elhanan_mishraky@intuit.com",
    name="email_decomposer",
    license='Apache License 2.0',
    description='Fuzzy decomposition of email prefix to first/last name',
    version=VERSION,
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/intuit/email-decomposer",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=reqs,
    setup_requires=["pytest-runner"],
    extras_require={
        'test': test_reqs,
    },
    tests_require=test_reqs,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)