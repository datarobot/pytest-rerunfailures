from setuptools import setup

test_deps = [
    "xmltodict==0.11.0",
    "pytest<8",
    "pytest-xdist>=1.23.2",
    "pytest-forked>=1.0.1",
]

setup(
    name="pytest-rerunfailures",
    description="pytest plugin to re-run tests with fixture invalidation to eliminate flaky failures",
    long_description=(open("README.rst").read() + "\n\n" + open("CHANGES.rst").read()),
    author="@continuous-integration",
    email="continuous-integration@datarobot.com",
    url="https://github.com/datarobot/pytest-rerunfailures",
    py_modules=["pytest_rerunfailures"],
    entry_points={"pytest11": ["rerunfailures = pytest_rerunfailures"]},
    install_requires=["pytest>=6,<8", "mock>=1.0.1"],
    tests_require=test_deps,
    setup_requires=["setuptools-scm==5.0.2", "wheel"],
    python_requires=">=3.7",
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="py.test pytest rerun failures flaky",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    use_scm_version=dict(version_scheme="python-simplified-semver", local_scheme="no-local-version"),
)
