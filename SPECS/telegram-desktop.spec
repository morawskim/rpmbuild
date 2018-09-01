#
# spec file for package telegram-desktop
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

Name:           telegram-desktop
Version:        1.3.14
Release:        1
License:        GPLv3
Summary:        A new era of messaging
Url:            https://telegram.org
Group:          Applications/Internet
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tsetup.%{version}.tar.xz
Source1:        tg.protocol
Source2:        %{name}.png
Source3:        %{name}.desktop
BuildRequires:  desktop-file-utils
ExclusiveArch:  x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Telegram is a messaging app with a focus on speed and security, it’s super
fast, simple and free. You can use Telegram on all your devices at the same
time — your messages sync seamlessly across any of your phones, tablets or
computers.

With Telegram, you can send messages, photos, videos and files of any type
(doc, zip, mp3, etc), as well as create groups for up to 200 people. You can
write to your phone contacts and find people by their usernames. As a result,
Telegram is like SMS and email combined — and can take care of all your
personal or business messaging needs.

%prep
%setup -n Telegram

%build

%install
install -p -D -m 755 Telegram %{buildroot}/%{_bindir}/telegram-desktop

# Installing desktop shortcut...
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{S:3}

# Installing icons...
size=256
dir="%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps"
install -d "$dir"
install -m 644 -p %{S:2} "$dir/%{name}.png"

# Installing tg protocol handler...
install -d "%{buildroot}%{_datadir}/kde4/services"
install -m 644 -p %{S:1} "%{buildroot}%{_datadir}/kde4/services/tg.protocol"

%post
%{desktop_database_post}

%postun
%{desktop_database_postun}

%files
%defattr(-,root,root)
%{_bindir}/telegram-desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/kde4/services/tg.protocol
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat Sep 01 2018 Marcin Morawski <marcin@morawskim.pl>
-  Update to 1.3.14

* Thu Dec 14 2017 Marcin Morawski <marcin@morawskim.pl>
-  Update to 1.2.1

* Mon Sep 04 2017 Marcin Morawski <marcin@morawskim.pl>
-  Update to 1.1.21

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.1.2-2
- Rebuild for openSUSE 42.3

* Sun Jun 04 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
