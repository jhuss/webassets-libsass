# coding=utf-8

"""
author    = "Jesús Jerez <jerezmoreno@gmail.com>"
copyright = "2014"
license   = "BSD"
"""

from __future__ import absolute_import
from webassets.filter import Filter


__all__ = ('LibSass',)


class LibSass(Filter):
    """
    Convert SASS/SCSS to CSS.

    This uses a python extension module `libsass <http://dahlia.kr/libsass-python>`_
    which is binding C/C++ implementation of a Sass compiler `Libsass <https://github.com/hcatlin/libsass>`_

    *Configuration options:*

    LIBSASS_STYLE (style)
        an optional coding style of the compiled result. choose one of:
        `nested` (default), `expanded`, `compact`, `compressed`

    LIBSASS_INCLUDES (includes)
        an optional list of paths to find @imported SASS/CSS source files

    LIBSASS_IMAGES (images)
        an optional path to find images
    """

    name = 'libsass'
    options = {
        'style': 'LIBSASS_STYLE',
        'includes': 'LIBSASS_INCLUDES',
        'images': 'LIBSASS_IMAGES',
    }


    def setup(self):
        super(LibSass, self).setup()

        import sass
        self.sass = sass

        if not self.style:
            self.style = 'nested'


    def input(self, _in, out, **kwargs):
        source_path = kwargs['source_path']

        out.write(
            self.sass.compile(
                filename=source_path,
                output_style=self.style,
                include_paths=(self.includes if self.includes else []),
                image_path=(self.images if self.images else '')
            )
        )
