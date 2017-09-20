try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '1.0.46'
setup(
	name="one_script",
	version=__version__,
	entry_points={
			'console_scripts': [
			'one_script=one:main',
			'two_script=one:main1',
			],
		},
)