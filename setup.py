from setuptools import setup

setup(
	name = 'ObservationHill',
	version = '0.1.0',
	url = 'https://github.com/ikarostech/ObservationHill.git',
	license = 'Free',
	author = 'ikarostech',
	author_email = 'ikarostech@live.jp',
	description = 'From twitter activities, detect suspitious index',
	install_requires = ['setuptools' , 'scipy' , 'dotenv'],
	packages = ["ObservationHill"],
	entry_points = {
		'console_scripts': [
			'ObservationHill = ObservationHill.main:main'
		]
	}
)
