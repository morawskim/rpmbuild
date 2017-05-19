#
# spec file for package dockerize
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

Name:           dockerize
Version:        0.2.2
Release:        2
License:        GPLv3
Summary:        A tool for creating minimal docker images from dynamic ELF binaries
Url:            https://github.com/larsks/dockerize
Group:          Development/Tools/Building
Source:         https://github.com/larsks/dockerize/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-base
BuildRequires:  python-setuptools
Requires:       python-base
Requires:       python-pyelftools
Requires:       python-Jinja2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Dockerize will pack up your dynamically linked ELF binaries and all their
dependencies and turn them into a Docker image.

Some example images built with this tool are available from:
https://hub.docker.com/u/dockerizeme/

%prep
%setup -q

%build
python ./setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE.txt
%{_bindir}/dockerize
%{python_sitelib}/dockerize/
%{python_sitelib}/dockerize-%{version}-py%{python_version}.egg-info

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed Mar 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
