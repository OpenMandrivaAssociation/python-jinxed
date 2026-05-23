%define module jinxed

Name:		python-jinxed
Version:	2.0.4
Release:	1
Summary:	Jinxed Terminal Library
License:	MPL-2.0
Group:		Development/Python
URL:		https://github.com/Rockhopper-Technologies/jinxed
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	ncurses
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	ncurses

%description
Jinxed is a pure-Python implementation of a subset of the Python curses library.

It provides jinxed.tigetstr(), jinxed.tparm(), and related terminfo functions
on all platforms with a virtual terminfo(5) database.

%files
%doc README.rst
%license LICENSE LICENSE.ncurses
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
