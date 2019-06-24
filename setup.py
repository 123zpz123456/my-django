from setuptools import setup, find_packages


setup(
    name = 'typeidea',
    version = '0.1',
    description = 'Blog System base on Django',
    author = 'the5fire',
    author_email = 'thefivefire@gmail.com',
    url = 'https://www.the5fire.com',
    license = 'MIT',
    packages = find_packages('typeidea'),    #打包typeidea下的所有Python包
    package_dir = {'': 'typeidea'},    #指明packages包都在哪个目录下
    package_data = {'': [    #方法一：打包数据文件
        'themes/*/*/*/*/*',     #需要按目录层级匹配
    ]},
    #include_package_data=True,   #方法二：匹配MANIFES.in文件
    install_requires=[
        'django~=1.11',
    ],
    extras_require = {
        'ipython': ['ipython===6.2.1']
    },
    scripts=[
        'typeidea/manage.py',
    ],
    entry_points={
        'console_scripts':[
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[    #Optional
        #软件成熟的如何？
        #3-Alpha
        #4-Beta
        #5-Production/Stable
        'Development Status :: 3 - Alpha',

        #指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        #选择项目许可证
        'License :: OSI Approved :: MIT License',

        #指定项目需要使用的Python版本
        'Programming Language :: Python :: 3.5',
    ],
)