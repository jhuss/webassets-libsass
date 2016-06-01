# coding=utf-8

"""
author    = "Jesús Jerez <jerezmoreno@gmail.com>"
copyright = "2014-2016"
license   = "BSD"
"""

from __future__ import print_function, absolute_import
from webassets.filter import Filter


__all__ = 'LibSass'


class LibSass(Filter):
    """
    Converts `Sass <http://sass-lang.com/>`_ markup to real CSS.

    Requires the ``libsass`` package (https://pypi.python.org/pypi/libsass)::

        pip install libsass

    `libsass <http://dahlia.kr/libsass-python>`_ is binding to C/C++
    implementation of a Sass compiler `Libsass
    <https://github.com/hcatlin/libsass>`_

    *Configuration Options:*

    LIBSASS_OUTPUT_STYLE (output_style)
        an optional coding style of the compiled result. choose one of:
        `nested` (default), `expanded`, `compact`, `compressed`

    LIBSASS_INCLUDE_PATHS (include_paths)
        an optional list of paths to find @imported SASS/CSS source files

    See libsass documentation for full documentation about these configuration
    options:

    http://hongminhee.org/libsass-python/sass.html#sass.compile
    """

    name = 'libsass'
    options = {
        'style': 'LIBSASS_OUTPUT_STYLE',
        'include': 'LIBSASS_INCLUDE_PATHS'
    }
    max_debug_level = None

    def setup(self):
        super(LibSass, self).setup()

        try:
            import sass
        except ImportError:
            raise EnvironmentError('The "libsass" package is not installed.')
        else:
            self.sass = sass

        if not self.style:
            self.style = 'nested'

    def input(self, _in, out, **kwargs):
        source_path = kwargs['source_path']

        out.write(
            self.sass.compile(
                filename=source_path,
                output_style=self.style,
                include_paths=(self.include if self.include else []),
            )
        )
