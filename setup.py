from distutils.core import *

import xtest

current_version = xtest.VERSION

if __name__ == '__main__':
    with open('requirements.txt') as f:
        required = f.read().splitlines()

    setup(
        name='xtest',
        version=current_version,
        packages=[
            'xtest',
            # 'xtest.tool',
        ],
        url='http://www.bitbucket.com',
        license='',
        author='Xtest',
        author_email='mayun@alibaba.com',
        description='hack tools',
        install_requires=required,

    )
