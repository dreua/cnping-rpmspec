Name:          cnping
Version:       1.0.0
Release:       1%{?dist}
Summary:       Minimal graphical real time IPv4 Ping Tool
License:       MIT or BSD
URL:           https://github.com/cntools/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: libXinerama-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel

%description
cnping is a minimal graphical real time IPv4 ping tool written in C.
It can send pings via ICMP (regular ping) or HTTP which is useful 
in case ICMP is prohibited. Responses are displayed as vertical bars 
in a graphical window. Red bars indicate a response was not (yet) 
received, white bars indicate the response was received with a height 
relative to the round trip time. Additional statistics are displayed 
as an overlay.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build CFLAGS="%optflags" LDFLAGS="%__global_ldflags"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
install -cp -m0755 cnping ${RPM_BUILD_ROOT}%{_bindir}/

%files
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_bindir}/cnping

%doc README.md cnping.png

%license LICENSE*

%changelog
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
