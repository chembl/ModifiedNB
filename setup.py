from setuptools import setup

setup(
    name='ModifiedNB',
    version='0.2',
    author='Eloy Félix',
    author_email='eloyfelix@gmail.com',
    description='Laplace corrected modified naïve bayes model',
    url='https://github.com/chembl/ModifiedNB/',
    license='MIT',
    packages=[
        'ModifiedNB',
        ],
    long_description=open('README.md', encoding='utf-8').read(),
    install_requires=[
        'scikit-learn>=0.19.0',
    ],
    include_package_data=True,
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering :: Chemistry'],
    zip_safe=False,
)
