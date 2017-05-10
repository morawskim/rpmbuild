#
# spec file for package python-sphinxcontrib-documentedlist
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           python-sphinxcontrib-documentedlist
Version:        0.4
Release:        1
License:        BSD
Summary:        Sphinx DocumentedList extension
Url:            http://bitbucket.org/birkenfeld/sphinx-contrib
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/0e/73/b32d730fde8cb2dd5f3ddb892cd74237b6174cb79bbd06da28a953dd4d7f/sphinxcontrib-documentedlist-0.4.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This file provides a Sphinx extension to convert a Python list into a table in
the generated documentation. The intended application of this extension is to
document the items of essentially list-like objects of immutable data (possibly
enums, though python 3.4 enums are not supported yet).

%prep
%setup -q -n sphinxcontrib-documentedlist-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.rst
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib_documentedlist-%{version}-py%{python_version}.egg-info
%{python_sitelib}/sphinxcontrib_documentedlist-%{version}-py%{python_version}-nspkg.pth

%changelog
* Wed May 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  change package name to python-sphinxcontrib-documentedlist

* Wed Aug 17 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
