webassets-libsass
=================
Filter for asset management "webassets" that uses "libsass"


Required
========
    libsass (libsass-python): http://dahlia.kr/libsass-python you need to have C/C++ compiler
    webassets: https://pypi.python.org/pypi/webassets


Installation
============
Option 1:
========
download and extract, then: python setup.py install

Option 2:
========
run pip install webassets-libsass


Use
===
Register filter:
===============
from webassets.filter import register_filter
from webassets_libsass import LibSass

register_filter(LibSass)

Like another webassets filter:
=============================
# foundation framework
foundation = Bundle(
    'scss/foundation/app.scss',
    filters='libsass',
    output='css/foundation.css'
)


Configuration Options
=====================
LIBSASS_OUTPUT_STYLE (output_style)
an optional coding style of the compiled result. choose one of: nested (default), expanded, compact, compressed

LIBSASS_INCLUDE_PATHS (include_paths)
an optional list of paths to find @imported SASS/CSS source files

Example:
env = Environment( ... )
env.config['LIBSASS_OUTPUT_STYLE'] = 'compressed'
Bundle('src/test.scss', filters='libsass', output='out/test.css')
