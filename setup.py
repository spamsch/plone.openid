from setuptools import setup, find_packages

version = '2.0'

setup(name='plone.openid',
      version=version,
      description="OpenID authentication support for PAS",
      long_description=open("README.txt").read() + \
                       open("docs/HISTORY.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration :: Authentication/Directory",
        ],
      keywords='PAS openid authentication',
      author='Wichert Akkerman - Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://svn.plone.org/svn/plone/plone.openid',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'zope.testing',
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
        'setuptools',
        'python-openid >=2.2.1,<2.3dev',
        'Products.PluggableAuthService',
        'ZODB3',
        # 'transaction',
        # 'Acquisition',
        # 'Zope2',
      ],
      )
