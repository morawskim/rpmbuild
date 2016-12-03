#
# spec file for package python-prompt_toolkit
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

Name:           python-prompt_toolkit
Version:        0.60
Release:        1
License:        BSD-3-Clause
Summary:        Library for building powerful interactive command lines in Python
Url:            https://github.com/jonathanslenders/python-prompt-toolkit
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/p/prompt_toolkit/prompt_toolkit-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-Pygments
BuildRequires:  python-six >= 1.9.0
BuildRequires:  python-wcwidth
Requires:       python-Pygments
Requires:       python-six >= 1.9.0
Requires:       python-wcwidth
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Prompt toolkit is a Library for building powerful interactive command
lines in Python.

%prep
%setup -q -n prompt_toolkit-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.rst
%{python_sitelib}/prompt_toolkit/
%{python_sitelib}/prompt_toolkit-%{version}-py%{python_version}.egg-info

%changelog
* Sat Dec 03 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
