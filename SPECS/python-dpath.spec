#
# spec file for package python-dpath
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

%define ver2 %(s=%{version}; echo "${s%.*}-${s##*.}")
%define ver3 %(s=%{version}; echo "${s%.*},${s##*.}")

Name:           python-dpath
Version:        1.4.0
Release:        2
License:        MIT
Summary:        Filesystem-like pathing and searching for dictionaries
Url:            https://github.com/akesterson/dpath-python
Group:          Development/Languages/Python
Source:         https://github.com/akesterson/dpath-python/archive/build,%{ver3}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-setuptools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A python library for accessing and searching dictionaries via /slashed/paths ala xpath

Basically it lets you glob over a dictionary as if it were a filesystem. It allows you to specify globs (ala the bash eglob syntax, through some advanced fnmatch.fnmatch magic) to access dictionary elements, and provides some facility for filtering those results.

%prep
%setup -qn dpath-python-build-%{ver2}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.rst LICENSE.txt
%{python_sitelib}/dpath/
%{python_sitelib}/dpath-%{version}-py%{python_version}.egg-info

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Apr 17 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
