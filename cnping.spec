# If you change this file, please inform @dreua since I most likely have to
# apply these changes to the other pdfarranger spec file I maintain, too.

# These must come from the calling environment
%global repo %{getenv:GITHUB_REPOSITORY}
%global sha %{getenv:GITHUB_SHA}


%global shortcommit %(c=%{sha}; echo ${c:0:7})
%define build_timestamp %(date +"%%Y%%m%%d")

Name:          cnping
Version:       0
Release:       %{build_timestamp}git%{shortcommit}%{?dist}
Summary:       Minimal graphical real time IPv4 Ping Tool
License:       MIT or BSD
URL:           https://github.com/%{repo}
Source0:       %{url}/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXinerama-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel

# For checks only
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

%global app_id com.github.cntools.cnping

%description
cnping is a minimal graphical real time IPv4 ping tool written in C.
It can send pings via ICMP (regular ping) or HTTP which is useful 
in case ICMP is prohibited. Responses are displayed as vertical bars 
in a graphical window. Red bars indicate a response was not (yet) 
received, white bars indicate the response was received with a height 
relative to the round trip time. Additional statistics are displayed 
as an overlay.

%prep
%autosetup -n %{name}-%{sha}

%build
%make_build CFLAGS="%optflags" LDFLAGS="%__global_ldflags"

%install
install -cpD -m0755 -t %{buildroot}%{_bindir}/ cnping
install -cpD -m0644 -t %{buildroot}%{_mandir}/man1/ cnping.1
install -cpD -m0644 -t %{buildroot}%{_datadir}/applications/ freedesktop/*.desktop
install -cpD -m0644 -t %{buildroot}%{_metainfodir}/ freedesktop/*.xml
mkdir -p %{buildroot}%{_datadir}/icons/
cp -r freedesktop/icons/* %{buildroot}%{_datadir}/icons/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE*
%doc README.md cnping.png
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_bindir}/cnping
%{_mandir}/man*/*.*
%{_datadir}/icons/hicolor/*/apps/%{app_id}.*
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop

%changelog
* Fri Jan 27 2023 David Auer <dreua@posteo.de>
- Modified for cnping-CI: Build given commit.

* Wed Dec 23 2020 David Auer <dreua@posteo.de> - 1.0.0-2
- Add supplemental files for linux desktop installation

* Fri Oct 04 2019 David Auer <dreua@posteo.de> - 1.0.0-1
- New version 1.0.0, remove all git commit related stuff
- Use CFLAGS and LDFLAGS
- Update URL

* Tue Aug 21 2018 David Auer <dreua@posteo.de> - 0-20180813gitaa3c971
- Add licenses

* Sun Jul 22 2018 David Auer <dreua@posteo.de> - 0-20180717git2af4ff9.4
- Proper use of %%build
- Remove exe

* Sat Jul 21 2018 David Auer <dreua@posteo.de> - 0-20180717git2af4ff9.3
- Remove unneeded requires
- Fix license
- Fix summary
- Add cflags to make

* Sat Jul 21 2018 David Auer <dreua@posteo.de> - 0-20180717git2af4ff9.2
- Fix file capabilities

* Sat Jul 21 2018 David Auer <dreua@posteo.de> - 0-20180717git2af4ff9
- Initial RPM release
