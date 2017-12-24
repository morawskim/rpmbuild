#
# spec file for package ApacheDirectoryStudio
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

%global build_number  2.0.0.v20170904-M13
%global valid_version %(c=%{build_number}; echo ${c//-/_})
%define _apache_studio_prefix %{_usr}/lib/ApacheDirectoryStudio

# Filtering provides and requires after scanning
%define __requires_exclude ^osgi
%define __provides_exclude ^osgi|eclipse

Name:           ApacheDirectoryStudio
Version:        %{valid_version}
Release:        1
License:        Apache-2.0
Summary:        LDAP browser and directory client
Url:            http://directory.apache.org/studio/
Group:          Applications/Tools
Source0:        http://ftp.ps.pl/pub/apache/directory/studio/%{build_number}/ApacheDirectoryStudio-%{build_number}-src.zip
Source1:        ApacheDirectoryStudio.desktop
# We need fix test on openSUSE vagrant box.
# Failed tests: 
#   JNDIConnectionWrapperTest>ConnectionWrapperTestBase.testConnectFailures:235 null
#   DirectoryApiConnectionWrapperTest>ConnectionWrapperTestBase.testConnectFailures:241 null
# On my local machine test are OK.
#
# On local machine
# telnet 555.555.555.555 389
# telnet: 555.555.555.555: Name or service not known
#
# On vagrant box
# telnet 555.555.555.555 389
# Trying 555.555.555.555...
# telnet: connect to address 555.555.555.555: Connection refused
Patch0:         %{name}-fix-tests.patch
BuildRequires:  maven > 3.5
BuildRequires:  java-sdk >= 1.8.0
Requires:       java >= 1.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Apache Directory Studio is a complete directory tooling platform intended to be
used with any LDAP server however it is particularly designed for use with
ApacheDS. It is an Eclipse RCP application, composed of several Eclipse (OSGi)
plugins, that can be easily upgraded with additional ones. These plugins can
even run within Eclipse itself.

%prep
%setup -qn org.apache.directory.studio.parent-%{build_number}
%patch0 -p1
cp %{S:1} .

%build
MAVEN_OPTS="-Xmx512m" ./build.sh
%{__sed} -i 's#@@PREFIX@@#%{_apache_studio_prefix}#g' %{S:1}

%install
%__install -d -m 755 %{buildroot}%{_apache_studio_prefix}
%__cp -pr product/target/products/org.apache.directory.studio.product/linux/gtk/%{_build_arch}/ApacheDirectoryStudio/* "%{buildroot}/%{_apache_studio_prefix}"
install -D -m 644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%{desktop_database_post}

%postun
%{desktop_database_postun}

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_datadir}/applications/%{name}.desktop
%dir %{_apache_studio_prefix}
%{_apache_studio_prefix}/*

%changelog
* Sun Dec 24 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
