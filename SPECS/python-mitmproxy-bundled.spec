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
Release:        4
License:        MIT
Summary:        An SSL-capable man-in-the-middle proxy
Url:            http://mitmproxy.org
Group:          Development/Languages/Python
Source0:        https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz
Source1:        python-mitmproxy-bundled.SuSEfirewall
Source2:        mitmproxy-bin.skeleton
Source3:        https://github.com/mitmproxy/mitmproxy.org/raw/master/logo/logo-inverted.png
Source4:        https://github.com/mitmproxy/mitmproxy.org/raw/master/logo/logo.png
Source5:        mitmproxy.desktop
Patch0:         %{name}.fix-doc-build.patch
Patch1:         %{name}-support_python27.patch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip
BuildRequires:  python-virtualenv
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  python-Sphinx
BuildRequires:  python-sphinxcontrib-documentedlist
BuildRequires:  desktop-file-utils
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
%patch1
%__sed -i 's,@@VERSION@@,%{version},g' "docs/conf.py"

%build
virtualenv-2.7 --clear --verbose venv2.7
source ./venv2.7/bin/activate
pip install -e ./release/
LANG=en_EN.utf-8 python -u ./release/rtool.py bdist

pushd docs
make man
make singlehtml
popd

%install
%{__mkdir} -p %{buildroot}/%{_bindir}
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/etc/sysconfig/SuSEfirewall2.d/services/%{name}"

%__install -D -m0755 "release/build/binaries/pathod" "%{buildroot}/%{_bindir}"
%__install -D -m0755 "release/build/binaries/mitmdump" "%{buildroot}/%{_bindir}"
%__install -D -m0755 "release/build/binaries/mitmproxy" "%{buildroot}/%{_bindir}"
%__install -D -m0755 "release/build/binaries/pathoc" "%{buildroot}/%{_bindir}"
%__install -D -m0755 "release/build/binaries/mitmweb" "%{buildroot}/%{_bindir}"

%__install -D -p -m 0644 docs/_build/man/mitmproxydocs.1 %{buildroot}/%{_mandir}/man1/mitmproxydocs.1

# Installing icons...
size=256
dir="%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps"
install -d "$dir"
%__install -D -p -m 0644 '%{S:3}' %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/mitmproxy-inverted.png
%__install -D -p -m 0644 '%{S:4}' %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/mitmproxy.png

# Installing desktop shortcut...
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{S:5}

%post
%{desktop_database_post}

%postun
%{desktop_database_postun}


%files
%defattr(-,root,root,-)
%doc CHANGELOG CONTRIBUTORS LICENSE README.rst
%doc %{_mandir}/man1/mitmproxydocs.1%{?ext_man}
%attr(0755, root, root) %{_bindir}/mitmdump
%attr(0755, root, root) %{_bindir}/mitmproxy
%attr(0755, root, root) %{_bindir}/mitmweb
%attr(0755, root, root) %{_bindir}/pathoc
%attr(0755, root, root) %{_bindir}/pathod
%attr(0644, root, root) /etc/sysconfig/SuSEfirewall2.d/services/%{name}
%{_datadir}/applications/mitmproxy.desktop
%{_datadir}/icons/hicolor/*/apps/mitmproxy*.png

%files doc
%defattr(-,root,root,-)
%doc docs/_build/singlehtml

%changelog
* Thu Jun 08 2017 Marcin Morawski <marcin@morawskim.pl>
-  add logo and desktop file

* Tue Jun 06 2017 Marcin Morawski <marcin@morawskim.pl>
-  use virtualenv to build package

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed May 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  fix typo

* Sun Apr 16 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
