Summary:  Measures the power consumption of a machine
Name:     powerstat
License:  GPL-2.0-only
Version:  0.03.03
Release:  1%{?dist}

URL:      https://github.com/ColinIanKing/powerstat
Source0:  %{url}/archive/V%{version}/%{name}-V%{version}.tar.gz

BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  make
# This is not linked to the executable
Requires: bash-completion
# RAPL not available on other architectures
ExclusiveArch: %{ix86} x86_64

%description
Powerstat measures the power consumption of a machine using the
battery stats or the Intel RAPL interface. The output is like
vmstat but also shows power consumption statistics. At the end
of a run, powerstat will calculate the average, standard
deviation and min/max of the gathered data.

%prep
%autosetup

%build
%make_build

%install
%make_install

%check
# Smoke test binary works, no tests available
./powerstat -h

%files
%doc README.md
%license COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8*
%{_datadir}/bash-completion/completions/powerstat

%changelog
* Wed Jul 19 2023 Benson Muite <benson_muite@emailplus.org> - 0.03.03-1
- Initial packaging
