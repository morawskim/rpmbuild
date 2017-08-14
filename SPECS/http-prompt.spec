#
# spec file for package http-prompt
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

Name:           http-prompt
Version:        0.8.0
Release:        3
License:        MIT
Summary:        An interactive command-line HTTP client featuring autocomplete and syntax highlighting
Url:            https://github.com/eliangcs/http-prompt
Group:          Development/Languages/Python
Source:         https://github.com/eliangcs/http-prompt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-setuptools
BuildArch:      noarch
Requires:       python-click >= 5.0
Requires:       httpie >= 0.9.2
Requires:       python-Pygments >= 2.1.0
Requires:       python-six >= 1.10.0
Requires:       python-prompt_toolkit >= 0.60
Requires:       python-parsimonious >= 0.6.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HTTP Prompt is an interactive command-line HTTP client featuring autocomplete and syntax highlighting, built on HTTPie and prompt_toolkit.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc LICENSE README.rst
%{python_sitelib}/http_prompt/
%{python_sitelib}/http_prompt-%{version}-py%{python_version}.egg-info
%{_bindir}/http-prompt

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 0.8.0-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Feb 18 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
