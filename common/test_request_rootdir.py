# -- coding:utf-8 --
# pytest 的内置 fixture 可以获取到配置相关的信息，request.config.rootdir 用于获取项目的跟目录。
# 这个文件没有用例，主要在于。在项目的根目录，在项目的根目录加上pytest.ini这个文件；
# pytest的配置文件除了 pytest.ini，还有 tox.ini 和 setup.cfg 也可以当配置文件