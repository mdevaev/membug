#!/usr/bin/env python


import setuptools


# ===== Main =====
if __name__ == "__main__":
    setuptools.setup(
        name="membug",
        version="0.1",
        url="https://github.com/yandex-sysmon/membug",
        license="LGPLv3",
        author="Devaev Maxim",
        author_email="mdevaev@gmail.com",
        description="Small set of memory debugging tools",
        platforms="any",

        py_modules=[
            "membug",
        ],

        classifiers=[ # http://pypi.python.org/pypi?:action=list_classifiers
            "Development Status :: 2 - Pre-Alpha",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Debuggers",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
