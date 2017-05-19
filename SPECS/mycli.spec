#
# spec file for package mycli
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

Name:           mycli
Version:        1.8.1
Release:        2
License:        BSD
Summary:        Interactive CLI for MySQL Database with auto-completion and syntax highlighting
Url:             http://mycli.net
Group:          Productivity/Databases/Clients
Source:         https://files.pythonhosted.org/packages/source/m/mycli/mycli-%{version}.tar.gz
Patch01:        mycli-1.7.0-mv-authors.patch
Patch02:        71f503af.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-click >= 4.1
Requires:       python3-pycrypto => 2.6.1
Requires:       python3-Pygments >= 2.0
Requires:       python3-prompt_toolkit >= 1.0.0
Requires:       python3-PyMySQL >= 0.6.2
Requires:       python3-sqlparse >= 0.2.2
Requires:       python3-configobj >= 5.0.6
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nice interactive shell for MySQL Database with auto-completion and
syntax highlighting.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
rm -rf mycli.egg-info
mv AUTHORS SPONSORS mycli/
sed -i -e '1 d' mycli/main.py

%build
FLAGS="%{optflags}" /usr/bin/python3 setup.py build '--executable=/usr/bin/python3 -s'

%install
CFLAGS="%{optflags}"  /usr/bin/python3 setup.py install -O1 --skip-build --root %{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%license LICENSE.txt
%doc mycli/AUTHORS README.md mycli/SPONSORS
%{_bindir}/mycli
%{python3_sitelib}/mycli
%{python3_sitelib}/mycli-%{version}-py?.?.egg-info

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Mar 06 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
