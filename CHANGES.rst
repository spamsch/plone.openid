Changelog
=========

2.0.5 (unreleased)
------------------

- Nothing changed yet.


2.0.4 (2015-03-21)
------------------

- Removed unused testing code with dependency to PloneTestCase
  [tomgross]


2.0.3 (2015-02-11)
------------------

- Ported tests to plone.app.testing
  [tomgross]


2.0.2 (2013-12-07)
------------------

- Replace deprecated test assert statements.
  [timo]

- Use system random when available. This is part of the fix for
  https://plone.org/products/plone/security/advisories/20121106/24
  [davisagli]

- Fixed extractCredentials to strip whitespaces around __ac_identity_url.
  This fixes http://dev.plone.org/plone/ticket/11044
  [datakurre]


2.0.1 (2012-12-09)
------------------

- Fixed to store timestamp as part of nonce. This fixes
  http://dev.plone.org/plone/ticket/11987
  [datakurre]

- Add MANIFEST.in.
  [WouterVH]


2.0 - 2010-07-18
----------------

- Package metadata cleanup and definition of all package dependencies.
  [hannosch]

- Relicense to BSD.
  [Plone Foundation]

- Refactor tests to be simple python test cases. This removes
  all dependencies on Plone code.
  [wichert]

- Specify package dependencies.
  [hannosch]

- Handle the case where the handles for a given domain are empty but a
  request for them is made anyway. This fixes
  http://dev.plone.org/plone/ticket/9178
  [jvloothuis]


1.2 - 2008-08-19
----------------

- Fixed bug where you could not log in via OpenID, immediately log out,
  and then immediately log in again.
  [davisagli]

- Upgraded to python-openid>=2.2.1 to fix handling of OpenID providers
  that use identifier recycling.  (c.f.
  http://developer.yahoo.com/openid/faq.html)  This closes
  http://dev.plone.org/plone/ticket/8051.
  [davisagli]

- Use the OpenID "claimed identifier" so that the proper identity URL is
  displayed when using delegation.
  [davisagli]


1.1 - 2008-04-21
----------------

- Writing test and fixes for bug #7176 whereby a traceback
  was produced when an empty string identity was placed in the openid
  login form.
  [andrewb]

- Do not enable OpenID support if python has no SSL support.
  [wichert]


1.0.1 - 2007-11-09
------------------

- Also accept https URLs as valid identifiers. This fixes
  http://dev.plone.org/plone/ticket/7298
  [wichert]


1.0 - 2007-08-15
----------------

- First stable release
  [wichert]
