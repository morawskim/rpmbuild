#
# spec file for package mkosi
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

Name:           mkosi
Version:        3
Release:        2
License:        LGPL-2.1
Summary:        Build Legacy-Free OS Images
Url:            https://github.com/systemd/mkosi
Group:          System/Management
Source:         https://github.com/systemd/mkosi/archive/v%{version}.tar.gz
Patch0:         %{name}-109-fix_zyypper_call.patch
Requires:       python3 >= 3.5
Recommends:     squashfs
Recommends:     btrfs-progs
Recommends:     dosfstools
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     tar
Recommends:     veritysetup
Recommends:     xz
# To build other distros:
Recommends:     debootstrap >= 1.0.83
Recommends:     dnf
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A fancy wrapper around dnf --installroot, debootstrap, pacstrap and zypper that
may generate disk images with a number of bells and whistles.

Generated images are "legacy-free". This means only GPT disk labels
(and no MBR disk labels) are supported, and only systemd based images
may be generated. Moreover, for bootable images only EFI systems are
supported (not plain MBR/BIOS).

%prep
%setup -q
%patch0 -p1

%build

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README
%license LICENSE
%{_bindir}/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 3-2
- Rebuild for openSUSE 42.3

* Wed Jul 26 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

