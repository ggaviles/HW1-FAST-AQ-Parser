from setuptools import setup

setup(
    name='HW1-FAST-AQ-Parser',
    version='0.1.0',    
    description='Building a FAST[AQ] Parser + Building a DNA -> RNA Transcriber',
    url='https://github.com/ggaviles/HW1-FAST-AQ-Parser',
    author='Giovanni Aviles',
    author_email='giovanni.aviles@ucsf.edu',
    license='BSD 2-clause',
    packages=['seqparser'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: MacOS :: MacOS 12.6',        
        'Programming Language :: Python :: 3.10.8',
    ],
)
