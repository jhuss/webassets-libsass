## webassets-libsass ##

Filter for asset management "[webassets](https://github.com/miracle2k/webassets)" that uses "[libsass](https://github.com/hcatlin/libsass)"


###Required:###

* libsass (*libsass-python*): <http://dahlia.kr/libsass-python>


###Installation:###

* install **libsass**: `easy_install libsass` or `pip install libsass`, 
this will install the module, you need to have the C++ support for GCC to compile ( on fedora: `yum install gcc-c++` )

* install **webassets**:

    ####Option 1:####
    
    `easy_install webassets` or `pip install webassets`
    
    copy **libsass.py** to **filter** directory on **webassets** installation
    
    example: `/usr/lib/python2.7/site-packages/webassets/filter/`
    
    ####Option 2:####
    
    download **webassets** source, extract, copy **libsass.py** to **filter** directory and run `setup.py install`


###Use:###

Like another webassets filter:
```
# foundation framework
foundation = Bundle(
    'scss/foundation/app.scss',
    filters='libsass',
    output='css/foundation.css'
)
```

###Config Options:###

####LIBSASS_STYLE####
an optional coding style of the compiled result. choose one of: `nested` (default), `expanded`, `compact`, `compressed`

####LIBSASS_INCLUDES####
an optional list of paths to find `@imported` SASS/CSS source files

####LIBSASS_IMAGES####
an optional path to find images
