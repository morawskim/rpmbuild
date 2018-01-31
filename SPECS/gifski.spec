#
# spec file for package gifski
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           gifski
Version:        0.7.3
Release:        1
License:        AGPL3
Summary:        GIF encoder based on libimagequant (pngquant, gifquant?)
Url:            https://gif.ski
Group:          Development/Tools/Other
Source:         https://github.com/ImageOptim/gifski/archive/%{version}.tar.gz
BuildRequires:  rust >= 1.23.0
BuildRequires:  cargo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Highest-quality GIF encoder based on pngquant.

gifski converts video frames to GIF animations using pngquant's fancy features
for efficient cross-frame palettes and temporal dithering. It produces animated
GIFs that use thousands of colors per frame.

%prep
%setup -q

%build
cargo build --release

%install
%{__install} -D -p -m 0755 target/release/%{name}   %{buildroot}/%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Wed Jan 31 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
