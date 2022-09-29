from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    reqs = f.read().split("\n")

with open("test_requirements.txt", "r") as f:
    test_reqs = f.read().split("\n")

setup(
    name="email_decomposer",
    url="https://github.com/intuit/email-decomposer.git",

    use_scm_version={
        "write_to": "email_decomposer/__version.py",
        "write_to_template": "__version__ = \"{version}\"\n",
    },

    author="Elhanan Mishraky",
    author_email="elhanan_mishraky@intuit.com",
    description='Fuzzy decomposition of email prefix to first/last name',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,

    setup_requires=["setuptools-scm<=6.0.1"],
    extras_require={
        "dev": test_reqs
    },
)
