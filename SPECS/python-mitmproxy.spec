#
# spec file for package python-mitmproxy
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

Name:           python-mitmproxy
Version:        0.17.1
Release:        2
License:        MIT
Summary:        An SSL-capable man-in-the-middle proxy
Url:            http://mitmproxy.org
Group:          Development/Languages/Python
Source0:        https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz
Source1:        mitmproxy.SuSEfirewall
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-Sphinx
BuildRequires:  python-sphinxcontrib-documentedlist
BuildRequires:  python-pip
BuildRequires:  make
Provides:       python-netlib = %{version}
Obsoletes:      python-netlib < %{version}
Requires:       python-ipaddress >= 1.0.15, python-ipaddress < 1.1
Requires:       python-enum34 >= 1.0.4, python-enum34 < 2
Requires:       python-watchdog >= 0.8.3, python-watchdog < 0.9
Requires:       python-urwid >= 1.3.1, python-urwid < 1.4
Requires:       python-tornado >= 4.3, python-tornado < 4.4
Requires:       python-Pillow >= 3.2
Requires:       python-blinker >= 1.4
Requires:       python-configargparse >= 0.10
Requires:       python-html2text >= 2016.1.8
Requires:       python-lxml >= 3.5.0
Requires:       python-pyparsing >= 2.0
Requires:       python-pyperclip >= 1.5.22
Requires:       python-six >= 3.2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the mitmproxy and pathod projects, as well as their
shared networking library, netlib.

mitmproxy is an interactive, SSL-capable intercepting proxy with a console
interface.

mitmdump is the command-line version of mitmproxy. Think tcpdump for HTTP.

pathoc and pathod are perverse HTTP client and server applications designed
to let you craft almost any conceivable HTTP request, including ones that
creatively violate the standards.

%package doc
Summary:        Mitmproxy documentation
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
Mitmproxy documentation.

%prep
%setup -q -n mitmproxy-%{version}

%build
python setup.py build

pushd docs
make man
make singlehtml
popd

%install
python setup.py install --prefix=%{_prefix} --root %{buildroot}
%__install -D -p -m 0644 docs/_build/man/mitmproxydocs.1 %{buildroot}/%{_mandir}/man1/mitmproxydocs.1
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/etc/sysconfig/SuSEfirewall2.d/services/%{name}"

%post

%postun

%files
%defattr(-,root,root,-)
%doc CHANGELOG CONTRIBUTORS LICENSE README.rst
%doc %{_mandir}/man1/mitmproxydocs.1%{?ext_man}
%{_bindir}/mitmdump
%{_bindir}/mitmproxy
%{_bindir}/mitmweb
%{_bindir}/pathoc
%{_bindir}/pathod
%{python_sitelib}/mitmproxy/
%{python_sitelib}/netlib/
%{python_sitelib}/pathod/
%{python_sitelib}/mitmproxy-%{version}-py%{python_version}.egg-info
%attr(0644, root, root) /etc/sysconfig/SuSEfirewall2.d/services/%{name}

%files doc
%defattr(-,root,root,-)
%doc docs/_build/singlehtml

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed May 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  fix typo

* Mon Apr 24 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
