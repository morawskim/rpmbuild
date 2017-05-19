#
# spec file for package python-mitmproxy-bundled
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

%define MITMPROXY_ROOT /usr/lib/mitmproxy

Name:           python-mitmproxy-bundled
Version:        0.18.1
Release:        2
License:        MIT
Summary:        An SSL-capable man-in-the-middle proxy
Url:            http://mitmproxy.org
Group:          Development/Languages/Python
Source0:        https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz
#Source0:        https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz#/mitmproxy-%{version}.tar.gz
Source1:        python-mitmproxy-bundled.SuSEfirewall
Source2:        mitmproxy-bin.skeleton
Patch0:         %{name}.fix-doc-build.patch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  python-Sphinx
BuildRequires:  python-sphinxcontrib-documentedlist
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
BuildArch:      noarch
Requires:       %{name} = %{version}

%description doc
Mitmproxy documentation.

%prep
%setup -q -n mitmproxy-%{version}
%patch0
%__sed -i 's,@@VERSION@@,%{version},g' "docs/conf.py"

%build
#python setup.py build

pushd docs
make man
make singlehtml
popd

%install
%{__mkdir} -p %{buildroot}/%{MITMPROXY_ROOT} %{buildroot}/%{_bindir}
PYTHONUSERBASE=%{buildroot}/%{MITMPROXY_ROOT} pip install mitmproxy==%{version} --user
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/etc/sysconfig/SuSEfirewall2.d/services/%{name}"
for bin_name in mitmdump mitmproxy mitmweb pathoc pathod
do
%{__sed} -e "s#@MITMPROXY_ROOT@#%{MITMPROXY_ROOT}#g" \
  -e "s#@BIN_FILE@#$bin_name#g" \
  %{SOURCE2} > %{buildroot}/%{_bindir}/${bin_name}-bundled
done

%{__chmod} go=rx %{buildroot}/%{MITMPROXY_ROOT}/lib \
  %{buildroot}/%{MITMPROXY_ROOT}/lib/python2.7 \
  %{buildroot}/%{MITMPROXY_ROOT}/lib/python2.7/site-packages

%__install -D -p -m 0644 docs/_build/man/mitmproxydocs.1 %{buildroot}/%{_mandir}/man1/mitmproxydocs.1

%post

%postun

%files
%defattr(-,root,root,-)
%doc CHANGELOG CONTRIBUTORS LICENSE README.rst
%doc %{_mandir}/man1/mitmproxydocs.1%{?ext_man}
%attr(0755, root, root) %{_bindir}/mitmdump-bundled
%attr(0755, root, root) %{_bindir}/mitmproxy-bundled
%attr(0755, root, root) %{_bindir}/mitmweb-bundled
%attr(0755, root, root) %{_bindir}/pathoc-bundled
%attr(0755, root, root) %{_bindir}/pathod-bundled
%{MITMPROXY_ROOT}/*
%attr(0644, root, root) /etc/sysconfig/SuSEfirewall2.d/services/%{name}

%files doc
%defattr(-,root,root,-)
%doc docs/_build/singlehtml

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed May 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  fix typo

* Sun Apr 16 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
