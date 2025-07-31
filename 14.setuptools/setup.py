import setuptools

setuptools.setup(
    include_package_data=True,
    name='calc',
    version='0.0.1',
    description='calc python module',
    # url='https://github.com/limegurutech/examples/tree/main/python/pip%20installable%20package',
    author='Bhargav',
    author_email='rbsinh96@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='calc python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)