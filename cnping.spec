%global commit aa3c971b78c3cfd4f7cb2ee009b8c6b48cdd353f
%global releasedate 20180813
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:          cnping
Version:       0
Release:       %{releasedate}git%{shortcommit}%{?dist}
Summary:       Minimal graphical real time IPv4 Ping Tool
License:       MIT or BSD
URL:           https://github.com/cnlohr/%{name}
Source0:       %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXinerama-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel

%description
cnping is a minimal graphical real time IPv4 ping tool written in c.
It can send pings via ICMP (regular ping) or HTTP which is useful 
in case ICMP is prohibited. Responses are displayed as vertical bars 
in a graphical window. Red bars indicate a response was not (yet) 
received, white bars indicate the response was received with a height 
relative to the round trip time. Additional statistics are displayed 
as an overlay.

%prep
%autosetup -n %{name}-%{commit}
rm cnping.exe

%build
make cnping CFLAGS="%{optflags}"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -cp -m0755 cnping ${RPM_BUILD_ROOT}%{_bindir}/

%files
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_bindir}/cnping

%doc README.md cnping.png

%license LICENSE*

%changelog
* Tue Aug 21 2018 David Auer <dreua@posteo.de> - 0-20180813gitaa3c971
- Add licenses

* Sun Jul 22 2018 David Auer <dreua@posteo.de> - 0-20180717git2af4ff9.4
- Proper use of %build
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
