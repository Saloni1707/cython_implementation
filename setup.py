from setuptools import setup
from Cython.Build import cythonize

setup(
    name="CyImplement",
    ext_modules=cythonize(
    [
    "utils/cy_helpers.pyx",
    "utils/mongo_utils.pyx"
    ],
    compiler_directives={"language_level":"3"}
    ),
    zip_safe=False,
)