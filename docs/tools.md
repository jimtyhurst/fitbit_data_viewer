# Choice of tools

We list some of the factors that led to the choice of tools for this project.

**Contents**

- [datetime](#datetime)
- [MyST](#myst)
- [Polars](#polars)
- [pytest](#pytest)
- [uv](#uv)

---

## datetime
https://docs.python.org/3/library/datetime.html

- It is in the Python Standard Library, so it is used widely.
- However, many people complain about the API being unintuitive and too complex.
- Other packages to consider:
  - Arrow
    - "... offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps."
    - https://arrow.readthedocs.io/
    - https://github.com/arrow-py/arrow
  - Pendulum
    - "Python datetimes made easy."
    - https://pendulum.eustace.io/
    - https://github.com/sdispater/pendulum

## MyST
https://myst-parser.readthedocs.io/en/latest/index.html

MyST is a [Sphinx](https://www.sphinx-doc.org/) and [Docutils](https://docutils.sourceforge.io/) extension to parse MyST, a rich and extensible flavour of Markdown for authoring technical and scientific documentation.

## Polars
https://pola.rs/

We have adopted [Polars](https://pola.rs/), rather than [Pandas](https://pandas.pydata.org/), as the package for DataFrames.

- Polars is much faster.
- Polars can manage larger datasets.
- This new analytics project seemed like a good opportunity to learn Polars and experiment with Polars.

## pytest
https://github.com/pytest-dev/pytest

- pytest is very popular.
- pytest has a simpler API and is easier to use than the [unittest](https://docs.python.org/3/library/unittest.html) package included with standard Python.

## ruff
https://astral.sh/ruff

- ruff provides lots of functionality and options for linting and formatting.
- ruff is _very_ fast.

## uv
https://docs.astral.sh/uv/

- uv makes it easy to manage:
  - Python versions.
  - Python virtual environment.
  - Package dependencies, including distinguishing between application dependencies and development environment dependencies.
  - Building the package for this project.
- uv is _very_ fast installing packages.
