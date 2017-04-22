#
# spec file for package python-parsimonious
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/morawskim/rpmbuild/issues
#

Name:           python-parsimonious
Version:        0.7.0
Release:        1
License:        MIT
Summary:        The fastest pure-Python PEG parser I can muster
Url:            https://github.com/erikrose/parsimonious
Group:          Development/Languages/Python
Source:         https://github.com/erikrose/parsimonious/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Parsimonious aims to be the fastest arbitrary-lookahead parser written in pure
Python—and the most usable. It's based on parsing expression grammars (PEGs),
which means you feed it a simplified sort of EBNF notation. Parsimonious was
designed to undergird a MediaWiki parser that wouldn't take 5 seconds or a GB
of RAM to do one page, but it's applicable to all sorts of languages.

%prep
%setup -qn parsimonious-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%{python_sitelib}/parsimonious/
%{python_sitelib}/parsimonious-%{version}-py%{python_version}.egg-info

%changelog
* Sat Apr 22 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
