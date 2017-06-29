#
# spec file for package bcal
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

Name:           bcal
Version:        1.6
Release:        1
License:        GPLv3
Summary:        Byte CALculator. The engineer's utility for storage conversions and calculations.
Url:            https://github.com/jarun/bcal
Group:          Applications/Engineering
Source:         https://github.com/jarun/bcal/archive/v%{version}.tar.gz
BuildRequires:  gcc binutils make gzip
BuildRequires:  gcc-fortran
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bcal (Byte CALculator) is a command-line utility for storage conversions and
calculations. Storage, hardware and firmware developers work with numerical
calculations regularly e.g., storage unit conversions, address calculations
etc. If you are one and can't calculate the hex address offset for (512 - 16)
MiB immediately, or the value when the 43rd bit of a 64-bit address is set,
bcal is for you.

Though it started with storage, the scope of bcal isn't limited to the storage
domain. Feel free to raise PRs to simplify other domain-specific numerical
calculations so it can evolve into an engineer's tool.

bcal follows Ubuntu's standard unit conversion and notation policy.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%{__install} -m755 -d %{buildroot}%{_bindir}
%{__install} -m755 -d %{buildroot}%{_mandir}/man1
%{__install} -m755 bcal %{buildroot}%{_bindir}/bcal
%{__install} -m644 bcal.1 %{buildroot}%{_mandir}/man1/bcal.1

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG README.md LICENSE
%{_bindir}/bcal
%{_mandir}/man1/bcal.1.gz

%changelog
* Thu Jun 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
